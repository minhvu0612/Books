import requests
from bs4 import BeautifulSoup
import pandas as pd

# get resource
def get_resource(url):
    response = requests.get(url) #json: html
    soups = BeautifulSoup(response.content, "html.parser") # html src
    return soups

# remove html tag
def remove_html(string):
    while(1):
        string = string.replace("  ", " ").replace("\n", "")
        if (string.find("  ") == -1): # This is 2-space
            break
    return string.strip()

# save data
def save_data(soups):
    # Total 12 feature
    dict_data = { # convert sang csv
        'Tieu de': [],
        'Tác giả': [],
        'Người dịch': [],
        'Nhà xuất bản': [],
        'Nhà phát hành': [],
        'Mã Sản phẩm': [],
        'Giấy phép XB': [],
        'Khối lượng': [],
        'Ngôn ngữ': [],
        'Định dạng': [],
        'Kích thước': [],
        'Ngày phát hành': [],
        'Số trang': []
    }
    i = 0
    for book in soups.findAll('a', {'class': 'image-border'}):
        # if i > 0:
        #     break
        # i = i + 1

        url = book.attrs['href']
        print("Retrieve data from " + url)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, "html.parser")
        print("Successfully ============> 100%\n")

        book_props = dict()
        book_props['Tieu de'] = book.attrs['title']

        for item in soup.select(".product-feature > ul > li"):
            string = remove_html(item.get_text()).split("\n")[0]
            book_props[string[0 : string.find(":")]] = string[string.find(":") + 2 :]

        for key in dict_data:
            if key in book_props:
                dict_data[key].append(book_props[key])
            else:
                dict_data[key].append("NaN")

    return dict_data

# exact data to csv
def data_to_csv(store, page):
    df = pd.DataFrame(store["data"])
    df.to_csv("../data/khoa_hoc_co_ban.csv", mode='a', header=(page == '1'))