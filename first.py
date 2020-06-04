from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq 

page_url = "http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH"

uClient = uReq(page_url)

page_soup = soup(uClient.read(), "html.parser")
uClient.close()

containers = page_soup.findAll("div", {"class": "item-container"})

out_filename = "graphics_card.csv"

headers = "brand,product_name,shipping \n"

f = open(out_filename, "w")
f.write(headers)


for container in containers:
    make_rating_sp = container.div.select("a")


    brand = make_rating_sp[0].img["title"].title()

    
    product_name = container.div.select("a")[2].text


    shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    print("brand: " + brand + "\n")
    print("product_name: " + product_name + "\n")
    print("shipping: " + shipping + "\n")

 
    f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")

f.close()  
