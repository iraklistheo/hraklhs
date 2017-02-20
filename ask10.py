import urllib2
import json
import sys

nomismata = raw_input("Dwste ta nomismata xwrismena me keno.px: cny eur:\n")

# Sta nomismata kratame mia lista me ta nomismata pou zhthse o xrhsths
nomismata = nomismata.split(' ')
# h hmeromhxnia pou 8a ginei epistrofh twn nomismatwn
startDate = raw_input("Dwste thn hmeromhnia pou sas endiaferei se morfh: YYYY-MM-DD \n")

array =[]
#trexw osa fores einai ta nomismata gia na parw thn timh olwn gia thn sugkekrimenh hmeromhnia 
#kai ta kanw add sto array
for i in range(0,len(nomismata)):	
	response = urllib2.urlopen("http://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s&currency=%s"%(startDate,startDate,nomismata[i]))
	the_page = response.read()		
	data = json.loads(the_page)
	#print data
	the_page = the_page.split(':')
	last = the_page[2]
	last = last.split('}')
	array.append(last[0])
	array.append(nomismata[i])

name = []

j=len(array)
for i in range(len(array)):	
	if not i%2:	
		name.append(array[i])

currency = [] #krataei to onoma tou nomismatos
value = []    #krataei thn ajia tou nomismatos
#Stous currency value vazw se kathe pinaka antistoixeia to nomisma me thn timh tou
#etsi otan ginei to sort se aujousa otan px 8elw na brw  poio nomisma exei thn value 590
# psaxnw sto pinaka value briskw to index tou 590 , kai se ayto to index ston currency 8a 
#brisketai to nomisma px USD

for i in range(len(array)):
	if not i%2:
		value.append(array[i])
	else:
		currency.append(array[i])

sort = []
sort = sorted(name,key=float)
#print 'nums:',nums

final = []
tmp = ""

#edw ginetai h diadikasia antistoixisis value se nomisma xrhsimopoiontas tous duo pinakes (value,currency)
#Pairnw thn prwth timh(value) estw 500 thn vazw ston final. psaxnw se poia 8esh(index) htan sto array values,
#kai ustera kanw append to currency[index] afou 8a einai to antistoixo nomisma
for i in range(len(sort)):
	tmp = sort[i]
	final.append(tmp)
	for j in range(len(value)):
		if tmp == value[j]:
			final.append(currency[j])

j = 0
x = 0

# edw ginetai print tou telikou pinaka pou exei sort values me ta nomismata tou
for i in range(len(final)/2):
	j = x + 1
	sys.stdout.write(str(final[x]))
	sys.stdout.write("->")
	sys.stdout.write(str(final[j]))
	x = j + 1
	print 
