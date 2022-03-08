# archana.csv
import pandas as pd
import numpy as np
import time
import csv

def main():
	s_time = time.time() # time taken to read data
	ingredient_list = []
	with open("archana.csv", "r", encoding = "utf8") as file:
		reader = csv.reader(file)
		for i in reader:
			if len(i) != 0:
				ingredient_list.append(i[3])		
	e_time = time.time()
	print()
	print("Time taken: ", (e_time-s_time), "seconds")

if __name__ == '__main__':
	main()