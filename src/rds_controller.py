#!/usr/bin/env python3

import pymysql


conn = pymysql.connect(host="bynetinstallerdb-1.crpb8hkd9mij.us-east-1.rds.amazonaws.com",
                             user="admin",
                             password="Lilah!1234",
                             db="packages")


cur = conn.cursor()


def init_clients_table():
    """
    :return: creates clients table if not exist
    """

    cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            company_name VARCHAR(100) NOT NULL,
            full_name VARCHAR(100) NOT NULL,
            email VARCHAR(200) NOT NULL,
            phone_number VARCHAR(20) NOT NULL
        )
    """)
    conn.commit()


def insert_client(comapny_name, full_name, email, phone_number):
    """
    @company_name: A string of client's company name
    @full_name: A string of client's full name
    @email: A string of client's email
    @phone_number: A string of client's phone number
    :reuturn: new client record is insrted into clients database
    """

    query = """INSERT INTO `clients` (company_name, full_name, email, phone_number)
               VALUES (%s, %s, %s, %s)
    """
    record = (comapny_name, full_name, email, phone_number)
    cur.execute(query, record)
    conn.commit()
