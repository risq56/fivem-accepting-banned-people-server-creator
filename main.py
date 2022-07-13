import wget 
import shutil
import zipfile
import os
import requests
location = input("where do you want the artifact to be located ? : \n") ##### location of the artifact


response = requests.get("https://pastebin.com/raw/9wTUbr9q")
content = response.text


url = content  #######this is the url of the artifact do not touch unless you know what you're doing :)
r = requests.get(url, stream=True) #########downloading the artifact
if r.status_code == 200:
    with open("artifact.zip", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
        ##########downloading the artifact

shutil.move("artifact.zip", location)###### moving the artifact
with zipfile.ZipFile(f"{location}\\artifact.zip","r") as zip_ref:
    zip_ref.extractall(location)
os.remove(f"{location}\\artifact.zip") #####deleting the zip file downloaded
os.remove(f"{location}\\components.json")
wget.download("https://pastebin.com/raw/NsqrSGAj" , f"{location}\\components.json")
os.remove(f"{location}\\svadhesive.dll")
os.remove(f"{location}\\server.cfg")
wget.download("https://pastebin.com/raw/S15h9VUP" , f"{location}\\server.cfg")





