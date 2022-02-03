def tam_bolenleri_bul(sayi):
 tam_bolenler = []
 
 for i in range(2, sayi):
    if (sayi % i == 0):
        tam_bolenler.append(i) 
 return tam_bolenler

print(tam_bolenleri_bul(15))