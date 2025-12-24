import lab_python_fp as lpf
from operator import abs
import time
#-------------------------------------
# Task 1
#-------------------------------------
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {},
    {'title': 'Стол'}
]
print(lpf.field(goods, 'title'))
print(lpf.field(goods, 'title', 'price'))
#-------------------------------------
# Task 2
#-------------------------------------
print(lpf.gen_random(5, 1, 10))
#-------------------------------------
# Task 3
#-------------------------------------
data = lpf.gen_random(10, 1, 3)
for i in lpf.Unique(data):
    print(i)
#-------------------------------------
# Task 4
#-------------------------------------
data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
result = sorted(data, key=abs, reverse=True)
print(result)
result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
print(result_with_lambda)
#-------------------------------------
# Task 5
#-------------------------------------
@lpf.print_result
def test_1():
    return 1
@lpf.print_result
def test_2():
    return 'iu5'
@lpf.print_result
def test_3():
    return {'a': 1, 'b': 2}
@lpf.print_result
def test_4():
    return [1, 2]
print('!!!!!!!!')
test_1()
test_2()
test_3()
test_4()
#-------------------------------------
# Task 6
#-------------------------------------
with lpf.cm_timer_1():
    time.sleep(5.5) 
with lpf.cm_timer_2():
    time.sleep(5.5) 