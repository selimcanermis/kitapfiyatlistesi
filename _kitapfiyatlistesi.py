import requests
from bs4 import BeautifulSoup

ithaki_url = "https://www.dr.com.tr/Yayinevi/ithaki-yayinlari/s=5119"
isbankasi_url = "https://www.dr.com.tr/Yayinevi/is-bankasi-kultur-yayinlari/s=5109"
yky_url = "https://www.dr.com.tr/Yayinevi/yapi-kredi-yayinlari/s=10615"
can_url = "https://www.dr.com.tr/Yayinevi/can-yayinlari/s=1883"
dogan_url = "https://www.dr.com.tr/yayinevi/dogan-kitap/s=2744"
kronik_url = "https://www.dr.com.tr/yayinevi/kronik-kitap/s=5786"
sel_url = "https://www.dr.com.tr/yayinevi/sel-yayincilik/s=8753"
altin_url = "https://www.dr.com.tr/yayinevi/altin-kitaplar/s=510"
kodlab_url = "https://www.dr.com.tr/yayinevi/kodlab/s=5693"

ithaki_html = requests.get(ithaki_url).content
isbankasi_html = requests.get(isbankasi_url).content
yky_html = requests.get(yky_url).content
can_html = requests.get(can_url).content
dogan_html = requests.get(dogan_url).content
kronik_html = requests.get(kronik_url).content
sel_html = requests.get(sel_url).content
altin_html = requests.get(altin_url).content
kodlab_html = requests.get(kodlab_url).content

ithaki_soup = BeautifulSoup(ithaki_html, "html.parser")
isbankasi_soup = BeautifulSoup(isbankasi_html, "html.parser")
yky_soup = BeautifulSoup(yky_html, "html.parser")
can_soup = BeautifulSoup(can_html, "html.parser")
dogan_soup = BeautifulSoup(dogan_html, "html.parser")
kronik_soup = BeautifulSoup(kronik_html, "html.parser")
sel_soup = BeautifulSoup(sel_html, "html.parser")
altin_soup = BeautifulSoup(altin_html, "html.parser")
kodlab_soup = BeautifulSoup(kodlab_html, "html.parser")

def ithaki():
    list = ithaki_soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
    count = 0
    titleScript(ithaki_soup)

    for i in list:
        name = i.find("a", {"class":"prd-name"}).string
        author = i.find("a", {"class":"who"})
        price = i.find("div", {"class":"prd-price"}).string
        count +=1

        if not author:
            author = "Anonim"
        else:
            author = author.string

        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

def isbankasi():
    list = isbankasi_soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
    count = 0
    titleScript(isbankasi_soup)

    for i in list:
        name = i.find("a", {"class":"prd-name"}).string
        author = i.find("a", {"class":"who"})
        price = i.find("div", {"class":"prd-price"}).string
        count +=1

        if not author:
            author = "Anonim"
        else:
            author = author.string

        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

def yky():
    list = yky_soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
    count = 0
    titleScript(yky_soup)

    for i in list:
        name = i.find("a", {"class":"prd-name"}).string
        author = i.find("a", {"class":"who"})
        price = i.find("div", {"class":"prd-price"}).string
        count +=1

        if not author:
            author = "Anonim"
        else:
            author = author.string

        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

def can():
    list = can_soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
    count = 0
    titleScript(can_soup)

    for i in list:
        name = i.find("a", {"class":"prd-name"}).string
        author = i.find("a", {"class":"who"})
        price = i.find("div", {"class":"prd-price"}).string
        count +=1

        if not author:
            author = "Anonim"
        else:
            author = author.string

        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

def dogan():
    list = dogan_soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
    count = 0
    titleScript(dogan_soup)

    for i in list:
        name = i.find("a", {"class":"prd-name"}).string
        author = i.find("a", {"class":"who"})
        price = i.find("div", {"class":"prd-price"}).string
        count +=1

        if not author:
            author = "Anonim"
        else:
            author = author.string

        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

def kronik():
    list = kronik_soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
    count = 0
    titleScript(kronik_soup)

    for i in list:
        name = i.find("a", {"class":"prd-name"}).string
        author = i.find("a", {"class":"who"})
        price = i.find("div", {"class":"prd-price"}).string
        count +=1

        if not author:
            author = "Anonim"
        else:
            author = author.string

        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

def sel():
    list = sel_soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
    count = 0
    titleScript(sel_soup)

    for i in list:
        name = i.find("a", {"class":"prd-name"}).string
        author = i.find("a", {"class":"who"})
        price = i.find("div", {"class":"prd-price"}).string
        count +=1

        if not author:
            author = "Anonim"
        else:
            author = author.string

        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

def altin():
    list = altin_soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
    count = 0
    titleScript(altin_soup)

    for i in list:
        name = i.find("a", {"class":"prd-name"}).string
        author = i.find("a", {"class":"who"})
        price = i.find("div", {"class":"prd-price"}).string
        count +=1

        if not author:
            author = "Anonim"
        else:
            author = author.string

        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

def kodlab():
    list = kodlab_soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"})
    count = 0
    titleScript(kodlab_soup)

    for i in list:
        name = i.find("a", {"class":"prd-name"}).string
        author = i.find("a", {"class":"who"})
        price = i.find("div", {"class":"prd-price"}).string
        count +=1

        if not author:
            author = "Anonim"
        else:
            author = author.string

        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

def menu():
    while True:
        print("-"*30)
        choice = input("1- Ithaki Yayinlari\n2- Is Bankasi Yayinlari\n3- Yapı Kredi Yayinlari\n4- Can Yayinlari\n5- Dogan Kitap\n6- Kronik Kitap\n7- Sel Yayincilik\n8- Altin Kitap\n9- Kodlab\n0- Exit\nYour Choice?: ")
        print("-"*30)
        if choice == "0":
            break
        else:
            if choice=="1":
                ithaki()
            elif choice=="2":
                isbankasi()
            elif choice=="3":
                yky()
            elif choice=="4":
                can()
            elif choice=="5":
                dogan()
            elif choice=="6":
                kronik()
            elif choice=="7":
                sel()
            elif choice=="8":
                altin()
            elif choice=="9":
                kodlab()

def titleScript(param):
    title = param.find("h1",{"class":"cat-name"}).string
    print("-"*120)
    print("|" + title.rjust(60) + "|".rjust(59," "))
    print("-"*120)

menu()

