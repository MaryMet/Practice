# Week 3: Variable Types
# author: Mary Metcalfe

a = int (3)
b = float (3.5)
e = bool ( 10 ==9 )
d = str ("how now brown cow")
kids = [ 'Angie , Willow , Eryk']

print (a)
print (b)
print (d)
print (e)
print (kids)

print (type(a))
print (type(b))
print (type(10 ==9))
print (type(d))
print (type(kids))

print('variable {} is of type:{} and value: {}'.format('a', type(a), a))
print('variable {} is of type:{} and value:{}'.format('b', type(b), b))
print('variable {} is of type:{} and value:{}'.format('d', type(d), d))
print('variable {} is of type:{} and value:{}'.format('kids', type(kids), kids))
print('variable {} is of type:{} and value:{}'.format('e', type(e), e))