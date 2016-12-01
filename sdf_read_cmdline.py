# RAK Sept. 2014. python program to process sdf files.
# bz R.K. Rolling, edited bz Heinen Stefan

# For command-line arguments
import sys
from sys import argv

if len(argv) < 4:
   print "\n ** Syntax is: python sdf_read.py filename.sdf MOLECULE PROP [PROP2...]"
   print "\n  MOLECULE may be ALL or an index (1,2...) or an sdf label (19HC_ACT_A_293,...)"
   print "\n  PROP may be GEOM, CHARGE, NATOM, NAME, XYZ, NUM_MOLECULES or any property in"
   print "\n  sdf file such as:"
   print "   InstanceId Type InChIKey Synonyms Model GENERIC_NAME PdbId"
   print "   AmbiguousFlag DRUG_GROUPS ResidueNumber SYNONYMS InChI MolecularWeight"
   print "   MissingHeavyAtoms ModifiedDate SMILES ChemCompId DRUGBANK_ID ChainId\n"
   quit()

sdf_filename = sys.argv[1]
sdf_geom = sys.argv[2]
sdf_prop = sys.argv[3:]

from sdf_read import read

read(sdf_filename, sdf_geom, sdf_prop)

