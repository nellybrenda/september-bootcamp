attendee_name = "Brenda Nelly"

if attendee_name.isupper() == False:
	attendee_name = attendee_name.lower()
	print(attendee_name)
else:
	print("This attendee's name is already in uppercase.")
	print(attendee_name)

	# automate the gradingapp system to ensure that it uses a forloop to ask for the five subjects marks
#student details

student_name = input("Enter your name:\n")
student_class = input("Enter your class:\n")
clclass_teacher =  input("Enter your class teacher's name:\n")

#scores per subject
total_score = 0
subjects = ["math", "Eng", "Kiswahili", "Science", "Social Studies"]
for i in range(len(subjects)):
  
   marks = int(input("What is your" +" "+ subjects[i] +" "+"score:\n"))
   total_score += 