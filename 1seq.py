num_list = []
n = int(input("Введите количество элементов списка: "))
for i in range(n):
    num_list.append(int(input("Введите "+str(i+1)+"-й элемент: ")))

num_list.sort()
print(num_list)