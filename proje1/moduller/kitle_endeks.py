def kitle_endeks():
    print("VÜCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI ")
    boy = float(input("Boy (cm):"))
    kilo = int(input("Kilo (kg):"))

    endeks = kilo/(boy*boy/10000)

    if endeks <=18:
        print("\n zayıf VKİ:{}".format(endeks))
    elif endeks > 18 and endeks <=25 :
        print("\n kilolu VKİ:{}".format(endeks))
    elif endeks > 25 and endeks <=30:
        print("\n obez VKİ:{}".format(endeks))
    elif endeks > 30:
        print("\n ciddi obez VKİ:{}".format(endeks))
    input("çıkış için bir tuşa basınız")
    exit()
kitle_endeks()
