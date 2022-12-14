# This is how you create an empty set
s = set()

#And this is how you add elements to the set:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(1)
<<<<<<< HEAD
s.add(6)
=======
s.add(6)
s.add(7)
s.add(8)
s.add(9)
>>>>>>> cbb1c143a3830a03dbd701b3a3c201b434303ea8

s.remove(2)
<<<<<<< HEAD
s.remove(3)
=======
s.remove(4)
>>>>>>> cbb1c143a3830a03dbd701b3a3c201b434303ea8

#This is how you print and view the contents of the set that you've created.
print(s)

#This is how you find teh size of the set:
print(f"The set has {len(s)} elements")