import time
import csv

def main():
	s_time = time.time() # time taken to read data
	unwanted_items = {'Salt to taste', 'Salt-As needed', 'Water as needed', 'Salt as needed', 'Ghee as required', 'Oil as needed', ''}
	with open("ingredients.csv", "r", encoding = "utf8") as file:
		reader = csv.reader(file)
		ing_list = []
		lst = list(reader)
		for i in range(len(lst)):
			temp = str(lst[i])
			temp = temp.strip("['']")
			ing_list.append(temp)
		ing_list = [i for i in ing_list if i not in unwanted_items]
		for i in ing_list:
			print(i)
				
	e_time = time.time()
	print()
	print("Time taken: ", (e_time-s_time), "seconds")

if __name__ == '__main__':
	main()
