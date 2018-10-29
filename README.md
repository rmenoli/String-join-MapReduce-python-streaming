# String-join-using-MapReduce-python-streaming

## Abstract and possibile application
Let's assume we want compare the facebook's posts of two people in order to understand if they talks about same topics and which topics they share. A way to do this analyisis is compare pair-whise their post and compute for each pair the  Jaccard similarity coefficient based on bigrams in the posts. The similarity between people could be seen as the avarage of the Jaccard similarity coefficient. The most common post could be seen as the pair with less Jaccard similarity coefficient. If the number of posts is huge (or we want do comparison between many people) we could use MapReduce framework to speed up the computation. This repository provides the a quick guide to compare two files containing sentences using MapReduce framworks and python streaming.

## Algoithm
Let's collocate in this scenario: there are two distinct file strucured like s1_f.txt and s2_f.txt. Our aim is to compute the Jaccard similarity coefficent based on bigrams if letter between all the pairs of the two files.

The code follows the idea proposed by Elsayed, Lin and Oard 2008. The main idea of the paper is

Inline-style: 
![alt text](https://github.com/rmenoli/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

The computation is performed in two MapReduce steps:

1. Indexing: build a standard inverted index, where each n-gram is associated with a list of sentences that contain it and the number of occurrences of the n-gram.

2. Pairwise Similarity: create pairs of sentences that share the same n-grams, find how many n-grams each pair shares and compute the similarity.

Elsayed, Lin and Oard 2008 assumes that all sentences are in the same file. They consider th following similarity measure: `$$ax^2 + bx + c = 0$$` "$sim(d_{i},d_{j})=\sum_{t\in V}w_{t,i}\cdot w_{t,j}$" where $sim(d_{i},d_{j})$ is the similarity between sentences $d_{i}$ and $d_{j}$, $V$ is the vocabulary set and $w_{t}$ is the weight which indicate the importance of each term t. If a term is not in the sentences the weight of the term for that document is 0.

In order to complete the task of the assignment (i.e. finding the similar pairs between the two documents and use as similarity distance the Jaccard similarity), I change a little the idea of Elsayed, Lin and Oard 2008. My solution performs two MapReduce job (indexing and pairwise similarity)


