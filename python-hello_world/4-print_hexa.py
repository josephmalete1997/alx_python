alphabets = [0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f',0,0,'a','b','c','d','e','f']
    
for i in range(0,98):
    if i >= 10 and i <= 15:
        print("{0} = 0x{1}".format(i,alphabets[i]))
    elif i >= 26 and i <= 31:
        print("{0} = 0x{1}".format(i,alphabets[i]))
    elif i >= 42 and i <= 47:
        print("{0} = 0x{1}".format(i,alphabets[i]))
    elif i >= 58 and i <= 63:
        print("{0} = 0x{1}".format(i,alphabets[i]))
    elif i >= 74 and i <= 79:
        print("{0} = 0x{1}".format(i,alphabets[i]))
    elif i >= 90 and i <= 95:
        print("{0} = 0x{1}".format(i,alphabets[i]))
    else:
        print("{0} = 0x{0}".format(i))
    
