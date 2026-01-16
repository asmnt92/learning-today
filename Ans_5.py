dct={'student1':50,'student2':80,'student3':70}

student=None
mark=0

for key,val in dct.items():
    if val > mark:
        mark=val
        student=key

print(student,mark)


# print(sorted(dct,key=dct.get,reverse=True)[0],dct[sorted(dct,key=dct.get,reverse=True)[0]])

