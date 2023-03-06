# labs from Week 06
# I am playing catch up
# lets mange our students
# Author : MAry Metcalfe

def display_menu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 
 return choice


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

def do_add():
 
 print("in adding")
def do_view():
 
 print("in viewing")

choice = display_menu()
while(choice != 'q'):

 if choice == 'a':
    do_add()
 elif choice == 'v':
    do_view()
 elif choice !='q':
     print("\n\nplease select either a, v or q")
 choice = display_menu
