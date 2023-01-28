#!/usr/bin/env python3

# External modules
from flask import Flask, render_template, request, flash, redirect, url_for
import secrets

# Internal modules
import list_packages, downloader
#import rds_controller


# Global variables
TEMPLATES_FOLDER = "../templates"
EXPOSED_PORT = 8081
HOST = "0.0.0.0"


app = Flask(__name__, template_folder=TEMPLATES_FOLDER)
app.config['SECRET_KEY'] = secrets.token_hex(16)


# Initialize clients table if not exist before the first request
#@app.before_first_request
#def init():
#    rds_controller.init_clients_table()


# Page not found (404) handler
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


# Installer route - main application route
@app.route("/", methods=["GET", "POST"])
def installer():
    """
    :return: - GET: installer web page to  select a package.
             - POST: package instalation script downloaded on client machine.
    """

    if request.method == "POST":
        package = request.form.get("package-select")
        package_url = list_packages.get_packages()[package]
        downloader.download_file(package_url)
	package_file_key = package_url.split("/")[4]
        return render_template("success.html", package=package, package_file_key=package_file_key)

    if request.method == "GET":
        packages = list(list_packages.get_packages().keys())
        return render_template("installer.html", packages=packages)


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

            # Insert into packagesweb.clients table
            #rds_controller.insert_client(company_name,
            #                             full_name,
            #                             email,
            #                             phone_number)

            # Notify about successful change
            flash("Your details saved successfuly!", category="success")
        except:
            # Notify about failure in details insertion
            flash("Failed to insert your values!", category="error")
        finally:
            return redirect(url_for("installer"))

    if request.method == "GET":
        return render_template("details.html")


if __name__ == "__main__":
    app.run(host=HOST, port=EXPOSED_PORT, debug=True)
