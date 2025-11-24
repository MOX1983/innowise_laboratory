

students = list() # list of dictionaries for storing the student's name and a list of his grades

while True: # endless loop, if you select the 5th item, it stops
    try:
        print("""\n--- Student Grade Analyzer ---
1. Add a new student  
2. Add grades for a student  
3. Generate a full report  
4. Find the top student  
5. Exit program """)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            if not any(student.get("name") == name for student in students): # function to check if a name is in the list, if there is no name, then add it to the list.
                students.append({"name": name, "grades": list()})
            else:
                print("There is already such a name.")

        elif choice == 2:
            name = input("Enter student name: ")
            if any(student.get("name") == name for student in students): # function to check if a name is in the list
                for student in students:
                    if student.get("name") == name:
                        grades = student.get("grades")
                        while True:
                            try:
                                grade = input("Enter a grade (or 'done' to finish): ")
                                if grade == "done":
                                    break
                                else:
                                    grades.append(int(grade))
                            except ValueError:
                                print("Invalid input. Please enter a number.")
            else:
                print("There is no such student")

        elif choice == 3:
            print("""--- Student Report ---""")
            list_average_grades = list() # list of all average scores for finding the min, max, overall element
            for student in students:
                name = student.get("name")
                try:
                    average_grade = sum(student.get("grades")) / len(student.get("grades"))
                    list_average_grades.append(average_grade)
                except ZeroDivisionError:
                    average_grade = "N/A"
                print(f"{name}'s average grade is {average_grade}")
            print("-----------------")
            print(f"Max Average: {max(list_average_grades)}" )
            print(f"Min Average: {min(list_average_grades)}" )
            print(f"Overall Average: {sum(list_average_grades) / len(list_average_grades)}")

        elif choice == 4:
            if students:
                max_average = max(list(map(lambda student: sum(student.get("grades")) / len(student.get("grades")) if student.get("grades") else 0, students))) # find the maximum score
                average = list(map(lambda student: sum(student.get("grades")) / len(student.get("grades")) if student.get("grades") else 0, students)) # find all the average grades to find the student's name with the highest grade
                print(f"The student with the highest average is {students[average.index(max_average)].get("name")} with a grade of {max_average}.")
            else:
                print("The student list is empty")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Exit program")