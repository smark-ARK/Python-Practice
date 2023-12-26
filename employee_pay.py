def get_employee_data():
    """
    Prompts the user to enter employee information and returns a dictionary containing the employee's name, hours worked, and hourly rate.

    Returns:
        dict: A dictionary containing the employee's information
    """
    employee_name = input("Enter employee name: ")
    if employee_name == '':
        return None
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    return {"name": employee_name, "hours_worked": hours_worked, "hourly_rate": hourly_rate}


def calculate_income(employee_data):
    """
    Calculates the employee's gross income based on the hours worked and hourly rate.

    Args:
        employee_data (dict): A dictionary containing the employee's information

    Returns:
        float: The employee's gross income
    """
    gross_income = employee_data["hours_worked"] * employee_data["hourly_rate"]
    return gross_income


def calculate_income_tax(gross_income, tax_rate):
    """
    Calculates the employee's income tax based on the gross income and tax rate.

    Args:
        gross_income (float): The employee's gross income
        tax_rate (float): The applicable tax rate

    Returns:
        float: The employee's income tax
    """
    income_tax = gross_income * tax_rate
    return income_tax


def calculate_superannuation(gross_income, superannuation_rate):
    """
    Calculates the employee's superannuation deduction based on the gross income and superannuation rate.

    Args:
        gross_income (float): The employee's gross income
        superannuation_rate (float): The applicable superannuation rate

    Returns:
        float: The employee's superannuation deduction
    """
    superannuation_deduction = gross_income * superannuation_rate
    return superannuation_deduction


def calculate_net_pay(gross_income, income_tax, superannuation_deduction):
    """
    Calculates the employee's net pay by subtracting income tax and superannuation deduction from the gross income.

    Args:
        gross_income (float): The employee's gross income
        income_tax (float): The employee's income tax
        superannuation_deduction (float): The employee's superannuation deduction

    Returns:
        float: The employee's net pay
    """
    net_pay = gross_income - (income_tax + superannuation_deduction)
    return net_pay


def display_employee_results(employee_data, gross_income, income_tax, superannuation_deduction, net_pay):
    """
    Displays the calculated results for the employee, including name, gross income, income tax, superannuation deduction, and net pay.

    Args:
        employee_data (dict): A dictionary containing the employee's information
        gross_income (float): The employee's gross income
        income_tax (float): The employee's income tax
        superannuation_deduction (float): The employee's superannuation deduction
        net_pay (float): The employee's net pay
    """
    print("Employee Name:", employee_data["name"])
    print("Gross Income:", gross_income)
    print("Income Tax:", income_tax)
    print("Superannuation Deduction:", superannuation_deduction)
    print("Net Pay:", net_pay)
    print("\n")


# Define tax and superannuation rates
tax_rate = 0.2
superannuation_rate = 0.1

# Get employee data for multiple employees
employees = []
print("\nPlease Enter Employee data, Press Enter While keeping Employee name empty to exit\n")
while True:
    print("\n")
    employee_data = get_employee_data()

    if not employee_data:
        break

    employees.append(employee_data)

# Calculate and display results for each employee
print("\nOutput: ")
for employee_data in employees:
    gross_income = calculate_income(employee_data)
    income_tax = calculate_income_tax(gross_income, tax_rate)
    superannuation_deduction = calculate_superannuation(gross_income, superannuation_rate)
    net_pay = calculate_net_pay(gross_income, income_tax, superannuation_deduction)

    display_employee_results(employee_data, gross_income, income_tax, superannuation_deduction, net_pay)
