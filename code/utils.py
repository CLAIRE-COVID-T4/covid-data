import numpy as np
import gensim

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from umap import UMAP


REDUCERS = {"pca": PCA, "tsne": TSNE, "umap": UMAP}


def project_embeddings(data, n_components=2, reducer_name="tsne"):
    data = StandardScaler().fit_transform(data)
    reducer_class = REDUCERS[reducer_name]
    reducer = reducer_class(n_components=n_components)
    embeddings = reducer.fit_transform(data)
    return embeddings


def load_embeddings(filename):
    model = gensim.models.KeyedVectors.load_word2vec_format(filename, binary=False)
    return model.index2word, model.vectors


def load_cluster_data(filename):
    return np.loadtxt(filename, skiprows=1)


def load_cluster_composition(filename):
    data = {}
    with open(filename, "r") as f_handle:
        for i, line in enumerate(f_handle.readlines()):
            if i == 0:
                continue
            values = line.rstrip("\n").split(" ")
            cluster_idx, GO_idxs = values[0], values[1:]
            data[int(cluster_idx)] = [int(p) for p in GO_idxs]
    return data