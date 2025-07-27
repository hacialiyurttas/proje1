def bolunen_sayilar():
    maxsayi=int(input("maximum sayi seciniz"))
    bolum=int(input("bölünen sayi seciniz"))
    
    for sayi in range(0,maxsayi+1):
        if sayi % bolum ==0:
            print(sayi)
    input("çıkış yapıacaktır")
    exit()
bolunen_sayilar()