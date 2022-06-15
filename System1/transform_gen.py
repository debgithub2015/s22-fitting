import sys

NUM = int(sys.argv[1])

file = open('transform','w')
file.write('''
for i in {00..04}
do
awk '!($5="")' S22x5_%02d_$i.in > tmp.in
sed -i 's/sla pw  vdW1/sla pw obk8 vdW1/g' tmp.in
mv tmp.in S22x5_%02d_$i.in
echo $i
done
awk '!($5="")' S22x5_%02d_00_RefA.in > tmp.in
sed -i 's/sla pw  vdW1/sla pw obk8 vdW1/g' tmp.in
mv tmp.in S22x5_%02d_00_RefA.in
awk '!($5="")' S22x5_%02d_00_RefB.in > tmp.in
sed -i 's/sla pw  vdW1/sla pw obk8 vdW1/g' tmp.in
mv tmp.in S22x5_%02d_00_RefB.in
'''%(NUM,NUM,NUM,NUM,NUM,NUM))
file.close()

