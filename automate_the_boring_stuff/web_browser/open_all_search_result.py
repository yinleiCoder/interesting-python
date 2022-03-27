import sys
import webbrowser
import bs4
import requests

"""
浏览器分标签页打开所有搜索结果:
    打开“乐山人事网”，想站内搜索“公开招聘事业单位工作人员”。
    通常我们会开浏览器，查找该结果，然后依次用鼠标单击结果链接在新的浏览器标签页打开，可以稍后再来查看。
    
    改进：
        1. 从命令行参数中获取查询关键字
        2. 取得查询结果页面
        3. 为每个结果打开一个浏览器标签页
Usage: 
    python open_all_search_result.py 公开招聘事业单位工作人员
"""
print('Searching...')
# retrive html source code
res = requests.get('http://www.lspta.com.cn/search.html?keyword=' + ''.join(sys.argv[1]))
res.raise_for_status()

# retrive top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# open a browser tab for each result
linkElems = soup.select('div.infos.searchPageList > ul > li > a')
for i in range(len(linkElems)):
    urlToOpen = f'http://www.lspta.com.cn/{linkElems[i].get("href")}'
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)