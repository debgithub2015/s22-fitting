
for i in {1..22}
do
  cd System$i/
  echo $i
  bash bash_submit.sh $i
  cd ..
done

sbatch graphite_bilayer/run.sh
sbatch graphite_monolayer/run.sh
 

