#2. Kullanıcının girdiği kısa ve uzun kenar değerlerine göre dikdörtgenin alanını ve çevresini hesaplayınız.
#Daha sonra Dikdörtgenin Alanı: ….. Çevresi:……. şeklinde bir çıktı üretiniz. Burada noktalar kullanıcının
#gireceği değerlere göre değişecektir.
kisa_kenar=int(input("kısa kesarını giriniz:"))#kısa kenar girilir
uzun_kenar=int(input(" uzun kenarını giriniz:"))#uzun kenar girilir
cevre=(uzun_kenar+kisa_kenar)*2         #dikdörtgenin çevresi hesaplanarak çevre değeşkenine atandı
alan=kisa_kenar*uzun_kenar#dikdörtgenin alan hesaplanarak çevre değeşkenine atandı
print("alanı:",alan,"çevresi:",cevre) #ekrana yazdırılır
