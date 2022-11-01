# functions printing and returning
# print something in a function, its only for displaying
# some data, you are doing nothing with the data

# when you return in a function, you are going to use it
# in another part of your program
from addfruit import add_fruit
from divide_fruit import divide_fruit
from subtract_fruit import subtract_fruit
from display_fruit import display_fruit


apples= int(input("How many apples?"))
oranges= int(input("How many oranges?"))

# add fruit
# whenever you return items you must put
# returned items in variable
fruitAdded= add_fruit(apples,oranges)
print(fruitAdded)

# subtract fruit
fruitSubtracted= subtract_fruit(apples,oranges)
print(fruitSubtracted)

# divide fruit
fruitDivided= divide_fruit(apples,oranges)
print(fruitDivided)

# display the added fruit, subtract fruit, divided fruit
display_fruit(fruitAdded,fruitSubtracted,fruitDivided)
# print(displayFruit)