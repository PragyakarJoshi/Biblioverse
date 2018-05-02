import requests, re
from bs4 import BeautifulSoup

def GetBookUrl(name):
    name.replace(' ','+')
    url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&q=' + name + '&search_type=books'
    search_page = requests.get(url)
    soup = BeautifulSoup(search_page.content, 'lxml')
    try:
        best_match = soup.find('table', {'class': 'tableList'}).find('a', href=True)['href']
        book_page_url = 'https://www.goodreads.com' + best_match
        return book_page_url
    except:
        return "Book not Found"

def GetBookSoup(name):
    url = GetBookUrl(name)
    book_page = requests.get(url)
    book_soup = BeautifulSoup(book_page.content, 'lxml')
    try:
        return book_soup
    except:
        return "No Content Found"

def GetBookName(name):
    url = GetBookUrl(name)
    soup = GetBookSoup(url)
    book_names = soup.find_all('h1', class_="bookTitle")
    for book_name in book_names:
        title = book_name.string.strip()
    return title

def GetBookAuthor(name):
    url = GetBookUrl(name)
    soup = GetBookSoup(url)
    author_names = soup.find_all('a', class_="authorName")
    for author_name in author_names:
        author = author_name.string.strip()
    return author

def GetBookReviews(name):
    url = GetBookUrl(name)
    soup = GetBookSoup(url)
    review_list = []
    book_reviews = soup.find_all('div', class_="reviewText stacked")
    for review in book_reviews:
        review_list.append(review.text)
    return review_list
