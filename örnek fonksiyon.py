def tam_bolenleri_bul(sayi):
    tam_bolenleri=[]
    
    for i in range(2,sayi):
        if(sayi%i==0):
            tam_bolenleri.append(i)

    return tam_bolenleri
print(tam_bolenleri_bul(15))
