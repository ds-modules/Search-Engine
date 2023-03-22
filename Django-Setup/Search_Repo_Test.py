import time
import numpy as np
from github import Github
import re
import sys


def main(keyword):
    client = Github('cec181f6847eb6472425', '1ab6e2c3b3ed83f4b25ecd390cd5ef65c629b591')

    def search_github(keyword, query):
        '''
        keyword: what you want to search (query)
        query: https://docs.github.com/en/search-github/searching-on-github/searching-code#search-within-a-users-or-organizations-repositories
        '''
        contentFiles = []
        html_urls = []
        result = client.search_code(keyword + ' ' + query)
    
        for file in result:
            contentFiles.append(file)
        
        for file in result:
            html_urls.append(file.html_url)
        
        return contentFiles, html_urls
    
    search_output = search_github(keyword, 'org:ds-modules extension:ipynb')
    contentFiles = search_output[0]
    html_urls = search_output[1]

    if len(contentFiles) == 0:
        print('None Found')
    else:
        repo_tabs = []
        for i in range(len(contentFiles)):
            print(contentFiles[i].html_url)
            repo = re.search(r'ds-modules/(.*?)/', html_urls[i]).group(1)
            if repo not in repo_tabs:
                repo_tabs.append(repo)

        current_repo = re.search(r'ds-modules/(.*?)/', html_urls[0]).group(1)
        for i in range(len(contentFiles)):
            repo = re.search(r'ds-modules/(.*?)/', html_urls[i]).group(1)
            index = repo_tabs.index(repo)
    return contentFiles

main(sys.argv[1])
