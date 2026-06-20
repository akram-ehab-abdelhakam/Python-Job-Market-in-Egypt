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
salary = []

def scrape_page(page_url):

    print(f"page: {page_url}")
    result = requests.get(page_url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    job_titles = soup.find_all('h2', {'class': 'css-193uk2c'})
    print(f"found {len(job_titles)}")

    if not job_titles:
        return

    company_names = soup.find_all('a', {'class': 'css-ipsyv7'})
    location_names = soup.find_all('span', {'class': 'css-16x61xq'})
    job_skills = soup.find_all('div', {'class': 'css-1rhj4yg'})

    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)
        links.append(job_titles[i].find('a').attrs['href'])
        company_name.append(company_names[i].text)
        location_name.append(location_names[i].text)
        skill.append(job_skills[i].text)

    for link in job_titles:   
        pass

    start_index = len(links) - len(job_titles)
    for i in range(start_index, len(links)):
        job_url = "https://wuzzuf.net" + links[i]
        print(f"Salary from: {job_url}")
        try:
            job_result = requests.get(job_url)
            job_src = job_result.content
            job_soup = BeautifulSoup(job_src, 'lxml')
            sal = job_soup.find('span', {'class': 'css-2rozun'})
            if sal:
                salary.append(sal.text.strip())
            else:
                salary.append("Not specified")
        except Exception as e:
            print(f"Error fetching salary: {e}")
            salary.append("Error")
        time.sleep(0.3)  



scrape_page("https://wuzzuf.net/search/jobs?q=python&a=hpb")          
for i in range(0,50):
    scrape_page(f"https://wuzzuf.net/search/jobs?q=python&start={i}&a=hpb")

output_path = "wuzzuf.csv"
file_list = [job_title, company_name, location_name, skill, links, salary]
exported = zip_longest(*file_list)

with open(output_path, 'w', encoding='utf-8') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['job title', 'company_name', 'location', 'skills', 'links', 'salary'])
    wr.writerows(exported)

print(f"saved to: {output_path}")