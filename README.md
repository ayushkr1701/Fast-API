
# Configuration Management System for Onboarding Organisations from Different Countries

A FastAPI application to manage the configurations and provide functionalities for CRUD(create, Read, Update, Delete) operations for the same.
We have utilized the PostgreSQL as our relational database management system( replace the DATABASE_URL in /app/databse.py with the postgresSQL or create a .env file in the rooot directory and then create a variable DATABASE_URL having value as the PostgresSQL server link) and SQLAlchemy as the ORM to interact with the database.
The datatable named configurations takes three values, id which is the primary key, country_code having type as String and we have made sure it's unique as different countries will have different code, for ex: United States: USA, India: In and then the last column as config having type JSON , JSON because different countries can have different configurations, for ex: in India, we have PAN, GSTIN numbers but for USA, the registration number would be different. All this has been defined in /app/models.py

Now, the FastAPI endpoints for CRUD operations are created, the crud functions are defined in /app/cruds.py named as create_configuration for create, get_configuartion for read, upadte_configuration for update and delete_configuration for delete purposes and the respective endpoints can be found in /app/main.py which are /create_configuration , /get_configuartion/{country_code} , /upadte_configuration , /delete_configuration/{country_code} .

There is an /app/exceptions.py which has a function to check if configuration for a particular country is not found.

### How to run

1. Clone this repo by running the command 'git clone https://github.com/ayushkr1701/Fast-API ' in the terminal.
2. Now create a virtual environment by running command 'virtualenv -p python3.12 <name>'.
3. Now activate the virtual environment by running the command '<name>\scripts\activate'.
4. Once the virtual env gets started install all the dependencies by running the command 'pip install -r requirements.txt' 
5. Now start the api by running command 'uvicorn app.main:app'. You will see it's showing uvicorn running on port 8000.

### How to test

1. Open Postman, click on File, then New and then HTTP.
2. Now enter http://127.0.0.1:8000/ in the URL box.
3. First we will create configuartion whose endpoint is "POST /create_configuration". So select the method as POST and the url becomes now http://127.0.0.1:8000/create_configuration , now click on Body and select raw and enter the details. for ex:
    {
        "country_code": "UK",
        "config": {
            "business_name": "ok ok ok.",
            "registration_number": "3456789",
            "additional_details": {
                "key": "new"
            }
        }
    }

4. Similarly we can check other endpoints by carefully selecting the method and its respective endpoint url.
