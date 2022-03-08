# archana.csv
import pandas as pd
import numpy as np
import time
import csv
# time taken to read data
s_time = time.time()
with open("archana.csv", "r", encoding = "utf8") as file:
	reader = csv.reader(file)
	for i in reader:
		print(i)
e_time = time.time()
print("Read without chunks: ", (e_time-s_time), "seconds")