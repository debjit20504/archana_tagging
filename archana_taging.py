import time
import csv

def main():
	s_time = time.time() # time taken to read data
	unwanted_items = {'Salt to taste', 'Salt-As needed', 'Water as needed', 'Salt as needed', 'Ghee as required', 'Oil as needed', 'Salt and Pepper to taste', 'Water as needed', 'Oil for frying', 'Salt as required', 'Salt according to taste', 'Oil for cooking'}
	with open("ingredients.csv", "r", encoding = "utf8") as file:
		reader = csv.reader(file)
		ing_list = []
		lst = list(reader)
		for i in range(len(lst)):
			temp = str(lst[i])
			temp = temp.strip("['']")
			if '()' in temp:
				temp = temp.replace("()", "")
			ing_list.append(temp)
		ing_list = [i for i in ing_list if i not in unwanted_items]
		new_lst = []
		new_lst = remove_bracket_elements(ing_list)
	new_lst.remove("" "")
	#   for converting to csv file this l1 is used which is taking so much time
	new_l1 = []
	for i in new_lst:
		if ('Chilli' in i) or ('Chillies' in i):
			i = i.replace("Red Chillies","Cayanne")
			i = i.replace("Red Chilli","Cayanne")
			i = i.replace("Green Chillies","Cayanne")
			i = i.replace("Green Chilli","Cayanne")
			i = i.replace("Chillies","Cayanne")
			i = i.replace("Chilli","Cayanne")
		new_l1.append(i)	
	l1 = []
	while new_l1!=[]: 
		l1.append(new_l1[:1])
		new_l1 = new_l1[1:]
	for i in l1:
		print(i)
	# file = open('archana_testing.csv', 'w+', newline ='', encoding = "utf8")	
	# with file:
	# 		write = csv.writer(file)
	# 		write.writerows(l1)
	e_time = time.time()
	print()
	print("Time taken: ", (e_time-s_time), "seconds")
def remove_bracket_elements(lst):
	lst1 = []
	un = {'hing', 'Haldi', 'Dhania', 'Moongphali', 'Jeera', 'Gajjar', 'Hing', 'Gajjar', 'Maida', 'besan', 'Aloo', 'Saunf', 'tej patta', 'Matar', 'Kathal', 'Laung', 'Pudina', 'gobi', 'Palak', 'Dalchini', 'Badi Elaichi', 'Lobia', 'Parval', 'Gingelly', 'Elaichi', 'Bengal Gram Dal', 'Til seeds', 'Vatana', 'lauki', 'Badam', 'kopra'}
	start = end = 0
	for i in lst:
		for j in range(len(i)):
			if i[j]=='(':
				start = j
			if i[j]==')':
				end = j
		un_i = i[start+1:end]
		if un_i in un:
			i = i.replace(un_i,"")
			i = i.replace("()","")
		lst1.append(i)
		start = end = 0
	return lst1

if __name__ == '__main__':
	main()
