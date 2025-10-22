Cars=["Toyota", "Mercedize", "Honda"]
# print(Cars[0])
# print(Cars[1])
# print(Cars[2])

Cars[2]="Ford"
# print(Cars)

x=len(Cars)
# print(x)
# for x in Cars:
#     print(x)

Cars.append("Honda") # to add into an array
# print(Cars)
Cars.pop(1)        # to delete something in an array
# print(Cars)
# print(Cars[1:]) # array slicing

# 2d arrays by nested listed method 
# cityTemperature=[["New York",32,42,55,60], ["Las Vegas",42,55,62,65], ["Indiana",92,82,72,47]]
# print(cityTemperature[0][0])

# 2D arrays by list comprehension method 
rows,cols=3,4
# array=[[0 for c in range(cols) ] for r in range(rows)]
# print(array)
# print(array[1][2])
# array[1][2]=5 # assigning specifica values to the matrix 
# print(array)

# Loops through arrays
array=[[3,4,5,6],[7,8,9,10],[11,12,13,14]]

for r in range(rows):
    for c in range(cols):
        print(f"Row{r}, Col(c)=array[r][c])