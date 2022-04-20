from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
import json, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = '\\'.join([ROOT_DIR, 'config.json'])
# read config file
with open(config_path) as config_file:
    config = json.load(config_file)
    config = config['share_point']
USERNAME = config['user']
PASSWORD = config['password']
SHAREPOINT_URL = config['url']
SHAREPOINT_FOLDER = config['folder']

print(SHAREPOINT_FOLDER)

auth = AuthenticationContext(SHAREPOINT_URL) 
auth.acquire_token_for_user(
    USERNAME, PASSWORD)
ctx = ClientContext(SHAREPOINT_URL, auth)
web = ctx.web
ctx.load(web)
ctx.execute_query()
print('Connected to SharePoint: ',web.properties['Title'])


def folder_details(ctx, SHAREPOINT_FOLDER):  
    folder = ctx.web.get_folder_by_server_relative_url(SHAREPOINT_FOLDER)  
    fold_names = []  
    sub_folders = folder.files   
    ctx.load(sub_folders)  
    ctx.execute_query()  
    for s_folder in sub_folders:    
        fold_names.append(s_folder.properties["Name"]) 
    return fold_names

print("file name :", folder_details(ctx, SHAREPOINT_FOLDER))


dir = "C:\\Users\\kaddi\\Downloads\\"
name = "Data workflow.csv_05_04.xlsx"

with open(dir+name, 'rb') as content_file:
    file_content = content_file.read()

#def upload(ctx, )
file = web.get_folder_by_server_relative_url(SHAREPOINT_FOLDER).upload_file(name, file_content).execute_query()

