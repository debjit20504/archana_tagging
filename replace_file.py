import csv
def main():
	l = []
	l1 = []
	new_l1 = []
	with open("archana_testing.csv", "r", encoding = "utf8") as file:
		reader = csv.reader(file)
		lst = list(reader)
		for i in lst:
			l.append(i[0])
	with open("alias_file.csv", "r", encoding = "utf8") as file1:
		reader1 = csv.reader(file1)
		lst1 = list(reader1)
		# for i in range(len(lst1)):
		# 	print(lst1[i][1] + " - " + lst1[i][3])
		# 	if i>100:
		# 		break
		# 	if lst1[i][1] in l1:
		# 		l1replace()
		for i in l:
			temp = list(i.split(" "))
			for j in range(len(lst1)):
				if lst1[j][1] in temp:
					temp1 = temp.index(lst1[j][1])
					temp[temp1] = lst1[j][3]
				l1.append(temp)
		for i in l1:
			s = ''
			for j in i:
				s += j
				s += ' '
			new_l1.append(s)
		final_lst = []
		while new_l1!=[]: 
				final_lst.append(new_l1[:1])
				new_l1 = new_l1[1:]
		for i in final_lst:
			i[0] = i[0].strip()
if __name__ == '__main__':
	main()