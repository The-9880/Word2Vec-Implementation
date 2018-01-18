import tensorflow
import keras
import numpy as np

#   Need to load and populate the dictionaries for use again.
wordReference = {}
intReference = {}

f = open('wordReference.txt', 'r')
s = open('intReference.txt', 'r')

hello = f.readlines()

for x in hello:
    thisLine = x.split()
    wordReference[thisLine[0]] = thisLine[1]
    intReference[thisLine[1]] = thisLine[0]

f.close()
s.close()

for x in wordReference:
    print(str(x) + str(wordReference[x]))

model = keras.models.load_model("Word2VecLearned.h5")


def oneHotEncoding(inputSize, word):
    inputVec = np.zeros(inputSize)
    inputVec[intReference[word]] = 1
    return inputVec

inp = ""
entered = []
while inp != "QUIT":
    inp = str(input())
    entered.append(str(inp))
    if(input == "e"):
        print("Getting response.")
        answer = model.predict(oneHotEncoding(168,entered[entered.count()]))
        for x in range(0, 167): #   hard-coded size of the output -- fix later.
            if answer[x] == 1:
                print(intReference[x])