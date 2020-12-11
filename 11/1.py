def init_2d(x1: int, x2: int, value='.'):
    return [[value for a in range(x1)] for a in range(x2)]


def print_2d(data):
    for y in data:
        print(y)
    print('\n\n')


# with open('test_data') as file:
with open('data') as file:
    data = file.read().splitlines()

CHAIR_EMPTY = 'L'
CHAIR_OCC = '#'

print('PART ONE')


def cnt_occupied_adjacents(x, y, map, max_distance = 1):
    cnt = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            point_done = False
            d = 1
            while not point_done and not (d > max_distance):
                _x = x + j * d
                _y = y + i * d
                if (_x < 0
                        or _y < 0
                        or _x >= len(map[0])
                        or _y >= len(map)):
                    point_done = True
                    continue
                if (map[_y][_x] == CHAIR_OCC):
                    cnt += 1
                    point_done = True
                elif (map[_y][_x] == CHAIR_EMPTY):
                    point_done = True
                d += 1
    return cnt


seat_map = data

val_changed = True
while val_changed:
    val_changed = False
    new_map = init_2d(len(seat_map[0]), len(seat_map), )
    cnt_occ = 0
    cnt_free = 0
    for y in range(len(seat_map)):
        for x in range(len(seat_map[0])):
            if (seat_map[y][x] == CHAIR_EMPTY and not cnt_occupied_adjacents(x, y, seat_map)):
                new_map[y][x] = CHAIR_OCC
                val_changed = True
            elif (seat_map[y][x] == CHAIR_OCC and cnt_occupied_adjacents(x, y, seat_map) >= 4):
                new_map[y][x] = CHAIR_EMPTY
                val_changed = True
            else:
                new_map[y][x] = seat_map[y][x]

            if new_map[y][x] == CHAIR_OCC:
                cnt_occ += 1
            elif new_map[y][x] == CHAIR_EMPTY:
                cnt_free += 1
    seat_map = new_map
    # print(f'occ {cnt_occ}')
    # print(f'free {cnt_free}')
    # print_2d(seat_map)

print(f'occ {cnt_occ}')

print('\n\n\nPART TWO')

seat_map = data

val_changed = True
while val_changed:
    val_changed = False
    new_map = init_2d(len(seat_map[0]), len(seat_map), )
    cnt_occ = 0
    cnt_free = 0
    for y in range(len(seat_map)):
        for x in range(len(seat_map[0])):
            cnt_occ_adj = cnt_occupied_adjacents(x, y, seat_map, 100)
            if (seat_map[y][x] == CHAIR_EMPTY and not cnt_occ_adj):
                new_map[y][x] = CHAIR_OCC
                val_changed = True
            elif (seat_map[y][x] == CHAIR_OCC and cnt_occ_adj >= 5):
                new_map[y][x] = CHAIR_EMPTY
                val_changed = True
            else:
                new_map[y][x] = seat_map[y][x]

            if new_map[y][x] == CHAIR_OCC:
                cnt_occ += 1
            elif new_map[y][x] == CHAIR_EMPTY:
                cnt_free += 1
    seat_map = new_map
    # print(f'occ {cnt_occ}')
    # print(f'free {cnt_free}')
    # print_2d(seat_map)

print(f'occ {cnt_occ}')
