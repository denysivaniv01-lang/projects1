code = "Python Programming"

print(code[:6]) 
print(code[-6:])
print(code[:: 2])
print(code[-5:])
print("\n")

word = input("Напишіть слово: ") #пишем слово
low_word = word.lower().strip() # робить слова маленькі і видалєм рядки
reversed_word = low_word[::-1] #створюєм зміну де збергієм значення

if low_word == reversed_word: #перевіряєм чи в нас слово мале і без пробілів та дивимся щоб слово було починалося з кінця (перевертаєм)
    print("Це палідром")

else:
    print("Це не палідром")
#перевіряєм резульатити