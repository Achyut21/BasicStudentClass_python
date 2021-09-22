class student:
    def __init__(self, id, name, mid1_marks, mid2_marks, quiz_marks):
        self.id = id
        self.name = name
        self.mid1_marks = mid1_marks
        self.mid2_marks = mid2_marks
        self.quiz_marks = quiz_marks

    def result(self):
        if self.total() >= 80:
            print("Your Grade is A")
        elif 80 > self.total() >= 60:
            print("Your Grade is B")
        elif 60 > self.total() >= 50:
            print("Your Grade is C")

    def total(self):
        return self.mid1_marks + self.mid2_marks + self.quiz_marks

    def display(self):
        print("\n================================================")
        print(f"ROLL NO: {self.id}")
        print(f"Student name: {self.name}")
        print(f"Mid1 marks: {self.mid1_marks}")
        print(f"Mid2 marks: {self.mid2_marks}")
        print(f"Total Marks: {self.total()}")
        print(f"Result: {self.result()}")
        print("================================================")


if __name__ == '__main__':
    name = input("Enter your name: ")
    id = int(input("Enter your roll no: "))
    mid1 = int(input("Enter your mid marks: "))
    mid2 = int(input("Enter your md 2 marks: "))
    quiz = int(input("Enter your quiz marks: "))
s1 = student( id, name, mid1, mid2, quiz)
s1.display()
