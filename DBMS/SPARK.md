# Q1 : 
```python
'''
    Q1 : SELECT name FROM Customer WHERE month(startDate)=7
'''

res = customer.map(lambda x : x.split(','))\
              .filter(lambda x : x[1].split('/')[1] == '07')\
              .map(lambda x : x[-1])
res.take(5)
```
---

# Q2 : 
```python
'''
    Q2 : SELECT DISTINCT name FROM Customer WHERE month(startDate)= 7 (Without Distinct)
'''
res = customer.map(lambda x : x.split(','))\
              .filter(lambda x : x[1].split('/')[1] == '07')\
              .map(lambda x : (x[-1],1))\
              .reduceByKey(lambda x,y:x+y)\
              .map(lambda x : x[0])
res.take(5)
```
---
# Q3 : 
```python
from operator import methodcaller,add

def f_1(x):
   return (x[0],x[1]), (int(x[1]),1)
def f_2(x,y):
   return tuple(map(add,x,y))
def f_3(x):
   return  x[0][0],(x[1][0], 1)

out = order.map(methodcaller('split',','))\
           .map(f_1)\
           .reduceByKey(f_2)\
           .map(f_3)\
           .reduceByKey(f_2)\
           .collect()

out = sorted(out,key=lambda x : int(x[0]))
out
```

