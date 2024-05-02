import nltk
import json
import pickle
import random
import numpy as np

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('punkt')


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD



file = open(r"intents.json").read()
data = json.loads(file)




words_repository = []
corpus = []
classes = []

lemmatizer = WordNetLemmatizer()
ignore = ['!','?']




for record in data['intents']:
  for pattern in record['patterns']:
    word = nltk.word_tokenize(pattern)
    word = [ lemmatizer.lemmatize(w.lower()) for w in word if w not in ignore]
    words_repository.extend(word)
    title = record["tag"]
    corpus.append((word,title))
    if title not in classes:
      classes.append(title)
      
      
words = list(set(words_repository))
words = sorted(words)
classes = sorted(classes)



word_file = 'words.pkl'
classes_file = 'classes.pkl'
corpus_file = 'corpus.pkl'
pickle.dump(words,open(word_file, 'wb'))
pickle.dump(classes,open(classes_file, 'wb'))
pickle.dump(corpus,open(corpus_file, 'wb'))



dataset=[]

for pattern , class_p in corpus:
  input_vec = [0] * len(words)
  output_vec = [0] * len(classes)

  for w in pattern:
    input_vec[words.index(w)] = 1

  output_vec[classes.index(class_p)] = 1

  dataset.append([input_vec, output_vec])

random.shuffle(dataset)
dataset = np.array(dataset, dtype=object)



train_x = list(dataset[:, 0])
train_y = list(dataset[:, 1])

 

model = Sequential()
model.add(Dense(256, input_shape=(len(train_x[0]),),
                activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

 

 
sgd = SGD(learning_rate=0.001,
          momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd, metrics=['accuracy'])
 
hist = model.fit(np.array(train_x), np.array(train_y),
                 epochs=400, batch_size=3, verbose=1)



model.save('chatbot_model_v2.h5', hist)
