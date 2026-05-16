Vip_status = input("Введіть Vip стутус Так/Ні: ").lower()
age = int(input("Введіть ваші роки "))
document = input("напишіть чи є доукументи (Так/Ні): ").lower()

if (age >= 18 and document == "так")or Vip_status == "так":
    print("Прохід доуступний")

else:
    if age < 18:
        print('Нема досттатьо років')
    elif document != "так":
        print("Немає паспорту")