from math import sqrt
class Vector:
  def __init__(this, x, y):
    this.x = x
    this.y = y

  def __repr__(this):
    return f"Vector({this.x},{this.y})"
  
  def __add__(this, other):
    return Vector(this.x + other.x, this.y + other.y)
  
  def __sub__(this, other):
    return Vector(this.x - other.x, this.y - other.y)
  
  def __mul__(this, other):
    return Vector(this.x * other, this.y * other)
  
  def __eq__(this, other):
    return this.x == other.x and this.y == other.y
  
  def __len__(this):
    return round(sqrt(this.x**2 + this.y**2))
  
  def __getitem__(this, index):
    if index == 0:
      return this.x
    elif index == 1:
      return this.y
    else:
      return None

v1 = Vector(2, 4)
v2 = Vector(3, 1)
print(v1)                     # Output: Vector(2, 4)
print(v1 + v2)                # Output: Vector(5, 5)
print(v1 - v2)                # Output: Vector(-1, 3)
print(v1 * 3)                 # Output: Vector(6, 12)
print(v1 == Vector(2, 4))  # Output: True
print(len(v1))                # Output: 4 (magnitude of Vector(2, 4) is ~4.47, rounded to 4)
print(v1[0])                  # Output: 2 (x component)
print(v1[1])                  # Output: 4 (y component)
print(v1[5])                  # Output: None