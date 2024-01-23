from sympy import *
from mpmath import *
mp.dps = 15; mp.pretty = True   # option cho mpmath (15 là số chữ số thập phân)

def calcSideAngleSide(s1, A2, s3):
    if A2>0 and A2<180:
        s2 = sqrt(s1**2+s3**2-2*s1*s3*cos(radians(A2)))
        A1 = degrees(acos((s2**2+s3**2-s1**2)/(2*s2*s3)))
        A3 = 180 - (A1 + A2)
        Radius = s1/(2*sin(radians(A1)))
        Area = 0.5*s1*s3*sin(radians(A2))
        return (s1, s2, s3, A1, A2, A3, Radius, Area)
    else:
        return None

def calcAngleSideAngle(A1, s2, A3):
    if A1>0 and A3>0 and A1+A3<180:
        A2 = 180 - (A1 + A3)
        s1 = s2*sin(radians(A1))/sin(radians(A2))
        s3 = s2*sin(radians(A3))/sin(radians(A2))
        Radius = s1/(2*sin(radians(A1)))
        Area = 0.5*s1*s3*sin(radians(A2))
        return (s1, s2, s3, A1, A2, A3, Radius, Area)
    else:
        return None

def calcSideSideSide(s1, s2, s3):
    if s1>0 and s2>0 and s3>0 and s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
        A1 = degrees(acos((s2**2+s3**2-s1**2)/(2*s2*s3)))
        A2 = degrees(acos((s1**2+s3**2-s2**2)/(2*s1*s3)))
        A3 = 180 - (A1 + A2)
        Radius = s1/(2*sin(radians(A1)))
        Area = 0.5*s1*s3*sin(radians(A2))
        return (s1, s2, s3, A1, A2, A3, Radius, Area)
    else:
        return None
    
triangle = calcSideSideSide(13,14,15)
print(triangle)
# x = degrees(pi/3)
# print(nsimplify(x))