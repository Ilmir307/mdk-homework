def calc(items,disc):
    total=0
    for i in items:
        total=total+i
    if disc==True:
        total=total-total*0.1
    else:
        total=total
    x = total
    print("Итого:",x)
    return x

data=[100,200,50]
print(calc(data,True))
