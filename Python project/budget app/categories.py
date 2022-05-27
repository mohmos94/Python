import datetime


class Categories:

    # general list for print statement

    list_categories = ["food", "bills", "clothes", "party", "saving", "stock"]


    # constructor
    def __init__(self):
        # doesnt need any initialization value right know
        pass

# function for adding entries for item
    def add_entries_item(self):
        item_list = []
        choice = input("enter category: ").lower()
        item_name = input("enter item name: ")
        cost = int(input("enter price or saving: "))
        month = int(input('Enter a month: '))
        day = int(input('Enter day: '))

        date_bought = datetime.date(2022, month, day)
        for item in Categories.list_categories:
            if choice == item:
                print(f'added entries to the following item: {choice}')
                item_list = [choice, item_name, cost, date_bought]
                break
            else:
                print("category doesnt exist")
        return item_list

