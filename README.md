# Modular modpack manifest.json Generator
A small python script that automatically generates a `manifest.json` file for you simply from folders and empty files.  
It automatically downloads the latest release of forge and each mod for your desired Minecraft version.

## Difference
This is a fork of the [modpack-manifest-generator](https://github.com/jadc/modpack-manifest-generator).

That generator uses a single list file, called `mods.txt`, with each mod id on a new line.  
This generator reads individual file names in a folder.

The advantage of this method is to allow collaboration by multiple people. Rather than attempting to merge multiple changes into a single file, all you have to do is create or delete standalone files.

tl;dr: If you are making a modpack by yourself, the original [modpack-manifest-generator](https://github.com/jadc/modpack-manifest-generator) will work fine for you. If you are making a modpack with other people, this generator will save you a lot of headaches.

## Instructions
An example modpack is included to guide you.

1. Navigate to the `mods` folder. Create a new folder if you want to organize, otherwise create a new text document. (extension does not matter)
2. Name the new text document the project ID of each mod you want.  
   ![Project ID](https://i.imgur.com/sSSJuMi.png)

3. Edit `manifest-template.json` to your liking. Ensure `version` is set to the desired Minecraft version of the modpack.  
   a. If you are planning to have an overrides folder, add `"overrides": "overrides"`

4. Generate the manifest.json by double-clicking `generate.py` with Python installed.  
   *(alternatively, run it in terminal if you know how)*

5. A manifest.json should now be in the directory.  
   Move that to your modpack folder, zip it up, and your modpack should import into MultiMC perfectly.

## Download
There are no compiled releases. Clone or download the source.
