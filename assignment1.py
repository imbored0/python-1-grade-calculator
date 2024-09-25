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

def lab_percentage(labs_done: int) -> float:
  if labs_done <= 6 and labs_done >= 0:
      if labs_done == 6:
          return (labs_done - 1) * (15/5)
      else:
          return labs_done * (15/5)
  else:
    print("Too many or too little labs, assuming 0 labs done!")
    return 0

def quiz_percentage(quizzes_done: int) -> float:
  if quizzes_done <= 6 and quizzes_done >=0:
      if quizzes_done == 6:
          return (quizzes_done - 1) * (15/5)
      else:
          return quizzes_done * (15/5)
  else:
    print("Too many or too little quizzes, assuming 0 quizzes done!")
    return 0

def assignment_percentage(a1: float, a2: float, a3: float, a4: float) -> float:
  if (a1 < 0 or a1 > 100) or (a2 < 0 or a2 > 100) or (a3 < 0 or a3 > 100) or (a4 < 0 or a4 > 100):
    print("An assignment grade is too high or too low, assuming all assignments are a 0!")
    return 0
  else:
    return (a1 * (4/100)) + (a2 * (4/100)) + (a3 * (4/100)) + (a4 * (4/100))

def midterm_percentage(m1: float, m2: float) -> float:
  if (m1 < 0 or m1 > 100) or (m2 < 0 or m2 > 100):
    print("A midterm grade is too high or too low, assuming all midterms are a 0!")
    return 0
  else:
    return (m1 * (12.5/100)) + (m2 * (12.5/100))

def final_percentage(final: float) -> float:
  if final < 0 or final > 100:
    print("The final exam grade is too high or too low, assuming final is a 0!")
    return 0
  else:
    return final * (18/100)

def midfinalprep_percentage(midfinalprep: float) -> float:
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

#print outcome

print("Your grade is:", total_grade_tally)
