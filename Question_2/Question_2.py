"""Question_2 - WAP to get the Social Links, Email & Contacts details of a website on user input."""


# importing required libraries
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# connecting to the  website and getting response
url = "https://ful.io"

response = requests.get(url)

# using BeautifulSoup parsing html
html_page = bs(response.content,'html.parser')

#extracting all the anchor tags from the html code
all_links = html_page.find_all('a')

#declaring lists for appending the ouput in them
links=[]
emails=[]
contact=[]

# filtering links with href from the anchor tags 
for link in all_links:
    href = link['href']

    if href:
        #from all the href extracting links that contain ful
        if r'ful' in href:
            #from all the href extracting external  links 
            if href.split(":")[0] in ['https'] and r'ful' in href:
                links.append(href)

            #from href extracting email using mailto
            if r'mailto' in href:
               mail_id = href.split(":")[1]
               emails.append(mail_id)

    #from href extracting contacts that contain tel
    if r'tel' in href:
        phn_no = href.split(":")[1]
        contact.append(phn_no)

#printing the output in the required format
print("Social Links -")
for link in links:
    print(link)

print("Email/s -")
for email in emails:
    print(email)

print("Contact -")
for num in contact:
    print(num)
