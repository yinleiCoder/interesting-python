import requests
from plotly.graph_objs import Bar
from plotly import offline
"""
对Github上使用Go的项目进行按照star排序可视化
"""

url = 'https://api.github.com/search/repositories?q=language:go&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
resp = requests.get(url, headers=headers)
print(f"Status Code:{resp.status_code}")
resp_dict = resp.json()
print(f'Total repositories: {resp_dict["total_count"]}')
print(resp_dict.keys())
repo_dicts = resp_dict['items']
repo_links, stars, labels = [], [], []
print(f'Repositories returned: {len(repo_dicts)}')
for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict["stargazers_count"])
    owner = repo_dict["owner"]["login"]
    created_at = repo_dict["created_at"]
    updated_at = repo_dict["updated_at"]
    description = repo_dict["description"]
    label = f'{owner}<br/>{description}<br/>{created_at}<br/>{updated_at}'
    labels.append(label)
    # print(f'Name: {repo_dict["name"]}')
    # print(f'Owner: {repo_dict["owner"]["login"]}')
    # print(f'Stars: {repo_dict["stargazers_count"]}')
    # print(f'Repository: {repo_dict["html_url"]}')
    # print(f'Created: {repo_dict["created_at"]}')
    # print(f'Updated: {repo_dict["updated_at"]}')
    # print(f'Description: {repo_dict["description"]}')

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
      'color': 'rgb(60, 100, 150)',
      'line': {'width': 1.5, 'color': 'rgba(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': '2022 Github 小星星最多的Go语言开发的项目',
    'titlefont': {'size': 24},
    'xaxis': {
        'title': '仓库名',
        'titlefont': {'size': 22},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': '小星星数',
        'titlefont': {'size': 22},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_github.html')