li = []
li.append(3)
print(li)
li.append(68)
print(li)
li.append(1)
print(li)
li.insert(1,"Banana")
print(li)

another_list =["Milk","Bread"]
li.extend(another_list)
print(li)
# Метод extend(another_list) розпаковує список і додає кожен його елемент окремо по декілька. A append додає один об'єкт