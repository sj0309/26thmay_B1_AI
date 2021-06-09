a = input('Enter any characters: ')
b = {i:a.count(i) for i in a}
print(b)

c = list(b.values())

if (max(c)-min(c)<1 or c.count(max(c))==1):
    print("MYSTRING")
else:
    print("NOT MYSTRING")
        

