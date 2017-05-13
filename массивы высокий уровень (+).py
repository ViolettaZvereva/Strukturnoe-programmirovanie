def bin_to_dec(n):
    stepen=len(n)
    print (stepen)
    chislo_dec=0
    for i in range (0, stepen):
        chislo_dec += int(n[i])*(2**(stepen-i-1))

    return chislo_dec
    
x = (input("Введите число= " ))
print (x," = ", bin_to_dec(x))

