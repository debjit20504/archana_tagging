import csv
with open("archana_remaining.csv", "r", encoding = "utf8") as file:
	reader = csv.reader(file)
	ing_list = []
	lst = list(reader)
	l1 = []
	l2 = []
	for i in range(0,18000,1000):
		l2.append(i)
	temp = 0
	set_value = temp
	temp_value = 0
	count = 0
	while(temp<18221):
		for i in range(18002,18221):
			l1.append(lst[i])
			# if i % 1000 == 0 and i != 0:
				# temp_value = i
				# count += 1
			# if i==temp_value:
			# 	file1 = open('archana_remaining_'+str(l2[count-1]+1)+'-'+str(temp+1)+'.csv', 'w+', newline ='', encoding = "utf8")	
			# 	with file1:
			# 		write = csv.writer(file1)
			# 		write.writerows(l1)
			# 	l1 = []
			# temp+=1
			file1 = open('archana_remaining_18002-18221.csv', 'w+', newline ='', encoding = "utf8")	
			with file1:
				write = csv.writer(file1)
				write.writerows(l1)


# with open("archana_1-100.csv", 'r', encoding = 'utf8') as file:
# 	reader = csv.reader(file)
# 	ing_list = []
# 	lst = list(reader)
# 	l1 = []
# 	for i in range(0,len(lst)):
# 		print(lst[i].insert(0,))
		
# 	file1 = open('new_archana_1-100.csv', 'w+', newline ='', encoding = "utf8")	
# 	with file1:
# 		write = csv.writer(file1)
# 		write.writerows(l1)

# import pandas
# #This line I found on the internet to read only a single column of a csv file
# df = pandas.read_csv("archana.csv", usecols=["ingredients"])
# #Creating a full list of ingredients which will have all the ingredients from all entries
# FullList=[]
# #looping over the elements in df["ingredients"]
# #I am not sure what data type it is but whatever it is, it has a length
# for i in range(0,len(df["ingredients"])):
# #The ith element is comma separated ingredients for a particular recipe
# 	s=df["ingredients"][i]
# 	#splitting the comma seperated string using "," as delimiter
# 	SmallList = s.split(",")
# 	for j in range(len(SmallList)):
# 		SmallList[j] = str(i+1) + " " + SmallList[j]
# 	#Adding this small list to the fulllist
# 	FullList.extend(SmallList)
# with open("new_ingredients.txt","w",encoding = "utf8") as f:
#     for j in FullList:
#         #I have used strip function so that the leading spaces(which were present in each line) are removed
#         f.write(j.strip()+"\n")
