# Toplama Cikarma
print(2 + 2)
print(3 + -2)

# Carpma Bolme
print(2 * 10)
print(3 / 2)  # python3: sonuc 1.5 python2: sonuc 1 // neden? python3 bolmede float, python2 bolmede int doner... 
print("3 / 3:::", type(3 / 3))
print("3 * 3:::", type(3 * 3))

# Islem Onceligi ve Parantez Kullanimi
# print(2 + 8 * 5) sonuc 50 cikmadi :)))
print ( (2 + 8) * 5 )

# Kalansiz bolme (int)
print(3 / 3)
print("3 / 3:::", type(3 / 3))

print(3 // 3)
print("3 // 3:::", type(3 // 3))
print(4 // 3)
# Mod Alma (Kalani Bulma) 
print("Kalan Nedir? ", 9 % 3)
print("Kalan Nedir? ", 20 % 6)
print(20 // 6) # Kalansiz bolmeyi her kolinin icinde 6 urun oldugunu dusunup kac koli kullanabilecegimizi bulmak icin kullandik

# Kalansiz Bolme ve Kalani Bulma / divmod
print("divmod'u goster")
print( divmod(20, 6) )