products = ["молоко", "чай", "хлеб"]

#Получить элемент списка можно по индексу. 0 - индекс первого элемента.

print(products[1])

numbers=[1,2,3,4,5]
some_list = [1,"hello",3.14, True]

#Главная особенность списков - это то, что элементы в нем - изменяемы
# т.е. можно добавлять элементы, изменять и удалять их.

colors = ["red", "green", "blue", "rtx3060"]
#Добавить элемент в конец списка
colors.append("white")
print(colors)
#Удалить элемент
colors.remove("rtx3060")
print(colors)
#Добавить элемент в определенное место списка
colors.insert(0,"black")
print(colors)


names = ['Альфред', 'Имануил', "Изабелла"]

for n in names:
    if n == "Альфред":
        print(n)




