from categories import Categories
from calculation import Calculation
from charts import Charts

# global list
category_expense = {
    "food": 0,
    "bills": 0,
    "saving": 0,
    "clothes": 0,
    "party": 0

}
category_budget = {
    "food": 1000,
    "bills": 600,
    "saving": 500,
    "clothes": 400,
    "party": 800,
    "stock": 1000
}

# expenses

food = []
bills = []
clothes = []
party = []

# saving

saving = []
stock = []

# object from classes

cat = Categories()
calc = Calculation()
chart = Charts()

list_categories = ["food", "bills", "clothes", "party", "saving", "stock"]

while True:
    print("Welcome to the budget App")
    choice = input("do you wanna check the budget, expenses: or charts ")
    if choice == "budget":
        choice = input("enter item that you wanna see your budget on: ")
        budget = Calculation().budget(category_budget, category_expense, choice)
        if choice == "food":
            category_budget[choice] = budget
            print(category_budget)
        elif choice == "bills":
            category_budget[choice] = budget
            print(category_budget)
        elif choice == "clothes":
            category_budget[choice] = budget
            print(category_budget)
        elif choice == "party":
            category_budget[choice] = budget
            print(category_budget)
        elif choice == "stock":
            category_budget[choice] = budget
            print(category_budget)
        elif choice == "saving":
            category_budget[choice] = budget
            print(category_budget)
        else:
            print("could not find the item in the budget")
            break

    elif choice == "expenses":
        expense_list = cat.add_entries_item()
        for item in expense_list:
            if item == "food":
                food.append(expense_list)
                calculation_value = calc.calculate_list(food)
                category_expense["food"] = calculation_value
                print(category_expense)
                print(food)
            elif item == "bills":
                bills.append(expense_list)
                calculation_value = calc.calculate_list(bills)
                category_expense["bills"] = calculation_value
                print(category_expense)
                print(bills)
            elif item == "clothes":
                clothes.append(expense_list)
                calculation_value = calc.calculate_list(clothes)
                category_expense["clothes"] = calculation_value
                print(category_expense)
                print(clothes)
            elif item == "party":
                party.append(expense_list)
                calculation_value = calc.calculate_list(party)
                category_expense["party"] = calculation_value
                print(category_expense)
                print(party)
            elif item == "stock":
                stock.append(expense_list)
                calculation_value = calc.calculate_list(stock)
                category_expense["stock"] = calculation_value
                print(category_expense)
                print(stock)
            elif item == "saving":
                saving.append(expense_list)
                calculation_value = calc.calculate_list(saving)
                category_expense["saving"] = calculation_value
                print(category_expense)
                print(saving)
            else:
                break
    elif choice == "charts":
        chart.pie_chart(category_budget)

    else:
        print("input value did not match the request check your spelling")
