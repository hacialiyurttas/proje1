def anamenu():

    print ("╔════════════════════════════════════════╗")
    print ("║      PYTHON ÇALIŞMALARI ANAMENU        ║")
    print ("║   1-Hesap makinesi                     ║")
    print ("║   2-Oyunlar                            ║")
    print ("║   3-Çizimler                           ║")
    print ("║   4-Kitle Endeks                       ║")
    print ("║   5-Daire Alan                         ║")
    print ("║   6-Bölünen Sayılar                    ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║                                        ║")
    print ("║   Seciminiz nedir?                     ║")
    print ("║                                        ║")
    print ("╚════════════════════════════════════════╝")

    secim = input()
    print ("seçiminiz:",secim," idi")
    if secim == "1" :
        print ("Hesap Makinesi seçtiniz")
        import moduller.hesap_makinesi_ana_ekran
        moduller.hesap_makinesi_ana_ekran.hesap_makinesi_ana_ekran()
    elif secim == "2" :
        print ("Oyunlar seçtiniz")
        import moduller.oyun_ana_ekran
        moduller.oyun_ana_ekran.oyun_ana_ekran()
    elif secim == "3" :
        print ("Çizimler seçtiniz")
        import moduller.cizim_ana_ekran
        moduller.cizim_ana_ekran.cizim_ana_ekran()
    elif secim == "4" :
        print ("Kitle Endeks seçtiniz")
        import moduller.kitle_endeks
        
    elif secim == "5" :
        print ("Daire Alan Hesapla")
        import moduller.daire_alan_hesapla
        moduller.daire_alan_hesapla.daire_alan_hesapla()
    elif secim == "6" :
        print ("Bölünen Sayıları Bulma")
        import moduller.bolunen_sayilar
        moduller.bolunen_sayilar.bolunen_sayilar()
    
    else : print ("yanlış seçim yaptınız lütfen secimi tekrarlayın",anamenu())
        
anamenu()