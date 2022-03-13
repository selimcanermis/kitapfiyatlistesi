import requests
from bs4 import BeautifulSoup

tl = "TL"

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
iletisim_dr_url = "https://www.dr.com.tr/yayinevi/kodlab/s=5693"

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
iletisim_idefix_url = "https://www.idefix.com/yayinevi/kodlab/s=5693"

##### BKMKITAP URLS #####
ithaki_bkm_url = "https://www.bkmkitap.com/ithaki-yayinlari"
isbankasi_bkm_url = "https://www.bkmkitap.com/is-bankasi-kultur-yayinlari"
yky_bkm_url = "https://www.bkmkitap.com/yapi-kredi-yayinlari"
can_bkm_url = "https://www.bkmkitap.com/can-yayinlari"
dogan_bkm_url = "https://www.bkmkitap.com/dogan-kitap"
kronik_bkm_url = "https://www.bkmkitap.com/kronik-kitap"
sel_bkm_url = "https://www.bkmkitap.com/sel-yayincilik"
altin_bkm_url = "https://www.bkmkitap.com/altin-kitaplar"
ayrinti_bkm_url = "https://www.bkmkitap.com/ayrinti-yayinlari"
iletisim_bkm_url = "https://www.bkmkitap.com/iletisim-yayinevi"

##### AMAZON URLS #####
ithaki_amazon_url = "https://www.amazon.com.tr/s?k=ithaki+yay%C4%B1nlar%C4%B1&crid=2YCQIGL9BZ9G9&sprefix=ithaki%2Caps%2C1000&ref=nb_sb_ss_ts-doa-p_1_6"
isbankasi_amazon_url = "https://www.amazon.com.tr/s?k=i%C5%9F+bankas%C4%B1+k%C3%BClt%C3%BCr+yay%C4%B1nlar%C4%B1&crid=22YVSOHU7K7L0&sprefix=i%C5%9F+bank%2Caps%2C286&ref=nb_sb_ss_ts-doa-p_1_7"
yky_amazon_url = "https://www.amazon.com.tr/s?k=yap%C4%B1kredi+yay%C4%B1nlar%C4%B1&crid=13DVRCOWUUX2Q&sprefix=yap%C4%B1kre%2Caps%2C300&ref=nb_sb_ss_ts-doa-p_1_7"
can_amazon_url = "https://www.amazon.com.tr/s?k=can+yay%C4%B1nlar%C4%B1&pd_rd_r=ab672a0b-6888-4830-b067-6f3c80239127&pd_rd_w=7QShS&pd_rd_wg=wBzWr&pf_rd_p=0e939789-7c0b-4bf9-983d-efb3107eb66a&pf_rd_r=H6RW9D1ABY9QR6PK4MG4&qid=1647182680&ref=sugsr_0_5"
dogan_amazon_url = "https://www.amazon.com.tr/s?k=do%C4%9Fan+kitap+yay%C4%B1nlar%C4%B1&crid=50UN54GCX5CQ&sprefix=do%C4%9Fan+kitap%2Caps%2C345&ref=nb_sb_ss_ts-doa-p_2_11"
kronik_amazon_url = "https://www.amazon.com.tr/s?k=kronik+kitap&crid=1GS4PBUQRIUKU&sprefix=kronik%2Caps%2C968&ref=nb_sb_ss_ts-doa-p_1_6"
sel_amazon_url = "https://www.amazon.com.tr/s?k=sel+yay%C4%B1nc%C4%B1l%C4%B1k&sprefix=sel+yay%C4%B1n%2Caps%2C700&ref=nb_sb_ss_ts-doa-p_1_9"
altin_amazon_url = "https://www.amazon.com.tr/s?k=alt%C4%B1n+kitap&crid=3PYAW0FG5PN8S&sprefix=alt%C4%B1n+kita%2Caps%2C320&ref=nb_sb_ss_ts-doa-p_2_10"
ayrinti_amazon_url = "https://www.amazon.com.tr/s?k=ayr%C4%B1nt%C4%B1+yay%C4%B1nlar%C4%B1&pd_rd_r=ed0938d5-0e84-4aad-88e4-0e996628d84e&pd_rd_w=uaACk&pd_rd_wg=6fnND&pf_rd_p=0e939789-7c0b-4bf9-983d-efb3107eb66a&pf_rd_r=5YZJ42HR5NSQV80K32FC&qid=1647182478&ref=sugsr_1_6"
iletisim_amazon_url = "https://www.amazon.com.tr/s?k=ileti%C5%9Fim+yay%C4%B1nlar%C4%B1&pd_rd_r=ed0938d5-0e84-4aad-88e4-0e996628d84e&pd_rd_w=uaACk&pd_rd_wg=6fnND&pf_rd_p=0e939789-7c0b-4bf9-983d-efb3107eb66a&pf_rd_r=5YZJ42HR5NSQV80K32FC&qid=1647182478&ref=sugsr_2_5"



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
    elif store == "amazon":
        title = param.find("a",{"class":"col col-12 text-title mt"}).string.upper()
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
    if not title:
        title = "No Title"
    else:
        title = title.string
    return title


