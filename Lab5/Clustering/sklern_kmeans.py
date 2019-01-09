import numpy as np
import pandas as pd
import random

from sklearn.metrics import accuracy_score

import utils
import pyprind
from sklearn.cluster import KMeans


if __name__ == '__main__':
    data, label = utils.load_data()
    feature = np.array(data)
    clf = KMeans(n_clusters=2)
    s = clf.fit(feature)
    print(s)
    print(clf.labels_)
    print(clf.inertia_)
    acc1 = accuracy_score(label, clf.labels_)
    acc2 = accuracy_score(label, 1-clf.labels_)
    acc = acc1 if acc1>acc2 else acc2
    print("acc = " + str(acc))