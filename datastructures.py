# list datastructures

fruits=["Mangoes", "Banana", "Pineapple", "Oranges"]
fruits[1]="Watermelon"
num=[5,8,1,-3,6,2,0,15]

print(fruits)
print(f"I love eating {fruits[1]}")

for i in fruits:
    print(i)

# tuples datastructure, order, index, immutable or unchanged
cars=('suzuki', 'Toyota', 'Nissan', 'Mercedes')

print(cars)
print(f"I love {cars[2]} cars")

# set datastructures
colors={"yellow", "blue", "green", "white", "orange"}
print(colors)

# dictionaries datastructures
staff={"name":"Erick", "age":50, "salary":300000}
print(staff)
print(staff['name'])