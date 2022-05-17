from twilio.rest import Client
"""
Twilio发送短信：
    利用SMS短信服务、MMS多媒体消息服务需要查找运营商的SMS网关、MMS网关。
    但使用非电子邮件短信网关服务更可靠。
    Twilio是一个SMS网关服务，让我们通过程序发送短信。
    pip install twilio
    https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1

    accountSID: ACc9cce1d61af6d7753ac5a8f88dff0ee0
    authTOKen: a34b209345bd456cf7a4c798e03131ef
    TwilioNumber:+17579934567
    myCellPhone: +86 137 9595 0539
"""
accountSID = 'ACc9cce1d61af6d7753ac5a8f88dff0ee0'
authToken = 'a34b209345bd456cf7a4c798e03131ef'
twilioCil = Client(accountSID, authToken)
myTwilioNumber = '+17579934567'
myCellPhone = '+8613795950539'
message = twilioCil.messages.create(body='Mr Yin - Come here - I miss you.', from_=myTwilioNumber, to=myCellPhone)
print(message.to)
print(message.from_)
print(message.body)
print(message.status)
print(message.date_created)
print(message.date_sent == None)
print(message.sid)
updatedMessage = twilioCil.messages.get(message.sid)
print(updatedMessage.status)
print(updatedMessage.date_sent)