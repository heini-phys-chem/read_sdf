# read_sdf

A python script to extract information from .sdf files,
by Rolling King edited by Heinen Stefan

Command line should look like:
```
python sdf_read.py <filename>.sdf MOLECULE PROP [PROP2...]
```
##### MOLECULE 
Defines which molecule or molecules will be extracted. Possible keywords:
```
ALL
index (1,2...)
sdf label (19HC_ACT_A_293,...) 
```
#### PROP 
Which property you want to extract
```
GEOM
CHARGE
NATOM
NAME
XYZ
NUM_MOLECULES 
```
or any property in sdf file such as: <br\>
InstanceId Type InChIKey Synonyms Model GENERIC_NAME PdbId <br\>
AmbiguousFlag DRUG_GROUPS ResidueNumber SYNONYMS InChI MolecularWeight <br\>
MissingHeavyAtoms ModifiedDate SMILES ChemCompId DRUGBANK_ID ChainId <br\>
