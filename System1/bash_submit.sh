for i in 0
do
  sbatch submit$i
  sleep 1.0
done

sbatch submit_ref

