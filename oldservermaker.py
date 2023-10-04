import os,requests
import concurrent.futures

def serverstart():
    print("starting batch script")
    import subprocess
    subprocess.call([r'run.bat'])
    

def download(url):
    try:
        get_response = requests.get(url,stream=True)
        file_name  = url.split("/")[-1]
        with open("server.jar", 'wb') as f:
            for chunk in get_response.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        print("download done")
        return 0
    except:
        print("download failed")
        return 1
        

def versionfinder():
   global version
   if version == "1.16.2":
       return "https://launcher.mojang.com/v1/objects/c5f6fb23c3876461d46ec380421e42b289789530/server.jar"
   if version == "1.16.1":
       return "https://launcher.mojang.com/v1/objects/a412fd69db1f81db3f511c1463fd304675244077/server.jar"
   if version == "1.16":
       return "https://launcher.mojang.com/v1/objects/a0d03225615ba897619220e256a266cb33a44b6b/server.jar"
   else:
       print("currently not stored as script is in alpha")
       return "n"


def getSystemRam():
    import platform,socket,re,uuid,json,psutil,logging
    try:
        return int(round(psutil.virtual_memory().total / (1024.0 **3)))
    except Exception as e:
        logging.exception(e)

def web(url):
    try:
        import webbrowser
        webbrowser.open(url, new=0, autoraise=True)
    except:
        print("problem opening website")

def eulamaker():
    file = open("eula.txt","w")
    content = "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#Mon Aug 17 19:04:18 BST 2020\neula=True"
    file.write(content)
    file.close()
    
def config():
    global port,  serverip
    file = open("server.properties","w")
    print("tool loaded")
    run = True
    while run == True:
        try:
            spawnp = str("spawn-protection=" + str(int(input("how many block of spawn do you want protected? "))) + "\n")
            tickmax =  "max-tick-time=60000\n"
            port = str(int(input("what is the port number of server default minecraft server is 25565 > ")))  + "\n"
            qport = "querry.port =" + str(port)
            generator = "generator-setting=\n"
            sync = "sync-chunk-writes=true\n"
            force = "force-gamemode=false"
            nether = "allow-nether="+ str(input("allow nether?\nwrite false to disable\nwrite true to enable\n > ") + "\n")
            enforcwhitelist = "enforce-whitelist=false\n"
            gamemode = "force-gamemode=false\n"
            console = "broadcast-console-to-ops=" + str(input("would you like to broadcast console to operators/op?\nwrite true to enable\nwrite false to disable\n > "))+ "\n"
            enqury = "enable-query=false\n"
            monsters = "spawn-monsters=" + str(input("would you like to spawn monsters?\nwrite true to enable\nwrite false to disable\n > ")) + "\n"
            broadron = "broadcast-rcon-to-ops=true\n"
            oppremission = "op-permission-level=" + str(4) + "\n"
            pvp = "pvp=" + str(input("would you like pvp?\nwrite true to enable\nwrite false to disable\n > ")) + "\n"
            enitbroad = "entity-broadcast-range-percentage=100\n"
            difficulty = "difficulty=" + str(input("what difficulty would you want?\nwrite 0 for peaceful\nwrite 1 for easy\nwrite 2 for medium\nwrite 3 for hard\n  > ")) + "\n"
            playeridletimeout = "player-idle-timeout=0" + "\n"
            snooper = "snooper-enable=true" + "\n"
            level = "level-type=" + input("what level type would you want? superflat or default? ") + "\n"
            enablestatus = "enablestatus=true\n"
            hardcore = "hardcore=" + str(input("active hardcore?\nwrite false to disable\nwrite true to enable\n > "))+ "\n"
            commandblock = "enable-command-block=" + str(input("allow commandblock?\nwrite false to disable\nwrite true to enable\n > "))+ "\n"
            playersize = "max-player=" + str(input("how many player allowed to join recommended for normal system 10-20? ")) + "\n"
            networkcompressionthreshold = "network-compression-threshold=256" + "\n"
            worldsize = "max-world-size=29999984\n"
            resourcepacksha1= "resource-pack-sha1=\n"
            funcpre = "function-permission-level=2\n"
            rconport = "rcon.port=25575" + "\n"
            serverport = "server-port=" + str(port) + "\n"
            import socket
            serverip = "server-ip=" +  str(socket.gethostbyname(socket.gethostname())) + "\n"
            npc = "spawn-npcs="+ str(input("allow spawning of npcs?\nwrite false to disable\nwrite true to enable\n > "))+ "\n"
            flight = "allow-flight="  + str(input("allow flight in none creative can be unstable?\nwrite false to disable\nwrite true to enable\n > "))+ "\n"
            levelname = "level-name=world\n"
            viewdistance = "view-distance=" + str(input("what view distance do you want on server recommended for normal system 10-20? ")) + "\n"
            resourcepack= "resource-pack=\n"
            spawnanimal = "spawn-animal=" + str(input("allow spawning of animals?\nwrite false to disable\nwrite true to enable\n > "))+ "\n"
            whitelist = "whitelist=false\n"
            rpass = "rcon.password=\n"
            generatestruc = "generate-structures=" + str(input("allow generating of structures?\nwrite false to disable\nwrite true to enable\n > "))+ "\n"
            onlinemode = "online-mode=" + str(input("disable or enable online mode this will allow if disabled cracked accounts but allows game to run without internet?\nwrite false to disable\nwrite true to enable\n > "))+ "\n"
            maxbuild = "max-build-height=256\n"
            levelseed = "level-seed=" + input("what is the seed? ") + "\n"
            proxy = "prevent-proxy-conenctions=false\n"
            unt = "use-native-transport=true\n"
            enablejmx = "enable-jmx-monitoring=false\n"
            motd = "motd=" + input("what is the moto of the server? ") + "\n"
            enablercon = "enable-rcon=false\n"
            final = spawnp + tickmax + qport + generator + sync  + force +  nether + enforcwhitelist + gamemode + console + enqury + playeridletimeout + difficulty +broadron+monsters+oppremission+pvp+enitbroad+snooper+level+enablestatus+hardcore+commandblock+playersize+networkcompressionthreshold+worldsize+resourcepacksha1
            final =  final + funcpre +rconport + serverport +serverip+npc+flight+levelname+viewdistance+resourcepack+spawnanimal+whitelist+rpass+generatestruc+onlinemode+maxbuild+levelseed+proxy+unt+enablejmx+motd+enablercon
            print("generating properties file")
            print(final)
            file.write(final)
            run = False
            
            
                     
        except:
            print("invaild")
        file.close()


