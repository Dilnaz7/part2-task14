list = []
list1= []

yes = 'y'

while yes == 'y':
    new = int(input('Введите число, которое хотите добавить в список:\n'))
    list.append(new)
    print(list)
    yes = input('Хотите добавить ещё число в список? y/n\n')

for x in list:
    if x % 2 == 0:
        list1.append(x)
    else:
        list1.append(0)

print(list)
print(list1)