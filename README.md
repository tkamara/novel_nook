# Novel Nook - A Webstack Book Catalog

Welcome to Novel Nook, a web-based book catalog that provides users with the ability to log in or register, manage their book lists, and perform various operations such as adding, deleting, searching, and viewing books. This project is built using a web stack and aims to create a user-friendly environment for book enthusiasts to organize and keep track of their reading collections.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [Adding Books](#adding-books)
  - [Deleting Books](#deleting-books)
  - [Searching Books](#searching-books)
  - [Viewing Book Lists](#viewing-book-lists)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication: Register and log in securely to access personalized book lists.
- Add books: Easily add new books to your catalog with details like title, author, and genre.
- Delete books: Remove unwanted or finished books from your collection.
- Search functionality: Quickly find books using various search criteria.
- View book lists: Browse your book collection in an organized and user-friendly interface.

## Getting Started

### Prerequisites

Make sure you have the following installed before running the project:

- Python
- MongoDB
- Flask

### Installation

1. Clone the repository:

```bash
git clone https://github.com/tkamara/novel-nook.git
```

2. Navigate to the project directory:

```bash
cd novel-nook
```

3. Install dependencies:

```bash
pip install Flask
```

4. Set up your MongoDB database and update the configuration in `config/config.js` accordingly.

Visit [http://localhost:5000](http://localhost:5000) in your browser to access Novel Nook.

## Usage

### User Registration

1. Navigate to the registration page.
2. Fill in the required information.
3. Click the "Register" button.

### User Login

1. Navigate to the login page.
2. Enter your registered email and password.
3. Click the "Login" button.

### Adding Books

1. Log in to your account.
2. Navigate to the "Add Books" section.
3. Fill in the details of the book (title, author, genre, etc.).
4. Click the "Add Book" button.

### Deleting Books

1. Log in to your account.
2. Navigate to your book list.
3. Find the book you want to delete.
4. Click the "Delete" button next to the book.

### Searching Books

1. Log in to your account.
2. Navigate to the "Search" section.
3. Enter the search criteria (title, author, genre, etc.).
4. Click the "Search" button.

### Viewing Book Lists

1. Log in to your account.

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python
- Database: MongoDB
