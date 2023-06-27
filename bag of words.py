import numpy as np

# data indicates number of occurencxes of each words in the poem 'The little piggy rhyme ' per line
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

# function finds the nearest matching pair of lines using bag of words concept, to find the
# least summation of differences of occurences of words per line
def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)

    for d in range (len(data)):
        for j in range (len(data)):
            sum = 0
            if j == d:
                dist[d][j] = np.inf
            else:
                for i in range (len(data[d])):
                    sum += abs(data[d][i] - data[j][i])
                dist[d][j] = sum

# unravel : A quick way to get the index of the element with the lowest value in a 2D array (or in fact, any dimension) is by the function

np.unravel_index(np.argmin(dist), dist.shape))
    ans = np.unravel_index(np.argmin(dist), dist.shape)
    print(ans)
    return()

find_nearest_pair(data)
