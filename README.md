# BookStore

It is a public web portal implemented using Python/Django(MVT structure).

It contains the list of book and also have information about its copies and book info link provided by Google Book Api. Anybody can access it, there is no need to login or authenticate(for now).
  


## Features

1. User can add a book or also copy of a existing book to the bookstore.

2. User can also remove or delete the book from the bookstore.

3. User can also get the information about the book on clicking on its title.

4. There is also a search box which shows the books with the help of Google Book Api for the given query.

5. Searched books have indication on their bottom, weather it is already exist in bookstore or not.

6. For existing books, user can add or remove a copy from bookstore and for non-existing books, user can add this book to the bookstore. 

7. User also able to see the copies of a book and ID of book provided by Google Book Api.

8. If a book already existed in inventory but now its copies becomes 0 then it will show "Out of Stock".

### Assumption

In start bookstore have no book. User can add books to the bookstore via search box.

Using Python3.

### Installation

Create a virtual environment.

Clone the repo:

    git clone https://github.com/sandeepsajan0/inventorybooksapp.git

Install all requirements:

      pip3 install -r requirements.txt

You have to configure database for run server locally:

Now you need to migrate the database:

    python3 manage.py makemigrations

    python3 manage.py migrate

Now you can run the sever:

    python3 manage.py runserver

hurray! you app is running on: http://127.0.0.1:8000/

### Contributing Guides

It has a simple structure.

For configuration issues or information, you should go through `settings.py`.

For feature implementation or function issue, go through `views.py`.

For template issues, go through `booklist.html` and `main.css`.

For database or model information, go through `models.py`.


