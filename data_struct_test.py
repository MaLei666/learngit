#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname,fields,homedir,sh)
# from collections import defaultdict
# d = defaultdict(list)
# pairs={'a': [1, 2], 'b': [4]}
# for key, value in pairs:
#     d[key].append(value)

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair(%r, %r)' % (self.x, self.y)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p=Pair(3, 4).__repr__()
print(p)
print('p is {0!r}'.format(p))
def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)

