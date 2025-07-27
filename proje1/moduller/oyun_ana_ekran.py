def oyun_ana_ekran():
        print ("╔════════════════════════════════════════╗")
        print ("║      OYUNLAR ANAMENU                   ║")
        print ("║   1-Sayi Bulma                         ║")
        print ("║   2-Kablumbaga                         ║")
        print ("║   3-Çıkış                          ║")
        print ("║                                        ║")
        print ("║   Seciminiz nedir?                     ║")
        print ("║                                        ║")
        print ("╚════════════════════════════════════════╝")

        secim = input()
        print ("seçiminiz:",secim," idi")
        if secim == "1" :
            print ("Sayi Bulma Oyunu seçtiniz")
            import moduller.sayi_bulma
            moduller.sayi_bulma.sayi_bulma()
        elif secim == "2" :
            print ("Kablumbaga yarisi oyunu seçtiniz")
            import moduller.kablumbaga
            moduller.kablumbaga.kablumbaga()
        elif secim == "3" :
            print ("Programdan Çıkılacaktır")
            exit()
        else : print ("yanliş seçim yaptiniz lütfen secimi tekrarlayin")
        oyun_ana_ekran()
oyun_ana_ekran()

