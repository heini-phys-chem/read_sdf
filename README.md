# read_sdf

A python script to extract information from .sdf files,
by Rolling King edited by Heinen Stefan

Syntax is: python sdf_read.py filename.sdf MOLECULE PROP [PROP2...]

MOLECULE may be ALL or an index (1,2...) or an sdf label (19HC_ACT_A_293,...)

PROP may be GEOM, CHARGE, NATOM, NAME, XYZ, NUM_MOLECULES or any property in

sdf file such as:
InstanceId Type InChIKey Synonyms Model GENERIC_NAME PdbId
AmbiguousFlag DRUG_GROUPS ResidueNumber SYNONYMS InChI MolecularWeight
MissingHeavyAtoms ModifiedDate SMILES ChemCompId DRUGBANK_ID ChainId
