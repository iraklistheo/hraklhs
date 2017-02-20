a = raw_input("Dwste mia protash px: Geia! T! kaneis? \n")
toPrint= [] 
j=1

#Kanonas an einai meta to ! kefalaio htan telos protashs opote to
# krataei(to kanei append sto toPrint) diaforetika to agnoei.

# Trexei enan ena tous chars kai tous pros8etei 
#sthn toPrint.An brei ! elegxei ton epomeno char 
#(proxorontas ena akoma bima an einai keno)
#px: 'geia! Ti kaneis'-> swsto enw to 'e!mai' to kanei 'emai'  

for i in range(len(a)):
	j=i+1
	if a[i]=='!':
		if j < len(a) and a[j]==' ':
			j+=1;
		if j < len(a) and a[j].istitle(): 			
			toPrint.append(a[i])
	else:
		toPrint.append(a[i])

if(a[-1]=='!'):
	toPrint.append('!')

print ''.join(toPrint)

