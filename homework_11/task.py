from urllib import urlopen


page = urlopen('http://rss.slashdot.org/slashdot/slashdot')

titles = []
descriptions = []


def parse_tag(line, tag, closing_tag):
    if tag in line:
        left = line.find(tag) + len(tag)
        right = line.find(closing_tag)
        res = line[left + 1:right]

        return res

    return


in_item = False
for line in page:
    if '<item' in line and '<items' not in line:
        in_item = True
    if '</item>' in line and '</items>' not in line:
        in_item = False

    if in_item:
        title = parse_tag(line, '<title', '</title>')
        if title:
            titles.append(title)

        description = parse_tag(line, '<description', '</description>')
        if description:
            descriptions.append(description)

print len(titles)
print len(descriptions)