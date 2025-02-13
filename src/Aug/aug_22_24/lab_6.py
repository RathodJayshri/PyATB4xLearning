# Syntax = for variable_name in range(start,stop,step) by default step is 1

# for i in range(1,10,1):
#     print(i)  bydefault end = "\n"

# for i in range(1,10,1):
#     print(i, end= " ")

# for i in range(1,10,2):
#     print(i, end= " ")

# for jayshri in range(1,5,1):
#     print(jayshri)

# for i in range(1,10):
#     print("hello ->",i)

# for i in range(1,11):
#     print("Hello World!")

# for jayshri in range(10,0,-2):
#     print(jayshri)
#nothing will return or print


class Employee:
    def __init__(self, name, job_title, annual_salary):
        self.name = name
        self.job_title = job_title
        self.annual_salary = annual_salary

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_job_title(self):
        return self.job_title

    def set_job_title(self, job_title):
        self.job_title = job_title

    def get_annual_salary(self):
        return self.annual_salary

    def set_annual_salary(self, annual_salary):
        self.annual_salary = annual_salary


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_salary(self):
        total_salary = sum(emp.get_annual_salary() for emp in self.employees)
        return total_salary


class Solution:
    def solution(self, s):
        lines = s.strip().split("\n")
        company = Company()

        for line in lines:
            name, job_title, annual_salary = line.split(",")
            annual_salary = float(annual_salary.strip())
            employee = Employee(name.strip(), job_title.strip(), annual_salary)
            company.add_employee(employee)

        return company.calculate_total_salary()


def main():
    print("John Doe", "Software Engineer", 60000),
    print("Jane Smith", "Product Manager", 75000)
    print("Enter each employee on a new line. Type 'END' to finish input.")

    input_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        input_lines.append(line)

    input_data = "\n".join(input_lines)
    ret = Solution().solution(input_data)
    print(f"Total Salary Bill: {ret}")


if __name__ == '__main__':
    main()



