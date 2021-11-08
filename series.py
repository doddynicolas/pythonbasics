number = int(input('give the n-digit serie:  '))
serie = input('give the serie:  ')
length = len(serie)
i = 0
while i < length:
    if number == 0 or number == length:
        print(serie)
        break
    elif number > length:
        print('the digit is too large')
        break
    else:
        j = i
        n = 0
        if (length - j) >= number:
             liste = []
             while n < number:
                n+=1
                if j < length:
                    liste +=serie[j]
                j+=1 
             liste = "".join(liste)   
             print(liste) 

    i+=1
