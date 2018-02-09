from bs4 import BeautifulSoup as soup
import requests


# functions for scraping my starred repos

def detailed_starred_repos(username):
    client = requests.get("http://www.github.com/" + username + "?tab=stars")
    page_soup = soup(client.content, 'html.parser')
    starred_repos = page_soup.findAll('div', {'class': 'position-relative'}).findAll('div')
    return starred_repos[1:]


def starred_repos_titles(username):
    repos = detailed_starred_repos(username)
    titles = [repo.find('div').find('h3').find('a').span.text + repo.find('div').find('h3').find('a').text for repo in
              repos]
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


# functions for scraping my followers

def detailed_followers(username):
    client = requests.get("http://www.github.com/" + username + "?tab=followers")
    page_soup = soup(client.content, 'html.parser')
    repos = page_soup.findAll('div', {'class': 'position-relative'})[0].findAll('div')
    return repos


def followers_titles(username):
    repos_detailed = detailed_followers(username)
    titles = [(repo.findAll('div')[1].find('span').findAll('span')[0].text + "--" +
               repo.findAll('div')[1].find('span').findAll('span')[1].text) for repo in repos_detailed]
    return titles


# functions for scraping my pinned repos

def detailed_pin_repos(username):
    client = requests.get("http://www.github.com/" + username)
    page_soup = soup(client.content, 'html.parser')
    repos = page_soup.findAll('form', {'class': 'js-pinned-repos-reorder-form'})[0].find('ol').findAll('li')
    return repos


def pinned_repos_titles(username):
    repos_detailed = detailed_pin_repos(username)
    titles = [repo.find('div').find('span').find('a').text for repo in repos_detailed]
    return titles


def pinned_repos_descriptions(username):
    repos_detailed = detailed_pin_repos(username)
    descriptions = [repo.find('div').find('p').text for repo in repos_detailed]
    return descriptions


# Main program


user = input("Enter your username: ")
