echo $1
NUM="$1"
echo $NUM

python gen_in.py $NUM
python gen_inA.py $NUM
python gen_inB.py $NUM
python gen_submit.py $NUM
python transform_gen.py $NUM

