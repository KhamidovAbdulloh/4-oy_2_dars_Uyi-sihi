class F(object):
    pass
class E(object):
    pass
class D(object):
    pass
class C(D, F):
    pass
class B(D, E):
    pass
class A(B, C):
    pass

print('MRO A : ', A.mro())
print('MRO B : ', B.mro())
print('MRO C : ', C.mro())
print('MRO D : ', D.mro())
print('MRO E : ', E.mro())
print('MRO F : ', F.mro())

input()
