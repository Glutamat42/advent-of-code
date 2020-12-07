with open('data') as file:
    data_uniq_p_group = file.read()

data = data_uniq_p_group.split('\n\n')

data_uniq_p_group = [d.replace('\n', '') for d in data]

counts = [len(set(d)) for d in data_uniq_p_group]

print(sum(counts))

print('Part 2')
counts = []
for group in data:
    group = group.split('\n')
    all_yes = group[0]
    for person in group:
        for ay in all_yes:
            if ay not in person and person is not '':
                all_yes = all_yes.replace(ay, '')
    counts.append(len(all_yes))
print(sum(counts))
