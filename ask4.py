import sys
import numpy

print "Dwste thn akolou8ia ari8mwn.( toulaxiston 5)"
sequence = map(float, raw_input().split())

# thn apo8hkeuw edw sortarismenh se aujousa seira
sortetSeq = sorted(sequence)
flag = "true"

if(len(sortetSeq)<=4):
	print "prepei na dwsete toulaxiston 5 ari8mous"
	flag ="false"
mesos_oros=0
#ston ypologismo meso orou agnow ta prwta 2 stoixeia kai ta 2 teleutaia
#afou 8a einai ta 2 mikrotera kai ta dyo megalutera
#gia auto jekinw thn for apo to trito stoixeio kai teleiwnei 2 prin to telos.
for i in range(2,len(sortetSeq)-2):
	mesos_oros+=sortetSeq[i]

mesos_oros = mesos_oros / (len(sortetSeq)-4)

#sto a8roisma kratw gia olous tous ari8mous: thn diafora ka8e ari8mou me ton meso oro upsomenh sto tetragono.
a8roisma = 0
for i in range(2,len(sortetSeq)-2):
	a8roisma += (sortetSeq[i]- mesos_oros)**2

#h tupikh apoklish einai h riza tou a8roisma me to plh8os twn ari8mwn.
if flag=="true":
	print 'H tupikh apoklish einai:',numpy.sqrt(a8roisma/(len(sortetSeq)-4)) 