import mysql.connector
import os
from dotenv import load_dotenv


# Load environment variables (database secrets)
load_dotenv()


# Global variables
MYSQL_HOST = "mysql"
MYSQL_PORT = "3306"


# Create connection to database
db_connection = mysql.connector.connect(host=MYSQL_HOST,
				                        port=MYSQL_PORT,
			                            user="root",
                                        password=os.getenv("MYSQL_ROOT_PASSWORD"),
			                            database=os.getenv("MYSQL_DATABASE")
)


# create a curosor instance
cursor = db_connection.cursor()


def init_clients_table():
    """
    :return: creates clients table if not exist
    """

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            company_name VARCHAR(100) NOT NULL,
            full_name VARCHAR(100) NOT NULL,
            email VARCHAR(200) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
        )
    """)
    db_connection.commit()


def insert_client(comapny_name, full_name, email, phone_number):
    """
    @company_name: A string of client's company name
    @full_name: A string of client's full name
    @email: A string of client's email
    @phone_number: A string of client's phone number
    :reuturn: new client record is insrted into clients database
    """

    record = (comapny_name, full_name, email, phone_number)
    cursor.execute(""" 
                    INSERT INTO clients(company_name, full_name, email, phone_number) 
                    VALUES (%s, %s, %s, %s)""", 
                    record)
    db_connection.commit()