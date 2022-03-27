from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
Selenium模块控制浏览器：
    selenium可让python直接控制浏览器，实现方法是单击链接并填写登录信息，几乎就像人类用户与页面交互一样。
    selenium允许更高级的多的方式与网页交互。但因为他启动了web浏览器，只是想从往网上下载一些文件，那么会有点慢，并且难以在后台运行。
    如果与网页交互的方式依赖于更新网页的js代码，那么需要使用selenium而不是requests。
    因为好点的大型系统肯定会有软件系统来识别他们怀疑是脚本的流量，这些脚本可能会获取他们的信息或注册多个免费账户。
    这些网站可能会在一段时间后拒绝向你提供页面，让你编写的所有脚本失效。
    向网站透露你正在使用脚本的一种主要方式就是请求头的user-agent。
    selenium的user-agent和普通浏览器一样，而且他的流量模式也是一样的。
    一个由selenium控制的浏览器会像普通浏览器一样下载图片、广告、cookie、隐私入侵追踪器等。
    但selenium仍然可以被网站检测到。
    
    selenium所作的事情远远超过了这里的代码，它还可以修改浏览器的cookie，截取页面快照，以及运行自定义的js代码。
    更多信息请访问下方selenium官网技术文档。

selenium: https://www.selenium.dev/selenium/docs/api/py/index.html#
"""

browser = webdriver.Chrome()
print(type(browser))
browser.get('https://www.baidu.com')

# 页面中寻找元素
# try:
#     elem = browser.find_element(by=By.CLASS_NAME, value='s_ipt')
#     print('found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('was not able to find an element with that name.')

# 单击页面
# linkElem = browser.find_element(by=By.ID, value='hotsearch-refresh-btn')
# print(type(linkElem))
# linkElem.click()

# 填写并提交表单: 要填写表单只要找到那个文本字段的<input>或<textarea>，然后调用send_keys()填写表单，在任何元素上调用submit()都等用于单击该元素所在表单的submit按钮
# userElem = browser.find_element(by=By.ID, value='user_name')
# userElem.send_keys('your real username here')
# passwordElem = browser.find_element(by=By.ID, value='user_pass')
# passwordElem.send_keys('your real password here')
# passwordElem.submit()

# 发送特殊键
# htmlElem = browser.find_element(by=By.TAG_NAME, value='html')
# htmlElem.send_keys(Keys.END)
# htmlElem.send_keys(Keys.HOME)

# 单击浏览器按钮: 模拟单击各种浏览器按钮
browser.back()
browser.forward()
browser.refresh()
browser.quit()

