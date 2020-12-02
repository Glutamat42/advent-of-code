

with open('data') as file:
    data = file.readlines()

print('task 1 - two entries')
for i in range(len(data)):
    for j in range(i,len(data)):
        v1 = int(data[i])
        v2 = int(data[j])
        if v1 + v2 == 2020:
            print(f'{v1} * {v2} = {v1 * v2}')

print('task 2 - 3 entries')
for i in range(len(data)):
    for j in range(i,len(data)):
        for k in range(j, len(data)):
            v1 = int(data[i])
            v2 = int(data[j])
            v3 = int(data[k])
            if v1 + v2 + v3 == 2020:
                print(f'{v1} * {v2} * {v3} = {v1 * v2 * v3}')