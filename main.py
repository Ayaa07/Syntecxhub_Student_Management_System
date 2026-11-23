import json
import os


class Student:
    def __init__(self, student_id, name, grade):
        self.id = student_id
        self.name = name
        self.grade = grade


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Student(item["id"], item["name"], item["grade"]) for item in data]
        except Exception:
            return []

    def save_data(self):
        data = [{"id": s.id, "name": s.name, "grade": s.grade} for s in self.students]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def add_student(self, student_id, name, grade):
        for s in self.students:
            if s.id == student_id:
                print(f" Error: Student with ID '{student_id}' already exists.")
                return

        new_student = Student(student_id, name, grade)
        self.students.append(new_student)
        self.save_data()
        print("Student added successfully.")

    def list_students(self):
        if not self.students:
            print("\n No student records found.")
            return

        print("\n" + "=" * 35)
        print(f"{'ID':<10} | {'Name':<12} | {'Grade':<6}")
        print("=" * 35)
        for s in self.students:
            print(f"{s.id:<10} | {s.name:<12} | {s.grade:<6}")
        print("=" * 35)

    def delete_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                self.students.remove(s)
                self.save_data()
                print(f"Student with ID '{student_id}' deleted successfully.")
                return
        print("No student found with that ID.")


def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. List Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            s_id = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            try:
                grade = float(input("Enter Grade (0-20): "))
                manager.add_student(s_id, name, grade)
            except ValueError:
                print(" Error: Grade must be a valid number.")

        elif choice == "2":
            manager.list_students()

        elif choice == "3":
            s_id = input("Enter Student ID to delete: ").strip()
            manager.delete_student(s_id)

        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print(" Error: Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()  
