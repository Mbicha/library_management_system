## Library Management System

This is a web application for helping librarians keep track of books issued.

# Technologies

HTML,
Tailwindcss,
JavaScript,
Python3 (flask),
Database (Mysql)

# Author
Charles Mbithi (mbithicharlse@gmail.com)

# Folders and directories
|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[app](/build/app/) | Has [css](/build/app/static/), [html](/build/app/templates/), and [image](/build/app/static/img/) directories containing templates and resources for the website.|
|[Main App](/build/app/__init__.py)| Main script of the application
|[Authentication](/build/app/auth.py)| Has authentication blueprint for the application.|
|[Base](/build/app/base.py)| Initialize SQLAlchemy|
|[DB Operations](/build/app/db_operations.py)| Operations for the database.|
|[Main](/build/app/main.py)| Blueprint for other pages.|
|[Model](/build/app/model.py)| Define schema for the Library Management System.|
|[Utils](./build/app/utils/)| Util classes for generating books and users.|
|[Add Books and Users](./build/app/auto_insert_book_users.py)| Automatically adds books and users with help of functions in util directory.|
