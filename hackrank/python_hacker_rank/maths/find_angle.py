"""A
|\
| \
|  \
|   \
|    \
|     \M
|      \
|       \
|        \
|_________\
B          C

it is right angle triangle find consider triangle BCM
m = AC/2
<CMB = 90
find angle b= ?

SOH CAH TOA

"""
"""
New logic is if in right angle triangle , hypotenus mid point is divided then it is called isosceles triangle   

so AM = MC= BM so MBC = BCM
"""

"""
B
|
|
|
|
|______________
M              C

"""
import math

if __name__ == "__main__":
    AB = float(input())
    BC = float(input())

    if 0 < AB <= 100 and 0 < BC <= 100 and AB.is_integer() and BC.is_integer():
        # AC = math.sqrt(AB**2 + BC**2)
        # MC = AC/2
        # angle_radian = math.asin(MC / BC)
        angle_radian = math.atan2(AB, BC)

        angle_degree = math.degrees(angle_radian)

        if angle_degree - math.floor(angle_degree) < 0.5:
            print(math.floor(angle_degree), chr(176), sep='')
        else:
            print(math.ceil(angle_degree), chr(176), sep='')







