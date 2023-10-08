print('x y z f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F=x and(y or not(z))and(z or not(y))
            print(x,y,z,F)