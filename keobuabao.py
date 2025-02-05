from random import randint
print ("nhap :")
player = input ()
computer = randint(0,2)

if computer == 0:
	computer = "keo"
if computer == 1:
	computer = "bua"
if computer == 2 :
	computer = "bao"

print ("----")
print ("you choose :" + player)
print (" computer choose:" + computer)
print ("----")
if player == computer:
	print ("draw")
else :
	if player == "keo":
		if computer == "bao":
			print ("win")
		else :
			print ("lose")
	elif player == "bua":
		if computer == "keo":
			print ("win")
		else :
			print ("lose")
	elif player == "bao":
		if computer == "bua":
			print ("win")
		else :
			print ("lose")

	else:
		print ("nhap sai")


		

 	




