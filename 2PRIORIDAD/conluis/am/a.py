import components.tools as t

a = t.Encode('hola mundo', 'asdf')
print(a)
print(t.Decode(a, 'asdf'))