#coding=utf-8
import requests
from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print "response code:", r.status_code  # 请求返回码

# 处理有关每篇文章的返回信息
submissions_ids = r.json()
submission_dicts = []
for submission_id in submissions_ids[:30]:
    # 对于每一篇文章都执行一次api调用
    url_new = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url_new)
    print "submission_r code:", submission_r.status_code  # 打印每次请求的返回码
    response_dict = submission_r.json()
    # print response_dict
    submission_dict = {'title': response_dict['title'], 'link': 'http://news.ycombinator.com/item/id=' + str(submission_id), 'comments': response_dict.get('descendants', 0)}
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
print "submission_dicts:" + str(submission_dicts)
for submission_dict in submission_dicts:
    print("Title:", submission_dict['title'])
    print("Discussion Link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])





