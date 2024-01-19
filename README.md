# Virtual-Library
An online library with lots and books and blogs and  a recommender system to suggest you good books

# Overview

This is a Django-based virtual library website that allows users to upload and download ebooks and blogs. Users can create accounts, log in, add blogs, add books, view all posts, view individual posts, download ebooks, and search for books. The website also features a contact form for users to reach out.

## Features:

1. **User Authentication:**
   - Users can create accounts, log in, and log out.
   - New users are automatically logged in upon registration.

2. **Homepage:**
   - Displays a feed of all blog posts and recently uploaded books.
   - Users can click on individual posts to view details.

3. **Add Blog:**
   - Logged-in users can create and upload new blog posts.
   - Includes fields for name, title, subtitle, content, and optional image.

4. **Add Book:**
   - Logged-in users can add new books to the library.
   - Fields include name, title, category, author, about, book cover image, and the actual book file.

5. **View All Posts:**
   - Displays all blog posts for users to browse.

6. **View Post:**
   - Allows users to view an individual blog post along with comments.
   - Logged-in users can leave comments on blog posts.

7. **View Book:**
   - Displays details about a specific book.
   - Logged-in users can leave reviews for the book.

8. **Download Book:**
   - Users can download ebooks from the library.

9. **All Books:**
   - Shows a page with all books sorted by upload date.

10. **Logout:**
    - Allows users to log out of their accounts.

11. **Contact Form:**
    - Users can fill out a contact form, which sends a message including the user's name, email, and message to a predefined Twilio number.

12. **Search:**
    - Users can search for books based on title, author, name, category, or about.

## Requirements:

- Django
- Twilio
- Python

## Installation:

1. Clone the repository:
   git clone https://github.com/your-username/virtual-library.git
   cd virtual-library

2. Install dependencies:
   pip install -r requirements.txt
   
3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
   
4. Create a superuser account:
   python manage.py createsuperuser

5. Run the development server:
   python manage.py runserver

6. Visit `http://localhost:8000/` in your web browser.

## Usage:

1. Create a superuser account using the `createsuperuser` command.
2. Log in with the superuser account to access admin features.
3. Use the website to add blogs, add books, download ebooks, and interact with other features.
