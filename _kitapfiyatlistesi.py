import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("C:\\Users\\selim-can\\kitapfiyatlistesi")
import urls
import info

tl = "TL"
start = False


def titleScript(param, store):
    if store == "dr":
        title = param.find("h1",{"class":"cat-name"}).string.upper()
        print("-"*120)
        print("|" + title.rjust(60) + "|".rjust(59," "))
        print("-"*120)

    elif store == "idefix":
        title = param.find("h1").string.upper()
        print("-"*120)
        print("|" + title.rjust(60) + "|".rjust(59," "))
        print("-"*120)

    elif store == "bkm":
        title = param.find("a",{"class":"col col-12 text-title mt"}).string.upper()
        print("-"*120)
        print("|" + title.rjust(60) + "|".rjust(59," "))
        print("-"*120)  
    elif store == "kidega":
        title = param.find("div",{"class":"col-md-9 col-xs-9 ttl"}).find("h1").string.upper()
        title = titleCheck(title)
        print(title)
        print("-"*120)
        print("|" + title.rjust(60) + "|".rjust(59," "))
        print("-"*120)
    elif store == "ilknokta":
        print("title ilknoktadayım")
        title = param.find("div", {"class":"publisher"}).string.upper()
        print("title yazılacak")
        print(title)
        title = titleCheck(title)
        print(title)
        print("-"*120)
        print("|" + title.rjust(60) + "|".rjust(59," "))
        print("-"*120)

def authorCheck(author):
    if not author:
        author = "Anonim"
    else:
        author = author.string
    return author

def titleCheck(title):
    print("buraya da girdim")
    if not title:
        title = "No Title"
    else:
        title = title
    return title


def getSoup(url, store):
    html_request = requests.get(url)
    soup = BeautifulSoup(html_request.content, "html.parser")
    getList(soup, store)

def getList(soup, store):
    if store == "dr":
        #list_dr = soup.find("div",{"id":"container"}).find_all("div",{"class":"prd-content"}) #!Long way
        list_dr = soup.find_all("div",{"class":"prd-content"}) #!Short way
        count = 0
        titleScript(soup, store)

        for i in list_dr:
            name = i.find("a", {"class":"prd-name"}).string
            author = i.find("a", {"class":"who"})
            price = i.find("div", {"class":"prd-price"}).string
            count +=1

            author = authorCheck(author)

            print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))

    elif store == "idefix":
        #list_idefix = soup.find("div",{"id":"container"}).find_all("div",{"class":"product-info"}) #!Long way
        list_idefix = soup.find_all("div",{"class":"product-info"}) #!Short way
        count = 0
        titleScript(soup, store)

        for j in list_idefix:
            name = j.find("div", {"class":"box-title"}).find("a").string
            author = j.find("a", {"class":"who"})
            price = j.find("span", {"id":"prices"}).string
            count +=1

            author = authorCheck(author)

            print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.strip().ljust(5))
    
    elif store == "bkm":
        #list_kyurdu = soup.find("div",{"class":"grid_9"}).find_all("div",{"class":"product-cr"})
        list_bkm = soup.find_all("div",{"class":"col col-12 drop-down hover lightBg"}) #!Short way
        count = 0
        titleScript(soup, store)

        for k in list_bkm:
            name = k.find("a", {"class":"fl col-12 text-description detailLink"}).string.strip()
            author = k.find("a", {"class":"fl col-12 text-title"}).string
            price = k.find("div", {"class":"col col-12 currentPrice"}).string.strip()
            count +=1
            #print(len(price))
            author = authorCheck(author)

            print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price[:-4].ljust(5), tl) 

    elif store == "kidega":
        #list_kyurdu = soup.find("div",{"class":"grid_9"}).find_all("div",{"class":"product-cr"})
        list_kidega = soup.find_all("div",{"class":"prd-inner itemWrap"}) #!Short way
        count = 0
        titleScript(soup, store)

        for l in list_kidega:
            name = l.find("h3", {"class":"book-name"}).string.strip()
            author = l.find("span", {"class":"manufacturer-name"})
            price = l.find("div", {"class":"urunListe_satisFiyat"}).text.strip()
            count +=1
            #print(len(price))
            author = authorCheck(author)

            print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price[:-1].ljust(5), tl) 

    elif store == "ilknokta":
        #list_kyurdu = soup.find("div",{"class":"grid_9"}).find_all("div",{"class":"product-cr"})
        list_kidega = soup.find_all("div",{"class":"prd_info"}) #!Short way
        count = 0
        titleScript(soup, store)

        for l in list_kidega:
            name = l.find("div", {"class":"name"}).find("a").string.strip()
            author = l.find("div", {"class":"writer"}).find("a")
            price = l.find("span", {"class":"price price_sale convert_cur"}).text.strip()
            count +=1
            #print(len(price))
            author = authorCheck(author)

            print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price[:-1].ljust(5), tl)


