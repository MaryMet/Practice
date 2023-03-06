# I am not sure where this is going
#Author: Mary Metcalfe

students= []
def read_modules():
 return []
def do_add(students):
 current_student = {}
 current_student["name"]=input("enter name : ")
 current_student["modules"]= read_modules()
 students.append(current_student)
#test
do_add(students)
do_add(students)
print (students)

def read_modules():
 modules = []
 module_name = input("\tEnter the first Module name (blank to quit):").strip()

 while module_name != "":
    module = {}
    module["name"]= module_name

module["grade"]=int(input("\t\tEnter grade:"))
modules.append(module)
 
module_name = input("\tEnter next module name (blank to quit):").strip()

