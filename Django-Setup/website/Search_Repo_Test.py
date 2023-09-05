import time
import numpy as np
from github import Github, Auth, GithubIntegration
import re
import sys
import requests
import json
from urllib.parse import urlencode


def main(keyword):
    auth = Auth.Token('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')
    client = Github(auth=auth)

    def search_github(keyword):
        '''
        keyword: what you want to search (query)
        query: https://docs.github.com/en/search-github/searching-on-github/searching-code#search-within-a-users-or-organizations-repositories
        '''

        contentFiles = []
        html_urls = []
        result = client.search_code(f'org:ds-modules {keyword}')
    
        for file in result:
            contentFiles.append(file)
        
        for file in result:
            html_urls.append(file.html_url)
        
        return contentFiles, html_urls
    
    search_output = search_github(keyword)
    contentFiles = search_output[0]
    html_urls = search_output[1]

    if len(contentFiles) == 0:
        return []
    else:
        repo_tabs = []
        all_repos = []
        for i in range(len(contentFiles)):
            repo = re.search(r'ds-modules/(.*?)/', html_urls[i]).group(1)
            all_repos.append(repo)
            if repo not in repo_tabs:
                repo_tabs.append(repo)

        current_repo = re.search(r'ds-modules/(.*?)/', html_urls[0]).group(1)
        for i in range(len(contentFiles)):
            repo = re.search(r'ds-modules/(.*?)/', html_urls[i]).group(1)
            index = repo_tabs.index(repo)
    return repo_tabs

print(main(sys.argv[1]))
