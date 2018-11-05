import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print('Status code:',r.status_code)

response_dict= r.json()

# print(response_dict)
# print(response_dict.keys())
print('Total repositories:',response_dict['total_count'])
repo_dicts = response_dict['items']
print('Repositories returned:',len(repo_dicts))

# repo_dict= repo_dicts[0]
# print('\nKeys:',len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# 研究第一个仓库
print('\nSelected information about first repository:')
for repo_dict in repo_dicts :
    print('Name:',repo_dict['name'])
    print('Owner:',repo_dict['owner']['login'])
    print('Stars:',repo_dict['stargazers_count'])
    print('Repository:',repo_dict['html_url'])
    print('Description:',repo_dict['description'])
    print('\n')
