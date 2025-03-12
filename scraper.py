import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error

class GitHubTrendingScraper:
    def __init__(self):
        self.base_url = 'https://github.com/trending'
        self.weekly_url = 'https://github.com/trending?since=weekly'
        self.monthly_url = 'https://github.com/trending?since=monthly'
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '123456',
            'database': 'github_trending'
        }

    def scrape(self, type='daily'):
        url_options = {
            'daily': self.base_url,
            'weekly': self.weekly_url,
            'monthly': self.monthly_url
        }
        url = url_options.get(type, self.base_url)
        proxies = {
            'http': 'http://localhost:7890',
            'https': 'http://localhost:7890'
        }
        response = requests.get(url, proxies=proxies)
        soup = BeautifulSoup(response.text, 'html.parser')
        repos = []
        for article in soup.find_all('article', {'class': 'Box-row'}):
            repo = {}
            repo['title'] = article.find('h2').text.strip().replace('\n', '').replace(' ', '')
            repo['description'] = article.find('p', {'class': 'col-9'}).text.strip() if article.find('p', {'class': 'col-9'}) else ''
            repo['author'] = article.find('h2').find('a').text.strip().split('/')[0]
            repo['language'] = article.find('span', {'itemprop': 'programmingLanguage'}).text.strip() if article.find('span', {'itemprop': 'programmingLanguage'}) else ''
            repo['stars'] = article.find('a', {'href': lambda x: x and 'stargazers' in x}).text.strip() if article.find('a', {'href': lambda x: x and 'stargazers' in x}) else ''
            repo['type'] = type
            repos.append(repo)
        return repos

    def save_to_database(self, repos):
        try:
            connection = mysql.connector.connect(**self.db_config)
            if connection.is_connected():
                cursor = connection.cursor()
                # 删除同一天且相同类型的记录
                delete_sql = '''DELETE FROM trending_repos 
                              WHERE DATE(created_at) = CURDATE() AND type = %s'''
                for repo in repos:
                    cursor.execute(delete_sql, (repo['type'],))
                # 插入新数据
                insert_sql = '''INSERT INTO trending_repos 
                        (title, description, author, language, stars, type) 
                        VALUES (%s, %s, %s, %s, %s, %s)'''
                for repo in repos:
                    values = (repo['title'], repo['description'], 
                             repo['author'], repo['language'], repo['stars'], repo['type'])
                    cursor.execute(insert_sql, values)
                connection.commit()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == '__main__':
    scraper = GitHubTrendingScraper()
    repos = scraper.scrape()
    scraper.save_to_database(repos)