import re

required_attrs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def validate(arr):
    for attr in required_attrs:
        if attr not in [x.split(':')[0] for x in arr]:
            return False
    return True


with open('data') as file:
    data = file.read()

data = data.split('\n\n')

data = [x.replace('\n', ' ').split(' ') for x in data]

valid_cnt = 0
for d in data:
    valid_cnt += validate(d)

print(valid_cnt)


print('Part 2')

def validate_values(arr):
    for d in [x.split(':') for x in arr]:
        if d[0] == 'byr' and not (1920 <= int(d[1]) <= 2002): return False
        if d[0] == 'iyr' and not (2010 <= int(d[1]) <= 2020): return False
        if d[0] == 'eyr' and not (2020 <= int(d[1]) <= 2030): return False
        if d[0] == 'hgt':
            if d[1][-2:] == 'cm' and 150 <= int(d[1][:-2]) <= 193: continue
            if d[1][-2:] == 'in' and 59 <= int(d[1][:-2]) <= 76: continue
            return False
        if d[0] == 'hcl' and not re.search('#[0-9a-f]{6}', d[1]): return False
        if d[0] == 'ecl' and not (d[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']): return False
        if d[0] == 'pid' and not re.search('^[0-9]{9}$', d[1]): return False
    return True

valid_cnt = 0
for d in data:
    valid_cnt += validate(d) and validate_values(d)

print(valid_cnt)