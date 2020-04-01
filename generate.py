# Modpack manifest.json Generator
# by Jad Chehimi

import requests
import json

# Prepare headers with unique user-agent
headers = {'User-Agent': 'modmanifestgen'}

# Reads manifest template
with open('manifest-template.json') as m:
    manifest = json.load(m)

# Check if version is configured in manifest
if manifest['minecraft']['version'] == '':
    print('Error. There is no Minecraft version specified in the manifest.json')
    exit()

# Determines latest forge modloader version depending on mc version
modLoaderData = requests.get('https://addons-ecs.forgesvc.net/api/v2/minecraft/modloader', headers=headers)
for key in modLoaderData.json():
    if(key['latest'] == True):
        if(key['gameVersion'] == manifest['minecraft']['version']):
            modLoaders = []
            modLoaders.append({"id":key['name'], "primary":True})
            manifest['minecraft']["modLoaders"] = modLoaders

# Reads mod list
i = open('mods.txt')

# Prepares output file
mods = {
    'files': []
}

# If a mod fails to get added, add it to a queue to be logged at the end
failureQueue = []

# For every mod id
for projectID in i:
    # API GET Request
    data = requests.get('https://addons-ecs.forgesvc.net/api/v2/addon/' + projectID, headers=headers).json()

    # Gets mod name
    modname = data['name']

    # Used to check if mod was successfully added
    buildExists = False

    # Gets file id for latest build in desired mc version
    for key in data['gameVersionLatestFiles']:
        # If mod has desired mc version
        if key['gameVersion'] == manifest['minecraft']['version']:
            # Prepares json for mod
            mod = {}
            mod['!'] = modname + ' (' + key['projectFileName'] + ')'
            mod['projectID'] = int(projectID)
            mod['fileID'] = key['projectFileId']
            mod['required'] = True

            mods['files'].append(mod)
            print('Added \'' + modname + '\' for MC ' + key['gameVersion'] + ' (' + key['projectFileName'] + ')')
            buildExists = True
            break
    
    if buildExists != True:
        failureQueue.append(modname)

# Logs mods that don't have a build for the desired version
if failureQueue:
    print('\nThe following mods lack a build for MC ' + manifest['minecraft']['version'] + ', and were not added.')
    print(failureQueue)

# Add files object to manifest
manifest['files'] = mods['files']

# Output manifest json to file (with beautify)
with open('manifest.json', 'w') as o:
    json.dump(manifest, o, sort_keys=True, indent=4)

print('Done. Press ENTER to close this window.')

# Pause to allow viewing of logs
input()