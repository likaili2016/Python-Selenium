# coding=utf-8

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行api调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# print ("Status code:", r.status_code)

# api响应存储在一个变量中
response_dict = r.json()

# 处理结束
# print(response_dict.keys())
# print ("Total Repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print ("Repositories returned:", len(repo_dicts))

names, plot_dicts = [], []
for i in repo_dicts:
    names.append(i['name'])
    plot_dict = {'value': i['stargazers_count'], 'label': i['description'], 'link': i['html_url']}
    plot_dicts.append(plot_dict)
print names
print plot_dict
print plot_dicts