def getSoup(url, store):
    html_request = requests.get(url)
    soup = BeautifulSoup(html_request.content, "html.parser")
    getList(soup, store)

# TODO getList fonksiyonu sadece D&R çin ayarlı onu düzelt
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

    elif store == "amazon":
        #list_kyurdu = soup.find("div",{"class":"grid_9"}).find_all("div",{"class":"product-cr"})
        list_amazon = soup.find_all("div",{"class":"col col-12 drop-down hover lightBg"}) #!Short way
        count = 0
        titleScript(soup, store)

        for l in list_amazon:
            name = l.find("a", {"class":"fl col-12 text-description detailLink"}).string.strip()
            author = l.find("a", {"class":"fl col-12 text-title"}).string
            price = l.find("div", {"class":"col col-12 currentPrice"}).string.strip()
            count +=1
            #print(len(price))
            author = authorCheck(author)

            print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price[:-4].ljust(5), tl) 


def ithaki(store):
    if store == "dr":
        getSoup(ithaki_dr_url, store)
    elif store == "idefix":
        getSoup(ithaki_idefix_url, store)
    elif store == "bkm":
        getSoup(ithaki_bkm_url, store)
    elif store == "amazon":
        getSoup(ithaki_amazon_url, store)

def isbankasi(store):
    if store == "dr":
        getSoup(isbankasi_dr_url, store)
    elif store == "idefix":
        getSoup(isbankasi_idefix_url, store)
    elif store == "bkm":
        getSoup(isbankasi_bkm_url, store)
    elif store == "amazon":
        getSoup(isbankasi_amazon_url, store)

def yky(store):
    if store == "dr":
        getSoup(yky_dr_url, store)
    elif store == "idefix":
        getSoup(yky_idefix_url, store)
    elif store == "bkm":
        getSoup(yky_bkm_url, store)
    elif store == "amazon":
        getSoup(yky_amazon_url, store)

def can(store):
    if store == "dr":
        getSoup(can_dr_url, store)
    elif store == "idefix":
        getSoup(can_idefix_url, store)
    elif store == "bkm":
        getSoup(can_bkm_url, store)
    elif store == "amazon":
        getSoup(can_amazon_url, store)

def dogan(store):
    if store == "dr":
        getSoup(dogan_dr_url, store)
    elif store == "idefix":
        getSoup(dogan_idefix_url, store)
    elif store == "bkm":
        getSoup(dogan_bkm_url, store)
    elif store == "amazon":
        getSoup(dogan_amazon_url, store)

def kronik(store):
    if store == "dr":
        getSoup(kronik_dr_url, store)
    elif store == "idefix":
        getSoup(kronik_idefix_url, store)
    elif store == "bkm":
        getSoup(kronik_bkm_url, store)
    elif store == "amazon":
        getSoup(kronik_amazon_url, store)

def sel(store):
    if store == "dr":
        getSoup(sel_dr_url, store)
    elif store == "idefix":
        getSoup(sel_idefix_url, store)
    elif store == "bkm":
        getSoup(sel_bkm_url, store)
    elif store == "amazon":
        getSoup(sel_amazon_url, store)

def altin(store):
    if store == "dr":
        getSoup(altin_dr_url, store)
    elif store == "idefix":
        getSoup(altin_idefix_url, store)
    elif store == "bkm":
        getSoup(altin_bkm_url, store)
    elif store == "amazon":
        getSoup(altin_amazon_url, store)

def ayrinti(store):
    if store == "dr":
        getSoup(ayrinti_dr_url, store)
    elif store == "idefix":
        getSoup(ayrinti_idefix_url, store)
    elif store == "bkm":
        getSoup(ayrinti_bkm_url, store)
    elif store == "amazon":
        getSoup(ayrinti_amazon_url, store)

def iletisim(store):
    if store == "dr":
        getSoup(iletisim_dr_url, store)
    elif store == "idefix":
        getSoup(iletisim_idefix_url, store)
    elif store == "bkm":
        getSoup(iletisim_bkm_url, store)
    elif store == "amazon":
        getSoup(iletisim_amazon_url, store)

#! Burada klavyeden farklı bir şey girerse sorgusu yok!!!
def menu():
    while True:
        print("-"*30)
        store_choice = input("1- D&R\n2- Idefix \n3- BKM Kitap \n0- Exit\nYour Choice?: ")
        print("-"*30)
        if store_choice == "0":
            break
        else:
            if store_choice == "1":
                store = "dr"
            elif store_choice == "2":
                store = "idefix"
            elif store_choice == "3":
                store = "bkm"

        print("-"*30)
        choice = input("1- Ithaki Yayinlari\n2- Is Bankasi Yayinlari\n3- Yapı Kredi Yayinlari\n4- Can Yayinlari\n5- Dogan Kitap\n6- Kronik Kitap\n7- Sel Yayincilik\n8- Altin Kitap\n9- Ayrinti Yayinlari\n10- İletisim Yayinlari\n0- Back\nYour Choice?: ")
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
                iletisim(store)


menu()

