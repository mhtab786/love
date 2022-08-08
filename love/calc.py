print("$$$_____$$$$$$$_$$$$$$$_$$$_______$$$_$$$$$$$$$$")
print("$$$____$$$____$$$____$$$_$$$_____$$$__$$$_______")
print("$$$____$$$_____$_____$$$_$$$_____$$$__$$$_______")
print("$$$_____$$$_________$$$___$$$___$$$___$$$$$$$$__")     #ascii art
print("$$$______$$$_______$$$_____$$$_$$$____$$$_______")
print("$$$_______$$$_____$$$______$$$_$$$____$$$_______")
print("$$$$$$$$$___$$$$$$$_________$$$$$_____$$$$$$$$$$")




my=input("your name ")
hes=input("his/her name ")

t=my.count("t")
r=my.count("r")
u=my.count("u")
e=my.count("e")
t1=hes.count("t")
r1=hes.count("r")
u1=hes.count("u")
e1=hes.count("e")

# print(type(t))
l=my.count("l")
o=my.count("o")
v=my.count("v")
ee=my.count("e")
l1=hes.count("l")
o1=hes.count("o")
v1=hes.count("v")
e11=hes.count("e")

true=str(t+r+u+e+t1+r1+u1+e1)
love=str(l+o+v+ee+l1+o1+v1+e11)
tv=int(true+love)

if tv<=10 or tv>=90:
    print(f"your score is {tv}, you go together like coke & mentos")
elif tv<=50 and tv>=40:
    print(f"your score is {tv}, you are alright together")
else:
    print(f"your score is {tv}")