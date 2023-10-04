import requests
import json
import os
import time


manifest = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
output = requests.get(manifest)
better = json.loads(output.text)
better["versions"]


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class MakerBot:
    def PrintGettingVersionJson(self):
        self.JsonLookup = []
        for ids in self.FileJson["versions"]:
            StoreVer = (ids["id"])
            StoreUrl = (ids["url"])
            print("Version: " + StoreVer)
            self.JsonLookup.append([StoreVer,StoreUrl])

    def GettingVersionJson(self):
        self.JsonLookup = []
        for ids in self.FileJson["versions"]:
            StoreVer = (ids["id"])
            StoreUrl = (ids["url"])
            self.JsonLookup.append([StoreVer,StoreUrl])
            
    def LocateJarUrl(self):
        output = requests.get(self.ServerJarUrl)
        self.VerJson = json.loads(output.text)
        #print(self.ServerJarUrl)
        #print(self.VerJson.keys())
        self.ServerJarDownload = self.VerJson['downloads']['server']['url']
        
        
    def DownloadServerJar(self):
        query_parameters = {"downloadformat": "jar"}
        response = requests.get(self.ServerJarDownload, params=query_parameters)
        print("Please Wait Downloading Jar!")
        with open("server.jar", mode="wb") as file:
            file.write(response.content)
        print("\n\n\n\n")
        cls()
        print("download Compeleted")
        print("You must manually download java Version " + str(self.VerJson['javaVersion']['majorVersion']))
        return False

    def FindVersionInJson(self):
        for Vers in self.JsonLookup:
            if self.jarVer.lower() == Vers[0]:
                self.jarVer = Vers[0]
                self.ServerJarUrl = Vers[1]
                return True
        print("can't find any versions")
        return False

    
    def __init__(self,slient):
        run = True
        manifest = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
        output = requests.get(manifest)
        self.FileJson = json.loads(output.text)
        if (slient == False):
            self.PrintGettingVersionJson()
        else:
            self.GettingVersionJson()
        while run:
            try:
                self.jarVer =input("Server Jar Version\n--Type 'latest' for newest version--\n--Type 'show' for to see all versions--\n>").lower()
                if (self.jarVer == "latest"):
                    self.jarVer = self.JsonLookup[0][0]
                    self.ServerJarUrl = self.JsonLookup[0][1]
                    self.LocateJarUrl()
                    run = self.DownloadServerJar()
                    
                elif (self.jarVer.lower() == 'show'):
                    self.PrintGettingVersionJson()
            
                else:
                    self.FindVersionInJson()
                    self.LocateJarUrl()
                    run = self.DownloadServerJar()
                
            except Exception as e:
                print(e)
                print("Could not find any server jars for this version")

        print("inital Download Complete :3")
        

def main():
    run = True
    while run:
        
        try:
            choice = int(input("1.output all Minecraft versions\n2.slient Load\n>"))
            if (choice == 1):
                run = False
                ClassRunner = MakerBot(False)
            elif (choice ==2):
                run = False
                ClassRunner = MakerBot(True)
        except Exception as e:
            print("\nnot a valid choice\n")
        time.sleep(1)


#runs main class
main()
