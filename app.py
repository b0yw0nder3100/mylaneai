from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_company_data():
    companies = []
    with open('company_attributes.csv', mode='r', newline="") as csvfile:
        reader = csv.DictReader(csvfile,  escapechar='\\', doublequote=True)
        for row in reader:
            companies.append(row)
    return companies


@app.route('/')
def index():
    company_data = load_company_data()
    
    selected_company_name = request.args.get('company', company_data[0]["company_name"])
    
    selected_company = next((item for item in company_data if item["company_name"] == selected_company_name), None)
    
    return render_template('index.html', companies=company_data, selected_company=selected_company)
