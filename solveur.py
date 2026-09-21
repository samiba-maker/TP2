a = 1
b = 3
c = 2

def resoudre_second_degre(a, b, c):
    if a == 0:
        raise ValueError("Le coefficient 'a' ne peut pas être nul")
    
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        if x1 < x2:
            return (x1, x2)
        else:
            return (x2, x1)

    elif delta == 0:
        x = (-b)/(2*a) 
        return (x,)

    else:          #delta < 0
        z1 = (-b - (-delta)**0.5*1j)/(2*a)
        z2 = (-b + (-delta)**0.5*1j)/(2*a) 
        return (z1, z2)

print(resoudre_second_degre(a, b, c))