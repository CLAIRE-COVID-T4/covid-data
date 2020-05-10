from pathlib import Path
import argparse

from matplotlib import pyplot as plt
import seaborn as sns

from settings import NAMESPACES, PLOT_DIR
from utils import REDUCERS, load_embeddings, load_cluster_data, project_embeddings

sns.set_context('poster')
sns.set_style('white')
sns.set_color_codes()
PLOT_KWDS = {'alpha': 0.5, 's': 1, 'linewidths': 0, 'marker': '.'}


def parse_args():
    parser = argparse.ArgumentParser()
    subps = parser.add_subparsers()
    clust_parser = subps.add_parser("plot_clustering")
    clust_parser.add_argument("--embeddings-file", required=True,
                              help="Path to the embeddings file.")
    clust_parser.add_argument('--reducer', choices=REDUCERS.keys(), default="tsne",
                             help="Reducer to map the embeddings into low dimensional space.")
    clust_parser.set_defaults(command="plot_clustering")

    embs_parser = subps.add_parser("plot_embeddings")
    embs_parser.add_argument("--embeddings-file", required=True,
                             help="Path to the embeddings file.")
    embs_parser.add_argument('--reducer', choices=REDUCERS.keys(), default="tsne",
                             help="Reducer to map the embeddings into low dimensional space.")
    embs_parser.set_defaults(command="plot_embeddings")
    return parser.parse_args()


def extract_title(filename):
    return "_".join(filename.stem.split("_")[:2])


def plot_embeddings(projection, title):
    """ Plot GO terms embeddings. """
    plt.scatter(projection[:, 0], projection[:, 1], **PLOT_KWDS)
    plt.title(title)
    plt.savefig(PLOT_DIR / f"{title}.pdf")


def plot_clustering(projection, cluster_data, title):
    """ Plot the clustering in 2d and save it in pdf. Visualization can be improved. """

    go_index = cluster_data[:, 0]
    cluster_labels = cluster_data[:, 1]
    cluster_probs = cluster_data[:, 2]
    color_palette = sns.color_palette('Paired', len(cluster_labels))
    cluster_colors = [color_palette[x] if x >= 0 else (0.5, 0.5, 0.5) for x in cluster_labels]
    cluster_member_colors = [sns.desaturate(x, p) for x, p in zip(cluster_colors, cluster_probs)]

    plt.scatter(projection[:, 0], projection[:, 1], c=cluster_member_colors, **PLOT_KWDS)
    plt.title(title)
    plt.savefig(PLOT_DIR / f"{title}.pdf")


if __name__ == "__main__":
    args = parse_args()
    filename = Path(args.embeddings_file)

    _, embeddings = load_embeddings(filename)
    projection = project_embeddings(embeddings, reducer_name=args.reducer)

    if args.command == "plot_embeddings":
        title = extract_title(filename)
        plot_embeddings(embeddings, title)

    if args.command == "plot_clustering":
        cluster_data_filename = filename.parent / f"{filename.stem}_cluster_data.txt"
        cluster_data = load_cluster_data(cluster_data_filename)
        title = extract_title(cluster_data_filename)
        plot_clustering(embeddings, cluster_data, title)
