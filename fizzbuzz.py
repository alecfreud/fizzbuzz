def multiple(i, div):
    if i % div == 0: return i
def switcher(i):
    switcher = {
        multiple(i,3) : 'Fizz',
        multiple(i,5): 'Buzz',
        multiple(i,15): 'FizzBuzz', }
    return switcher.get(i,i)
print(list(map(switcher, list(range(1,101)))))
