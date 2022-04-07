nums1 = input("Введите элементы первого списка через запятую: ")
nums2 = input("Введите элементы второго списка через запятую: ")

num_list1 = [int(i) for i in nums1.split(',')]
num_list2 = [int(i) for i in nums2.split(',')]

for i in reversed(num_list1):
    if i in num_list2:
        num_list1.remove(i)

print(num_list1)
