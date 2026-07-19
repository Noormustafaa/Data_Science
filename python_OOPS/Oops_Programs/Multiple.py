class A:
    varA ="Weclome To Class A"

class B: 
    varB = "Welcome to class B"


class C(A, B):
    varc="Welcome to class C"
  
  
c1 = C()
  
print(c1.varc)
print(c1.varA)
print(c1.varB)
