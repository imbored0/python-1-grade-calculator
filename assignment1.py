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

total_grade_tally = 0 #the final grade returned at the end

#functions for calculating grades

def lab_percentage(labs_done: Int) -> Float:
  if labs_done <= 6 and >= 0:
    return labs_done * (20/6)
  else:
    print("Too many or too little labs, assuming 0 labs done!")
    return 0

def quiz_percentage(quizzes_done: Int) -> Float:
  if quizzes_done <= 6 and >=0:
    return quizzes_done * (15/6)
  else:
    print("Too many or too little quizzes, assuming 0 quizzes done!")
    return 0

def assignment_adder(a1, a2, a3, a4
