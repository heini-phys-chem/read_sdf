# RAK Sept. 2014. python program to process sdf files.

# Tell whether string may be converted to int
def is_integer(s):
   try:
      int(s)
      return True
   except ValueError:
      return False


# Class for an atom containing charge and coordinates.
class atom(object):
   def __init__(self, Z, x, y, z):   # Constructor function
      self.Z = Z
      self.x = x
      self.y = y
      self.z = z
      self.charge = 0

   def set_charge(self, q1):         # Set charge on atom
      self.charge = q1


# Class for a molecule/entry in sdf file.
class molecule(object):

   def __init__(self):               # Constructor function
      self.atom_list = []             # atoms
      self.label = ""                 # label from sdf 1st line
      self.properties = { } ;         # dict to hold properties

   def __repr__(self):               # allows python print to work on objects
      print "Label: %s" % self.label

      print "Molecular Geometry:"
      self.print_geom()

      print "Charges of Atoms:"
      for a in self.atom_list:
        print "%4s%4d" % (a.Z, a.charge)

      print "Total Charge: %d" % self.get_charge()

      print "Properties (%d)" % len(self.properties)
      for i in self.properties.items():
        print "\t%-25s%s" % (i[0],i[1])
      return ""

   def get_charge(self):      # Sum up total charge.
      q = 0
      for a in self.atom_list:
         q += a.charge
      return q

   def get_natom(self):       # Get total number of atoms.
      return len(self.atom_list)

   def add_atom(self, atom):  # Add atom to molecule
      self.atom_list.append(atom)

   def get_nH(self):          # Get number of H atoms.
      nH = 0
      for a in self.atom_list:
         if a.Z == "H":
           nH += 1
      return nH

   def get_nNoH(self):        # Get number of non H atoms.
      return self.get_natom() - self.get_nH()

   def set_label(self, l):    # Set label for molecule.
      self.label = l

   def print_geom(self):      # Print geometry.
      for a in self.atom_list:
         print "%s%15.5f%15.5f%15.5f" % (a.Z, a.x, a.y, a.z)

   def print_tm_geom(self):      # Print geometry.
      s = 1.0/0.52917721092
      for a in self.atom_list:
         print "%20.14f%20.14f%20.14f%7s" % (a.x*s, a.y*s, a.z*s, a.Z)

molecule_list = []

# Function to find the index for a given molecule label
def molecule_list_index_from_label(lbl):
   for i in range(len(molecule_list)):
      if molecule_list[i].label == lbl:
         return i
   raise IndexError

def read(sdf_filename, sdf_geometry, sdf_property):

   # Read whole file into one string.
   sdf_file = open(sdf_filename, 'r').read()
   
   # Separate by $$$$ into string entries.  Delimiter is omitted.
   sdf_entries = sdf_file.split('$$$$\n')
   del sdf_entries[-1]   # Delete last empty entry, created by split.
   
   # Loop over molecular entries.
   for entry in sdf_entries:
   
      # Split string block into lines in a list.
      block = entry.split('\n')
      one_mol = molecule()  # create (empty molecule)
   
      for line in range(len(block)):
   
         w1 = block[line][0:3] #Ugh. Need 1st 3 characters to read number of atoms, when 1st 2 entries merge.
   
         # Split line.  Remove extra white space.
         words_init = [x.strip() for x in block[line].split(' ')]
         words = filter(None, words_init)  # Remove any empty entries.
   
         if line == 0:
            lbl = words[0]
            one_mol.set_label(lbl)
   
         elif line == 1:
            if words[1] != "3D":
               print "Warning: 3D not found"
   
         elif line == 2:
            pass
   
         elif line == 3:
            natom = int(w1)  # must use w1 for cases where natom > 100 in sdf
            still_geom_section = True
   
         elif line >= 4 and line < natom+4:
            one_atom = atom(words[3], float(words[0]), float(words[1]), float(words[2]))
            one_mol.add_atom(one_atom)
   
         elif still_geom_section:
            if len(words) > 1 and words[0] == 'M':
               if words[1] == "CHG":
                  one_mol.atom_list[int(words[3])].set_charge(int(words[4]))
               elif words[1] == "END":
                  still_geom_section = False
      
         else:
            if len(words) > 1 and words[0] == '>':
               prop_name = words[1]
            elif len(words) == 0:
               pass
            else:        # remove < and > in property string
               one_mol.properties[prop_name[1:-1]] = block[line]
    
      molecule_list.append(one_mol)
   
   
   # Make list of molecule indices for which to output data
   indices_to_print = []
   
   if sdf_geometry.upper() == 'ALL':
      indices_to_print = range(len(molecule_list))
   
   elif is_integer(sdf_geometry):  # use integer index to identify molecule
      i = int(sdf_geometry)-1
      try: 
         if i < 0 or i >= len(molecule_list):
            raise IndexError
         indices_to_print.append(i)
      except IndexError:
         print "Molecule index (1,2,...) is invalid.  List has %d entries." % len(molecule_list)
         quit()
   
   else:                      # use label to identify molecule
      try:
         i = molecule_list_index_from_label(sdf_geometry)
         indices_to_print.append(i)
      except IndexError:
         print "Label %s not found in molecule_list" % sdf_geometry
         quit()

   for prop in sdf_property:
     if prop == "NUM_MOLECULES":
       print len(molecule_list)
   
   # Print out requested properties
   for i in indices_to_print:
   
      for prop in sdf_property:
   
         if prop.upper() == 'ALL':
            print molecule_list[i],
   
         elif prop.upper() == 'GEOM':
            molecule_list[i].print_geom()

         elif prop.upper() == 'TM_GEOM':
            molecule_list[i].print_tm_geom()
     
         elif prop.upper() == 'CHARGE':
            print molecule_list[i].get_charge()
     
         elif prop.upper() == 'NATOM':
            print molecule_list[i].get_natom()
   
         elif prop.upper() == 'NAME':
            print molecule_list[i].label
   
         elif prop.upper() == 'XYZ':
            print "%5d" % molecule_list[i].get_natom()
            print "%s" % molecule_list[i].label
            molecule_list[i].print_geom()

         elif prop.upper() == 'NUM_MOLECULES':
            pass
     
         else:
            print molecule_list[i].properties[prop]

