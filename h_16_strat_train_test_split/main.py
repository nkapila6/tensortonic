# 30.01.2026, 12:30 PM
# Nikhil Kapila
# https://www.tensortonic.com/problems/stratified-split

import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    """
    Split features X and labels y into train/test while preserving class proportions.
    """
    # X: array-like, shape (N,D) or (N,)
    # y: array-like, shape (N,)
    # test_size: float in (0,1) - fraction in test set
    # rng: optional for reproducible shuffling

    #  not checking for edge case where len(X) != len(y), not mentioned in the problem statement either tbh
    
    X,y = np.array(X), np.array(y)
    rng = np.random.default_rng() if rng is None else np.random.default_rng(rng)
    
    # calc how many samples should go based on test_size ratio
    unique_y, counts = np.unique(y, return_counts=True)
    train_idx, test_idx = [],[]

    for yo in unique_y:
        # where does this class exist in y? gonna be same in x too
        idx = np.where(y==yo)[0]
        # shuffle: https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html
        rng.shuffle(idx) # shuffled idx

        split_size= int(np.floor(test_size*len(idx)+.5))

        # edge cases:
        # at least one in train:
        if split_size>=len(idx) and len(idx)>0:
            split_size = len(idx)-1
        # if split size is 0 but class exists in idx then add 1
        #

        train_idx.extend(idx[split_size:])
        test_idx.extend(idx[:split_size])

    # print("returning")
    rng.shuffle(train_idx)
    rng.shuffle(test_idx)
    return (X[train_idx], X[test_idx], y[train_idx], y[test_idx])

def verifier(*args):
    X_train, X_test, y_train, y_test = args
    print("verifying:")
    print(X_train, X_test, y_train, y_test)
    unique, counts = np.unique(y_test, return_counts=True)

    print(dict(zip(unique, counts/len(y_test))))


def main():
    print("test1")
    X,y = [1,2,3,4,5], [0,0,0,1,1]
    print(f"input: {X,y}")
    verifier(*stratified_split(X,y, 0.4))

    print("\n\ntest2")
    X,y=[[1,2],[3,4],[5,6]],[0,1,0]
    print(f"input: {X,y}")
    verifier(*stratified_split(X,y, .33))

if __name__ == "__main__":
    main()

