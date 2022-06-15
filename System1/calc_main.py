import os
import sys


NUM = int(sys.argv[1])
start = int(sys.argv[2])
slutt = int(sys.argv[3])
mypwx='/deac/thonhauserGrp/chakrad/quantum-espresso-6.3/qe-6.3-openmpi-3.1.1/bin/pw.x'
 
for i in range(start,slutt):
   in_filename = 'S22x5_%02d_%02d.in'%(NUM,i)
   res_filename = in_filename.split('.')[0]+'.txt'
   print res_filename
   os.popen('mpirun %s < %s > %s' %(mypwx,in_filename,res_filename))

