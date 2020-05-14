# COVID Datasets
A collection of COVID-related datasets useful for drug-repurposing tasks. See the [**Nomenclature**](#nomenclature) section for an explanation of the terms used.

## Content Summary

Apart from `drug-structures.sdf`, all data files are in TSV format (Tab-Separated Values), where the first line contains the column names. The file contents are:

 - `host-host.tab`: a collection of Human Protein-Protein Interactions, from [1].
 - `drug-host.tab`: a collection of experimentally validated Drug-Protein interaction, from [1].
 - `drug-drug.tab`: a collection of Drug-Drug interaction, from [1].
 - `go-terms.tab`: Gene Ontology (GO) terms associated to each Human protein contained in `host-host.tab`.
 - `drug-structures.sdf`: drug Structure-Data File (SDF), from the open-data collection of [3].
 - `virus-host/`: a collection of various Human viruses, from [4].
 - `disease-gene/`: a collection of disease-gene associations and mappings.
 - `uniprot_features/`: additional gene features gathered from UniProt [12]

In the `code` folder you will find the code used to create compact representations of the GO-terms. Instead, in the `GO_terms` folder you will find the generated clusters and embeddings.

## Content Details

This section describes the content of the files in the `data` folder.

#### `drug-drug.tab`
A collection of drug-drug combinations with the following columns:

- `DrugBankID_InteractorA` --> the DrugBank ID of the first drug
- `DrugBankID_InteractorB` --> the DrugBank ID of the second drug
- `Adverse` --> a boolean value `N` or `Y` where
    - `N`: the two drugs produce an experimentally validated combination
    - `Y`: the two drugs produce a clinically-reported adverse interaction

#### `drug-host.tab`
A collection of drug-protein interactions with the following columns:
- `DrugBankID` --> the DrugBank ID of the drug
- `EntrezGeneID` --> the Entrez ID of the gene associated with the protein targeted by the drug

#### `drug-structures.sdf`
The [SDF](https://en.wikipedia.org/wiki/Chemical_table_file) file of drug structures containing 10674 distinct drugs (11151 with aliases), and *almost* all the drugs listed in `drug-host.tab` (i.e. the ones downloadable with and without registration to the DrugBank service, that amount to 4283 of the 4428 drugs). This file contains the 2D structure of the drugs indexed by their DrugBank ID, providing also additional information such as:
- `Secondary Accession Numbers`
- `Common Name`
- `CAS Number`
- `Synonyms`

#### `go-terms.tab`
A collection of GO terms. There can be more than one GO term associated with a specific gene. The file has the following columns:
- `EntrezGeneID` --> the Entrez ID of the gene
- `GOID` --> the GO term ID associated with the gene
- `Evidence` --> the code that indicates how the annotation to a particular term is supported. For more information see the [official guide](http://geneontology.org/docs/guide-go-evidence-codes/).
- `Qualifier` --> the annotation qualifier. For more information see the [official guide](http://geneontology.org/docs/go-annotations/).
- `GOTerm` --> the name of the GO term
- `PubMed` --> the publication ID in the PubMed database [5].
- `Category` --> Can be `Function`, `Process` or `Component`

#### `host-host.tab`
A collection of drug-drug combinations with the following columns:

- `EntrezGeneID_InteractorA` --> the Entrez ID of the first gene
- `EntrezGeneID_InteractorB` --> the Entrez ID of the second gene


#### `virus-host/*.tab`

All the files in this folder contain the Virus-Virus, Virus-Human, and Human-Human PPIs related to a specific virus (e.g., SARS-CoV, SARS-CoV-2, MERS-CoV, HIV, etc).
All proteins are denoted by their Entrez IDs.
- `BioGRIDInteractionID` --> the BioGRID ID for the interaction
- `EntrezGeneID_InteractorA` --> the Entrez Gene database ID for Interactor A
- `EntrezGeneID_InteractorB` --> the Entrez Gene database ID for Interactor B
- `BioGRIDID_InteractorA` --> the BioGRID ID for Interactor A
- `BioGRIDID_InteractorB` --> the BioGRID ID for Interactor B
- `SystematicName_InteractorA` --> a plain text systematic name if known for Interactor A
- `SystematicName_InteractorB` --> a plain text systematic name if known for Interactor B
- `OfficialSymbol_InteractorA` --> a common gene name/official symbol for Interactor A
- `OfficialSymbol_InteractorB` --> a common gene name/official symbol for Interactor B
- `Synonyms_InteractorA` --> list of aliases for Interactor A
- `Synonyms_InteractorB` --> list of aliases for Interactor B
- `ExperimentalSystem` --> the [Experimental Evidence Codes](https://wiki.thebiogrid.org/doku.php/experimental_systems) supported by the BioGRID
- `ExperimentalSystemType` --> the type of the Experimental Evidence Codes
- `Author` --> the first author surname of the publication in which the interaction has been shown
- `PublicationSource` --> the publication source in which the interaction has been shown, with format `SOURCE:ID`
- `OrganismID_InteractorA` --> the NCBI Taxonomy ID for Interactor A
- `OrganismName_InteractorA` --> the NCBI Taxonomy Name for Interactor A
- `OrganismID_InteractorB` --> the NCBI Taxonomy ID for Interactor B
- `OrganismName_InteractorB` --> the NCBI Taxonomy Name for Interactor B
- `Throughput` --> the interaction throughput type: high, low, both
- `Score` --> the quantitative score recorded by the original publication depicting P-Values, Confidence Score, SGA Score, etc.
- `Modification` --> the Post Translational Modification for any Biochemical Activity experiments
- `Qualifications` --> additional plain text recorded for interaction
- `Tags` --> additional tag that classified the interaction
- `SourceDatabase` --> the database name in which the interaction was provided
- `SWISSPROTAccessions_InteractorA` --> one or more matching swiss-prot accessions for Interactor A
- `TREMBLAccessions_InteractorA` --> one or more matching trembl accessions for Interactor A
- `REFSEQAccessions_InteractorA` --> one or more matching refseq accessions for Interactor A
- `SWISSPROTAccessions_Interactor B` --> one or more matching swiss-prot accessions for Interactor B
- `TREMBLAccessions_InteractorB` --> one or more matching trembl accessions for Interactor B
- `REFSEQAccessions_InteractorB` --> one or more matching refseq accessions for Interactor B
- `OntologyTermIDs` --> the official ontology term ids, if ontology terms are recorded for the interaction
- `OntologyTermNames` --> the official ontology term name associated with the Ontology Term ID, if ontology terms are recorded for the interaction
- `OntologyTermCategories` --> the official ontology term category, if ontology terms are recorded for the interaction
- `OntologyTermQualifierIDs` --> additional qualifying term IDs associated with `TREMBL Accessions Interactor B`
- `OntologyTermQualifierNames` --> additional qualifying term names associated with `REFSEQ Accessions Interactor B`
- `OntologyTermTypes` --> additional types for terms classified as phenotypes


#### `disease-gene/disgenet/all_gene_disease_associations.zip`
This file contains the gene-disease associations of DisGeNET. See also [https://www.disgenet.org/dbinfo](https://www.disgenet.org/dbinfo). The columns are:

- `EntrezGeneID` --> NCBI Entrez Gene Identifier
- `GeneSymbol` --> Official Gene Symbol
- `DSI` -->	 the Disease Specificity Index for the gene
- `DPI` -->	the Disease Pleiotropy Index for the gene
- `DiseaseID` --> UMLS concept unique identifier
- `DiseaseName` --> name of the disease
- `DiseaseType` --> the DisGeNET disease type: disease, phenotype and group
- `DiseaseClass` --> the MeSH disease class(es)
- `DiseaseSemanticType` -->	the UMLS Semantic Type(s) of the disease
- `Score` --> DisGENET score for the Gene-Disease association (see https://www.disgenet.org/dbinfo)
- `EI` --> the Evidence Index for the Gene-Disease association
- `YearInitial` --> first time that the Gene-Disease association was reported
- `YearFinal` --> last time that the Gene-Disease association was reported
- `NofPmids` --> total number of publications reporting the Gene-Disease association
- `NofSnps` --> total number of SNPs associated to the Gene-Disease association
- `Source` --> original source reporting the Gene-Disease association

Note that:
- `DiseaseType` can be one of the following pathologies: "disease", "Group" (set of diseases), "phenotype"
- `Score` is confidence score in the range [0,1]
- `Source` indicates the sources related to the specific association (can be many)
- `NofPmids` is the number of evidences in the literature that report the specific association

#### `disease-gene/disgenet/disease_mappings.tab`
Mappings from UMLS concept unique identifier to disease vocabularies: DO, EFO, HPO, ICD9CM, MSH, NCI, OMIM, and ORDO. The columns are:
- `DiseaseID` --> UMLS concept unique identifier
- `Name` --> Name of the disease
- `Vocabulary` --> the name of the vocabulary in the range [DO, EFO, HPO, ICD9CM, MSH, NCI, OMIM, and ORDO]
- `Code` --> the id of DiseaseID in the vocabulary
- `VocabularyName` --> the name of DiseaseID in the vocabulary

#### `disease-gene/disgenet/uniprot2entrez.tab`
Mapping from UniProt knowledge base (UniProtKB) to genes Entrez IDs. The columns are:

- `UniProtKBID` --> UniProtKB Identifier
- `EntrezGeneID` --> the gene Entrez ID

#### `disease-gene/menche_disease_genes.tab`
This file contains the disease gene associations provided by [8]. Each line contains the genes (gene IDs) associated with one disease. The columns are:

- `DiseaseName` --> name of the disease
- `NumberOfAllGenes` --> number of all associated genes
- `NumberOfOMIMGenes` --> number of associated genes from OMIM
- `NumberOfGWASGenes` --> number of associated genes from GWAS
- `OMIMEntrezGeneIDs` --> comma-separated list of OMIM genes in Entrez IDs
- `GWASEntrezGeneIDs` --> comma-separated list of GWAS genes in Entrez IDs

#### `uniprot_features/domains.tab`
This file contains genes-domains and genes-families associations. Each line contains the genes associated with one or more domains and families. The columns are:

- `UniProtKBID` --> the UniProtKB Identifier
- `EntrezGeneID` --> the gene Entrez ID
- `GeneSymbol` --> Official Gene Symbol
- `Domain` --> semicolon-separated list of domains (see https://www.uniprot.org/help/domain)
- `ProteinFamilies` --> comma-separated list of families (see https://www.uniprot.org/help/family_membership)

#### `uniprot_features/gene-drug_associations.tab`
This file contains the gene-drug associations with the following columns:

- `UniProtKBID` --> the UniProtKB Identifier
- `EntrezGeneID` --> the gene Entrez ID
- `GeneSymbol` --> Official Gene Symbol
- `DrugBankIDs` --> semicolon-separated list of DrugBank IDs associated with the gene (see https://www.uniprot.org/database/DB-0019)

#### `uniprot_features/gene-pathways_associations.tab`
This file contains the gene-pathways associations. The columns are:

- `UniProtKBID` --> the UniProtKB Identifier
- `EntrezGeneID` --> the gene Entrez ID
- `GeneSymbol` --> Official Gene Symbol
- `ReactomeIDs` --> semicolon-separated list of [reactome](https://reactome.org/) pathways IDs associated with the gene


## Clustering and Node2vec: how-to

See [README](https://github.com/CLAIRE-COVID-T4/covid-data/tree/master/code#code-to-reproduce-node2vec-and-dbscan-analysis-of-go-terms) in the `code` folder.

#### GO_terms
This folder contains the result of the computation of the GO terms embeddings, with dimension 128, and clustering.
See [README](https://github.com/CLAIRE-COVID-T4/covid-data/tree/master/GO_terms#gene-ontology-go-terms-embeddings-and-clustering) in `GO_terms` for more information.

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
[14] dbSNP, [https://www.ncbi.nlm.nih.gov/snp/](https://www.ncbi.nlm.nih.gov/snp/) \
[15] Aditya, G., and Leskovec, J. node2vec: Scalable feature learning for networks. Proceedings of the 22nd ACM SIGKDD international conference on Knowledge discovery and data mining. 2016.

