import pickle
import smtplib
import imaplib
import ssl
import email
from email.message import EmailMessage

class Lib:
    EMAIL_ADDRESS = "youremailaddress@163.com"#you can also use other mail website
    EMAIL_PASSWORD = "123321"#your iamp/smtp code, you will find it on your own mail website 

    def send(self, subject, content):
        # smtp = smtplib.SMTP("smtp.163.com", 25)
        context = ssl.create_default_context()
        smtp = smtplib.SMTP_SSL("smtp.163.com", 465, context = context)
        sender = self.EMAIL_ADDRESS
        receiver = self.EMAIL_ADDRESS
        filename = "pk.pickle"
        
        with open('sd' + filename, "wb+") as f:
            pickle.dump(content, f)
        with open('sd' + filename, "rb") as f:
            filedata = f.read()

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        msg.add_attachment(filedata, maintype='pickle', subtype='pickle', filename=filename)


        smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
        smtp.send_message(msg)

        smtp.quit()
    

    def recv(self):
        recv = {}
        server = imaplib.IMAP4_SSL(host='imap.163.com', port=993)
        # command 
        imaplib.Commands['ID'] = ('NONAUTH', 'AUTH', 'SELECTED')
        args = ('name', 'imaplib', 'version', '1.0.0')
        typ, dat = server._simple_command('ID', '("' + '" "'.join(args) + '")')

        server.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
        server.select("Inbox")
        try:
            typ, data = server.search(None, 'UNSEEN')
        except:
            return None

        fetch_data_list = []
        for num in data[0].split():
            typ, fetch_data = server.fetch(num, '(RFC822)')
            fetch_data_list.append(fetch_data)
        
        for i in range(len(fetch_data_list)):
            msg = email.message_from_bytes(fetch_data_list[i][0][1])
            if msg['From'] != self.EMAIL_ADDRESS:
                continue
            for part in msg.walk():
                if part.get_content_maintype() == "pickle":
                    filename = part.get_filename()
                    content = part.get_payload(decode=True)
                    with open('rc' + filename, 'wb+') as f:
                        f.write(content)
                    with open('rc' + filename, 'rb') as f:
                        recv[msg['Subject']] = pickle.load(f)
        
        server.close()
        server.logout()
        return recv
        