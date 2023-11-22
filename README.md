
Django Tree Menu is a Django application that allows you to create hierarchical tree menus, store them in a database, and display them on your website using custom template tags. You can create and edit menus through the standard Django admin panel.

Task
Create a Django application that enables:

Database entry of menus through the Django admin.
Displaying menus on any desired page by name using a template tag.
Implementation Features
Menus are created using template tags.
Everything below the selected item is expanded. The first level of nesting under the selected item is also expanded.
Menu data is stored in the database.
Editable in the standard Django admin.
The active menu item is determined based on the URL of the current page.
Multiple menus can exist on one page, identified by name.
Clicking on a menu item leads to navigation to the specified URL, either explicitly or through a named URL.
Only one database query is required to render each menu.
Tech Stack
Django
Python Standard Library
Getting Started
Clone the repository and navigate to the project directory.
Install Poetry if not already installed: pip install poetry.
Activate the virtual environment using Poetry: poetry shell.
Install dependencies: pip install -r requirements.txt.
Run migrations: python manage.py migrate.
Start the server: python manage.py runserver.
Create a superuser for the database: python manage.py createsuperuser.
Load data using the load_data.py script: python load_data.py.
Access the admin panel at http://127.0.0.1:8000/admin/.
Access the menu at http://127.0.0.1:8000/tree_menu/.
License
MIT License

Future Improvements
Add the ability to apply styles and classes to menu elements.
Implement menu caching for performance optimization.
Extend support for other types of databases.
Create additional examples and documentation for using the application.