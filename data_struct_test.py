#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname,fields,homedir,sh)
# from collections import defaultdict
# d = defaultdict(list)
# pairs={'a': [1, 2], 'b': [4]}
# for key, value in pairs:
#     d[key].append(value)

from collections import deque
class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line
    def clear(self):
        self.history.clear()
