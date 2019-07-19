#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname,fields,homedir,sh)
# from collections import defaultdict
# d = defaultdict(list)
# pairs={'a': [1, 2], 'b': [4]}
# for key, value in pairs:
#     d[key].append(value)


from functools import partial
def spam(a, b, c, d):
    print(a, b, c, d)

s1 = partial(spam, 1)
s2 = partial(spam, d=42)
s3 = partial(spam, 1, 2, d=42)












