def set_bit(value, bit):
    return value | (1<<bit)

# def clear_bit(value, bit):
#     return value & ~(1<<bit)


def parse_row(d):
    return parse_bin(d[:7], 'B')

def parse_col(d):
    return parse_bin(d[-3:], 'R')

def parse_bin(d, char):
    val = 0
    for i in range(len(d)):
        c = d[i]
        if c == char:
            bit_index = len(d) - 1 - i  # -1 because len([1]) return 1, but it is index 0
            val = set_bit(val, bit_index)
    return val

def calc_seat_id(row, col):
    return row*8+col

with open('data') as file:
    data = file.read().splitlines()


# ------------

print('Part 1')


max_id = 0
for d in data:
    id = calc_seat_id(parse_row(d), parse_col(d))
    if id > max_id: max_id = id
print(max_id)


print('Part 2')
used_ids = []
for d in data:
    used_ids.append(calc_seat_id(parse_row(d), parse_col(d)))
used_ids.sort()

# find free seet
for i in range(used_ids[0], used_ids[-1] + 1):
    if i not in used_ids:
        print(i)
