from bs4 import BeautifulSoup
import mechanicalsoup
import urllib.request


def amazon(product,number_of_results=1):

    URL = f"https://www.amazon.in/s?k={product}"

    req = urllib.request.Request(URL)

    webpage = urllib.request.urlopen(req)

    soup = BeautifulSoup(webpage, "html.parser")

    product_name = soup.find_all("span",{"class":"a-size-base-plus a-color-base a-text-normal"},limit=number_of_results)
    product_price = soup.find_all("span",{"class":"a-price-whole"},limit=number_of_results)
    product_rating = soup.find_all("span",{"class":"a-icon-alt"},limit=number_of_results)
    image_link = soup.find_all("img", {"class":"s-image"}, limit=number_of_results)

    for i in range(number_of_results):
        product_name[i]=product_name[i].text
        product_price[i]=product_price[i].text
        product_rating[i]=product_rating[i].text
        image_link[i] = image_link[i].get("src")



    print(product_name,product_price,product_rating,image_link)


def snapdeal(product,number_of_results=1):

    URL = f"https://www.snapdeal.com/search?keyword={product}"

    req = urllib.request.Request(URL)

    webpage = urllib.request.urlopen(req)

    soup = BeautifulSoup(webpage, "html.parser")
     
    product_name = soup.find_all("p",{"class":"product-title"},limit=number_of_results)
    product_price = soup.find_all("span",{"class":"lfloat product-price"},limit=number_of_results)
    product_rating = soup.find_all("div",{"class":"clearfix rating av-rating"},limit=number_of_results)
    image_link = soup.find_all("img", {"class":"product-image"}, limit=number_of_results)

    for i in range(number_of_results):
        product_name[i]=product_name[i].get("title")
        product_price[i]=product_price[i].get("display-price")
        product_rating[i] = float(str(product_rating[i]).split("width:")[-1].split("%")[0])/20
        image_link[i] = image_link[i].get("src")

    print(product_name,product_price,product_rating,image_link)





def flinks(product,no_of_products):
    browser = mechanicalsoup.StatefulBrowser()
    url= f"https://www.flipkart.com/search?q={product}"

    browser.open(url)


    href= browser.page.find_all("a")
    links=[]

    for link in href:
        if(len(links)==no_of_products):
                    break
        
        if(link.get("href")!=None):
            if(link.get("target")!=None):
                links.append(flipkart(link.get("href")))
    print(links)

    


def flipkart(url):

    URL = "https://www.flipkart.com" + url

    req = urllib.request.Request(URL)

    webpage = urllib.request.urlopen(req)

    soup = BeautifulSoup(webpage, "html.parser")
     
    product_name = soup.find("span",{"class":"B_NuCI"}).text
    product_price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).text
    product_rating = soup.find("div",{"class":"_3LWZlK"}).text

    return (product_name,product_price,product_rating)


