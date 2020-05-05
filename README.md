# COVID Datasets
 Collection of COVID-related datasets useful for drug-repurposing tasks.

## Contents

Apart from `drug-structures.sdf`, All files are in TSV format (Tab-Separated Values), where the first line contains the column names. The file contents are:

 - `host-host.tab`: a collection of Human Protein-Protein Interactions (PPI), from [1]. The two columns of this file contains the Entrez IDs of the two interacting proteins.
 - `drug-host.tab`: a collection of experimentally validated Drug-Protein interaction, from [1]. The two columns of this file contain, respectively, the DrugBank ID of the drug and the Entrez ID of the Human protein targeted by the drug.
 - `drug-drug.tab`: a collection of Drug-Drug interaction, from [1]. Other than the two DrugBank IDs contained in the first two colums, this file contain a third column (`Adverse`) that specifies if

   - the two drugs produce a clinically-reported adverse interaction (`Y`);
   - the two drugs produce a experimentally validated combination (`N`).

 - `go-terms.tab`: Gene Ontology (GO) terms associated to each Human protein contained in `host-host.tab`. This file contains also other information regarding each GO term, as its GO ID, or its category (`Process`, `Function`, or `Component`).
 - `drug-structures.sdf`: drug Structure-Data File (SDF), from the open-data collection of [3]. This file contains the 3D structures of a subset of the drugs listed in `drug-host.tab` (i.e. the ones downloadable without registration).
 - `virus-host/*.tab`: collection of various Human viruses, from [4]. All the files in this folder contain the Virus-Virus, Virus-Human, and Human-Human PPIs related to a specific virus (e.g., SARS-CoV, SARS-CoV-2, MERS-CoV, HIV, etc). All proteins are denoted by their Entrez IDs.

## References

[1] Cheng, F., Kovács, I.A. & Barabási, A. Network-based prediction of drug combinations. Nat Commun 10, 1197 (2019), [https://doi.org/10.1038/s41467-019-09186-x](https://doi.org/10.1038/s41467-019-09186-x) \
[2] National Center for Biotechnology Information (NCBI), [https://www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/) \
[3] DrugBank, [https://www.drugbank.ca/](https://www.drugbank.ca/) \
[4] BioGrid, [https://thebiogrid.org/](https://thebiogrid.org/) 

