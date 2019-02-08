import bs4
import requests
from bs4 import BeautifulSoup as soup
list = []
numberofrecords = int(input("Number of values you want to create csv file\n"))
for i in range(0, numberofrecords):
    i = int(input("Enter record values one by one\n"))
    list.append(str(i))
print("Creating your CSV file, Please Wait\n")
filename = "Patents.csv"
f = open(filename, "w")
headers = "Title, Abstract, Filing_date, Inventors, Assignee\n"
f.write(headers)
for i in list:
    headr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
    my_url = ""
    my_url = "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PALL&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.htm&r=1&f=G&l=50&s1="+i+".PN.&OS=PN/"+i+"&RS=PN/"+i
    page = requests.get(my_url, headers=headr)
    page_html = soup(page.content, "lxml")
    body = page_html.body
    titletemp = body.find('font', {"size": "+1"})
    Title = titletemp.text.strip('\n')
    print(Title)
    abs = body.findAll('p')
    Abstract = abs[0].text.strip('\n')
    print("Scraping Abstraction")
    th = body.findAll("th", {"scope": "row"})
    td = body.findAll("td", {"width": "90%"})
    Inventors="Null"
    Assignee="Null"
    Filing_date="Null"
    for i in range (len(th)):
        if th[i].text.strip() == 'Inventors:':
            Inventors = td[i].text.strip()
        if th[i].text.strip("\n") == 'Assignee:':
            Assignee = td[i].text.strip("\n")
        if th[i].text.strip() == 'Filed:':
            Filing_date = td[i].text.strip()
    print("Scraped successfully")
    f.write('"' + Title + '","' + Abstract + '","' + Filing_date +
            '","' + Inventors + '","' + Assignee + '"\n')
f.close()
