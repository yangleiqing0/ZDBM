import numpy

a = numpy.array([1, 2.3, 444])
# print(numpy.array(a).astype(numpy.int))
print(a[1:2])

b = numpy.array([[1, 2, 3], [4, 0, 6]])
# b = numpy.array([[[1, 2, 3], [4, 0, 6]], [[1, 2, 3], [4, 0, 6]]])
print(b*b)
print()
print(b+b)
print("---")
b[:, 1:] = 0
print(b)
c = a == 2.3
print("===")
print(a[[2, 0]])
print(["==--"], b)
print(b[numpy.ix_([1, 0], [0, 1])])

d = numpy.arange(4*2).reshape(4, 2)
e = numpy.arange(6).reshape(3, 2)


print(d)
print(e.T)
re = numpy.dot(d, e.T)
print(re)
r1 = numpy.where(re % 3 == 1, 100, 200)
print(r1)
print('-----')
r = numpy.where(re % 3 == 2, 0, r1)
print(r)
print((r > 0).all())
r.sort(1)
print(r)
r.sort(0)
print(r)
print(numpy.unique(r))
print("====")
a1 = numpy.array([0, 1, 3, 5])
b1 = numpy.array([1, 2, 3, 4])
# print(numpy.where(numpy.in1d(a1, b1), a1, 555))
print(numpy.setdiff1d(a1, b1))
print(numpy.setxor1d(a1, b1))


a2 = numpy.array([[0, 1, 3, 5], [0, 0, 0, 0]])
b2 = numpy.array([[1, 2, 3, 4], [1, 1, 1, 1]])

print(numpy.concatenate([a2, b2]))
print(numpy.concatenate([a2, b2], axis=1))

print(numpy.hstack((a2, b2)))
print(numpy.vstack((a2, b2)))

c2 = numpy.random.randn(3, 2)
# print(c2.repeat(2))
print(c2)
# print(numpy.tile(c2, (2, 3)))
print("-1-1-1")
print(c2.take([0], axis=0))
print(c2.take([0], axis=1))
# c2.put([0, 1, 3], [10, 20, 30])
print(c2)

c2.tofile("test.txt")

d2 = numpy.fromfile("test.txt")
d2.shape = 3, 2
print(d2)

