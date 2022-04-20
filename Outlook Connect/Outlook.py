from numpy import rint
import win32com.client
import pandas as pd 


# set up connection to outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6)

# Access to the email in the inbox
messages = inbox.Items


message = messages.GetLast()

print(message.subject) # get the subject of the email
print(message.senton.date())
print(message.senton.time())
print("*****************************")
print(message.sender)
print("******************")

attachments = message.Attachments
for attachment in attachments:
    print(attachment.FileName)
    attachment.SaveAsFile("C:\\Users\\kaddi\\Downloads"+ '\\'  + attachment.FileName)
    print("successfully saved !")


