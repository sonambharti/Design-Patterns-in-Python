"Decorator Use Case Example Code"
from value import Value
from add import Add
from sub import Sub

A = Value(10)
B = Value(12)
C = Value(54)

print(Add(A, B))
print(Add(A, 100))
print(Sub(C, A))
print(Sub(Add(C, B), A))
print(Sub(100, 101))
print(Add(Sub(Add(C, B), A), 100))
print(Sub(123, Add(C, C)))
print(Add(Sub(Add(C, 10), A), 100))
print(A)
print(B)
print(C)