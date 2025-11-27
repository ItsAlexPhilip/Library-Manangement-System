from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret"

books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "status": "Available",
     "summary": "A story about racial injustice in the Deep South.", "cover": "images/to_kill_a_mockingbird.jpg"},
    {"id": 2, "title": "1984", "author": "George Orwell", "status": "Available",
     "summary": "A dystopian novel about totalitarian government surveillance.", "cover": "images/1984.jpg"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "status": "Available",
     "summary": "A critique of the American Dream in 1920s society.", "cover": "images/the_great_gatsby.jpg"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "status": "Available",
     "summary": "A romantic story exploring manners and social standing.", "cover": "images/pride_and_prejudice.jpg"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "status": "Available",
     "summary": "A young boy's journey through adolescent alienation.", "cover": "images/the_catcher_in_the_rye.jpg"},
    {"id": 6, "title": "Moby Dick", "author": "Herman Melville", "status": "Available",
     "summary": "The obsessive quest of Captain Ahab for revenge on a whale.", "cover": "images/moby_dick.jpg"},
    {"id": 7, "title": "War and Peace", "author": "Leo Tolstoy", "status": "Available",
     "summary": "An epic tale of Russian society during Napoleonic Wars.", "cover": "images/war_and_peace.jpg"},
    {"id": 8, "title": "The Hobbit", "author": "J.R.R. Tolkien", "status": "Available",
     "summary": "Bilbo Baggins’ adventure to reclaim treasure guarded by a dragon.", "cover": "images/the_hobbit.jpg"},
    {"id": 9, "title": "Fahrenheit 451", "author": "Ray Bradbury", "status": "Available",
     "summary": "A future where books are banned and burned by the government.", "cover": "images/fahrenheit_451.jpg"},
    {"id": 10, "title": "Jane Eyre", "author": "Charlotte Brontë", "status": "Available",
     "summary": "The life of an orphaned girl overcoming adversity and finding love.", "cover": "images/jane_eyre.jpg"},
    {"id": 11, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "status": "Available",
     "summary": "Epic fantasy quest to destroy a powerful ring.", "cover": "images/the_lord_of_the_rings.jpg"},
    {"id": 12, "title": "Animal Farm", "author": "George Orwell", "status": "Available",
     "summary": "An allegory of political corruption and revolution.", "cover": "images/animal_farm.jpg"},
    {"id": 13, "title": "The Odyssey", "author": "Homer", "status": "Available",
     "summary": "Epic journey of Odysseus returning home after the Trojan War.", "cover": "images/the_odyssey.jpg"},
    {"id": 14, "title": "Hamlet", "author": "William Shakespeare", "status": "Available",
     "summary": "The tragic tale of the Prince of Denmark.", "cover": "images/hamlet.jpg"},
    {"id": 15, "title": "Brave New World", "author": "Aldous Huxley", "status": "Available",
     "summary": "A dystopian society driven by technology and conditioning.", "cover": "images/brave_new_world.jpg"},
    {"id": 16, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "status": "Available",
     "summary": "A man wrestles with guilt after committing a crime.", "cover": "images/crime_and_punishment.jpg"},
    {"id": 17, "title": "The Kite Runner", "author": "Khaled Hosseini", "status": "Available",
     "summary": "A story of friendship, betrayal, and redemption in Afghanistan.", "cover": "images/the_kite_runner.jpg"},
    {"id": 18, "title": "The Alchemist", "author": "Paulo Coelho", "status": "Available",
     "summary": "A shepherd's journey to fulfill his personal legend.", "cover": "images/the_alchemist.jpg"},
    {"id": 19, "title": "The Da Vinci Code", "author": "Dan Brown", "status": "Available",
     "summary": "A symbologist uncovers secrets hidden in famous works of art.", "cover": "images/the_da_vinci_code.jpg"},
    {"id": 20, "title": "Harry Potter and the Sorcerer’s Stone", "author": "J.K. Rowling", "status": "Available",
     "summary": "The first year of Harry Potter at Hogwarts School.", "cover": "images/harry_potter_1.jpg"}
]


@app.route("/")
def index():
    return render_template("index.html", books=books)

@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    if not title or not author:
        flash("Please fill all fields", "error")
    else:
        new_id = max([b["id"] for b in books]) + 1 if books else 1
        books.append({"id": new_id, "title": title, "author": author, "status": "Available",
                      "summary": "No summary.", "cover": "images/placeholder.jpg"})
        flash(f"Book '{title}' added!", "success")
    return redirect(url_for("index"))

@app.route("/borrow_book/<int:book_id>", methods=["POST"])
def borrow_book(book_id):
    for book in books:
        if book["id"] == book_id and book["status"] == "Available":
            book["status"] = "Borrowed"
            flash(f"Book '{book['title']}' borrowed!", "success")
            break
    return redirect(url_for("index"))

@app.route("/return_book/<int:book_id>", methods=["POST"])
def return_book(book_id):
    for book in books:
        if book["id"] == book_id and book["status"] == "Borrowed":
            book["status"] = "Available"
            flash(f"Book '{book['title']}' returned!", "success")
            break
    return redirect(url_for("index"))

@app.route("/check_book", methods=["POST"])
def check_book():
    title = request.form.get("check_title")
    book = next((b for b in books if b["title"].lower() == title.lower()), None)
    if book:
        flash(f"'{book['title']}' is {book['status']}", "info")
    else:
        flash(f"Book '{title}' not found", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
