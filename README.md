# Prerequisites

- Python 3
- Flask
- Flask SQL Alchemy
- MariaDB
- Docker (if database is ran in a container)

# Project structure

- <code>./init_app.py</code> is the main application file
- <code>./config.py</code> contains all configuration properties
- <code>./app</code> contains application's source code
- <code>./shop-api.postman_collection.json</code> contains a Postman collection to test the REST API

# Preparing the environment

- Install Docker (used to host the database)
- Install MariaDB <code>docker run --name mariadb -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d docker.io/library/mariadb:10.4</code>
- Install Python 3.8
- Install Python pip
- Install all pip packages listed in <code>requirements.txt</code> (pip install -r requirements.txt on Linux)
- Install <code>python3-mysqldb</code> package if the server is ran on Linux
- Create a DB schema

# Running the server

- In order to start the server, run the following command:
  <code>python3 init_app.py</code>
- If server is started successfully, a message should appear, displaying <code>Running on <...> (Press CTRL+C to quit)</code>

# API usage

- Use the provided Postman collection for local API testing
- Further API documentation is provided in [Swaggerhub documentation](https://app.swaggerhub.com/apis-docs/Lucky44/RS-SHOP_API/1.0.0#/)
