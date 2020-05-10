### Code to reproduce Node2vec and DBScan analysis of GO terms

There are three main scripts:
- `embed.py` performs node2vec. See `python embed.py -h` for help
- `cluster.py` applied DBScan to the node2vec embeddings. See `python cluster.py -h` for help
- `visualize.py` plots the embeddings, either with or withour clustering information. See `python visualize.py -h` for help