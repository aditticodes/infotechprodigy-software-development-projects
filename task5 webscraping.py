import csv
import requests
from bs4 import BeautifulSoup

# Define the URL for the search results page
url = 'https://www.wish.com/search/beautiful%20dresses?sort=popular&ic_id=706_2&pid=searchbox&force_version=1619685322'


response = requests.get(url)

if response.status_code == 200:
  
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', class_='_1eF0d')

 
    product_list = []

 
    for product in products:
        try:
            name = product.find('div', class_='_18U26').text.strip()
        except AttributeError:
            name = ''

        try:
            price = product.find('div', class_='_18U27').text.strip()
        except AttributeError:
            price = ''

        try:
            rating = product.find('div', class_='_18U28').text.strip()
        except AttributeError:
            rating = ''

        product_list.append([name, price, rating])

    with open('products.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Price', 'Rating'])
        writer.writerows(product_list)

    print('Product information has been saved to products.csv')

else:
    print('Failed to fetch product information')