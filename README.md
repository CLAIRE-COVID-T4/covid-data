# COVID Datasets
A collection of COVID-related datasets useful for drug-repurposing tasks. See the [**Nomenclature**](#nomenclature) section for an explanation of the terms used.

## Content Summary

Apart from `drug-structures.sdf`, all data files are in TSV format (Tab-Separated Values), where the first line contains the column names. The file contents are:

 - `host-host.tab`: a collection of Human Protein-Protein Interactions, from [1].
 - `drug-host.tab`: a collection of experimentally validated Drug-Protein interaction, from [1].
 - `drug-drug.tab`: a collection of Drug-Drug interaction, from [1].
 - `go-terms.tab`: Gene Ontology (GO) terms associated to each Human protein contained in `host-host.tab`.
 - `drug-structures.sdf`: drug Structure-Data File (SDF), from the open-data collection of [3].
 - `virus-host/*.tab`: a collection of various Human viruses, from [4].
 - `diseases/`: a collection of gene to disease mappings
 - `uniprot_features`: additional gene features gathered from UniProt [12]

In the `clustering` and `node2vec` folders you will find the code used to create compact representations of the GO-terms. 

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

All the files in this folder contain the Virus-Virus, Virus-Human, and Human-Human PPIs related to a specific virus (e.g., SARS-CoV, SARS-CoV-2, MERS-CoV, HIV, etc).
All proteins are denoted by their Entrez IDs.
- `BioGRID Interaction ID` --> the BioGRID ID for the interaction
- `Entrez Gene Interactor A` --> the Entrez Gene database ID for Interactor A
- `Entrez Gene Interactor B` --> the Entrez Gene database ID for Interactor B
- `BioGRID ID Interactor A` --> the BioGRID ID for Interactor A
- `BioGRID ID Interactor B` --> the BioGRID ID for Interactor B
- `Systematic Name Interactor A` --> a plain text systematic name if known for Interactor A
- `Systematic Name Interactor B` --> a plain text systematic name if known for Interactor B
- `Official Symbol Interactor A` --> a common gene name/official symbol for Interactor A
- `Official Symbol Interactor B` --> a common gene name/official symbol for Interactor B
- `Synonyms Interactor A` --> list of aliases for Interactor A
- `Synonyms Interactor B` --> list of aliases for Interactor B
- `Experimental System` --> the [Experimental Evidence Codes](https://wiki.thebiogrid.org/doku.php/experimental_systems) supported by the BioGRID
- `Experimental System Type` --> the type of the Experimental Evidence Codes
- `Author` --> the first author surname of the publication in which the interaction has been shown
- `Publication Source` --> the publication source in which the interaction has been shown, with format `SOURCE:ID`
- `Organism ID Interactor A` --> the NCBI Taxonomy ID for Interactor A
- `Organism Name Interactor A` --> the NCBI Taxonomy Name for Interactor A
- `Organism ID Interactor B` --> the NCBI Taxonomy ID for Interactor B
- `Organism Name Interactor B` --> the NCBI Taxonomy Name for Interactor B
- `Throughput` --> the interaction throughput type: high, low, both
- `Score` --> the quantitative score recorded by the original publication depicting P-Values, Confidence Score, SGA Score, etc.
- `Modification` --> the Post Translational Modification for any Biochemical Activity experiments
- `Qualifications` --> additional plain text recorded for interaction
- `Tags` --> additional tag that classified the interaction
- `Source Database` --> the database name in which the interaction was provided
- `SWISS-PROT Accessions Interactor A` --> one or more matching swiss-prot accessions for Interactor A
- `TREMBL Accessions Interactor A` --> one or more matching trembl accessions for Interactor A
- `REFSEQ Accessions Interactor A` --> one or more matching refseq accessions for Interactor A
- `SWISS-PROT Accessions Interactor B` --> one or more matching swiss-prot accessions for Interactor B
- `TREMBL Accessions Interactor B` --> one or more matching trembl accessions for Interactor B
- `REFSEQ Accessions Interactor B` --> one or more matching refseq accessions for Interactor B
- `Ontology Term IDs` --> the official ontology term ids, if ontology terms are recorded for the interaction
- `Ontology Term Names` --> the official ontology term name associated with the Ontology Term ID, if ontology terms are recorded for the interaction
- `Ontology Term Categories` --> the official ontology term category, if ontology terms are recorded for the interaction
- `Ontology Term Qualifier IDs` --> additional qualifying term IDs associated with `TREMBL Accessions Interactor B`
- `Ontology Term Qualifier Names` --> additional qualifying term names associated with `REFSEQ Accessions Interactor B`
- `Ontology Term Types` --> additional types for terms classified as phenotypes


#### `diseases/disgenet/curated_gene_disease_associations.tab`
This file contains Gene-Disease associations from various resources such as UniProt, CGI, ClinGen, Genomics England Panel App, PsyGeNET, Orphanet, the HPO, and CTD (human data). See also [https://www.disgenet.org/dbinfo](https://www.disgenet.org/dbinfo). The columns are:

- `geneId` --> NCBI Entrez Gene Identifier
- `geneSymbol` --> Official Gene Symbol
- `DSI` -->	 the Disease Specificity Index for the gene
- `DPI` -->	the Disease Pleiotropy Index for the gene
- `diseaseId` --> UMLS concept unique identifier
- `diseaseName` --> name of the disease	
- `diseaseType` --> the DisGeNET disease type: disease, phenotype and group
- `diseaseClass` --> the MeSH disease class(es)
- `diseaseSemanticType` -->	the UMLS Semantic Type(s) of the disease
- `score` --> DisGENET score for the Gene-Disease association (see https://www.disgenet.org/dbinfo)
- `EI` --> the Evidence Index for the Gene-Disease association
- `YearInitial` --> first time that the Gene-Disease association was reported
- `YearFinal` --> last time that the Gene-Disease association was reported
- `NofPmids` --> total number of publications reporting the Gene-Disease association
- `NofSnps` --> total number of SNPs associated to the Gene-Disease association
- `source` --> original source reporting the Gene-Disease association

Note that:
- `diseaseType` can be one of the following pathologies: "disease", "Group" (set of diseases), "phenotype" (malformations)
- `score` is confidence score in the range [0,1]
- `source` indicates the sources related to the specific association (can be many)
- `NofPmids` is the number of evidences in the literature that report the specific association

#### `diseases/disgenet/disease_mappings.tab`
Mappings from UMLS concept unique identifier to disease vocabularies: DO, EFO, HPO, ICD9CM, MSH, NCI, OMIM, and ORDO. The columns are:
- `snpId` --> dbSNP variant Identifier
- `geneId` --> NCBI Entrez Gene Identifier
- `geneSymbol` --> Official Gene Symbol

#### `diseases/disgenet/variant_to_gene_mappings.tab`
Variants mapped to their corresponding genes, according to dbSNP. The columns are:
- `snpId` --> dbSNP variant Identifier
- `geneId` --> NCBI Entrez Gene Identifier
- `geneSymbol` --> Official Gene Symbol

#### `diseases/disgenet/entrez2uniprot.tab`
Mapping from UniProt knowledge base (UniProtKB) to genes Entrez IDs. The columns are:

- `UniProtKB` --> UniProtKB Identifier
- `GENEID` --> the gene Entrez ID

#### `diseases/menche_disease_genes.tab`
This file contains the disease gene associations provided by [8]. Each line contains the genes (gene IDs) associated with one disease. The columns are:

- `disease` --> name of the disease
- `number_of_all_genes` --> number of all associated genes
- `number_of_OMIM_genes` --> number of associated genes from OMIM
- `number_of_GWAS_genes` --> number of associated genes from GWAS
- `OMIM_genes` --> comma-separated list of OMIM genes
- `GWAS_genes` --> comma-separated list of GWAS genes

#### `uniprot_features/domains.tab`
This file contains genes-domains and genes-families associations. Each line contains the genes associated with one or more domains and families. The columns are:

- `Entry` --> the UniProtKB Identifier
- `Entrez ID` --> the gene Entrez ID
- `Entry name` --> the gene name
- `Domain [FT]` --> semicolon-separated list of domains
- `Protein families` --> comma-separated list of families

#### `uniprot_features/gene-drug_associations.tab`
This file contains the gene-drug associations with the following columns:

- `Entry` --> the UniProtKB Identifier
- `Entrez ID` --> the gene Entrez ID
- `Entry name` --> the gene name
- `DrugBank` --> list of DrugBank IDs associated with the gene

#### `uniprot_features/gene-pathways_associations.tab`
This file contains the gene-pathways associations. The columns are:

- `Entry` --> the UniProtKB Identifier
- `Entrez ID` --> the gene Entrez ID
- `Entry name` --> the gene name
- `Reactome` --> list of [reactome](https://reactome.org/) pathways IDs associated with the gene


## Clustering: how-to

To reproduce the procedure that generates clusters of the GO-terms, please do as follows:

##TODO

## Node2vec: how-to

To reproduce the procedure that generates GO-terms embeddings using node2vec, please do as follows:

##TODO

## Nomenclature

- CAS Number: a unique numerical identifier assigned by the Chemical Abstracts Service (CAS) to every chemical substance described in the open scientific literature.
- DrugBank ID: the identifier of a drug in the DrugBank database [3].
- Entrez ID: the identifier of a gene in the NCBI Entrez database [7].
- Gene-Ontology (GO) term: identifier of an entry in the Gene Ontology database [6], which contains information on the functions of genes.
- Secondary Accession Numbers: additional identifiers for the same drug.
- Structure-Data File (SDF): a [standardized format](https://en.wikipedia.org/wiki/Chemical_table_file) to represent the 3d structure of a compound. It wraps the [MDL Molfile](https://en.wikipedia.org/wiki/Chemical_table_file#Molfile) format.
- PPI: Protein-Protein Interactions.
- PubMed: Biomedical literature database service [5].
- OMIM: Online Mendelian Inheritance in Man catalog service [9].
- GWAS: Genome-Wide Association Studies catalog service [10].
- DisGeNET: a discovery platform integrating information on gene-disease associations from several public data sources and the literature [11].
- UniProt: a database of protein sequence and functional information, many entries being derived from genome sequencing projects [12].
- Evidence: see [Experimental Evidence Codes](https://wiki.thebiogrid.org/doku.php/experimental_systems)
- UMLS: Unified Medical Language System [13]
- dbSNP: Single Nucleotide Polymorphism Database [14]

## References

[1] Cheng, F., Kovács, I.A. and Barabási, A. Network-based prediction of drug combinations. Nat Commun 10, 1197 (2019), [https://doi.org/10.1038/s41467-019-09186-x](https://doi.org/10.1038/s41467-019-09186-x) \
[2] National Center for Biotechnology Information (NCBI), [https://www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/) \
[3] DrugBank, [https://www.drugbank.ca/](https://www.drugbank.ca/) \
[4] BioGrid, [https://thebiogrid.org/](https://thebiogrid.org/) \
[5] PubMed, [https://pubmed.ncbi.nlm.nih.gov/](https://pubmed.ncbi.nlm.nih.gov/) \
[6] Gene Ontology, [http://geneontology.org/](http://geneontology.org/) \
[7] NCBI , [https://www.ncbi.nlm.nih.gov/gene](https://www.ncbi.nlm.nih.gov/gene) \
[8] Menche, J., Sharma, A., Kitsak, M., Ghiassian, S. D., Vidal, M., Loscalzo, J., and Barabási, A. Uncovering Disease-Disease Relationships Through The Human Interactome \
[9] OMIM, [https://www.omim.org/](https://www.omim.org/) \
[10] GWAS, [https://www.ebi.ac.uk/gwas/](https://www.ebi.ac.uk/gwas/) \
[11] DisGeNET, [http://www.disgenet.org](http://www.disgenet.org) \
[12] UniProt, [https://www.uniprot.org/](https://www.uniprot.org/) \
[13] UMLS, [https://www.nlm.nih.gov/research/umls/index.html](https://www.nlm.nih.gov/research/umls/index.html) \
[14] dbSNP, [https://www.ncbi.nlm.nih.gov/snp/](https://www.ncbi.nlm.nih.gov/snp/)

