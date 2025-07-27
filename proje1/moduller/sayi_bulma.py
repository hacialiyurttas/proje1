def sayi_bulma():
    import random
    print("Sayi Tahmin Oyunu")
    deneme=3
    sayi=random.randint(0,10)
    bilindi=False
    for i in range(deneme):
    
        tahmin=int(input("0-10 arasinda bir sayi tahmin ediniz."))
        if sayi==tahmin:
            print("Tebrikler bildiniz.")
            bilindi=True
            break
        elif sayi>tahmin and i!=deneme-1:
            print("Daha büyük bir sayi tahmin ediniz.")
        
        elif sayi<tahmin and i!=deneme-1:
            print("Daha küçük bir sayi tahmin ediniz.")
    if not bilindi:
        print("Sayi ",sayi," idi.")
sayi_bulma()
