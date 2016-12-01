# read_sdf
a python program to extract information out of .sdf files

Syntax is: python sdf_read.py filename.sdf MOLECULE PROP [PROP2...]

MOLECULE may be ALL or an index (1,2...) or an sdf label (19HC_ACT_A_293,...)

PROP may be GEOM, CHARGE, NATOM, NAME, XYZ, NUM_MOLECULES or any property in

sdf file such as:
InstanceId Type InChIKey Synonyms Model GENERIC_NAME PdbId
AmbiguousFlag DRUG_GROUPS ResidueNumber SYNONYMS InChI MolecularWeight
MissingHeavyAtoms ModifiedDate SMILES ChemCompId DRUGBANK_ID ChainId
