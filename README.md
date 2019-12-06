# crud-task

## Project idea

The project idea was to create a basic product catalog interacting with external API.
I have used Django REST Framework to build this API. 

## Python version: 3.5+

## Instructions to run the script

1. Goto the directory where you want to store your project.
2. Clone the git repository to the project directory.
3. Open the terminal and navigate to the project directory from the terminal.
4. Create virtual environment from the terminal by typing ```virtualenv .env``` and activate it by typing `source .env/bin/activate`(for Linux), '.env\Scripts\activate'(for Windows).
    * If you don't have `virtualenv` installed then install it by typing `pip install virtualenv`.
5. Install the project dependencies by typing `pip install -r requirements.txt` on the terminal.
7. Migrate the database by typing `python manage.py makemigrations` and then `python manage.py migrate` on the terminal.
8. Create admin user if you want by typing `python manage.py createsuperuser` and give the required credentials on the terminal.
9. Now, Run the project from your **localhost** by typing `python manage.py runserver`
10. Navigate to the URL [127.0.0.1:8000](127.0.0.1:8000) or [localhost:8000](localhost:8000) from your browser.
11. You can terminate the server anytime by **CTRL+c**.

### URL's I've implemented:
* api/products/
* api/products/{pk}
* api/products/{pk}/attributes
* api/attributes/{pk}/
* api/products/{pk}/prices/
* api/prices/{pk}/

## Snapshots:

* **api/products/**
![](./md-images/SS1.png)
* **api/products/1/**
![](./md-images/SS2.png)
* **api/products/1/attributes/**
![](./md-images/SS3.png)
* **api/products/1/prices/**
![](./md-images/SS4.png)
