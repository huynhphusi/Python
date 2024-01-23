from sympy import *

# Tính diện tích tam giác bằng công thức Heron

a,b,c = 2,3,4

if a>0 and b>0 and c>0 and a+b>c and b+c>a and c+a>b:
    p = (a+b+c)/2                                       # Tính nửa chu vi
    area = sqrt(p*(p-a)*(p-b)*(p-c))                    # Tính diện tích

    print(f"Cạnh a = {a}, b = {b}, c = {c}")
    print(f"Diện tích S = {nsimplify(area)}")           #nsimplify(x): viết dạng căn, phân số
else:
    print("Đây không phải độ dài 3 cạnh của tam giác")