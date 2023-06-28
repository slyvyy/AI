# validating scores of model based on k neighbours
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Create a classifier and fit it to our data
knn = KNeighborsClassifier(n_neighbors=133)
knn.fit(x_train, y_train)
print(knn.fit(x_train, y_train))

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):
    global y_predict

    k = 100   # classify our test items based on the classes of 5 nearest neighbors

    # process each of the test data points
    for i, test_item in enumerate(X_test):

        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]
        # converting yo numpy array to perform argsort
        distances = np.array(distances)
        # argsort gives out the train_item(points) in increasing order of distance
        D = distances.argsort()    
        D = D[:k]

        y_predict[i] = np.round(np.mean(y_train[D]))
        
    print("training accuracy: %f"% knn.score(x_train,y_train))
    print("testing accuracy: %f"% knn.score(X_test,y_predict))

main(x_train, x_test, y_train, y_test)
