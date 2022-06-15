import sys
from numpy import *

Ryd = 13.6057*1000*2

for Num in range(5):
  Eval = zeros(23)
  Etot = zeros(23)
  Etot_graph_bi = 0
  Etot_graph_mono = 0
  Etxcscf = zeros(23)
  Etxcnscf = zeros(23)
  Etxcscf_graph_bi = 0
  Etxcscf_graph_mono = 0
  ErefA = zeros(23)
  ErefB = zeros(23)
  EtotA = zeros(23)
  EtotB = zeros(23)
  EtxcscfA = zeros(23)
  EtxcscfB = zeros(23)
  EtxcnscfA = zeros(23)
  EtxcnscfB = zeros(23)
  Etxcnscf_graph_bi = 0
  Etxcnscf_graph_mono = 0
  lines = 0
  E0  = zeros(23)
  E0A = zeros(23)
  E0B = zeros(23)
  Enlc = zeros(23)
  EnlcA = zeros(23)
  EnlcB = zeros(23)
  Enlc_graph_bi = 0
  Enlc_graph_mono = 0
  Eval_graph_bi = 0 
  Eval_graph_mono = 0
  E0_graph_bi = 0
  E0_graph_mono = 0
 
  for i in range(1,23):
#   print "System%i/S22_%02d_%02d.txt"%(Num,Num,i)
     file = open("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22x5-density/S22-optb88-rutgers/System%i/S22x5_%02d_%02d.xml"%(i,i,Num))
     content = file.readlines()
     file.close()
     for line in content:
	if '<etot>' in line:
               val = float(line.split('>')[-2].split('<')[0])
	       Etot[i] = val
	
	if '<etxc>' in line:
               val = float(line.split('>')[-2].split('<')[0])
               Etxcscf[i] = val

     file = open("pseudodir/S22x5_%02d_%02d.xml"%(i,Num))
     content = file.readlines()
     file.close()
     for line in content:
	if '<etxc>' in line:
               val = float(line.split('>')[-2].split('<')[0])
               Etxcnscf[i] = val
     
     Eval[i]=Etot[i]-Etxcscf[i]+Etxcnscf[i]     
     
     file = open("System%d/S22x5_%02d_%02d.txt"%(i,i,Num))
     content = file.readlines()
     file.close()
     for line in content:
	if 'Non-local corr. energy' in line:
		val = float(line.split()[-2])
                Enlc[i] = val/2
      
     E0[i] = Eval[i] - Enlc[i]

     file = open("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22x5-density/S22-optb88-rutgers/System%i/S22x5_%02d_00_RefA.xml"%(i,i))
     content = file.readlines()
     file.close()
     for line in content:
        	if '<etot>' in line:
                   val = float(line.split('>')[-2].split('<')[0])
	           EtotA[i] = val
	
        	if '<etxc>' in line:
                   val = float(line.split('>')[-2].split('<')[0])
                   EtxcscfA[i] = val

     file = open("pseudodir/S22x5_%02d_00_RefA.xml"%i)
     content = file.readlines()
     file.close()
     for line in content:
              if '<etxc>' in line:
                  val= float(line.split('>')[-2].split('<')[0])
                  EtxcnscfA[i] = val

     ErefA[i]=EtotA[i]-EtxcscfA[i]+EtxcnscfA[i]

     file = open("System%d/S22x5_%02d_00_RefA.txt"%(i,i))
     content = file.readlines()
     file.close()
     for line in content:
             if 'Non-local corr. energy' in line:
	         val = float(line.split()[-2])
                 EnlcA[i] = val/2
      
     E0A[i] = ErefA[i] - EnlcA[i]

     file = open("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22x5-density/S22-optb88-rutgers/System%i/S22x5_%02d_00_RefB.xml"%(i,i))
     content = file.readlines()
     file.close()
     for line in content:
        	if '<etot>' in line:
                     val= float(line.split('>')[-2].split('<')[0])
	             EtotB[i] = val
	
        	if '<etxc>' in line:
                     val= float(line.split('>')[-2].split('<')[0])
                     EtxcscfB[i]=val

     file = open("pseudodir/S22x5_%02d_00_RefB.xml"%i)
     content = file.readlines()
     file.close()
     for line in content:
        	if '<etxc>' in line:
                    val= float(line.split('>')[-2].split('<')[0])
                    EtxcnscfB[i]=val

     ErefB[i]=EtotB[i]-EtxcscfB[i]+EtxcnscfB[i]

     file = open("System%d/S22x5_%02d_00_RefB.txt"%(i,i))
     content = file.readlines()
     file.close()
     for line in content:
                if 'Non-local corr. energy' in line:
	             val = float(line.split()[-2])
                     EnlcB[i] = val/2
      
     E0B[i] = ErefB[i] - EnlcB[i]


