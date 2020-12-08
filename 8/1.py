def parse_instructions(data):
    instructions = []
    for d in data:
        d = d.split(' ')
        instructions.append((d[0], int(d[1]), False))
    return instructions


with open('data') as file:
    data = file.read().splitlines()

instructions = parse_instructions(data)


def loop(INSTRUC):
    INSTRUC = INSTRUC[:]
    IP = 0
    ACC = 0
    EXIT_CODE=0
    while True:
        # print(f'{IP + 1} - {INSTRUC[IP][0]}: {INSTRUC[IP][1]}')
        if INSTRUC[IP][2] == True:
            print('----LOOP DETECTED----')
            print(f'Instruc: {IP + 1} - {INSTRUC[IP][0]}: {INSTRUC[IP][1]}')
            print(f'Acc: {ACC}')
            EXIT_CODE = 1
            break
        INSTRUC[IP] = (INSTRUC[IP][0], INSTRUC[IP][1], True)

        if INSTRUC[IP][0] == 'jmp':
            IP += INSTRUC[IP][1] - 1
        if INSTRUC[IP][0] == 'acc':
            ACC += INSTRUC[IP][1]
        IP += 1

        if (IP == len(INSTRUC)):
            print('----COMPLETED----')
            print(ACC)
            break
    return EXIT_CODE


print('PART ONE')
loop(instructions)



print('\n\n\nPART TWO')
for i in range(len(instructions)):
    patched_instruc = instructions[:]
    if instructions[i][0] == 'nop':
        patched_instruc[i] = ('jmp', patched_instruc[i][1], False)
    elif instructions[i][0] == 'jmp':
        patched_instruc[i] = ('nop', patched_instruc[i][1], False)
    if loop(patched_instruc) == 0:
        break