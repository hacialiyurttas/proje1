def cizim_ana_ekran():
    print ("╔════════════════════════════════════════╗")
    print ("║      ÇİZİMLER ANAMENU                  ║")
    print ("║   1-Üçgen                              ║")
    print ("║   2-Altıgen                            ║")
    print ("║   3-HavaiFişek                         ║")
    print ("║                                        ║")
    print ("║   Seciminiz nedir?                     ║")
    print ("║                                        ║")
    print ("╚════════════════════════════════════════╝")

    secim = input()
    print ("seçiminiz:",secim," idi")
    if secim == "1" :
            print ("Üçgen")
            import moduller.ucgen
            moduller.ucgen.ucgen()
    elif secim == "2":
            print ("Altıgen")
            import moduller.altigen
            moduller.altigen.altigen()
    elif secim == "3" :
            print ("Havai Fişek")
            import moduller.havaifisek
            moduller.havaifisek.havaifisek()
       
    else : print ("yanliş seçim yaptiniz lütfen secimi tekrarlayin",cizim_ana_ekran())
            
cizim_ana_ekran()