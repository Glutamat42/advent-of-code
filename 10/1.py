data = [int(x) for x in open('data').read().splitlines()]
data.sort()

print('PART ONE')
dists = [0, 0, 0, 0]
for i in range(1, len(data)):
    dists[data[i] - data[i - 1]] += 1 if dists[data[i] - data[i - 1]] > 0 else 2
print(dists[1] * dists[3])

print('\n\n\nPART TWO')
print(dists)

seq_count = [0, 0, 0, 0, 0]
i = 0
while i < len(data):
    seq = 0 if i > 0 else 1
    while i + 1 < len(data) and data[i + 1] == data[i] + 1:
        seq += 1
        i += 1
    seq_count[seq] += 1
    i += 1
print(seq_count[2:])
print(pow(2, seq_count[2]) * pow(4, seq_count[3]) * pow(7, seq_count[4]))
