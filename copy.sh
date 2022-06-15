

for i in {2..22}
do
  mkdir System$i
  echo $i
  cp System1/*.py System$i/
  cp System1/*sh  System$i/
done

