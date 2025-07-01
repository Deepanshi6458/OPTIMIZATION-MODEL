from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus

# Step 1: Create the Linear Programming problem
model = LpProblem(name="chocolate-production", sense=LpMaximize)

# Step 2: Define the decision variables
dark = LpVariable(name="Dark_Chocolates", lowBound=0, cat='Integer')
milk = LpVariable(name="Milk_Chocolates", lowBound=0, cat='Integer')

# Step 3: Add constraints
model += (2 * dark + 1 * milk <= 100, "Cocoa_limit")
model += (1 * dark + 2 * milk <= 80, "Sugar_limit")

# Step 4: Objective function - Maximize profit
model += (40 * dark + 30 * milk, "Total_Profit")

# Step 5: Solve the problem
model.solve()

# Step 6: Print the results
print(f"Status: {model.status}, {LpStatus[model.status]}")
print(f"Produce {dark.value()} Dark Chocolates")
print(f"Produce {milk.value()} Milk Chocolates")
print(f"Maximum Profit: ₹{value(model.objective)}")
