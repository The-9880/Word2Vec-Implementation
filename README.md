# Word2Vec-Implementation

##  Motivation

I've been studying the University of Toronto's Neural Network course on coursera and been absolutely fascinated by the concepts and 
applications explained. In pursuit of this fascination, I'm now trying to implement every application of neural nets that I learn about as
I go along with the course.

## Word2Vec

In this code, I've implemented a skip-gram model to learn word embeddings via a neural network. Learning word embeddings is key in NLP
applications of Machine Learning to help ascribe vector representations of words in a way that captures syntactical and grammatic features.
Using a dimensionality-reduction technique like t-SNE and plotting the embedding vectors learned should offer insight into how well
the algorithm performs by seeing which words are plotted nearby one another - ideally, words that are closely related (or share many
features in their usage) should be plotted closer to each other.

Assuming a proper network architecture, an appropriate number of training epochs, etc. the quality of learning will 
then depend - as always - on the quality of data used. In this case, this means the size of the text corpus and its features (unique word count, amount of occurences
of each word, etc.). Even if a very large corpus is used, the algorithm can hardly be expected to learn a good vector embedding for a word
that occurs maybe only a few times in the training data.
