print("=========================")
print("   DICTIONARY ASSIGNMENT ")
print("=========================")
print("Q1_Student Profile System")
student = {
    "name": "Zoha",
    "age": 20,
    "city":"Karachi",
    "hobbies":["Gardening","Reading"],
     "skills":["talking","learning"],
 "marks" : {
        "english" : 88,
        "math" : 99,
        "science" : 78,
        "computer" : 90,
 },
   "attendance":{
   "total_classes" :95,
  "attended_classes" :88
   
    }
}
print(student["name"])
print(student["hobbies"][0])
print(len("skills"))
print("=========================")

print("Q2_Student Marks System")
total_marks = student["marks"]["english"] + student["marks"]["math"] + student["marks"]["science"] + student["marks"]["computer"]
average_marks = total_marks /  len(student["marks"])
print(average_marks)
print("=========================")

print("Q3_Grade checking system")
if(average_marks >= 80):
    print("Grade A")
elif(average_marks >= 70):
    print("Grade B")
elif(average_marks >= 60):
    print("Grade C")
else:
    print("Fail")
if average_marks>=60:
  print("Passed")
else:
  print("Fail")
print("=========================")

print("Q4_Attendance Management Syatem")
print(student["attendance"]["total_classes"])
print("=========================")
print("Q5_fee management system ")
fee={
  "fee_paid":True
}
if (fee["fee_paid"]==True):
  print("Fee cleared ")
else:
  print("Fee pending")
print("=========================")
print("Q6_Skills Management System")
student["skills"].append("drawing")
student["skills"].remove("talking")
print("Updated skills:",student["skills"])
print("Total skills:",len(student["skills"]))
print("=========================")
print("Q7_Login Authentication system")
userinfo={
  "username":"sajafamehboob",
  "password":"ansari12"
}
if userinfo["username"] == "sajafmehboob" and userinfo["password"] == "ansari12":
  print("Login successful")
else:
  print("Invalid Credentials")
print("=========================")
print("Q8_Address management system")
Student = {
    "Name" : "Sajafa Mehboob",
    "Age" : 15,
    "Address" : {
        "Area" : "Near Alladin Park",
        "Street" : "345 side Street",
        "House Number" : "813"
    }
}
print("Address:", Student["Address"])
UpdateArea = "Dha"
Student["Address"]["Area"] = UpdateArea
print("Updated Address:", Student["Address"])
ZipCode = "123456789"
Student["Address"]["Zip Code"] = ZipCode
print("Zip Code:", Student["Address"])
print("=========================")
print("Q9_Multiple Students Database:")
Students = {
    "Student1" : {
        "Name" : "Sajafa Ansari",
        "Age": 15,
        "City":"Karachi",
        "Marks":460
    },
    "Student2" : {
        "Name":"Minsa Sharif",
        "Age": 12,
        "City":"Islamabad",
        "Marks":459
    }
}
print("Student1 Name:",Students["Student1"]["Name"])
print("Student2 Name:",Students["Student2"]["Marks"])
UpdateCity = "Faisalabad"
UpdateCity = Students["Student1"]["City"] 
print("Student1 City:", UpdateCity)
print("=========================")
print("Q10_Final Student Report Card System:")
Student = {
    "Profile": {
        "Name" : input("Enter Your Name: "),
        "Age" : int(input("Enter Your Age: ")),
        "Class" : input("Enter Your City: "),
        "Roll Number" : input("Enter Your Roll Number:"),
        "Hobbies":["Reading","Cooking","Coding"],
        "Skills":["Driving","Designing","Typing"]
    },
    "Marks": {
        "Math" : int(input("Enter Math Marks: ")),
        "Science" : int(input("Enter Science Marks: ")),
        "English" : int(input("Enter English Marks: ")),
        "Computer" : int(input("Enter Computer Marks: "))
    },
    "Attendance": {
        "Total Classes" : int(input("Enter Total Classes: ")),
          "Present Classes" : int(input("Enter Present Classes: "))
     },
     "Fees Paid" : input("Have You Paid Your Fees? (Yes/No): ").lower(),
     "Address": {
         "Area" : input("Enter Your Area: "),
         "Street" : input("Enter Your Street: "),
         "House Number" : input("Enter Your House Number: "),
         "Zip Code" : input("Enter Your Zip Code: ")
     }, 
}
TotalMarks = sum(Student["Marks"].values())
AverageMarks = TotalMarks / len(Student["Marks"])

if(AverageMarks >= 80):
    Grade = "Grade: A"
elif(AverageMarks >= 70):
    Grade = "Grade: B"
elif(AverageMarks >= 60):
    Grade = "Grade: C"
else:
    Grade = "Fail"

AttendancePercentage = (Student["Attendance"]["Present Classes"] / Student["Attendance"]["Total Classes"]) * 100

print("__________ REPORT CARD __________")
print("_____ PROFILE:_____")
print("Name:", Student["Profile"]["Name"])
print("Age:", Student["Profile"]["Age"])
print("Class:", Student["Profile"]["Class"])
print("Roll Number:", Student["Profile"]["Roll Number"])


print("_____ MARKS:_____")
for subject, marks in Student["Marks"].items():
    print(f"{subject}: {marks}")

print("Total Marks:", TotalMarks)
print("Average Marks:", AverageMarks)
print("Final Result:", Grade)

if(AverageMarks >= 60):
    Status = "Pass"
else:
    Status = "Fail"

print("Attendance Percentage:", AttendancePercentage)

if (AttendancePercentage >= 75):
    print("Exam Status: Eligible For Exam")
else:
    print("Exam Status: Not Eligible For Exam Because Attendance is Less Than 75")

if(Student["Fees Paid"] == "yes"):
    print("Fees Status: Fees Cleared")
else:
    print("Fees Status: Fees Pending")

print("Hobbies:", ", ".Student["Profile"]["Hobbies"])
print("Skills:", ", ".Student["Profile"]["Skills"])

print("_____ ADDRESS:_____")
print("Area:",Student["Address"]["Area"])
print("Street:",Student["Address"]["Street"])
print("House Number:",Student["Address"]["House Number"])
print("Zip Code:",Student["Address"]["Zip Code"])
