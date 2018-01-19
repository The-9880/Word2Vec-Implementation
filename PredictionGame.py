import tensorflow
import keras
import numpy as np

#   Need to load and populate the dictionaries for use again.
wordReference = {}
intReference = {}

f = open('wordReference.txt', 'r')

hello = f.readlines()

for x in hello:
    thisLine = x.split()
    wordReference[int(thisLine[0])] = thisLine[1]
    intReference[thisLine[1]] = int(thisLine[0])
f.close()

model = keras.models.load_model("Word2VecLearned.h5")

def oneHotEncoding(inputSize, word):
    inputVec = np.zeros(inputSize)
    inputVec[intReference[word]] = 1
    inputVec = inputVec.reshape(168)
    return inputVec

print(model.predict(oneHotEncoding(168, wordReference[65])))

inp = ""
entered = []
while inp != "QUIT":
    inp = str(input())
    entered.append(str(inp))
    if(inp == "e"):
        entered.pop()
        print("Getting response.")
        answer = model.predict(oneHotEncoding(168,entered[len(entered)-1]))
        for x in range(0, 167): #   hard-coded size of the output -- fix later.
            if answer[x] == 1:
                print(intReference[x])