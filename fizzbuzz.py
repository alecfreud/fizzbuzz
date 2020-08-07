def multiple(i, div):
    if i % div == 0: return i
def switcher(i):
    switcher = {
        multiple(i,3) : 'Fuzz',
        multiple(i,5): 'Buzz',
        multiple(i,15): 'FuzzBuzz', }
    return switcher.get(i,i)
print(list(map(switcher, list(range(1,101)))))
