#local global variables

x="hello"
def my_funct1():
    y="MADAV"
    def my_funct2():
        print(y)
    my_funct2()

my_funct1()


#File Handling

#creating a file

file=open("student.txt","w")
file.write("student name: Madav\n")
file.close()

   
#appending

file=open("student.txt","a")
file.write("Instructor name:VENKY")
file.close()

#file reading

file=open("student.txt","r")
data=file.read()
print(data)
file.close()

#line by line reading
file=open("student.txt","r")
for line in file:
    print(line)
file.close()

#reading one line

file=open("student.txt","r")
print(file.readline())
file.close()

#reading file in list

file=open("student.txt","r")
lines=file.readlines()
print(lines)
file.close()

print(type(lines))

print(lines[1])

#with close()


with open("student.txt","a") as file:
 file.write("conpany name: SS")
 file.close()
 
 #checking if file is closed or not
 
 print(file.closed)
 
 #learning json format
 #craeting json file
 #import json
 
 import json
 
 
 with open("info.json","r") as file:
     student_info=json.load(file)
    
 print(student_info)
 
 #loading a dictionary to the json
 
 hosp_record={
        "Patient":"Steve",
        "Age":19,
        "city":"New York",
        "diagnosis":"Liver Issue"
 }

json_data=json.dumps(hosp_record)

print(json_data)


#pushing json data into json

with open("hosp_record.json","w") as file:
 json.dump(hosp_record,file)
