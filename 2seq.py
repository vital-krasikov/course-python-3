nums = input("Введите элементы списка через разделитель (,;/) ")

if nums.find(';') != -1:
    num_list = [int(i) for i in nums.split(';')]
elif nums.find('/') != -1:
    num_list = [int(i) for i in nums.split('/')]
else:
    num_list = [int(i) for i in nums.split(',')]

num_list_uniq = list(set(num_list))
print(num_list_uniq)