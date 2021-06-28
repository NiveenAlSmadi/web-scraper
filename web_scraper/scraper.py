import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):

    """
    get_citations_needed takes in a url and returns an integer
    """
    page = requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')
    result=soup.findAll(text='citation needed') 
    return  len(result)



def get_citations_needed_report(URL):

    """
    get_citations_needed_report takes in a url and returns a string
    the string should be formatted with each citation needed on own line, in order found.

    """
    page = requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser').findAll('p')
    report=[]
    for i in soup:
        a_exist=i.findAll('a',title="Wikipedia:Citation needed")
        if a_exist:
           report.append(i.text)
           report += '\n'
           print(f'The paragraph : {i.text}')

           print("*****************************************************************************************")

    return (report )     






if __name__=="__main__":
    
    get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
    get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Jordan')
    get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_chocolate')
    get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')
    get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Jordan')
    get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_chocolate')
 







