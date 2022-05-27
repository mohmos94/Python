from categories import Categories
from calculation import Calculation
from charts import Charts

test = Categories()

testing = Charts()

category_budget = {
    "food": 1000,
    "bills": 600,
    "saving": 500,
    "clothes": 400,
    "party": 800,
    "stock": 1000,

}

category_expense = {
    "food": 100,
    "bills": 0,
    "saving": 0,
    "clothes": 0,
    "party": 0

}

testing.pie_chart(category_budget)




