import requests
import subprocess
import os

ACCEPT_PRERELEASE = False

res = requests.get("https://api.github.com/repos/Anuken/Mindustry/releases").json() 

home = os.path.expanduser("~")

RELEASE = {}

print("searching for releases")

for release in res:
    is_prerelease = release.get("prerelease")
    if ACCEPT_PRERELEASE == is_prerelease:
        RELEASE = release

print("found release -> "+RELEASE.get("name"))
file_name = home +"/"+ RELEASE.get("tag_name").replace(".", "_")+".jar"
if not os.path.isfile(file_name):
    for assets in RELEASE.get("assets"):
        if assets.get("name").startswith("server"):
            print("server file found")
            subprocess.call(["python3", "-m", "httpie", "get", "--follow", "--Output="+file_name, assets.get("browser_download_url")])
            break
    print("finished download")

else: 
    print("already up to date")

print("starting server...")
subprocess.call(["sudo", "java", "-jar", file_name])
subprocess.call(["sudo", "poweroff"])
