# make dict
lunch1 = {
    'a': '1'
}
#lunch2 = dict(a='1')

# insert 
lunch1['b'] = '2'

# bring contents
idol = {
    'bts' : {
        'aa' : 24,
        'bb' : 25
    }
}

# dict + for/while
## basic
for key in lunch1:
    print(key, lunch1[key])

## bring value/key
for value in lunch1.values():
    print(value)

for key in lunch1.keys():
    print(key)

for key, value in lunch1.items():
    print(key, value)