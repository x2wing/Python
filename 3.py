from timeit import Timer
 
tmp = "Python 3.2.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32."
 
def case1():  # А. инкрементальные конкатенации в цикле
    s = ""
    for i in range(10000):
        s += tmp
 
def case2():  # Б. через промежуточный список и метод join
    s = []
    for i in range(10000):
        s.append(tmp)
    s = "".join(s)
 
def case3():  # В. списковое выражение и метод join
    return "".join([tmp for i in range(10000)])
 
def case4():  # Г. генераторное выражение и метод join
    return "".join(tmp for i in range(10000))
 
for v in range(1,5):
    print (Timer("func()","from __main__ import case%s as func" % v).timeit(200))