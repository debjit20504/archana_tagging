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
		new_lst = remove_bracket_elements(ing_list)
	new_lst.remove("" "")
	l1 = []
	while new_lst!=[]:
		l1.append(new_lst[:1])
		new_lst = new_lst[1:]
	file = open('archana_testing.csv', 'w+', newline ='', encoding = "utf8")	
	with file:
			write = csv.writer(file)
			write.writerows(l1)
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
