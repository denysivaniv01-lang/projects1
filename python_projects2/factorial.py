num = int(input("Введіть число для обчислення факторіалу від 1 до 10: "))
n = 1
for i in range(1,num+1):
    n*=i
    print(f"{i} = {n}",end="." "\n")

#Завданння з Підрамідою
for i in range(0,11):
    print(f"{i}",end="." "\n")