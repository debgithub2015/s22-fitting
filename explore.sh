#! /bin/bash
rm -rf out.dat
for j in */;do
echo  $j >> out.dat
cd $j/
grep -i 'terminated' *.txt | wc -l >> ../out.dat
cd ../
done 
