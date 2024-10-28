# ray_ellipsoid_intersection.py
#
# Usage:python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
#
# Written by Alwaleed Alrashidi 
# Other contributors: Prof Brad Denby (Boilerplate and lecture slide refernce code)
#

# import Python modules
# e.g., import math # math module

import sys # argv
import math

w=7.292115*10**-5
R_E_KM = 6378.1363
E_E    = 0.081819221456

d_l_x = float('nan') 
d_l_y = float('nan') 
d_l_z = float('nan') 
c_l_x = float('nan') 
c_l_y = float('nan') 
c_l_z = float('nan')  


if len(sys.argv) == 7:
    try:
        d_l_x = float(sys.argv[1])
        d_l_y = float(sys.argv[2])
        d_l_z = float(sys.argv[3])
        c_l_x = float(sys.argv[4])
        c_l_y = float(sys.argv[5])
        c_l_z = float(sys.argv[6])

    except ValueError:
        print("Error: d_l_x, d_l_y, d_l_z, c_l_x, c_l_y, c_l_z, must be numeric.")
        exit()
else:
    print(\
        'python3 conv_ops.py d_l_x, d_l_y, d_l_z, c_l_x, c_l_y, c_l_z.'\
            )
    exit()



a = d_l_x*d_l_x + d_l_y*d_l_y + (d_l_z*d_l_z)/(1-E_E*E_E)
b = 2*(d_l_x*c_l_x+d_l_y*c_l_y+(d_l_z*c_l_z)/(1-E_E**2))
c = c_l_x**2+c_l_y**2+(c_l_z**2)/(1-E_E**2)-R_E_KM**2
discr = b*b-4.0*a*c


if discr >= 0:
    d = (-b - math.sqrt(discr))/(2*a)
    if d < 0:
        d = (-b + math.sqrt(discr))/(2*a)
    if d > 0:
        l_d = [d*d_l_x+c_l_x, d*d_l_y+c_l_y, d*d_l_z+c_l_z]

print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point