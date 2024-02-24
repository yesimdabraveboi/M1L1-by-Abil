import random

katasandi = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

masukan = int(input("Masukan panjang password yang anda mau: "))

hasil = ""

for i in range (masukan):

    randomchar = random.choice(katasandi)
    hasil += randomchar

print ("Password anda adalah " + (hasil))
