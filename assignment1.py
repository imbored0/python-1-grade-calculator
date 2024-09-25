#input prompts
labs_completed = int(input("Enter the number of labs completed: "))
quizzes_completed = int(input("Enter the number of quizzes completed: "))
a1_grade = float(input("Enter grade for Assignment 1: "))
a2_grade = float(input("Enter grade for Assignment 2: "))
a3_grade = float(input("Enter grade for Assignment 3: "))
a4_grade = float(input("Enter grade for assignment 4: "))
m1_grade = float(input("Enter grade for Midterm 1: "))
m2_grade = float(input("Enter grade for Midterm 2: "))
f_grade = float(input("Enter grade for Final Exam: "))
m_and_fp_grade = float(input("Enter grade for Midterms and Final Preparation: "))

total_grade_tally: float = 0 #the final grade returned at the end

#functions for calculating grades

def lab_percentage(labs_done: int) -> float: #this function calculates the grade given based off of the amount of labs done, weighted to 20%
  if labs_done <= 6 and labs_done >= 0:
    return labs_done * (20/6)
  else if labs_done > 6:
    return 20
  else:
    print("Negative labs is impossible, assuming labs done are 0!") #just in case of abnormal inputs, every single function will have a case for if a negative number or number above the maximum is input
    return 0

def quiz_percentage(quizzes_done: int) -> float: #calculates the grade from amount of quizzes done, weighted to 15%
  if quizzes_done <= 6 and quizzes_done >=0:
    return quizzes_done * (15/6)
  else:
    print("Negative quizzes is impossible, assuming quizzes done is 0!")
    return 0

def assignment_percentage(a1: float, a2: float, a3: float, a4: float) -> float: #calculates the grade from all 4 assignments done, weighted to 4% each, or 16% total
  if (a1 < 0 or a1 > 100) or (a2 < 0 or a2 > 100) or (a3 < 0 or a3 > 100) or (a4 < 0 or a4 > 100):
    print("An assignment grade is too high or too low, assuming all assignments are a 0!")
    return 0
  else:
    return (a1 * (4/100)) + (a2 * (4/100)) + (a3 * (4/100)) + (a4 * (4/100))

def midterm_percentage(m1: float, m2: float) -> float: #calculates the grade from both of the midterms, weighted to 12.5%, or 25% total
  if (m1 < 0 or m1 > 100) or (m2 < 0 or m2 > 100):
    print("A midterm grade is too high or too low, assuming all midterms are a 0!")
    return 0
  else:
    return (m1 * (12.5/100)) + (m2 * (12.5/100))

def final_percentage(final: float) -> float: #calculates the final exam weighted to 18%
  if final < 0 or final > 100:
    print("The final exam grade is too high or too low, assuming final is a 0!")
    return 0
  else:
    return final * (18/100)

def midfinalprep_percentage(midfinalprep: float) -> float: #calculates the midterm/final prep, weighted to 6%
  if midfinalprep < 0 or midfinalprep > 100:
    print("The midterms and final preparation grade is too high or too low, assuming that grade is a 0!")
    return 0
  else:
    return midfinalprep * (6/100)

#final tally

total_grade_tally += lab_percentage(labs_completed)
total_grade_tally += quiz_percentage(quizzes_completed)
total_grade_tally += assignment_percentage(a1_grade, a2_grade, a3_grade, a4_grade)
total_grade_tally += midterm_percentage(m1_grade, m2_grade)
total_grade_tally += final_percentage(f_grade)
total_grade_tally += midfinalprep_percentage(m_and_fp_grade)

#round number to 2 decimal spots

total_grade_tally_returned = round(total_grade_tally, 2)

#print outcome

print("Your grade is:", total_grade_tally_returned)
