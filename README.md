# OPTIMIZATION-MODEL
COMPANY:CODTECH IT SOLUTIONS
NAME:DEEPANSHI
INTERN ID:CTO6DF2918
DOMAIN:DATA SCIENCE
DURATION:6 WEEKS
MENTOR:NEELA SANTOSH

Objective:

To solve a real-world business problem using optimization techniques (like Linear Programming) with the help of Python and PuLP library.

 Project Title:

Chocolate Factory Production Optimization

 Problem Statement:

A chocolate factory produces two types of chocolates – Dark and Milk.

Each type of chocolate requires a certain amount of cocoa and sugar.

The company has limited amounts of both resources.

The goal is to maximize total profit by deciding how many of each chocolate to produce.

 Tools & Technologies Used:

Python – for writing and executing the logic

PuLP library – for solving linear programming (LP) problems

VS Code – as the code editor and terminal

 Business Data (Assumptions):

Chocolate Type	Cocoa Required	Sugar Required	Profit per Unit

Dark	2 units	1 unit	₹40
Milk	1 unit	2 units	₹30


Total cocoa available: 100 units

Total sugar available: 80 units

 Steps Involved:

Step 1: Problem Setup

Imported pulp and defined a Linear Programming (LP) problem using LpProblem.

Set the problem as a Maximization problem since we want to maximize profit.
 Step 2: Define Decision Variables

Created two decision variables:

Dark_Chocolates: Number of dark chocolates to produce

Milk_Chocolates: Number of milk chocolates to produce

Both are defined as integers and must be ≥ 0.

 Step 3: Define Constraints

Cocoa Constraint: 2*Dark + 1*Milk ≤ 100

Sugar Constraint: 1*Dark + 2*Milk ≤ 80

These ensure that we don’t use more cocoa or sugar than available.

 Step 4: Objective Function

The goal is to maximize profit, defined as:

Profit = 40 * Dark + 30 * Milk

 Step 5: Solve the Problem

Used the solve() method from PuLP.

Got the optimal solution using the built-in solver.

 Output:

Optimal solution was found.

Example result:

Produce 20 Dark Chocolates
Produce 30 Milk Chocolates
Maximum Profit: ₹2200

 Key Learnings:

Learned how to model real-world business decisions using math and code.

Understood how Linear Programming can help in resource management.

Learned to use PuLP in Python to define constraints and goals clearly.
