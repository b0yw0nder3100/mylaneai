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

def load_job_post_data():
    job_posts = []
    with open('job_post_by_city.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job_posts.append(row)
    return job_posts

def load_job_family_data():
    job_family_posts = []
    with open('job_post_by_job_family.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job_family_posts.append(row)
    return job_family_posts

@app.route('/')
def index():
    company_data = load_company_data()
    job_post_data = load_job_post_data()
    job_family_data = load_job_family_data()


    selected_company_name = request.args.get('company', company_data[0]["company_name"])
  
    selected_company = next((item for item in company_data if item["company_name"] == selected_company_name), None)

  
    selected_job_posts = [
        post for post in job_post_data if post["company_name"] == selected_company_name
    ]
    
    selected_job_family_posts = [
        post for post in job_family_data if post["company_name"] == selected_company_name
    ]
    
    city_data = [{"name": post["city"], "count": int(post["position_count"])} for post in selected_job_posts]

    job_family_data = [{"name": post["job_family"], "count": int(post["position_count"])} for post in selected_job_family_posts]

    return render_template('index.html', companies=company_data, selected_company=selected_company, city_data=city_data, job_family_data=job_family_data)