# Grade Calculator Given marks for 5 subjects, calculate: Total Percentage Grade Pass/Fail

class GradeCalculator:
    def __init__(self, marks):
        self.marks = marks
        self.total_marks = sum(marks)
        self.percentage = (self.total_marks / 500) * 100
        self.grade = self.calculate_grade()
        self.pass_fail = self.check_pass_fail()

    def calculate_grade(self):
        if self.percentage >= 90:
            return 'A'
        elif self.percentage >= 80:
            return 'B'
        elif self.percentage >= 70:
            return 'C'
        elif self.percentage >= 60:
            return 'D'
        else:
            return 'F'

    def check_pass_fail(self):
        if all(mark >= 40 for mark in self.marks):
            return 'Pass'
        else:
            return 'Fail'

    def display_results(self):
        print(f"Total Marks: {self.total_marks}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Grade: {self.grade}")
        print(f"Result: {self.pass_fail}")

# Example usage
marks = [] 
for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)  
    
     
grade_calc = GradeCalculator(marks)
grade_calc.display_results() 