import shutil
import py7zr
import os
import requests
components	= """[
  "net:base",
  "net:tcp-server",
  "net:http-server",
  "citizen:server:net",
  "citizen:scripting:core",
  "citizen:scripting:lua",
  "citizen:scripting:lua54",
  "conhost:server",
  "citizen:server:main",
  "citizen:server:instance",
  "citizen:server:monitor",
  "citizen:server:impl",
  "citizen:server:state:fivesv",
  "citizen:server:state:rdr3sv",
  "citizen:server:fxdk",
  "citizen:devtools",
  "citizen:resources:core",
  "citizen:resources:metadata:lua",
  "vfs:core",
  "vfs:impl:server",
  "scripting:server",
  "citizen:scripting:mono",
  "citizen:scripting:v8node",
  "voip-server:mumble",
  "http-client",
  "citizen:server:gui"
]"""


cfg =  """# Only change the IP if you're using a server with multiple network interfaces, otherwise change the port only.
endpoint_add_tcp "0.0.0.0:30120"
endpoint_add_udp "0.0.0.0:30120"

# These resources will start by default.
ensure mapmanager
ensure chat
ensure spawnmanager
ensure sessionmanager
ensure basic-gamemode
ensure hardcap
ensure rconlog
# This allows players to use scripthook-based plugins such as the legacy Lambda Menu.
# Set this to 1 to allow scripthook. Do note that this does _not_ guarantee players won't be able to use external plugins.
sv_scriptHookAllowed 0

# Uncomment this and set a password to enable RCON. Make sure to change the password - it should look like rcon_password "YOURPASSWORD"
#rcon_password ""

# A comma-separated list of tags for your server.
# For example:
# - sets tags "drifting, cars, racing"
# Or:
# - sets tags "roleplay, military, tanks"
sets tags "default"

# A valid locale identifier for your server's primary language.
# For example "en-US", "fr-CA", "nl-NL", "de-DE", "en-GB", "pt-BR"
sets locale "root-AQ" 
# please DO replace root-AQ on the line ABOVE with a real language! :)

# Set an optional server info and connecting banner image url.
# Size doesn't matter, any banner sized image will be fine.
#sets banner_detail "https://url.to/image.png"
#sets banner_connecting "https://url.to/image.png"

# Set your server's hostname. This is not usually shown anywhere in listings.
sv_hostname "Impulse RolePlay "

# Set your server's Project Name
sets sv_projectName "My FXServer Project"

# Set your server's Project Description
sets sv_projectDesc "Default FXServer requiring configuration"

# Nested configs!
#exec server_internal.cfg

# Loading a server icon (96x96 PNG file)
load_server_icon myLogo.png

# convars which can be used in scripts
set temp_convar "hey world!"

# Remove the `#` from the below line if you want your server to be listed as 'private' in the server browser.
# Do not edit it if you *do not* want your server listed as 'private'.
# Check the following url for more detailed information about this:
# https://docs.fivem.net/docs/server-manual/server-commands/#sv_master1-newvalue
#sv_master1 ""

# Add system admins
add_ace group.admin command allow # allow all commands
add_ace group.admin command.quit deny # but don't allow quit
add_principal identifier.fivem:1 group.admin # add the admin to the group

# enable OneSync (required for server-side state awareness)
set onesync on

# Server player slot limit (see https://fivem.net/server-hosting for limits)
sv_maxclients 48
set sv_lan 1


# Steam Web API key, if you want to use Steam authentication (https://steamcommunity.com/dev/apikey)
# -> replace "" with the key
set steam_webApiKey "D32EAF76AB9FBED824F3A6C4D2626B0F"

# License key for your server (https://keymaster.fivem.net)
sv_licenseKey changeme"""


location = input("where do you want the artifact to be located ? :  \n(drag and drop the folder here) --> ") ##### location of the artifact



response = requests.get("https://runtime.fivem.net/artifacts/fivem/build_server_windows/master/5848-4f71128ee48b07026d6d7229a60ebc5f40f2b9db/server.7z")

# Save the downloaded file to disk
with open(f"{location}\\artifact.7z", "wb") as f:
    f.write(response.content)

# Extract the contents of the 7zip file
with py7zr.SevenZipFile(f"{location}\\artifact.7z", mode='r') as z:
    z.extractall(location)


os.remove(f"{location}\\artifact.7z") #####deleting the zip file downloaded
os.remove(f"{location}\\components.json")

with open (f"{location}\\components.json","w") as f:
	f.write(components)
os.remove(f"{location}\\svadhesive.dll")
with open (f"{location}\\server.cfg","w") as f:
	f.write(components)
os.system(f"start {location}\\FXServer.exe")




