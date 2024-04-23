class DataManager:
    def __init__(self, items, subfields_in_ai):
        self.items = items
        self.subfields_in_ai = subfields_in_ai

    def list_items(self):
        print("Items in the list:")
        for item in self.items:
            print(item)

    def print_subfields(self):
        print("Subfields in AI:")
        for subfield in self.subfields_in_ai:
            print(subfield)

    def odd_or_even(self):
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("The given number is even.")
        else:
            print("The given number is odd.")

    def check_eligibility(self):
        gender = input("Your Gender: ").lower()
        age = int(input("Your Age: "))
        if gender == "male" and age >= 21:
            print("ELIGIBLE")
        elif gender == "female" and age >= 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def calculate_percentage(self):
        p1 = float(input("Enter the total marks obtained: "))
        p2 = float(input("Enter the total possible marks: "))
        percentage = (p1 / p2) * 100
        print(f"Your percentage is: {percentage:.2f}%")

    def calculate_total_and_percentage(self):
        s1 = int(input("Subject 1: "))
        s2 = int(input("Subject 2: "))
        s3 = int(input("Subject 3: "))
        s4 = int(input("Subject 4: "))
        s5 = int(input("Subject 5: "))
        total = s1 + s2 + s3 + s4 + s5
        percentage = (total / 500) * 100
        print(f"Total is: {total}, Percentage is: {percentage:.2f}%")

    def triangle_properties(self):
        height = int(input("Enter triangle height: "))
        breadth = int(input("Enter triangle breadth: "))
        area = (height * breadth) / 2
        print(f"Area of triangle is: {area}")

        side1 = int(input("Enter triangle side 1: "))
        side2 = int(input("Enter triangle side 2: "))
        side3 = int(input("Enter triangle side 3: "))
        perimeter = side1 + side2 + side3
        print(f"Perimeter of triangle is: {perimeter}")


items = ['apple', 'banana', 'orange', 'grape']
subfields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]

manager = DataManager(items, subfields)
manager.list_items()
manager.print_subfields()
manager.odd_or_even()
manager.check_eligibility()
manager.calculate_percentage()
manager.calculate_total_and_percentage()
manager.triangle_properties()
