#Taken from RealistikPanel
#the purpose of this file has changed to be a quick config fetcher
import json
from os import path
from colorama import init, Fore


init() #Colorama thing
DefaultConfig = {
    "Port" : 80,
    #SQL Info
    "SQLHost" : "localhost",
    "SQLUser" : "root",
    "SQLDatabase" : "GDPyS",
    "SQLPassword" : "",
    "Chest1Wait" : 60,
    "Chest2Wait" : 240,
    "CronThreadDelay" : 3600,
    "LocalServer" : False,
    "LegacyPasswords" : False, #cvolton gmdprivateserver passwords if true, bcrypt if false
    "CheatlessAC" : True, #global switch
    "CheatlessExtremeDemonMinAttempts" : 100, #if a user submits an extreme demon score under this att count, they will be banned
    "CheatlessScoreCheck" : True,
    "CheatlessCronChecks" : True,
    "CheatlessMaxStars" : 5000
}

class JsonFile:
    @classmethod
    def SaveDict(self, Dict, File):
        """Saves a dict as a file"""
        with open(File, 'w') as json_file:
            json.dump(Dict, json_file, indent=4)

    @classmethod
    def GetDict(self, file):
        """Returns a dict from file name"""
        if not path.exists(file):
            return {}
        else:
            with open(file) as f:
                data = json.load(f)
            return data

UserConfig = JsonFile.GetDict("config.json")
#Config Checks
if UserConfig == {}:
    print(Fore.YELLOW+" No config found! Generating!"+Fore.RESET)
    JsonFile.SaveDict(DefaultConfig, "config.json")
    print(Fore.WHITE+" Config created! It is named config.json. Edit it accordingly and start the server again!")
    exit()
else:
    #config check and updater
    AllGood = True
    NeedSet = []
    for key in list(DefaultConfig.keys()):
        if key not in list(UserConfig.keys()):
            AllGood = False
            NeedSet.append(key)

    if AllGood:
        print(Fore.GREEN+" Configuration loaded successfully! Loading..." + Fore.RESET)
    else:
        #fixes config
        print(Fore.BLUE+" Updating config..." + Fore.RESET)
        for Key in NeedSet:
            UserConfig[Key] = DefaultConfig[Key]
            print(Fore.BLUE+f" Option {Key} added to config. Set default to '{DefaultConfig[Key]}'." + Fore.RESET)
        print(Fore.GREEN+" Config updated! Please edit the new values to your liking." + Fore.RESET)
        JsonFile.SaveDict(UserConfig, "config.json")
        exit()