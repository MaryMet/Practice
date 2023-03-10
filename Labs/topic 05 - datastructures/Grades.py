# messing with dictionaries, lists and tuples
# Grades
# Author : Mary Metcalfe

Student = {
    "Name" : "Mary",
    "Modules": [
        {
            "Course_name" : "Programming",
            "Grade": "45"
        },
        {
            "Course_name" :"History",
            "Grade": "99"
        }

    ]

}

print ("Student: {}".format(Student["Name"]))
for module in Student["Modules"]:
    print("\t {} \t: {}".format(module["Course_name"], module["Grade"]))
