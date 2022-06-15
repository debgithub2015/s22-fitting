import sys

Num = int(sys.argv[1])

for i in range(1):
  file = open('submit%i'%i,'w')
  file.write('''#!/bin/bash
#SBATCH --job-name=main%i_%i
#SBATCH --output="%i.o"
#SBATCH --error="%i.e"
#SBATCH --account="thonhauserGrp"
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=1
#SBATCH --time=01:00:00
#SBATCH --constraint=rhel7
#SBATCH --mail-user="chakrad@wfu.edu"
#SBATCH --mail-type=FAIL
#SBATCH --partition="small"
#SBATCH --mem=120Gb
ulimit -s unlimited
module load rhel7/openmpi/3.1.1-intel-2018  rhel7/compilers/intel-2018-lp64
python calc_main.py %i %i %i'''%(Num,i,Num,Num,Num,i,(i+1)*5) )
  file.close()


file = open('submit_ref','w')
file.write('''#!/bin/bash
#SBATCH --job-name=ref%i
#SBATCH --output="%i.o"
#SBATCH --error="%i.e"
#SBATCH --account="thonhauserGrp"
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=1
#SBATCH --time=01:00:00
#SBATCH --constraint=rhel7
#SBATCH --mail-user="chakrad@wfu.edu"
#SBATCH --mail-type=FAIL
#SBATCH --partition="small"
#SBATCH --mem=120Gb
ulimit -s unlimited
module load rhel7/openmpi/3.1.1-intel-2018  rhel7/compilers/intel-2018-lp64
python calc_ref.py %i '''%(Num,Num,Num,Num))
file.close()


