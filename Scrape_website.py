import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=tesla'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the first title
title = soup.title.string
print(f'Title: {title}\n')

# Extract h1, h2, and p texts
h1_tags = soup.find_all('h1')
h2_tags = soup.find_all('h2')
p_tags = soup.find_all('p')

# Print h1 texts
print('h1 texts:')
for h1 in h1_tags:
    print(h1.text)

# Print h2 texts
print('\nh2 texts:')
for h2 in h2_tags:
    print(h2.text)

# Print p texts
print('\np texts:')
for p in p_tags:
    print(p.text)

# Print up to the next title
current_title = title
paragraphs = []
for p in p_tags:
    if p.name == 'h1' or p.name == 'h2':
        if p.name == 'h1' and p.text != current_title:
            break
        current_title = p.text
    paragraphs.append(p.text)

print('\nParagraphs till next title:')
print('\n'.join(paragraphs))