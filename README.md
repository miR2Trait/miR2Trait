# miR2Trait
An integrated resource for investigating miRNA - disease associations

1) curated.csv --> Source data from DisGeNET for Gene <-> Disease mappings

2) miR.csv --> Source data from miRTarBase for the miRNA <-> Gene mappings

3) Dis.py -> Python script to produce a dictionary of gene:disease mapping from curated.csv

4) Dis_inv.py--> Python script to produce a dictionary of disease:gene mapping from curated.csv

5) mir.py --> Python script to produce a dictionary of miRNA:gene mapping from miR.csv

6) mir_inv.py --> Python script to produce a dictionary of gene:miRNA mapping from miR.csv

7) miRDis.py --> Python script that integrates the dictionaries of mir.py and dis.py to obtain miRNA:Disease mapping 

8) Dis_miR.py --> Python script that integrates the dictionaries of mir_inv.py and dis_inv.py to obtain  Disease-miRNA mapping 

9) miRNA-Disease.pkl: Pickle-d file of the miRNA-Disease mapping from miRDis.py

10) Disease-miRNA.pkl: Pickle-d file of the Disease-miRNA mapping from Dis_miR.py
