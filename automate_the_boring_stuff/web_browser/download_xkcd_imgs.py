import os
import requests
import bs4
"""
下载所有XKCD漫画:
    如果你希望复制某个网站的内容以在离线的时候阅读，那么可以手动导航到每个页面并保存。
    但这是很无聊的工作，交给程序去处理吧！
    XKCD是一个流行的极客漫画网站(关于浪漫、讽刺、数学、语言)，他官网首页有个prev按钮，让用户导航到前面的漫画。手动下载每张漫画要花较长的时间。
    1. 加载XKCD主页
    2. 保存该页的漫画图片
    3. 转入前一张漫画的链接
    4. 重复直到第一张漫画

拓展：
    下载页面并追踪链接是许多网盘爬虫的基础，可以看我Github仓库关于Go分布式爬虫爬取站酷作品集的例子。
"""
url = 'https://xkcd.in/?lg=cn'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # find the url of the comic image
    comicElem = soup.select('.comic-body a img')
    if comicElem:
        comicUrl = 'https://xkcd.in/' + comicElem[0].get('src')
        # download the image
        print('Downloading image %s...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        # save the image to folder
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imgFile:
            for chunk in res.iter_content(100000):
                imgFile.write(chunk)
        # get the prev button's url
        nextLink = soup.select('div.nextLink > a')[0]
        url = 'https://xkcd.in/' + nextLink.get('href')
    else:
        print('could not find comic image.')

print('Done')