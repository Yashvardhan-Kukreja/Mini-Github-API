from bs4 import BeautifulSoup as soup
import requests
user = input("Enter your GitHub username")

url = "http://www.github.com/" + user + "?tab=repositories"
client = requests.get(url)
page_soup = soup(client.content, 'html.parser')
detailed_repos = page_soup.findAll('div', {'id':'user-repositories-list'})

# functions for scraping my starred repos

def detailed_starred_repos(username):
    client = requests.get("http://www.github.com/" + username + "?tab=stars")
    page_soup = soup(client.content, 'html.parser')
    starred_repos = page_soup.findAll('div', {'class': 'position-relative'}).findAll('div')
    return starred_repos[1:]

def starred_repos_titles(username):
    repos = detailed_starred_repos(username)
    titles = [repo.find('div').find('h3').find('a').span.text + repo.find('div').find('h3').find('a').text for repo in repos]
    return titles

def starred_repos_descriptions(username):
    repos = detailed_starred_repos(username)
    descriptions = [repo.findAll('div')[1].find('p').text for repo in repos]
    return descriptions

# functions for scraping my repos

def detailed_repos(username):
    client = requests.get("http://www.github.com/" + username + "?tab=repositories")
    page_soup = soup(client.content, 'html.parser')
    repos = page_soup.findAll('div', {'id': 'user-repositories-list'})[0].find('ul').findAll('li')
    return repos

def repos_titles(username):
    repos_detailed = detailed_repos(username)
    titles = [repo.find('div').find('h3').find('a').text for repo in repos_detailed]
    return titles

def repos_descriptions(username):
    repos_detailed = detailed_repos(username)
    descriptions = [repo.findAll('div')[1].find('p').text for repo in repos_detailed]
    return descriptions




