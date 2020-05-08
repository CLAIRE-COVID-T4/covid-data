# COVID Datasets
A collection of COVID-related datasets useful for drug-repurposing tasks. See the [**Nomenclature**](#nomenclature) section for an explanation of the terms used.

## Content Summary

Apart from `drug-structures.sdf`, All files are in TSV format (Tab-Separated Values), where the first line contains the column names. The file contents are:

 - `host-host.tab`: a collection of Human Protein-Protein Interactions, from [1].
 - `drug-host.tab`: a collection of experimentally validated Drug-Protein interaction, from [1].
 - `drug-drug.tab`: a collection of Drug-Drug interaction, from [1].
 - `go-terms.tab`: Gene Ontology (GO) terms associated to each Human protein contained in `host-host.tab`.
 - `drug-structures.sdf`: drug Structure-Data File (SDF), from the open-data collection of [3].
 - `virus-host/*.tab`: collection of various Human viruses, from [4].


## Content Details

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

#### `go-terms.tab`
A collection of GO terms. There can be more than one GO term associated with a specific gene. The file has the following columns:
- `Entrez Gene` --> the Entrez ID of the gene
- `GO ID` --> the GO term ID associated with the gene
- `Evidence` --> the code that indicates how the annotation to a particular term is supported. For more information see the [official guide](http://geneontology.org/docs/guide-go-evidence-codes/).
- `Qualifier` --> the annotation qualifier. For more information see the [official guide](http://geneontology.org/docs/go-annotations/).
- `GO Term` --> the name of the GO term
- `PubMed` --> the publication ID in the PubMed database [5]. 
- `Category` --> Can be `Function`, `Process` or `Component`

#### `host-host.tab`
A collection of drug-drug combinations with the following columns:

- `Entrez Gene Interactor A` --> the Entrez ID of the first gene
- `Entrez Gene Interactor B` --> the Entrez ID of the second gene 


#### `virus-host/*.tab`

All the files in this folder contain the Virus-Virus, Virus-Human, and Human-Human PPIs related to a specific virus (e.g., SARS-CoV, SARS-CoV-2, MERS-CoV, HIV, etc). All proteins are denoted by their Entrez IDs.

## Nomenclature

- CAS Number: a unique numerical identifier assigned by the Chemical Abstracts Service (CAS) to every chemical substance described in the open scientific literature.
- DrugBank ID: the identifier of a drug in the DrugBank database [3].
- Entrez ID: the identifier of a gene in the NCBI Entrez database [7].
- Gene-Ontology (GO) term: identifier of an entry in the Gene Ontology database [6], which contains information on the functions of genes.
- Secondary Accession Numbers: additional identifiers for the same drug.
- Structure-Data File (SDF): a [standardized format](https://en.wikipedia.org/wiki/Chemical_table_file) to represent the 3d structure of a compound. It wraps the [MDL Molfile](https://en.wikipedia.org/wiki/Chemical_table_file#Molfile) format.
- PPI: Protein-Protein Interactions.
- PubMed: Biomedical literature database service [5].

## References

[1] Cheng, F., Kovács, I.A. & Barabási, A. Network-based prediction of drug combinations. Nat Commun 10, 1197 (2019), [https://doi.org/10.1038/s41467-019-09186-x](https://doi.org/10.1038/s41467-019-09186-x) \
[2] National Center for Biotechnology Information (NCBI), [https://www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/) \
[3] DrugBank, [https://www.drugbank.ca/](https://www.drugbank.ca/) \
[4] BioGrid, [https://thebiogrid.org/](https://thebiogrid.org/) \
[5] PubMed, [https://pubmed.ncbi.nlm.nih.gov/](https://pubmed.ncbi.nlm.nih.gov/) \
[6] Gene Ontology, [http://geneontology.org/](http://geneontology.org/) \
[7] NCBI , [https://www.ncbi.nlm.nih.gov/gene](https://www.ncbi.nlm.nih.gov/gene)

