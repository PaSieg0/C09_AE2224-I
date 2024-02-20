from math import e

g = 9.80665

def isop(p0, T, h1, h0):
    return p0*(e**(-(g/(287 * T) * (h1-h0))))
def gradp(p0, T1, T0, a):
    return p0*(T1/T0)**(-g/(a*287))


ulimits = [11000, 20000, 32000, 47000, 51000, 71000, 86000]
avalues = [-0.0065, 0, 0.001, 0.0028, 0, -0.0028, -0.002]

def isa(h):
    if h > 86000 or h < 0:
        return "Error, invalid altitude"
    T0 = 288.15
    p0 = 101325
    lower = 0
    for upper, a in zip(ulimits, avalues):
        if a == 0:
            p0 = isop(p0, T0, min(upper,h), lower)
        else:
            T1 = T0 + a * (min(upper,h) - lower)
            p0 = gradp(p0, T1, T0, a)
        
        if h < upper:
            return T1, p0, p0/(287*T1)
        lower = upper
        T0 = T1
    

if __name__ == "__main__":
    while 1:
        unit = input("1 . Calculate ISA for altitude in meters\n2 . Calculate ISA for altitude in feet\n3 . Calculate ISA for altitude in FL\nEnter your choice: ")
        if unit == '1':
            altitude = int(input("Enter desired altitude in meters:"))
        elif unit == '2':
            altitude = int(input("Enter desired altitude in feet:"))
            altitude *= 0.3048
        elif unit == '3':
            altitude = int(input("Enter desired altitude in FL:"))
            altitude *= 304.8
        print(isa(altitude))