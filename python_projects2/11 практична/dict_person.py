person = {"name": "Denis",
          "age": 16,
          "city": "Franik",
          "hobby": "Play video games"}
print(person)
person.update({"email": "%овв"})
print("="* 95)
person.update({"age": 15})
print(person)
print("="* 95)
person.pop("hobby")
print(f"Видалення елемента hobby{person}")

print("="* 95)

print(f"виводим ключі{person.keys()}")
print(f"виводим значення{person.values()}")
# test_comnt
print("d")
