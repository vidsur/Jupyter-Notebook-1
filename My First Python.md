```python
import math
```


```python
math.sqrt(25)
```




    5.0




```python
math.pi
```




    3.141592653589793




```python
import numpy
```


```python
from numpy import random
```


```python
# uniform random numbers in [0,1]
dataOne = random.rand(5,5)
dataOne
```




    array([[0.22584046, 0.3032918 , 0.45352976, 0.98786381, 0.44190991],
           [0.38022002, 0.84263334, 0.8280482 , 0.36518017, 0.74764321],
           [0.9354075 , 0.97147889, 0.63584466, 0.76560706, 0.96536456],
           [0.77713104, 0.96515155, 0.99743899, 0.32617209, 0.33163333],
           [0.964004  , 0.93309791, 0.62453516, 0.4694026 , 0.1163604 ]])




```python
numpy.mean(dataOne)
```




    0.6541916171647426




```python
numpy.median(dataOne)
```




    0.7476432138722124




```python
numpy.mode(dataOne)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-14-a2eec0707e9f> in <module>
    ----> 1 numpy.mode(dataOne)
    

    ~\anaconda3\lib\site-packages\numpy\__init__.py in __getattr__(attr)
        218             else:
        219                 raise AttributeError("module {!r} has no attribute "
    --> 220                                      "{!r}".format(__name__, attr))
        221 
        222         def __dir__():
    

    AttributeError: module 'numpy' has no attribute 'mode'



```python
numpy.sum(dataOne)
```




    16.354790429118566




```python
numpy.count_nonzero(dataOne)
```




    25




```python
print("i Love Data Science")
```

    i Love Data Science
    


```python
variablename=30
print(variablename)
```

    30
    


```python
variablename1= 'I Love Data Science'
print(variablename1)
```

    I Love Data Science
    


```python
variableName = 25

type(variableName)
```




    int




```python
variableName = 25.0

type(variableName)
```




    float




```python
varOne = 25

varTwo = 25.0

varThree = varOne + varTwo

print(varThree)
type(varThree)
```

    50.0
    




    float




```python
varOne = str(25)

varTwo = 'Hello'

varThree = varOne + varTwo

print(varThree)
```

    25Hello
    


```python
listOne = [1,2,3,4]
print(listOne[1:3])
```

    [2, 3]
    


```python
listtwo= [1,2,3,4]
print(listtwo[0:2])
```

    [1, 2]
    


```python
# Dictionaries
dictionary= {'red':567.12, 'blue':891.3, 'green':234, 'yellow':567, 'black':892}
dictionary['red']
x=dictionary['red']
y=dictionary['blue']
z=dictionary['green']
a=x+y+z
a
import statistics
print(statistics.mean([x,y,z]))
```

    564.14
    


```python
print(round(564.14))
```

    564
    


```python
b= x,y,z
print(statistics.median(b))
```

    567.12
    


```python

```
