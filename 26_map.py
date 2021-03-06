# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# it accepts two variables, our iterable and the func we'd like to apply
# map(function,iterable)


store = [("shirt", 20.00),

         ("pants", 25.00),

         ("jacket", 50.00),

         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

l = [20, 30, 40, 50]
m = lambda x: x*2
new_l = list(map(m,l))

for i in new_l:
    print(i)