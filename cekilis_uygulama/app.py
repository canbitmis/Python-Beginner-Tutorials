import random
import time

kullanıcılar = list()

def kullanıcı_ekle(x):
    print("-"*30)
    print("Kullanıcı Ekleme Ekranına Hoşgeldiniz!")
    ekle = input("Lütfen Eklenecek Kullanıcıyı Giriniz:")
    kullanıcılar.append(ekle)
    input("Devam Etmek İçin Enter Tuşuna Basınız...")

def kullanıcı_gor(x):
    say = 1
    print("-"*30)
    for i in x:
        print(str(say)+"-Kullanıcı Adı:",i)
        say+=1
    print("-"*30)
    input("Devam Etmek İçin Enter Tuşuna Basınız...")

def sec(x):
    say=1 #Listedeki elementleri sayar
    kisi_sec = int(input("Kaç Kişi Seçilsin?:"))
    rastgele_sec = random.sample(x,kisi_sec)
    for i in rastgele_sec:
        print(str(say)+"-Kullanıcı Adı:",i)
        say+=1
    print("-"*30)
    input("Devam Etmek İçin Enter Tuşuna Basınız...")

def karistir(x):
    print("-"*30)
    say=1
    random.shuffle(x)
    for i in x:
        print(str(say)+"-Kullanıcı Adı:",i)
        say+=1
    print("-"*30)
    input("Devam Etmek İçin Enter Tuşuna Basınız...")


while True:
    print("****ÇEKİLİŞ UYGULAMASINA HOŞGELDİNİZ!****")
    secim = int(input("1-Kullanıcı Ekle\n2-Kullanıcı Gör\n3-Kullanıcıları Karıştır\n4-Rastgele Seç\n"))

    if secim==1:
        kullanıcı_ekle(kullanıcılar)
    elif secim==2:
        kullanıcı_gor(kullanıcılar)
    elif secim==3:
        karistir(kullanıcılar)
    elif secim==4:
        print("Kişi seçme alanı hesaplanıyor...")
        time.sleep(2)
        sec(kullanıcılar)
    else:
        print("Lütfen Uygun Bir Tercih Yapınız...")





