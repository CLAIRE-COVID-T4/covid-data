# COVID Datasets
A collection of COVID-related datasets useful for drug-repurposing tasks. See the **Nomenclature** section for an explanation of the terms used.

## Content Summary

Apart from `drug-structures.sdf`, All files are in TSV format (Tab-Separated Values), where the first line contains the column names. The file contents are:

 - `host-host.tab`: a collection of Human Protein-Protein Interactions, from [1].
 - `drug-host.tab`: a collection of experimentally validated Drug-Protein interaction, from [1]. The two columns of this file contain, respectively, the DrugBank ID of the drug and the Entrez ID of the Human protein targeted by the drug.
 - `drug-drug.tab`: a collection of Drug-Drug interaction, from [1].

 - `go-terms.tab`: Gene Ontology (GO) terms associated to each Human protein contained in `host-host.tab`. This file contains also other information regarding each GO term, as its GO ID, or its category (`Process`, `Function`, or `Component`).
 - `drug-structures.sdf`: drug Structure-Data File (SDF), from the open-data collection of [3].
 - `virus-host/*.tab`: collection of various Human viruses, from [4]. All the files in this folder contain the Virus-Virus, Virus-Human, and Human-Human PPIs related to a specific virus (e.g., SARS-CoV, SARS-CoV-2, MERS-CoV, HIV, etc). All proteins are denoted by their Entrez IDs.


# Content Details

This section describes the content of the files in the `data` folder.

#### `drug-drug.tab`
A collection of drug-drug combinations with the following columns:

- `DrugBank Interactor A` --> the DrugBank ID of the first drug
- `DrugBank Interactor B` --> the DrugBank ID of the second drug 
- `Adverse` --> a boolean value `N` or `Y` where
    - `N`: the two drugs produce an experimentally validated combination
    - `Y`: the two drugs produce a clinically-reported adverse interaction

#### `drug-host.tab`
A collection of drug-protein interactions with the following columns:
- `DrugBank` --> the DrugBank ID of the drug
- `Target Entrez Gene` --> the Entrez ID of the gene associated with the protein

#### `drug-structures.sdf`
The [SDF](https://en.wikipedia.org/wiki/Chemical_table_file) file of all the drugs listed in `drug-host.tab` (i.e. the ones downloadable with and without registration to the DrugBank service). This file describes the 3D structure of the drug and provides additional information such as:
- `DrugBank ID`
- `Secondary Accession Numbers`
- `Common Name`
- `CAS Number`
- `Synonyms`


## Nomenclature

- CAS Number: a unique numerical identifier assigned by the Chemical Abstracts Service (CAS) to every chemical substance described in the open scientific literature.
- DrugBank ID: the identifier of a drug in the [DrugBank](https://www.drugbank.ca/) database.
- Entrez ID: the identifier of a gene in the [NCBI Entrez](https://www.ncbi.nlm.nih.gov/gene) database.
- Gene-Ontology (GO) term: identifier of an entry in the [Gene Ontology](http://geneontology.org/) database, which contains information on the functions of genes.
- Secondary Accession Numbers: additional identifiers for the same drug.
- Structure-Data File (SDF): a [standardized format](https://en.wikipedia.org/wiki/Chemical_table_file) to represent the 3d structure of a compound. It wraps the [MDL Molfile](https://en.wikipedia.org/wiki/Chemical_table_file#Molfile) format.
- PPI: Protein-Protein Interactions.


## References

[1] Cheng, F., Kovács, I.A. & Barabási, A. Network-based prediction of drug combinations. Nat Commun 10, 1197 (2019), [https://doi.org/10.1038/s41467-019-09186-x](https://doi.org/10.1038/s41467-019-09186-x) \
[2] National Center for Biotechnology Information (NCBI), [https://www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/) \
[3] DrugBank, [https://www.drugbank.ca/](https://www.drugbank.ca/) \
[4] BioGrid, [https://thebiogrid.org/](https://thebiogrid.org/) 

