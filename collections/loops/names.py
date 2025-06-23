names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

for name in names:
    if name != 'Max':
        upper_name = names[index].upper()
        upper_names.append(upper_name)

print(upper_names)
