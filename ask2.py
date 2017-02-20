akolou8ia = raw_input("Dwste thn ma8imatikh protash\n")

left_parethensis = 1
right_parethensis =1
counter = 1
failed = False
i = 0

while (i < len(akolou8ia)):
	if akolou8ia[i]==')':
	    right_parethensis+=1
	    counter-=1
	elif akolou8ia[i] =='(':
		left_parethensis+=1
		counter+=1
	if counter == 0:
		failed = True;
	i+=1

if left_parethensis == right_parethensis and not failed:
	print "true"
else:
	print "false"	