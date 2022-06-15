#!/bin/bash
#SBATCH --job-name=main1_0
#SBATCH --output="1.o"
#SBATCH --error="1.e"
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
ulimit -u unlimited
module load rhel7/openmpi/3.1.1-intel-2018  rhel7/compilers/intel-2018-lp64
sh copy.sh && sh prepare_all.sh && sh submit.sh

cd graphite_bilayer/
sbatch run.sh
cd ..

cd graphite_monolayer/
sbatch run.sh
cd ..
