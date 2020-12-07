with open('data') as file:
    data = file.read().splitlines()


def parse_content(string):
    res = []
    for content in string.split(','):
        content = list(filter(len, content.split(' ')))
        if not content[0] == 'no':
            res.append((content[1] + content[2], int(content[0])))
    return res


parsed_rules = {}
for d in data:
    source, content = d.split('contain')
    source = source.split(' ')
    parsed_rules[source[0] + source[1]] = parse_content(content)

possible_colors = ['shinygold']
appends = True
while appends:
    appends = False
    for k, v in parsed_rules.items():
        for pc in possible_colors:
            if pc in [c[0] for c in v] and k not in possible_colors:
                possible_colors.append(k)
                appends = True
                continue

# remove first entry - shinygold
possible_colors = possible_colors[1:]
print(len(possible_colors))

print('Part 2')


def calc_sub_bags(bag):
    content_sum = 1
    for content2 in parsed_rules[bag]:
        content_sum += content2[1] * calc_sub_bags(content2[0])
    return content_sum


print(calc_sub_bags('shinygold') - 1)
