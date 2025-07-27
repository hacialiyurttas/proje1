def hesap_makinesi_ana_ekran():
    print ("╔════════════════════════════════════════╗")
    print ("║      Hesap Makinesi                    ║")
    print ("║   1-Çarpma                             ║")
    print ("║   2-Toplama                            ║")
    print ("║   3-Bolme                              ║")
    print ("║   4-Cikarma                            ║")
    print ("║   5-Ana Ekran                          ║")
    print ("║   6-Cikis                              ║")
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
        print ("Çarpma işlemi yapılacaktır")
        import moduller.carpma
        moduller.carpma.carpma()
    elif secim == "2" :
        print ("Toplama işlemi yapılacaktır")
        import moduller.topla
        moduller.topla.topla()
    elif secim == "3" :
        print ("Bölme işlemi yapılacaktır")
        import moduller.bolme
        moduller.bolme.bolme()
    elif secim == "4" :
        print ("Çıkarma işlemi yapılacaktır")
        import moduller.cikarma
        moduller.cikarma.cikarma()
    elif secim == "5" :
        #print ("Ana Ekrana dönülecek")
        #import anamenu
        #anamenu1.anamenu()
        hesap_makinesi_ana_ekran()
    elif secim == "6" :
        print ("Programdan Çıkılacaktır")
        exit
    else : print ("yanlış değer girdiniz",hesap_makinesi_ana_ekran())
        
hesap_makinesi_ana_ekran()