from flask import Flask

app = Flask(__name__)

@app.route('/book/<author>/<title>')
def show_book(author, title):
    book = Book.query.filter_by(author=author, title=title).first_or_404()
    return render_template('show_book.html', book=book)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')