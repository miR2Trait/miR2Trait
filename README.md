# miR2Trait
An integrated resource for investigating miRNA - disease associations

1) curated.csv --> Source data from DisGeNET for Gene <-> disease mappings

6) miR.csv--> Source data from miRTarBase for the miRNA:Gene mapping

4) Dis.py -> Gene:disease mapping from ; outputs a dictionary of the mapping

5) Dis_inv.py--> Disease:gene mapping from DisGeNET; outputs a dictionary of the mapping

7) n_inverted.py --> Gene:miRNA mapping from miRTarBase; outputs a dictionary of the mapping

8) Nn.py --> miRNA:gene mapping from miRTarBase; outputs a dictionary of the mapping

2) d1.py --> miRNA:Disease mapping and the mapping is saved in miRNA-Disease.pkl format
miRNA-Disease.pkl: a Pickle-d file of the miRNA-Disease mapping from d1.py

3) D1-disease --> Generates Disease-miRNA mapping and the mapping is saved in Disease-miRNA.pkl format
Disease-miRNA.pkl: a Pickle-d file of the Disease-miRNA mapping from 
