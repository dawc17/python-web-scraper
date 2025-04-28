import requests
import bs4

targetUrl = "https://pyfound.blogspot.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def workspaceHtml(url):
    try:
        requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error: {url} is not reachable.")
        return None
    else:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: {url} returned status code {response.status_code}.")
            return None

def extractHeadlines(html):
    if html is None:
        return []
    soup = bs4.BeautifulSoup(html, 'html.parser')
    soup = soup.find_all('h3', class_='post-title')
    headlines = []
    for i in soup:
        headlines.append(i.text.strip())
    return headlines

html = workspaceHtml(targetUrl)
headlinesList = extractHeadlines(html)

for i in headlinesList:
    print(i)

