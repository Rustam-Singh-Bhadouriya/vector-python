import vector as vtr

v1 = vtr.vector([1,2,3,4])
print(v1.size())
v1.show()
print(v1.back())
print(v1.vectorValue)
v1.show()
revers = v1.reverse()
v1.show()
v1.show(revers)

v1.show(v1.size())

v1.push_back(6)
v1.show()

v1.pop_back()
v1.pop()
v1.insert(0 , 34)
v1.show()
v1.show(v1.at(2))