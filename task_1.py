from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Створення задачі лінійного програмування для максимізації
model = LpProblem("Production_Optimization", LpMaximize)

# Змінні: кількість вироблених одиниць Лимонаду і Фруктового соку
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Функція мети: максимізувати загальну кількість вироблених одиниць
model += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"  # Обмеження на воду
model += 1 * lemonade <= 50, "Sugar_Constraint"  # Обмеження на цукор
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"  # Обмеження на лимонний сік
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"  # Обмеження на фруктове пюре

# Розв'язання задачі
model.solve()

# Виведення результатів
print("Результати оптимізації:")
print(f"Кількість виробленого Лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість продуктів: {model.objective.value()}")
