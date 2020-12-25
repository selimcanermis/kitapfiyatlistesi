import requests
from bs4 import BeautifulSoup

ithaki_url = "https://www.dr.com.tr/Yayinevi/ithaki-yayinlari/s=5119"
isbankasi_url = "https://www.dr.com.tr/Yayinevi/is-bankasi-kultur-yayinlari/s=5109"
yky_url = "https://www.dr.com.tr/Yayinevi/yapi-kredi-yayinlari/s=10615"
can_url = "https://www.dr.com.tr/Yayinevi/can-yayinlari/s=1883"

ithaki_html = requests.get(ithaki_url).content
isbankasi_html = requests.get(isbankasi_url).content
yky_html = requests.get(yky_url).content
can_html = requests.get(can_url).content

ithaki_soup = BeautifulSoup(ithaki_html, "html.parser")
isbankasi_soup = BeautifulSoup(isbankasi_html, "html.parser")
yky_soup = BeautifulSoup(yky_html, "html.parser")
can_soup = BeautifulSoup(can_html, "html.parser")

def ithaki():
    list = ithaki_soup.find("div",{"id":"container"}).find_all("div",{"class":"content"})
    count = 0
    for i in list:
        name = i.find("h3").string
        author = i.find("a", {"who"}).string
        price = i.find("span", {"price"}).string
        count +=1
        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.ljust(10))

def isbankasi():
    list = isbankasi_soup.find("div",{"id":"container"}).find_all("div",{"class":"content"})
    count = 0
    for i in list:
        name = i.find("h3").string
        author = i.find("a", {"who"}).string
        price = i.find("span", {"price"}).string
        count +=1
        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.ljust(10))

def yky():
    list = yky_soup.find("div",{"id":"container"}).find_all("div",{"class":"content"})
    count = 0
    for i in list:
        name = i.find("h3").string
        author = i.find("a", {"who"}).string
        price = i.find("span", {"price"}).string
        count +=1
        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.ljust(10))

def can():
    list = can_soup.find("div",{"id":"container"}).find_all("div",{"class":"content"})
    count = 0
    for i in list:
        name = i.find("h3").string
        author = i.find("a", {"who"}).string
        price = i.find("span", {"price"}).string
        count +=1
        print(str(count).rjust(2), name.ljust(70,"."), author.ljust(30), price.ljust(10))

def menu():
    while True:
        choice = input("1- Ithaki Yayinlari\n2- Is Bankasi Yayinlari\n3- Yapı Kredi Yayınları\n4- Can Yayıbları\n5- Exit\nYour Choice?: ")
        if choice == "5":
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

menu()

