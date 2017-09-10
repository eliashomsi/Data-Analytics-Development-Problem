import subprocess

# the main idea is to notice that there are two diffrent types of clients. the first type buy items under a dozen while the sceond type by items in thousands therefore the average does not reflect real orders because the sample is not coherent
#  the solution would be to divide the sample and calculate two diffrent averages: B2C and B2B

#define main
def main():

	#open the newly created input file
	B2Bprice =0.0
	B2Cprice = 0.0
	B2Borders =0.0
	B2Corders = 0.0
	with open("sheet.tsv", "r") as file:
		for line in file:
			temp1, temp2, temp3, value, quantity, temp4, temp5, temp6 = line.split()
			value = int(value)
			quantity = int(quantity)

			if (quantity > 1000): #this is to differentiate between the two cases
				B2Bprice += value
				B2Borders += 1
			else:
				B2Cprice += value
				B2Corders += 1

	print("AOV of B2B is " , B2Bprice / B2Borders)
	print("AOV of B2C is " , B2Cprice / B2Corders)
#define run
if __name__ == "__main__":
	main()
