import requests
from bs4 import BeautifulSoup

##### D&R URLS #####
ithaki_dr_url = "https://www.dr.com.tr/Yayinevi/ithaki-yayinlari/s=5119"
isbankasi_dr_url = "https://www.dr.com.tr/Yayinevi/is-bankasi-kultur-yayinlari/s=5109"
yky_dr_url = "https://www.dr.com.tr/Yayinevi/yapi-kredi-yayinlari/s=10615"
can_dr_url = "https://www.dr.com.tr/Yayinevi/can-yayinlari/s=1883"
dogan_dr_url = "https://www.dr.com.tr/yayinevi/dogan-kitap/s=2744"
kronik_dr_url = "https://www.dr.com.tr/yayinevi/kronik-kitap/s=5786"
sel_dr_url = "https://www.dr.com.tr/yayinevi/sel-yayincilik/s=8753"
altin_dr_url = "https://www.dr.com.tr/yayinevi/altin-kitaplar/s=510"
ayrinti_dr_url = "https://www.dr.com.tr/yayinevi/ayrinti-yayinlari/s=1113"
kodlab_dr_url = "https://www.dr.com.tr/yayinevi/kodlab/s=5693"

##### IDEFIX URLS #####
ithaki_idefix_url = "https://www.idefix.com/yayinevi/ithaki-yayinlari/s=5119"
isbankasi_idefix_url = "https://www.idefix.com/yayinevi/is-bankasi-kultur-yayinlari/s=5109"
yky_idefix_url = "https://www.idefix.com/yayinevi/yapi-kredi-yayinlari/s=10615"
can_idefix_url = "https://www.idefix.com/yayinevi/can-yayinlari/s=1883"
dogan_idefix_url = "https://www.idefix.com/yayinevi/dogan-kitap/s=2744"
kronik_idefix_url = "https://www.idefix.com/yayinevi/kronik-kitap/s=5786"
sel_idefix_url = "https://www.idefix.com/yayinevi/sel-yayincilik/s=8753"
altin_idefix_url = "https://www.idefix.com/yayinevi/altin-kitaplar/s=510"
ayrinti_idefix_url = "https://www.idefix.com/yayinevi/ayrinti-yayinlari/s=1113"
kodlab_idefix_url = "https://www.idefix.com/yayinevi/kodlab/s=5693"


def titleScript(param, store):
    if store == "dr":
        title = param.find("h1",{"class":"cat-name"}).string
        print("-"*120)
        print("|" + title.rjust(60) + "|".rjust(59," "))
        print("-"*120)
    elif store == "idefix":
        title = param.find("h1").string
        #print("BURADAYIM")
        print("-"*120)
        print("|" + title.rjust(60) + "|".rjust(59," "))
        print("-"*120)

def authorCheck(author):
    if not author:
        author = "Anonim"
    else:
        author = author.string

    return author

def getSoup(url, store):
    html_request = requests.get(url).content
    soup = BeautifulSoup(html_request, "html.parser")
    getList(soup, store)

# TODO getList fonksiyonu sadece D&R çin ayarlı onu düzelt
def getList(soup, store):
    if store == "dr":
        list = soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
        count = 0
        titleScript(soup, store)

        for i in list:
            name = i.find("a", {"class":"prd-name"}).string
            author = i.find("a", {"class":"who"})
            price = i.find("div", {"class":"prd-price"}).string
            count +=1

            author = authorCheck(author)

            print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

    elif store == "idefix":
        list = soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
        count = 0
        titleScript(soup, store)

    

def ithaki(store):
    getSoup(ithaki_dr_url, store)

def isbankasi(store):
    getSoup(isbankasi_dr_url, store)

def yky(store):
    getSoup(yky_dr_url, store)

def can(store):
    getSoup(can_dr_url, store)

def dogan(store):
    getSoup(dogan_dr_url, store)

def kronik(store):
    getSoup(kronik_dr_url, store)

def sel(store):
    getSoup(sel_dr_url, store)

def altin(store):
    getSoup(altin_dr_url, store)

def ayrinti(store):
    getSoup(ayrinti_dr_url, store)

def kodlab(store):
    getSoup(kodlab_dr_url, store)

#! Burada klavyeden farklı bir şey girerse sorgusu yok!!!
def menu():
    while True:
        print("-"*30)
        store_choice = input("1- D&R\n2- Idefix \n0- Exit\nYour Choice?: ")
        print("-"*30)
        if store_choice == "0":
            break
        else:
            if store_choice == "1":
                store = "dr"
            elif store_choice == "2":
                store = "idefix"

        print("-"*30)
        choice = input("1- Ithaki Yayinlari\n2- Is Bankasi Yayinlari\n3- Yapı Kredi Yayinlari\n4- Can Yayinlari\n5- Dogan Kitap\n6- Kronik Kitap\n7- Sel Yayincilik\n8- Altin Kitap\n9- Ayrinti Yayinlari\n10- Kodlab\n0- Back\nYour Choice?: ")
        print("-"*30)
        if choice == "0":
            break
        else:
            if choice=="1":
                ithaki(store)
            elif choice=="2":
                isbankasi(store)
            elif choice=="3":
                yky(store)
            elif choice=="4":
                can(store)
            elif choice=="5":
                dogan(store)
            elif choice=="6":
                kronik(store)
            elif choice=="7":
                sel(store)
            elif choice=="8":
                altin(store)
            elif choice=="9":
                ayrinti(store)
            elif choice=="10":
                kodlab(store)


menu()

