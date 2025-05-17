import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?ref=browse-jobs&start=4"
page = requests.get(url, headers=headers)

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    jobs_details = []

    jobs = soup.find_all("div", {"class": "css-pkv5jc"})

    for job in jobs:
        try:
            title_tag = job.find("h2", class_="css-m604qf")
            job_title = title_tag.find("a").text.strip() 

            company_tag = job.find("a", class_="css-17s97q8")
            company_name = company_tag.text.strip() 

            job_link_tag = job.find("a", class_="css-o171kl")
            job_link = job_link_tag["href"] 

            location_tag = job.find("span", class_="css-5wys0k")
            job_location = location_tag.text.strip() 

            job_type_tag = job.find("span", class_="css-o1vzmt eoyjyou0")
            job_type = job_type_tag.text.strip() 

            jobs_details.append({
                "job title": job_title,
                "company name": company_name,
                "job type": job_type,
                "job location": job_location,
                "job link": job_link
            })

        except Exception as e:
            print(f"⚠️ Error parsing job: {e}")
            continue

    if jobs_details:
        keys = jobs_details[0].keys()
        with open(r'C:\Users\hossam\Desktop\web scraping\jobs.csv', 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(jobs_details)
            print("✅ CSV file created successfully.")
    else:
        print("❌ No job data found.")

main(page)
