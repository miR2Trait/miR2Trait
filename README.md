# miR2Trait
An integrated resource for investigating miRNA - disease associations

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7002878.svg)](https://doi.org/10.5281/zenodo.7002878)

The code and data comprising the **miR2Trait** resource are described in the [miR2Trait wiki](https://github.com/miR2Trait/miR2Trait/wiki). All code is developed using Python 3.x

## Code wikis:
1. [Creating Python dictionary data structures of processed DisGeNET data](https://github.com/miR2Trait/miR2Trait/wiki/Dictionaries-of-processed-DisGeNET-data)
2. [Creating Python dictionary data structures of processed miRTarBase data](https://github.com/miR2Trait/miR2Trait/wiki/Dictionaries-of-processed-miRTarBase-data)
3. [Generating the miR2Trait db mappings](https://github.com/miR2Trait/miR2Trait/wiki/Creating-the-miR2Trait-database-mappings)
4. [Querying miR2Trait by disease](https://github.com/miR2Trait/miR2Trait/wiki/miR2Trait:-Query-by-disease)
5. [Querying miR2trait by miRNA](https://github.com/miR2Trait/miR2Trait/wiki/miR2Trait:-Query-by-miRNA)
6. [miRNA List Enrichment Analysis](https://github.com/miR2Trait/miR2Trait/wiki/miRNA-List-Enrichment-Analysis)
7. [Disease Set Abundance Analysis](https://github.com/miR2Trait/miR2Trait/wiki/Disease-Set-Abundance-Analysis)
8. [Creation of miRNA-miRNA and disease-disease adjacency networks](https://github.com/miR2Trait/miR2Trait/wiki/Adjacency-Network-creation-for-miRNAs-and-Diseases)
9. [Top Nodes from Adjacency Networks](https://github.com/miR2Trait/miR2Trait/wiki/Top-Nodes-from-Adjacency-Networks) -- Network post-processing to yield consensus central nodes 
10. [Querying miRNA information from miRBase](https://github.com/miR2Trait/miR2Trait/wiki/Querying-miRNA-information-from-miRBase)
11. [Creating a toy MySQLdb](https://github.com/miR2Trait/miR2Trait/wiki/Creating-a-MySQLdb:-toy-example)

## Data wikis:
1. [Processed Source data](https://github.com/miR2Trait/miR2Trait/wiki/Data::Processed-Source-data)
2. [miR2Trait mappings](https://github.com/miR2Trait/miR2Trait/wiki/Data::pickled-mappings)
3. [Spectrum widths](https://github.com/miR2Trait/miR2Trait/wiki/Data::Spectrum-widths)
4. [Adjacency networks](https://github.com/miR2Trait/miR2Trait/wiki/Data::Adjacency-Networks)
5. [Human miRNA catalog](https://github.com/miR2Trait/miR2Trait/wiki/Data::miRBase_human)

### Dependencies:
Following Python 3.x libraries are required:
- pandas
- scipy
- pickle
- mysql-connector-python (optional: for creation of MySQL db)

**For more details, reproducible examples, and citation, please see**: 

Babu P, Palaniappan A. 2022. miR2Trait: an integrated resource for investigating miRNA-disease associations. PeerJ 10:e14146 https://doi.org/10.7717/peerj.14146

E-mail: apalania.at.scbt.sastra.edu