def ithaki(store):
    if store == "dr":
        getSoup(urls.ithaki_dr_url, store)
    elif store == "idefix":
        getSoup(urls.ithaki_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.ithaki_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.ithaki_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.ithaki_ilknokta_url, store)

def isbankasi(store):
    if store == "dr":
        getSoup(urls.isbankasi_dr_url, store)
    elif store == "idefix":
        getSoup(urls.isbankasi_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.isbankasi_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.isbankasi_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.isbankasi_ilknokta_url, store)

def yky(store):
    if store == "dr":
        getSoup(urls.yky_dr_url, store)
    elif store == "idefix":
        getSoup(urls.yky_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.yky_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.yky_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.yky_ilknokta_url, store)

def can(store):
    if store == "dr":
        getSoup(urls.can_dr_url, store)
    elif store == "idefix":
        getSoup(urls.can_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.can_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.can_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.can_ilknokta_url, store)

def dogan(store):
    if store == "dr":
        getSoup(urls.dogan_dr_url, store)
    elif store == "idefix":
        getSoup(urls.dogan_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.dogan_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.dogan_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.dogan_ilknokta_url, store)

def kronik(store):
    if store == "dr":
        getSoup(urls.kronik_dr_url, store)
    elif store == "idefix":
        getSoup(urls.kronik_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.kronik_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.kronik_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.kronik_ilknokta_url, store)

def sel(store):
    if store == "dr":
        getSoup(urls.sel_dr_url, store)
    elif store == "idefix":
        getSoup(urls.sel_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.sel_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.sel_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.sel_ilknokta_url, store)

def altin(store):
    if store == "dr":
        getSoup(urls.altin_dr_url, store)
    elif store == "idefix":
        getSoup(urls.altin_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.altin_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.altin_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.altin_ilknokta_url, store)

def ayrinti(store):
    if store == "dr":
        getSoup(urls.ayrinti_dr_url, store)
    elif store == "idefix":
        getSoup(urls.ayrinti_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.ayrinti_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.ayrinti_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.ayrinti_ilknokta_url, store)

def iletisim(store):
    if store == "dr":
        getSoup(urls.iletisim_dr_url, store)
    elif store == "idefix":
        getSoup(urls.iletisim_idefix_url, store)
    elif store == "bkm":
        getSoup(urls.iletisim_bkm_url, store)
    elif store == "kidega":
        getSoup(urls.iletisim_kidega_url, store)
    elif store == "ilknokta":
        getSoup(urls.iletisim_ilknokta_url, store)

#! Burada klavyeden farklı bir şey girerse sorgusu yok!!!
def menu():
    info.infoScript()
    global start
    while True:
        if start == False:
            print("-"*30)
            print("KITAP MAGAZALARI".rjust(25))
            print("-"*30)
            store_choice = input("1- D&R\n2- Idefix \n3- BKM Kitap \n4- Kidega \n5- İlk Nokta \n0- Exit\nYour Choice?: ")
            if store_choice == "0":
                break
            else:
                if store_choice == "1":
                    store = "dr"
                elif store_choice == "2":
                    store = "idefix"
                elif store_choice == "3":
                    store = "bkm"
                elif store_choice == "4":
                    store = "kidega"
                elif store_choice == "5":
                    store = "ilknokta"
                start = True   
        if start == True:
            print("-"*30)
            print("YAYINEVLERİ".rjust(22))
            print("-"*30)
            choice = input("1- Ithaki Yayinlari\n2- Is Bankasi Yayinlari\n3- Yapı Kredi Yayinlari\n4- Can Yayinlari\n5- Dogan Kitap\n6- Kronik Kitap\n7- Sel Yayincilik\n8- Altin Kitap\n9- Ayrinti Yayinlari\n10- İletisim Yayinlari\n0- Back\nYour Choice?: ")
            print("-"*30)
            if choice == "0":
                start = False
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
                    iletisim(store)

menu()

