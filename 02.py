from sympy import *

print(sqrt(50))                 # 5*sqrt(2)
print(latex(sqrt(50)))          # 5\sqrt{2}

x, y, z = symbols("x y z")
eqn = parse_expr('2x-y+2z-5=0', transformations='all')
print(eqn.lhs)
point = "M(1;2;5)"
point_name = point[0]
point_coor = point[2:-1].split(';')
point_coor = (int(point_coor[0]), int(point_coor[1]), int(point_coor[2]))
d = eqn.lhs.subs([(x,point_coor[0]), (y,point_coor[1]), (z,point_coor[2])])     # Thế số
a = eqn.lhs.coeff(x)
b = eqn.lhs.coeff(y)
c = eqn.lhs.coeff(z)
print(abs(d)/sqrt(a**2+b**2+c**2))           # Tính khoảng cách d(M,(P))