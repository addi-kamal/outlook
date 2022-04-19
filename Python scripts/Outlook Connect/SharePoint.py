from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File


sharepoint_user = 'kaddi@afdtech.com'
sharepoint_password = 'Kubart1@3adi'



#https://hartwoodsa.sharepoint.com/sites/TEST155/Shared%20Documents/General/
sharepoint_base_url = 'https://hartwoodsa.sharepoint.com/sites/TEST155/'

folder_in_sharepoint = '/sites/TEST155/Shared%20Documents/General/'

auth = AuthenticationContext(sharepoint_base_url) 
auth.acquire_token_for_user(
    sharepoint_user, sharepoint_password)
ctx = ClientContext(sharepoint_base_url, auth)
web = ctx.web
ctx.load(web)
ctx.execute_query()
print('Connected to SharePoint: ',web.properties['Title'])


def folder_details(ctx, folder_in_sharepoint):  
    folder = ctx.web.get_folder_by_server_relative_url(folder_in_sharepoint)  
    fold_names = []  
    sub_folders = folder.files   
    ctx.load(sub_folders)  
    ctx.execute_query()  
    for s_folder in sub_folders:    
        fold_names.append(s_folder.properties["Name"]) 
    return fold_names
print("hhhhhh")
print(folder_details(ctx, folder_in_sharepoint))



'''
dir = "C:\\Users\\kaddi\\Downloads"
name = "Data workflow.csv_05_04.xlsx"

with open(dir+name, 'rb') as content_file:
    file_content = content_file.read()


file = web.get_folder_by_server_relative_url(dir).upload_file(name, file_content).execute_query()

'''