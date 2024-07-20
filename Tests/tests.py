import grade_point as gp
import grade_calculator as gc

#For grade_point module.
result = gp.func("A", 4)
print(f"Grade point: {result}")

#For grade_calculator module.
while True:
	math = gc.getInput("Enter your score: ")
	if 0 <= math <= 100:
		break
grade = gc.calGrades(math)
print(f"You had a/an {grade}")
