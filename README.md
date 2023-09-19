# URL Shortener

A Python router using Flask and MySQL to allow users to create shortened URLs that redirect to the full URL.

# Prerequisites

MySQL is required to run the URL shortener. The user must also install dotenv, Flask and mysql-connector-python via:

```bash
pip install mysql-connector-python
pip install flask
pip install python-dotenv
```

Additionally, the user must create a database and table within MySQL. The table should have two columns, short and full.
Short should be a Primary Key, non-null, and of type VARCHAR
Full should be non-null and of type MEDIUMTEXT

The user must also configure the .env file. Rename the .env-example file to .env, and enter your database name, username, and password in the .env file.

# Usage

The entrypoint for the program is main.py. Once the program is running, the user can make a POST request to /addurl to add data to the SQL table. The body object must be in json as follows:

```json
{
  "short": "patkunst",
  "full": "http://www.linkedin.com/in/patrickkunst1999"
}
```

Once the shortened URLs are loaded into the database, the user can go to their browser and go to {base_url}/{short}. In my case, going to localhost:3000/patkunst will redirect me to http://www.linkedin.com/in/patrickkunst1999
