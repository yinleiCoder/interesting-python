import pprint

import imapclient
"""
IMAP:
    因特网消息访问协议IMAP规定了如何与电子邮件服务器提供商的服务通信，取回发送到你的电子邮件地址的邮件。
    python自带imaplib，但imapclient第三方更好用

    imapclient从IMAP服务器下载电子邮件，格式相当复杂。很可能希望将他们从这种格式转换为简单的字符串，
    pyzmail可以替我们完成解析这些邮件。

    接收邮件服务器：imap.qq.com，使用SSL，端口号993

pip install imapclient
pip install pyzmail36
"""
# 链接到imap服务器
imapObj = imapclient.IMAPClient('imap.qq.com', ssl=True)
# 登录到imap服务器
print(imapObj.login('1099129793@qq.com', 'aoxoodxlisupifej'))
# 选择文件夹
pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)
# 执行搜索
"""
IMAP搜索键：
ALL 返回该文件夹中的所有邮件
BEFORE date
ON date         返回给定date之前、当天、之后
SINCE date

SUBJECT string 
BODY string     返回string出现在主题、正文、主题或正文中的消息
TEXT string 

FROM string
TO string
CC string
BCC ssring

SEEN 
UNSEEN

ANSWERED
UNANSWERED

DRAFT
UNDRAFT

FLAGGED
UNFLAGGED

LARGER N
SMALLER N

NOT searchkey
OR search key1search key2
"""
UIDS = imapObj.search(['ALL'])
print(UIDS)
# 解除搜索匹配的大小限制
imapObj._MAXLINE = 10000000
# 取邮件并标记为已读
rawMessages = imapObj.fetch(UIDS, ['BODY[]'])
pprint.pprint(rawMessages)

# fetch返回的是字典，包含BODY[]、SEQ键，BODY[]键的消息内容格”式是RFC822，专门为IMAP服务器读取而设计的。需要使用pyzmail模块来解析。
# 删除电子邮件可以用delete_messages()并调用expunge永久删除电子邮件

# 从IMAP服务器断开
imapObj.logout()


