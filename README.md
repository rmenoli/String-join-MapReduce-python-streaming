# String-join-using-MapReduce-python-streaming

Exercise project for the course "Introduction of Big Data Management" - Univeristy of Helsinki, MS in Data Science 

## Abstract and possibile application
Let's assume we want compare the facebook's posts of two people in order to understand if they talks about same topics and which topics they share. A way to do this analyisis is compare pair-whise their post and compute for each pair the  Jaccard similarity coefficient based on bigrams in the posts. The similarity between people could be seen as the avarage of the Jaccard similarity coefficient. The most common post could be seen as the pair with less Jaccard similarity coefficient. If the number of posts is huge (or we want do comparison between many people) we could use MapReduce framework to speed up the computation. This repository provides the a quick guide to compare two files containing sentences using MapReduce framworks and python streaming.

## Algorithm
Let's collocate in this scenario: there are two distinct file strucured like s1_f.txt and s2_f.txt. Our aim is to compute the Jaccard similarity coefficent based on bigrams if letter between all the pairs of the two files.

The code follows the idea proposed by Elsayed, Lin and Oard 2008. The main idea is performe two MapReduce steps:

1. Indexing: build a standard inverted index, where each n-gram is associated with a list of sentences that contain it and the number of occurrences of the n-gram.

2. Pairwise Similarity: create pairs of sentences that share the same n-grams, find how many n-grams each pair shares and compute the similarity.

For further information read the paper in "pdf_folder".
