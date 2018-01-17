import numpy as np

#   I'll be using a n-gram model here to learn the word embeddings for NLP applications, or at least demonstrate the concept.

corpus = "A short story is a piece of prose fiction that can be read in one sitting . Emerging from earlier oral storytelling traditions in the 17th century , the short story has grown to encompass a body of work so diverse as to defy easy characterization . At its most prototypical the short story features a small cast of named characters , and focuses on a self-contained incident with the intent of evoking a single effect or mood . In doing so , short stories make use of plot , resonance , and other dynamic components to a far greater degree than is typical of an anecdote , yet to a far lesser degree than a novel . While the short story is largely distinct from the novel , authors of both generally draw from a common pool of literary techniques . Short stories have no set length . In terms of word count there is no official demarcation between an anecdote , a short story , and a novel . Rather , the form parameters are given by the rhetorical and practical context in which a given story is produced and considered , so that what constitutes a short story may differ between genres , countries , eras , and commentators . Like the novel , the short story predominant shape reflects the demands of the available markets for publication , and the evolution of the form seems closely tied to the evolution of the publishing industry and the submission guidelines of its constituent houses . The short story has been considered both an apprenticeship form preceding more lengthy works , and a crafted form in its own right , collected together in books of similar length , price , and distribution to novels . Short story writers may define their works as part of the artistic and personal expression of the form . They may also attempt to resist categorization by genre and fixed formation"
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

for sentence in corpus.split('.'):      #   Sentences are cohesive structures, so I'll consider each one at a time. Context tends to vary between them, so it wouldn't be right for the window to overlap onto the next/previous sentence.
    for index, word in enumerate(sentence): #   Considering each word as an input, what are the possible outputs given my window size?
        for outputWord in sentence[max(index - WINDOW, 0) : min(index + window, len(sentence))]:    #   To make sure I don't break the bounds of the list
            if outputWord != ',' and outputWord != word:
                dataset.append([word, outputWord])


