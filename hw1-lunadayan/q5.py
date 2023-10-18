"""
Question 5
The function calculate_final_grade lets the user input 4 grades and each one with its weight. After telling the program the four grades, the program will ask the user how we wants to
know his final grade: number, gpa, or letter. The program will calculate the final grade and print it in the chosen format. In this program, the user can interatively input the data
and select the output format.  
"""

def calculate_final_grade():
    grades = []
    weights = []
    
    for i in range(4):
        grade = float(input(f"Enter grade {i + 1}: ")) #user inputs grades
        weight = float(input(f"Enter weight for grade {i + 1}: ")) #user inputs corresponding weight
        grades.append(grade)
        weights.append(weight)
    
    output_format = input("Choose an output format (number, gpa, letter): ") #user chooses the output type

    #calculate the weighted sum of grades
    weighted_sum = sum(grade * weight for grade, weight in zip(grades, weights))
    total_weight = sum(weights)

    #calculate final grade
    final_grade = weighted_sum/total_weight

    #output format
    if output_format == 'number': 
        #return final grade as a number (0-100)
        return final_grade
    elif output_format == 'gpa':
        #return final grade as a gpa (0-4.0)
        if final_grade >= 90:
            return 4.0
        elif final_grade >= 80:
            return 3.0 + (final_grade - 80) / 10
        elif final_grade >= 70:
            return 2.0 + (final_grade - 70) / 10
        elif final_grade >= 60:
            return 1.0 + (final_grade - 60) / 10
        else:
            return 0.0
    else:
        #return final grade as a letter grade (a, b, c, d, or f)
        if final_grade >= 90:
            return 'A'
        elif final_grade >= 80:
            return 'B'
        elif final_grade >= 70:
            return 'C'
        elif final_grade >= 60:
            return 'D'
        else:
            return 'F'

final_grade = calculate_final_grade()
print(f'Your final grade is: {final_grade}')      #prints final grade with selected format. 
