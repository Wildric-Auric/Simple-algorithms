import os
dir="files" #direction of folder where lines are counted
extensions = [".cs"] #list containing files you want to apply this code on, by extension
COUNT = 0
count=0
for file in os.listdir(dir):
    filename = os.fsdecode(file) #Getting file name
    if filename.split(".")[1] in extensions:
        count+=1
        with open(dir+"/"+filename, "r") as txt:
            COUNT+= len(txt.readlines())
            
print("Number of code lines is: "+ str(COUNT))
print("Number of file iterated over: "+str(count))
