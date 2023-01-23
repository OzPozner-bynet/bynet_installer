#!/usr/bin/env python3

# External modules
from flask import Flask, render_template, request, flash, redirect, url_for
import secrets

# Internal modules
import list_packages, rds_controller


# Global variables
TEMPLATES_FOLDER = "../templates"
EXPOSED_PORT = 5000
HOST = "0.0.0.0"


app = Flask(__name__, template_folder=TEMPLATES_FOLDER)
app.config['SECRET_KEY'] = secrets.token_hex(16)


# Initialize clients table if not exist before the first request
@app.before_first_request
def init():
    rds_controller.init_clients_table()


# Installer route - main application route 
@app.route("/", methods=["GET", "POST"])
def installer():
    """
    :return: - GET: installer web page to  select a package.
             - POST: package instalation script downloaded on client machine.
    """

    if request.method == "GET":
        packages = list(list_packages.get_packages().keys())
        return render_template('installer.html', packages=packages)

    if request.method == "POST":
        file_key = request.form.get('packages-select')
        file_name = list_packages.get_packages()[file_key]
	return file_name


# Details form page
@app.route("/details", methods=["GET", "POST"])
def details():
    """
    :return: - GET: details form web page.
             - POST: new client record has been inserted into package_installer database.
    """

    if request.method == "POST":
        try:
            # Retreive form data
            company_name = request.form["company_name"]
            full_name = request.form["full_name"]
            email = request.form["email"]
            phone_number = request.form["phone_number"]

            print(company_name)

            # Insert into packagesweb.clients table
            rds_controller.insert_client(company_name,
                                         full_name,
                                         email,
                                         phone_number)

            # Notify about successful change
            flash("Your details saved successfuly!", category="success")
        except:
            # Notify about failure in details insertion
            flash("Failed to insert your values!", category="error")
        finally:
            return redirect(url_for("installer"))
    
    if request.method == "GET":
        return render_template("details.html")


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        packages = ["A", "B"]
        return render_template("test.html", packages=packages)
    if request.method == "POST":
        package = request.form.get("package-select")
        return package

if __name__ == "__main__":
    app.run(host=HOST, port=EXPOSED_PORT, debug=True)
