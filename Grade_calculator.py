def calculate_grade(marks):
    if marks >= 90:
        print("Grade: A")
        print("Excellent work! Keep it up!")
    elif marks >= 80:
        print("Grade: B")
        print("Great job! You are doing very well.")
    elif marks >= 70:
        print("Grade: C")
        print("Good effort! Keep improving.")
    elif marks >= 60:
        print("Grade: D")
        print("You passed! Work a little harder next time.")
    else:
        print("Grade: F")
        print("Don't worry! Keep practicing and you will improve.")


while True:
    try:
        marks = float(input("Enter your marks (0-100): "))
        
        if 0 <= marks <= 100:
            calculate_grade(marks)
            break
        else:
            print("Invalid input! Marks must be between 0 and 100.")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value.")