from bs4 import BeautifulSoup
import requests


URL = "https://www.indeed.com/?vjk=3f6b5ffb4571c3a4"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="mosaic-provider-jobcards")
print(results.prettify())

#job_elements = results.find_all("div", class_="jobsearch-ResultsList")

# for job_element in job_elements:
   # print(job_element, end="\n"*2)

#for job_element in job_elements:
  #  title_element = job_element.find()