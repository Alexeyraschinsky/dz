f = open("repozit.txt", 'w')
while True:
    f_1 = input()
    if f_1 == 'n' : break
    f.write(f_1)
    f.close()