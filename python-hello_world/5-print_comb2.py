num = []
for i in range(0,100):
    if i < 10:
        num.append("0{}".format(i))
    else:
        num.append(str(i))
print(', '.join(num))

    
