import math

print("###################")
print("Area perimetro del circulo")
print("###################")

# input

r=input("Dijite el valor del radio: ")

r= int(r)


# prossesing 

p = 2 * math.pi * r

a = math.pi * r**2

# output

print("###################")
print("el area es : " + str(a))
print("el perimetro es: " + str(p))
print("###################")