def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

def ipconfig():
    print("opening ipconfig script")
    file = open("ipconfig.bat","w")
    file.write("c:\windows\system32\ipconfig\necho gateway is what you need\npause")
    file.close()
    import subprocess
    subprocess.call([r'ipconfig.bat'])
     
        
def portforwarding():
    global port, serverip
    print("\n\n")
    print("this is the hard part")
    print("because I am one person who lives in one country I can't say what your router port forwarding looks like")
    print("but i can give you default gateway and a checker and search youtube.")
    choice= input("before that do you just want lan only? if so you can skip to starting the server?\n1.yes\n2.no\n> ")
    if choice == "1":
        print("okay")
    else:
        runport = True
        while runport == True:
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                routername = input("what is your routers name? ")
                print("your port number is " + str(port))
                print("your local ip is " + str(serverip))
                web("https://www.youtube.com/results?search_query=" + routername + "+portforwarding")
                executor.submit(ipconfig)
                input("hit enter to continue...")
                print("\n\n")
                runport = False

       
def startup():
    global version, port
    print("hello lets start off with somethings.")
    print("\n")
    print("forge/craftbucket/beta and alpha autocomplete is not in this version of script")
    print("format e.g 1.16.2, 1.9.")
    print("\n")
    run = 1
    while run == 1:
        version = input("what version of minecraft are you playing? ")
        print("\n\n")
        print("starting download don't close program...")
        result = versionfinder()
        if result == "n":
            print("not vaild version")
            print("\n")
        else:
            print("version found " + version)
            run = download(result)
            print("\n\n")
    print("making batch launcher for server")
    print("calculating recommend ram")
    rama = getSystemRam()
    ramamount = int(rama * 0.425 * 1024)
    print("using recommend size of " + str(ramamount) + "M")
    batch = "echo starting server\njava -Xmx" + str(ramamount) + "M -Xms512M -jar server.jar\necho server stopped"
    file = open("run.bat","w")
    file.write(batch)
    file.close()
    print("done eula required")
    run = True
    while run == True:
        print("\n\n")
        agree = input("do you agree to mojang eula.\nplease write yes\nto see eula type web.\n> ")
        if agree == "no":
            run = False
            quit
        if agree == "web":
            web("https://account.mojang.com/documents/minecraft_eula")
        if agree == "yes":
            eulamaker()
            run = False
    print("time to config worlds and options")
    print("starting configuation tool")
    config()
    print("laststep port forwarding ")
    portforwarding()
    print("your ready to start")
    print("\n\n\n\n")
    

try:
    f = open("server.jar","r")
    f.close()
    input("press enter to start server....")
    serverstart()
    print("server stopped")
    quit
except:
    startup()





