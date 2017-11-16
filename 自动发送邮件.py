import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '1486373118@qq.com'
msg['to'] = '2915912248@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com', '25')
smtp.login('1486373118@qq.com', 'qwe1230')
smtp.sendmail('1486373118@qq.com', '2915912248@qq.com', str(msg))
smtp.quit()