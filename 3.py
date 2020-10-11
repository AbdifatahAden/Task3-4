
from numpy import var
from pandas import Series
 
 ################################TASK3######################################################################

data = ['1', 2, 3.1, 'hi!', 5, -512, 12.42, 'sber', 10.10, 98]
 
s = Series(data, index=range(2, 12))

try:
    print(float(s[3]) + float(s[5]))
except ValueError:
    print('не может быть определён')

a = s[s.apply(lambda x: isinstance(x, int))]
if a.all():
    print(round(var(a), 2))
else:
    print('не может быть определён')

##################################################TASK4############################################################

np.random.seed(242)
s = pd.Series(np.random.normal(size=100) ** 3, index=[x * 3 for x in range(100)])
print(s[(x % 2 != 0 for x in s.index) and (s < 2.6)].sum(), ",", s[s < 0].count())