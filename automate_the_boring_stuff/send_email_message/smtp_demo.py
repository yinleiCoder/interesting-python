import smtplib
"""
SMTP:
    SMTP是用于发送电子邮件的协议，规定了电子邮件该如何格式化、加密、在邮件服务器之间传递，以及在单击发送后，计算机要处理的所有细节。
    SMTP只负责向别人发送电子邮件，IMAP负责取回发送给你的电子邮件。
    aoxoodxlisupifej(授权码)

    发送邮件服务器：smtp.qq.com，使用SSL，端口号465或587
    账户名：您的QQ邮箱账户名（如果您是VIP帐号或Foxmail帐号，账户名需要填写完整的邮件地址）
    密码：您的QQ邮箱密码
    电子邮件地址：您的QQ邮箱的完整邮件地址
"""

smtpObj = smtplib.SMTP('smtp.qq.com', 587)
# smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
print(smtpObj)
# 建立链接
print(smtpObj.ehlo())# 返回250代表成功
# TLS加密（465端口不需要）
print(smtpObj.starttls())# 220代表服务器准备就绪
# 登录smtp服务器
print(smtpObj.login('1099129793@qq.com', 'aoxoodxlisupifej'))#235表示认证成功

# 发送电子邮件
print(smtpObj.sendmail('1099129793@qq.com', ['1099129793@qq.com'], 'Subject: Hi!\ni am yinlei!'))

# 断开链接
smtpObj.quit()# 221表示会话结束

