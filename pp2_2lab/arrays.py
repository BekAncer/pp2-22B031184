car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"#not effective

cars = ["Ford", "Volvo", "BMW"]
cars.append("Mercedes")
for x in cars:
  print(x)
cars.pop(0)
cars.remove("Volvo")
print("new list")
for x in cars:
  print(x)