import pandas
#This line I found on the internet to read only a single column of a csv file
df = pandas.read_csv("archana.csv", usecols=["ingredients"])
#Creating a full list of ingredients which will have all the ingredients from all entries
FullList=[]
#looping over the elements in df["ingredients"]
#I am not sure what data type it is but whatever it is, it has a length
for i in range(0,len(df["ingredients"])):
#The ith element is comma separated ingredients for a particular recipe
    s=df["ingredients"][i]
    #splitting the comma seperated string using "," as delimiter
    SmallList = s.split(",")
    #Adding this small list to the fulllist
    FullList.extend(SmallList)
with open("ingredients.txt","w") as f:
    for j in FullList:
        #I have used strip function so that the leading spaces(which were present in each line) are removed
        f.write(j.strip()+"\n")
        


    

    
