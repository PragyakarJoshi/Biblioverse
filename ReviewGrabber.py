import requests, re
from bs4 import BeautifulSoup

def GetBookDetails(name):
    
    name.replace(' ','+')
    url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&q=' + name + '&search_type=books'
    search_page = requests.get(url)
    soup = BeautifulSoup(search_page.content, 'lxml')
    best_match = soup.find('table', {'class': 'tableList'}).find('a', href=True)['href']
    book_page_url = 'https://www.goodreads.com' + best_match
    url = book_page_url
    book_page = requests.get(book_page_url)
    soup = BeautifulSoup(book_page.content, 'lxml')
    book_names = soup.find('h1', class_="bookTitle")
    for book_name in book_names:
        title = book_name.string.strip()
    author_names = soup.find('a', class_="authorName")
    for author_name in author_names:
        author = author_name.string.strip()
    return title, author, book_page_url

def GetBookReviews(name):
    book_name, book_author, url = GetBookDetails(name)
    print("Extracting Reviews...")
    book_page = requests.get(url)
    soup = BeautifulSoup(book_page.content, 'lxml')
    review_list = []
    book_reviews = soup.find_all('div', class_="reviewText stacked")
    for review in book_reviews:
        review_list.append(review.text)
    return review_list
