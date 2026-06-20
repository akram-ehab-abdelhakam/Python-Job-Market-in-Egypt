import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import time





job_title = []
company_name = []
location_name = []
skill = []
links = []

def scrape_page(page_url):

    print(f"page: {page_url}")
    result = requests.get(page_url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    job_links = soup.find_all('a', {'class': 'position-absolute w-100 h-100 top-0 left-0'})
    print(f"found {len(job_links)}")

    for job in job_links:
        relative_url = job.get('href')
        if not relative_url:
            continue  
        
        full_url = "https://egypt.tanqeeb.com" + relative_url

        try:
            detail_result = requests.get(full_url)
            detail_src = detail_result.content
            detail_soup = BeautifulSoup(detail_src, 'lxml')

            title_elem = detail_soup.find('h3', {'class': 'text-title-color fs-24 font-weight-bold job-title-with-logo ltr'})
            title = title_elem.text.strip() if title_elem else 'N/A'

            company_elem = detail_soup.find('a', {'class': 'job-meta-company'})
            company = company_elem.text.strip() if company_elem else 'N/A'

            location_elem = detail_soup.find('div', {'class': 'job-meta-item'})
            location = location_elem.text.strip() if location_elem else 'N/A'

            skills_elem = detail_soup.find('span', {'class': 'text-dark w-100 fs-16 font-weight-medium col-6 col-md-9'})
            skills = skills_elem.text.strip() if skills_elem else 'N/A'

            job_title.append(title)
            company_name.append(company)
            location_name.append(location)
            skill.append(skills)
            links.append(full_url)   

        except Exception as e:
            print(f"Error page {full_url}: {e}")
            continue

        time.sleep(0.5)

scrape_page("https://egypt.tanqeeb.com/s/jobs/Python-developer-jobs?change_lang=1")

for i in range(2, 50):
    scrape_page(f"https://egypt.tanqeeb.com/s/jobs/Python-developer-jobs?countries[]=213&page_no={i}")

output_path = "tanqeeb_jobs.csv"
file_list = [job_title, company_name, location_name, skill, links]
exported = zip_longest(*file_list)

with open(output_path, 'w', encoding='utf-8') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['job title', 'company name', 'location', 'skills', 'detail link'])
    wr.writerows(exported)

print(f"saved to: {output_path}")