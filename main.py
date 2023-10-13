import makerbot, oldservermaker
import time
from subprocess import check_output


def autoSetup():
    GenerateStartup()
    
    runner = True
    while runner:
        print("Attempting to Start jar file")
        print("please type Stop into console to finish")
        output= check_output(['java', '-jar', 'server.jar'])
        decoded = output.decode()
        print(decoded + "\n\n\n")
        if decoded.find("You need to agree to the EULA in order to run the server") != -1:
            file = open("eula.txt","r")
            hold =file.read()
            file.close()
            run = True
            while run:
            
                try:
                    choice = int(input(hold + "\nDo you agree to the Eula\n1.yes\n2.no\n>"))
                    if (choice == 1):
                        run = False
                        print("Accepting Eula")
                        file = open("eula.txt","w")
                        hold = hold.replace("false","true")
                        print(hold)
                        file.write(hold)
                        file.close()
                    elif (choice ==2):
                        print("you can't proceed with setting up Mincraft")
                        return False
                        
                except Exception as e:
                    
                    print("\nnot a valid choice\n")
                time.sleep(1)
        else:
            print("\nSuccess your server runs... Exiting\n")
            run = False
            runner = False

def ChangeConfig():
    run = True
    while run:
        try:
            choice = int(input("\n1.Lagacy Creation config file(long)\n2.Search file\n3.Exit\n>"))
            if choice == 1:
                oldservermaker.config()
                
            elif choice == 2:
                search =input("Search Property?")
                file = open("server.properties","r")
                find = file.read().split("\n")
                index = -1
                file.close()
                for i in range(0,len(find)):
                    if find[i].find(search) != -1:
                        index = i
                
                if index == -1:
                    print("not found")
                else:
                    print(find[index] + "\nedit?\n")
                    edit = input(">")
                    find[index] = find[index].split("=")[0] + "=" + edit
                    print(find[index])
                    print("Writting")
                    file = open("server.properties","w")
                    for item in find:
                        file.write(item + "\n")
                    file.close()                
                
            elif choice == 3:
                run = False
        except:
            print("\nnot valid\n")

def GenerateStartup():
    #get ram in gigabytes
    rama =oldservermaker.getSystemRam()
    ramamount = int(rama * 0.3 * 1024)
    print("using recommend size of " + str(ramamount) + "M")
    batch = "echo starting server\njava -Xmx" + str(ramamount) + "M -jar server.jar\necho server stopped"
    from sys import platform
    if platform == "win32":
        # Windows...
        file = open("run.bat","w")
        file.write(batch)
        file.close()
    else:
        # linux etc..?
        file = open("run.sh","w")
        file.write(batch)
        file.close()
    
    
    

def main():
    run = True
    while run:
        
        try:
            choice = int(input("1.output all Minecraft versions\n2.slient Load\n>"))
            if (choice == 1):
                run = False
                ClassRunner = makerbot.MakerBot(False)
            elif (choice ==2):
                run = False
                ClassRunner = makerbot.MakerBot(True)
                
        except Exception as e:
            
            print("\nnot a valid choice\n")
        time.sleep(1)

    run = True
    while run:
        try:
            choice = int(input("\n1.AutoSetup\n2.ChangeConfig\n3.StartupMaker\n4.Exit\n>"))
            if (choice ==1):
                autoSetup()
            elif (choice ==2):
                print("not in use")
                
            elif (choice ==3):
                GenerateStartup()
            elif (choice ==4):
                run = False
                quit()
                        
        except Exception as e:
            print("\nnot a valid choice\n")
            print(e)
        time.sleep(1)
        


#runs main class
main()

