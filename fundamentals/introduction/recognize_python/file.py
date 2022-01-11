num1 = 42 ##variable declaration, initialize int
num2 = 2.3 ##variable declaration, initialize float
boolean = True ##variable declaration, boolean
string = 'Hello World' ##variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] ##variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} ##variable declaration, initialize dict
fruit = ('blueberry', 'strawberry', 'banana') ##variable declaration, initialize tuple
print(type(fruit)) ##log statement
print(pizza_toppings[1]) ## log statement at index 1 in list
pizza_toppings.append('Mushrooms') ## add value to list
print(person['name']) ##log statement in dict at name
person['name'] = 'George' ## replace with george in dict at name
person['eye_color'] = 'blue' ## add eye_color to dict and set to blue
print(fruit[2]) ## log statement in tuple at index 2

if num1 > 45: ## if statement
    print("It's greater") ## log statement
else: ## else statement
    print("It's lower") ## log statement

if len(string) < 5: ## if statement
    print("It's a short word!") ## log statement
elif len(string) > 15: ## else if statement
    print("It's a long word!") ## log statement
else: ## else statement
    print("Just right!") ## log statement

for x in range(5): ## for loop
    print(x) ## log statement
for x in range(2,5): ## for loop
    print(x) ## log statement
for x in range(2,10,3): ## for loop
    print(x) ## log statement
x = 0 
while(x < 5): ## while loop
    print(x) ## log statement
    x += 1 

pizza_toppings.pop() ## remove last index from list
pizza_toppings.pop(1) ## remove index 1 from list

print(person) ## log statement
person.pop('eye_color') ## remove eye_color from dict
print(person) ## log statement

for topping in pizza_toppings: ## for loop
    if topping == 'Pepperoni': ## if statement
        continue ## for loop continue
    print('After 1st if statement') ## log statement
    if topping == 'Olives': ## if statement
        break ## for loop break

def print_hello_ten_times(): ## function
    for num in range(10): ## for loop
        print('Hello') ## log statement

print_hello_ten_times()## execute function 

def print_hello_x_times(x):## function, parameter
    for num in range(x): ## for loop
        print('Hello') ## log statement

print_hello_x_times(4)## function, argument

def print_hello_x_or_ten_times(x = 10):## function, parameter
    for num in range(x): ## for loop
        print('Hello') ## log statement

print_hello_x_or_ten_times()## function, argument
print_hello_x_or_ten_times(4)## function, argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)