import sys
from numpy import *


Ryd = 13.6057*1000

Num = int(sys.argv[1])


Eval = zeros(35)
ErefA = 0
ErefB = 0

for i in range(35):
#   print "System%i/S22_%02d_%02d.txt"%(Num,Num,i)
#   file = open("System%i_norm/S22_%02d_%02d.txt"%(Num,Num,i))
   file = open("System%i/S22_%02d_%02d.txt"%(Num,Num,i))
   content = file.readlines()
   file.close()
   for line in content:
     if '!' in line:
       val=float(line.split()[-2])
       Eval[i] = val


imin = Eval.argmin()
#file = open("System%i_norm/S22_%02d_00_RefA.txt"%(Num,Num))
file = open("System%i/S22_%02d_00_RefA.txt"%(Num,Num))
content = file.readlines()
file.close()
for line in content:
  if '!' in line:
     ErefA = float(line.split()[-2])
     print ErefA
#file = open("System%i_norm/S22_%02d_00_RefB.txt"%(Num,Num))
file = open("System%i/S22_%02d_00_RefB.txt"%(Num,Num))
content = file.readlines()
file.close()
for line in content:
  if '!' in line:
     ErefB = float(line.split()[-2])
     
     print ErefB


#print 'B',ErefB
#
#print 'val',Eval
sep_list = [-0.8, -0.4,-0.3,  -0.2, -0.15, -0.1, -0.05, -0.025, 0.0, 0.025,0.05, 0.075, 0.1, 0.125,  0.15, 0.175,  0.2, 0.225, 0.25,0.275, 0.3, 0.325,0.35,0.375, 0.4,0.45,0.5,0.6,0.65, 0.7, 1.0,  1.5,  2.0,   3.0, 5.0]  

print repr((Eval - ErefA-ErefB )*Ryd)
print sep_list[imin],'\t', (Eval[imin] - ErefA-ErefB )*Ryd

Epred =  (Eval[imin] - ErefA-ErefB )*Ryd

print Epred

from ase.data.s22 import s22, get_interaction_energy_s22
EQC = get_interaction_energy_s22(s22[Num-1])
print 'QC energy', EQC*1000

print (Epred-(EQC*1000))/(EQC*1000)
