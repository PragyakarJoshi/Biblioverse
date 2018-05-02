from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/result', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        book_name = request.form['book_name']
        return render_template('output.html', book_name = book_name)
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
