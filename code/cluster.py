import argparse
from pathlib import Path

import numpy as np
import hdbscan as hdb
from sklearn.preprocessing import StandardScaler

from utils import load_embeddings


def parse_args():
    r"""Parses arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--embeddings-file", required=True,
                        help='Path to the file containing the node2vec embeddings.')
    parser.add_argument("--no-scaling", dest="scale", default=True, action="store_false",
                        help="Do not apply standard scaling.")
    return parser.parse_args()


def dbscan_clustering(args):
    r"""Runs DBScan on the provided node2vec embeddings."""

    filename = Path(args.filename)
    GO_indexes, data = load_embeddings(filename)

    if args.scale is True:
        scaler = StandardScaler()
        data = scaler.fit_transform(data)

    # Clustering with HDBSCAN (density based algorithm) tested some disnamespacetance measure and paprameters.
    clusterer = hdb.HDBSCAN(
        min_samples=15,
        min_cluster_size=2,
        metric='euclidean',
        cluster_selection_method='leaf',
        cluster_selection_epsilon=0.25).fit(data)

    cluster_labels = clusterer.labels_
    cluster_probs = clusterer.probabilities_
    clustering_data = np.column_stack((GO_indexes, cluster_labels, cluster_probs))

    # Saving cluster labels for future use.
    np.savetxt(
        filename.parent / f"{filename.stem}_cluster_data.txt",
        clustering_data,
        fmt='%s',
        header=f"{len(GO_indexes)} 3",
        delimiter=' ',
        comments='')

    # Saving cluster composition for future use.
    unique = np.unique(clustering_data[:, 1:2])
    with open(filename.parent / f"{filename.stem}_cluster_composition.txt", 'a') as f_handle:
        # file header
        f_handle.write(f"{len(unique)}\n")

        for element in unique:
            present = clustering_data[:,1] == element
            tmp_cluster = np.extract(present, clustering_data[:,0])
            hd = [element, len(tmp_cluster)]
            clus = np.append(hd, tmp_cluster)
            f_handle.write(f"{clus[0]}")
            for i in range(1, len(clus)):
                f_handle.write(f" {clus[i]}")
            f_handle.write("\n")


if __name__ == "__main__":
    args = parse_args()
    dbscan_clustering(args)
