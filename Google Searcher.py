'''
Have to install packages before running this.
This script gives top 5 results from Google search based on your search item and later on provides option to open them all at once.
'''

import requests , webbrowser , bs4

data = input('Enter what u want to search : ')

res = requests.get('https://google.com/search?q='+data)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')
linkElements = soup.select('.r a')
linkToOpen = min(5,len(linkElements))

for x in range(linkToOpen):
    link = linkElements[x].get('href')[7:]
    print('{} -> {}'.format(x+1,link))

x = int(input('If u want to open them all press 1 else any other key : '))
if x==1:
    for x in range(linkToOpen):
        webbrowser.open('https:/google.com'+linkElements[x].get('href'))
    print('Thanks for Using!')
else:
    print('Thanks for Using!')
    exit()
