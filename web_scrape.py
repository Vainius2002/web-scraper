import requests
from bs4 import BeautifulSoup
import re


while True:
    choice = input("\nChoose to scrape (computers or phones): ")

    url = ''
    first_url = ''
    second_url = ''
    third_url = ''

    if choice == "computers":
        url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
        categ_choice = input("Choose (laptops or tablets): ")

        if categ_choice == "laptops":
            second_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
        elif categ_choice == "tablets":
            first_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

    elif choice == "phones":
        third_url = "https://webscraper.io/test-sites/e-commerce/allinone/phones"
    
    else:
        print("Input must match as described.")


    info_list = []


    if second_url:
        conn = requests.get(second_url)
        convert = BeautifulSoup(conn.text, "html.parser")
        
        title = convert.find("h1", class_="page-header")
        main_info = convert.find_all("div", class_="caption")
        
        info_list.clear()
        info_list.append(title.text)

        for z in main_info:
            description = z.find("p", class_="description card-text")
            price = z.find("h4", class_="price float-end card-title pull-right")

            fixed_price = re.sub(r'\n', '', price.text)
            final_price = f'price: {fixed_price}'

            info_list.append((description.text, final_price))
        
        for x in info_list:
            print("-" * 185)
            print(x)


    elif first_url:
        conn2 = requests.get(first_url)
        convert2 = BeautifulSoup(conn2.text, "html.parser")
        
        title = convert2.find("h1", class_="page-header")
        main_info = convert2.find_all("div", class_="caption")
        
        info_list.clear()
        info_list.append(title.text)

        for z in main_info:
            description = z.find("a", class_="title")
            price = z.find("h4", class_="price float-end card-title pull-right")

            fixed_price = re.sub(r'\n', '', price.text)
            final_price = f'price: {fixed_price}'
            
            fixed_descr = description.text.replace("\n", "").replace("\t", "").strip()

            info_list.append((fixed_descr, final_price))
        
        for x in info_list:
            print("-" * 185)
            print(x)
    

    elif third_url:
        conn3 = requests.get(third_url)
        convert3 = BeautifulSoup(conn3.text, "html.parser")
        
        title = convert3.find("h2", class_="page-header")
        main_info = convert3.find_all("div", class_="caption")
        
        info_list.clear()
        info_list.append(title.text)

        for z in main_info:
            description = z.find("a", class_="title")
            price = z.find("h4", class_="price float-end card-title pull-right")

            fixed_price = re.sub(r'\n', '', price.text)
            final_price = f'price: {fixed_price}'
            
            fixed_descr = description.text.replace("\n", "").replace("\t", "").strip()

            info_list.append((fixed_descr, final_price))
        
        for x in info_list:
            print("-" * 185)
            print(x)
    