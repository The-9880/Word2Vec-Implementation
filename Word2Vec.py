import numpy as np
import tensorflow
import keras
from sklearn.model_selection import train_test_split        #   Probably won't use this... imported out of habit, I guess.

#   I'll be using a n-gram model here to learn the word embeddings for NLP applications, or at least demonstrate the concept.

corpus = "A short story is a piece of prose fiction that can be read in one sitting . Emerging from earlier oral storytelling traditions in the 17th century the short story has grown to encompass a body of work so diverse as to defy easy characterization . At its most prototypical the short story features a small cast of named characters and focuses on a self-contained incident with the intent of evoking a single effect or mood . In doing so short stories make use of plot resonance and other dynamic components to a far greater degree than is typical of an anecdote yet to a far lesser degree than a novel . While the short story is largely distinct from the novel authors of both generally draw from a common pool of literary techniques . Short stories have no set length . In terms of word count there is no official demarcation between an anecdote a short story and a novel . Rather the form parameters are given by the rhetorical and practical context in which a given story is produced and considered so that what constitutes a short story may differ between genres countries eras and commentators . Like the novel the short story predominant shape reflects the demands of the available markets for publication and the evolution of the form seems closely tied to the evolution of the publishing industry and the submission guidelines of its constituent houses . The short story has been considered both an apprenticeship form preceding more lengthy works and a crafted form in its own right collected together in books of similar length price and distribution to novels . Short story writers may define their works as part of the artistic and personal expression of the form . They may also attempt to resist categorization by genre and fixed formation"
corpus = corpus.lower() #   Convert to lowercase for consistency

corpus_words = []

for word in corpus.split():
    if word != '.' and word != ',':
        corpus_words.append(word)

print(len(corpus_words))
corpus_words = set(corpus_words)        #   Eliminate Duplicates
dictionary_size = len(corpus_words)     #   The size of our dictionary
print(len(corpus_words))

#   Dictionaries to map words to ints and vice-versa
wordReference = {}
intReference = {}

#   Populating the dictionaries
for index, word in enumerate(corpus_words):
    wordReference[index] = word
    intReference[word] = index

#   Now I need to start forming input-output pairs
#   I'll use a window size of 2 for now, and may modify it later depending on the results.
WINDOW = 2

dataset = []    #   List containing my input-output pairs

sentences = []
[sentences.append(i.split()) for i in corpus.split('.')]

for sentence in sentences:      #   Sentences are cohesive structures, so I'll consider each one at a time. Context tends to vary between them, so it wouldn't be right for the window to overlap onto the next/previous sentence.
    for index, word in enumerate(sentence): #   Considering each word as an input, what are the possible outputs given my window size?
        for outputWord in sentence[max(index - WINDOW, 0) : min(index + WINDOW, len(sentence)) + 1]:    #   To make sure I don't break the bounds of the list
            if outputWord != ',' and outputWord != word:
                dataset.append([word, outputWord])

print(dataset)
print(len(dataset))

def oneHotEncoding(inputSize, word):
    inputVec = np.zeros(inputSize)
    inputVec[intReference[word]] = 1
    return inputVec

X_train = []
y_train = []

for record in dataset:
    X_train.append(oneHotEncoding(len(corpus_words),record[0]))
    y_train.append(oneHotEncoding(len(corpus_words),record[1]))

X_train = np.asarray(X_train)
y_train = np.asarray(y_train)

#print(X_train)

#   Save the hashtables
f = open('wordReference.txt', 'w')
s = open('intReference.txt', 'w')
for x in wordReference:
    f.write(str(x) + " " + str(wordReference[x]) + " " + "\n")
    s.write(str(wordReference[x]) + " " + str(x) + " " + "\n")
f.close()
s.close()

#   Training the model
model = keras.models.Sequential()
model.add(keras.layers.Dense(6, input_dim = len(corpus_words), activation='relu'))
model.add(keras.layers.Dense(len(corpus_words), activation='softmax'))
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=None)

model.fit(X_train, y_train, batch_size=32, epochs=10000)
model.save("Word2VecLearned.h5")