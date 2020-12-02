
def split_input(lines):
    result = []
    for line in lines:
        s1 = line.split(' ')
        min = int(s1[0].split('-')[0])
        max = int(s1[0].split('-')[1])
        char = s1[1][0]
        pw = s1[2]
        result.append((min,max,char,pw))
    return result

with open('data') as file:
    data = file.readlines()
data = split_input(data)


print('part one')
valid_count = 0
for d in data:
    count = d[3].count(d[2])
    if count >= d[0] and count <= d[1]:
        valid_count += 1

print(valid_count)

print('part two')
valid_count = 0
for d in data:
    valid = int(d[3][d[0]-1] == d[2])
    valid += d[3][d[1]-1] == d[2]
    valid_count += valid == 1
print(valid_count)

