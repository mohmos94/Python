from categories import Categories


# calculation class inheritance from the categories class
class Calculation(Categories):
    # list to contain the value from the expenses and the saving for the budget app

    def __init__(self):
        pass

    def calculate_list(self, calculation_list):
        value = 0
        for item in calculation_list:
            print(f'item {item}')
            value += item[2]
        return value

    def budget(self, calculation_list, expense_list, search_item):
        for item in calculation_list:
            if item == search_item:
                calculation_list[item] -= expense_list[item]
                return calculation_list[item]
            else:
                print("could not find item in the category")


