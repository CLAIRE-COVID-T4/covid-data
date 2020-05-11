## Gene Ontology (GO) Terms embeddings and clustering
This folder contains 3 files for each different Gene Ontology (Biological Process, Cellular Component, and Molecular Function):
- the node embeddings of the associated Gene Ontology Directed Acyclic Graph (DAG) obtained with Node2vec;
- the results of a HDBScan clustering on the node embeddings;
- the composition of each cluster found by HDBScan.

We use the following placeholders for clarity:
- `<namespace>` is one among `biological_process`, `cellular_component` and `molecular_function`;
- `<dimension>` is the embedding dimension (128 in our case).

#### File `<namespace>_emb_<dimension>.txt`

This file contains the node embeddings. It is formatted as follows:

- the first line has two integers separated by spaces: the first one defines the number of nodes embedded, and the second one defines the embedding dimension;
- the remaining lines contain a series of 1 + `<dimension>` numbers separated by spaces. The first element is an integer representing the GO id of the embedded node. For example, if the id is 6, it refers to the GO term `GO:00000006`. The other `<dimension>` entries are float numbers representing the embedding vector.


#### File `<namespace>_emb_<dimension>_cluster_data.txt`

This file contains the results of the application of HDBScan  clustering to the node embeddings. It is formatted as follows:
- the first line contains two integers separated by spaces, which specify the number of rows and columns of the file;
- the remaining lines contain three numbers separated by spaces: the first one is an integer representing the GO id of the embedded node; the second one represents the cluster label assigned to the point (where -1 means unclustered); the third one indicates the affinity of the GO term to the cluster computed by HDBSCAN. 


#### File `<namespace>_emb_<dimension>_cluster_composition.txt`

This files contains the composition of each cluster found by HDBScan. Is is formatted as follows:
- the first line contains an integer representing the number of clusters found;
- the remanining lines contain a variable-size list of integers separated by spaces. The first integer is the cluster label where -1 means unclustered, the second integer is the size of the cluster, while the other integers are the GO ids of the terms in that cluster.


#### Reproducibility

Code to reproduce both the node2vec and HDBScan analyses can be found [here](https://github.com/CLAIRE-COVID-T4/covid-data/tree/master/code).
