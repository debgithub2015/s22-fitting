
for i in {1..22} 
do
  cd System$i/
  bash prepare.sh $i
  bash transform
  cd ..
done


