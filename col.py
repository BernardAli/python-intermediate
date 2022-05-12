from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
a = "aaaaabbbbccc"
counter = Counter(a)
print(counter)
print(counter.items())
print(counter.keys())
print(counter.values())
print(counter.most_common(2)[0][0])
print(list(counter.elements()))

# namedtuple
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)
print(pt.x)
print(pt.y)

# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)


# defaultdict
d = defaultdict(float)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['a'])
print(d['b'])
print(d['d'])

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(0)
d.extend([4, 5, 6, 7])
d.extendleft([4, 5, 6, 7])
print(d)
d.rotate(-1)
print(d)