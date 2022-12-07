test = '/a/e/'

print(test)
slash = test.rfind('/')
print(slash)
test = test.rstrip('/')
print(test)
print(test.rfind('/'))
test = test[0:test.rfind('/')+1]
print(test)
