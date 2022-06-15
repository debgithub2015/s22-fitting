import os
import sys


NUM = int(sys.argv[1])
mypwx='/deac/thonhauserGrp/chakrad/quantum-espresso-6.3/qe-6.3-openmpi-3.1.1/bin/pw.x'

i = 0
in_filename = 'S22x5_%02d_%02d_RefA.in'%(NUM,i)
res_filename = in_filename.split('.')[0]+'.txt'
os.popen('mpirun %s < %s > %s' %(mypwx,in_filename,res_filename))


in_filename = 'S22x5_%02d_%02d_RefB.in'%(NUM,i)
res_filename = in_filename.split('.')[0]+'.txt'
print res_filename
os.popen('mpirun %s < %s > %s' %(mypwx,in_filename,res_filename))

