# finding the most similar pair of lines and the tf-idf representation. bag of words and tf-idf

import operator as op
import math
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
 
    # 1. split the text into words, and get a list of unique words that appear in it
    newtxt = text.split()
    unique = []
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]
    for j in docs:
        unique = unique + j
        unique = list(set(unique))

    # 2. go over each unique word and calculate its term frequency, and its document frequency

    # initliazing dicts to hold term frequency, document frequency and tf-idf OF EACH LINE
    termf = {}
    docf = {}
    tdif ={}

    for u1 in unique :
        count = 0
        for d1 in docs:
            if u1 in d1:
                count +=1
        # getting log with base 10
        docf[u1] = math.log(len(docs)/count,10)

    i = 0
    for d in docs:
        tdif[i] = []
        for u in unique:
            termf[u] = op.countOf(d, u)
            termf[u] =  termf[u]/len(d)
            
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
            tdadd = termf[u] * docf[u]
            tdif[i].append(tdadd)
        i+=1

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.

    # np 2d array to hold differences in order to find out most smiliar pair
    dist = np.empty((len(tdif), len(tdif)), dtype=float)

    for x in range (len(tdif)):
        for y in range (len(tdif)):
            sum1 = 0
            if x == y:
                dist[x][y] = np.inf

            else:
                # iterating over tdif dict to get summation of differences
                for e in range(len(tdif[x])):
                    sum1 += abs(tdif[x][e] - tdif[y][e])
                dist[x][y] = sum1

    ans = np.unravel_index(np.argmin(dist), dist.shape)
    print(ans)
    return()
main(text)
