class Employee:
    raise_amount = 1.05
    def __init__(self, first_name, last_name, job_title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = salary
        self.email = first_name + "." + last_name + "@company.org"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

class Sales(Employee):
    salary = 50000

    def phone(self, phone_number):
        self.phone_number = phone_number

    def email(self, send_email):
        self.send_email = send_email
        what_is_name = input("What is your name?")
        send_to_cust = print(f"Dear {what_is_name}, Thank you for interest in our product. Please let me know if you have any questions. My email is {self.email} or my phone number is {self.phone_number}. Thanks, {what_is_name}")


class Development(Employee):
    salary = 100000

    def code(self, wr_code, first_name):
        self.wr_code = wr_code
        self.first_name = first_name
        print(f"{first_name} is weriting code.")
        print(f"{first_name} was sent emails to Mike O'Neil and Hannah Stern." )

sales_person = Sales("Brian", "Eliseykin", "Sales person", 50000)
developer = Development("Vlad", "Stanton", "Developer", 100000)