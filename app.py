from flask import Flask, render_template, request
from SentimentClassifier import RatingGenerator
from ReviewGrabber import GetBookDetails

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html', error = " ")

@app.route('/result', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        book_name = request.form['book_name']
        if book_name == "":
            return render_template('input.html', error = "* Please Enter a Valid Book Name * ")
        else:
            try:
                print("Extracting Book Details...")
                book_name, book_author, book_url = GetBookDetails(book_name)
                print("Book: " + book_name)
                print("Author: "+ book_author)
                print("URL: "+ book_url)
                print("Extracting Reviews...")
                rating, total_reviews, total_positives, total_negatives = RatingGenerator(book_name)
                print("Total Reviews: "+ total_reviews)
                print("Positive Reviews: " + total_positives)
                print("Negative Reviews: " + total_negatives)
                return render_template('output.html', book_author = book_author,  book_url = book_url, book_name = book_name, rating = rating, total_positives = total_positives, total_reviews = total_reviews, total_negatives = total_negatives)
            except:
                return render_template('input.html', error = "* Book Not Found! Please Enter Valid Book Name. * ")
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
