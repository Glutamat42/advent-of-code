with open('data') as file:
    data = file.read().splitlines()
    data = [int(x) for x in data]

print('PART ONE')
for i in range(25, len(data)):
    found = False
    for j in range(i - 25, i):
        for k in range(j + 1, i):
            if data[i] == data[j] + data[k]:
                found = True
    if not found:
        print(f'index: {i}, value:{data[i]}')
        break

print('\n\n\nPART TWO')
invalid_index = i
for i in range(invalid_index):
    sum = data[i]
    number_list = [data[i]]
    for j in range(i + 1, invalid_index):
        sum += data[j]
        number_list.append(data[j])
        if sum == data[invalid_index]:
            print(number_list)
            print(min(number_list))
            print(max(number_list))
            print(min(number_list) + max(number_list))