#  print Num,'\t', '1','\t',(Eval[0] - ErefA - ErefB )*Ryd,'\t','2','\t', (Eval[1] - ErefA - ErefB )*Ryd,'\t','3','\t', (Eval[2] - ErefA - ErefB )*Ryd, '\t', '4','\t',(Eval[3] - ErefA - ErefB )*Ryd,'\t', '5','\t', (Eval[4] - ErefA-ErefB )*Ryd,'6','\t', (Eval[5] - ErefA-ErefB )*Ryd, '7','\t', (Eval[6] - ErefA-ErefB )*Ryd,'8','\t', (Eval[7] - ErefA-ErefB )*Ryd
#  print Num,'\t', '1','\t',(E0[0] - E0A - E0B )*Ryd,'\t','2','\t', (E0[1] - E0A - E0B )*Ryd,'\t','3','\t', (E0[2] - E0A - E0B )*Ryd, '\t', '4','\t',(E0[3] - E0A - E0B )*Ryd,'\t', '5','\t', (E0[4] - E0A - E0B )*Ryd,'6','\t', (E0[5] - E0A - E0B )*Ryd, '7','\t', (E0[6] - E0A - E0B )*Ryd,'8','\t', (E0[7] - E0A - E0B )*Ryd
     print Num+1,'\t', i,'\t', (Enlc[i] - EnlcA[i] - EnlcB[i] )*Ryd


file = open("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22x5-density/S22-optb88-rutgers/graphite_bilayer/Graphite-vdW-df-obk8.xml")
content = file.readlines()
file.close()
for line in content:
   if '<etot>' in line:
     val = float(line.split('>')[-2].split('<')[0])
     Etot_graph_bi = val
   
   if '<etxc>' in line:
     val = float(line.split('>')[-2].split('<')[0])
     Etxcscf_graph_bi = val

file = open("pseudodir/Graphite-vdW-df-obk8.xml")
content = file.readlines()
file.close()
for line in content:
   if '<etxc>' in line:
     val = float(line.split('>')[-2].split('<')[0])
     Etxcnscf_graph_bi = val

Eval_graph_bi=Etot_graph_bi-Etxcscf_graph_bi+Etxcnscf_graph_bi    

file = open("graphite_bilayer/graphite.out")
content = file.readlines()
file.close()
for line in content:
   if 'Non-local corr. energy' in line:
     val = float(line.split()[-2])
     Enlc_graph_bi = val/2

E0_graph_bi = Eval_graph_bi - Enlc_graph_bi

file = open("/deac/thonhauserGrp/chakrad/calculations/database-calc/s22x5-density/S22-optb88-rutgers/graphite_monolayer/Graphite-sl-vdW-df-obk8.xml")
content = file.readlines()
file.close()
for line in content:
   if '<etot>' in line:
     val = float(line.split('>')[-2].split('<')[0])
     Etot_graph_mono = val
   
   if '<etxc>' in line:
     val = float(line.split('>')[-2].split('<')[0])
     Etxcscf_graph_mono = val

file = open("pseudodir/Graphite-sl-vdW-df-obk8.xml")
content = file.readlines()
file.close()
for line in content:
   if '<etxc>' in line:
     val = float(line.split('>')[-2].split('<')[0])
     Etxcnscf_graph_mono = val

Eval_graph_bi=Etot_graph_bi-Etxcscf_graph_bi+Etxcnscf_graph_bi    

file = open("graphite_monolayer/graphite-sl.out")
content = file.readlines()
file.close()
for line in content:
   if 'Non-local corr. energy' in line:
     val = float(line.split()[-2])
     Enlc_graph_mono = val/2
 
E0_graph_mono = Eval_graph_mono - Enlc_graph_mono

print "Graphite", '\t', (Enlc_graph_bi/2 - Enlc_graph_mono)*Ryd

