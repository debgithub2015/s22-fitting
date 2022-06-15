from ase import io
from numpy import *
import sys


NUM = int(sys.argv[1])
#i = 15


splitList = [4, 3, 5 , 6, 12, 12, 15, 5, 6, 12, 12, 10, 12, 12, 15, 6, 12, 12, 12, 12, 12, 13]

#sep_list = [-0.8, -0.4,-0.3,  -0.2, -0.15, -0.1, -0.05, -0.025, 0.0, 0.025,0.05, 0.075, 0.1, 0.125,  0.15, 0.175,  0.2, 0.225, 0.25,0.275, 0.3, 0.325,0.35,0.375, 0.4,0.45,0.5,0.6,0.65, 0.7, 1.0,  1.5,  2.0,   3.0, 5.0]  


def create_in_file(NUM,i):

  in_filename = 'S22x5_%02d_%02d_RefA.in'%(NUM,i)
  split = splitList[NUM-1]
#  shift = sep_list[i]
  ref_filename = "/deac/thonhauserGrp/chakrad/calculations/database-calc/s22x5/xyz_files/s%02d_05.xyz"%NUM

  atoms_ref= io.read(ref_filename)

  positions = atoms_ref.get_positions()
  posX = positions[:,0]
  posY = positions[:,1]
  posZ = positions[:,2]
  DeltaX = max(posX) - min(posX)
  DeltaY = max(posY) - min(posY)
  DeltaZ = max(posZ) - min(posZ)
  cell = (20+DeltaX,20+DeltaY,DeltaZ+20)
  atoms_ref.set_cell(cell)


  atoms_ref.center()

  atoms1 = atoms_ref[0:split]
  atoms2 = atoms_ref[split:]

#  print 'atoms1',atoms1
#  Delta = atoms2.get_center_of_mass() - atoms1.get_center_of_mass()
#  print 'Delta',Delta
#  Dist = sqrt(sum(Delta**2))
#  unit = Delta/Dist
#  #print 'pos2',atoms_core.get_positions()
#  atoms2.translate((-5+shift)*unit)

  atoms1.write('atoms1.xyz')
  Natoms = atoms1.get_number_of_atoms()

  types_atoms = set(atoms1.get_chemical_symbols())
  Ntyp = len(types_atoms)


  cell33 = atoms1.get_cell()
  #atoms.write('atoms.xyz

  text_control='''&control
    calculation='nscf'
    pseudo_dir ='/deac/thonhauserGrp/chakrad/calculations/database-calc/s22x5-density/S22-optb88-rutgers/pseudodir'
    outdir ='/deac/thonhauserGrp/chakrad/calculations/database-calc/s22x5-density/S22-optb88-rutgers/pseudodir' 
    nstep = 10
    prefix='S22x5_%02d_%02d_RefA'
    max_seconds=82000
    verbosity='high'
    forc_conv_thr=3d-3
   /'''%(NUM,i)

  text_system = '''
    &system
    ibrav=0
    nat = %i
    ntyp= %i
    ecutwfc = 50.0
    ecutrho = 600.0
    input_dft = 'sla pw obk8 vdW1'
  /'''%(Natoms,Ntyp)

  text_misc='''
  &electrons
    diagonalization='cg'
    diago_cg_maxiter=100
    conv_thr =  1.0d-6
  /'''

  text_species='''
  ATOMIC_SPECIES
'''
  if 'H' in types_atoms:
    text_species += 'H  1.0    h_pbe_v1.4.uspp.F.UPF\n'
  if 'N' in types_atoms:
    text_species += 'N  1.0    n_pbe_v1.2.uspp.F.UPF\n'
  if 'C' in types_atoms:
    text_species += 'C  1.0    c_pbe_v1.2.uspp.F.UPF\n'
  if 'O' in types_atoms:
    text_species +=  'O  1.0   o_pbe_v1.2.uspp.F.UPF\n'
  text_species += '   K_POINTS gamma'


  input_cell = list(cell33[0])+list(cell33[1])+list(cell33[2])

  text_cell='''
  CELL_PARAMETERS angstrom
  %1.6f\t %1.6f\t %1.6f
  %1.6f\t %1.6f\t %1.6f
  %1.6f\t %1.6f\t %1.6f
  '''%(tuple(input_cell))

  text_atomic_pos="ATOMIC_POSITIONS angstrom\n"
  file = open('atoms1.xyz','r')
  content = file.readlines()
  file.close()

  for line in content[2:]:
    text_atomic_pos += line

  full_text = text_control + text_system + text_misc + text_species+ text_cell + text_atomic_pos

  print full_text

  file = open(in_filename,'w')
  file.write(full_text)
  file.close()

for i in range(0,1):
  create_in_file(NUM,i)
