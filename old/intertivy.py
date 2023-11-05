# class Solution():
import itertools
a = ['abs', 'qwe', 'asd']
b = ['rty', 'fgh', 'cvb']
c = ['uio', 'jkl', 'bnm']
d = [a, b, c]
resultlist = []

print(i for i in itertools.combinations(d, 3))


# print(a[i:] + b[i:] + c[i:] for i in )

# def func():
# 	i=0
# 	for i in range(len(d)):
# 		func2(0, d[0])
# def func2(index, s):
# 	if index == len(d) - 1:
# 		resultlist.append(s)
# 	for element in s:
# 		return element + func2(i, d[i+1])
# 		# return [element + func(i, d[i+1]) for element in d[i]]
# func()