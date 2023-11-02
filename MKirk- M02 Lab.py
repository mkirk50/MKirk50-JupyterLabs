# Student Name: Mikayla Kirk
# File Name: MKirk - M02 Lab

# The app will:
#  1. ask for and accept a student's last name.
# quit processing student records if the last name entered is 'ZZZ'.
#  2. ask for and accept a student's first name.
#  3. ask for and accept the student's GPA as a float.
#  4. test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
#  5. test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
#  6. test the app using at least five students.

# Variables: 
#  student_lname : Student Last Name
#  student_fname : Student First Name
#  student_gpa  : Student GPA


student_lname = input("Please enter the student's Last Name or 'ZZZ' to quit: ")

while not student_lname == "ZZZ":    
    student_fname = input("Please enter the student's First Name: ")
    
    student_gpa = float(input("Please enter student's GPA: "))
    if student_gpa >= 3.5:
        print ("Student has made the Dean's List.") 
    elif student_gpa >= 3.25:
        print ("Student has made the Honor Roll.")

    student_lname = input("Please enter the student's last name or 'ZZZ' to quit: ")

