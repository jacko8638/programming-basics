#gets user to input num
number = input("enter a three digit number")
#finds how many hundreds there are in it as n int
hund = int(int(number) / 100)
#using indexing finds how many tens
tens = number[1]
#using indexing finds how many units
units = number[2]
#prints results
print("there are", hund," hundreds")
print("there are", tens," tens")
print("there are", units," units")

