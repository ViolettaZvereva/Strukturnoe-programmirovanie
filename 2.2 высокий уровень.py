import math
N= int (input ("введите число от 1 до 99 включительно= "))
if (1<N<100):
    print("число входит в диапазон")
    if (N==1 or N==21 or N==31 or N==41 or N==51 or N==61 or N==71 or N==81 or N==91):
        print (N," копейка")
    elif (N==2 or N==3 or N==4 or N==22 or N==23 or N==24 or N==32 or N==33 or N==34 or N==42 or N==43 or N==44 or N==52 or N==53 or N==54 or N==62 or N==63 or N==64 or N==72 or N==73 or N==74 or N==82 or N==83 or N==84 or N==92 or N==93 or N==94):
        print (N, "копейки")
    elif (4<N<21) or (24<N<31) or (34<N<41) or (44<N<51) or (54<N<61) or (64<N<71) or (74<N<81) or (84<N<91) or (94<N<100):
        print (N, "копеек")
else:
    print("число не входит в диапазон")
    input()
