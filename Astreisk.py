# if number of variable is less than the number of values , you can add an  ' * ' to the variable name and  then the rest of the values will be assigned to that valiable as a list.

fruits = ["Apple","Banana","strawberry","pineapple","raspberry"]

(green,yellow,*red) = fruits

print(green)
print(yellow)
print(red)

