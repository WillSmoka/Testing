### The only import you need!
import socket
 
### Options (Don't edit)
SERVER = "irc.twitch.tv"  # server
PORT = 6667  # port
### Options (Edit this)
PASS = "oauth:lquub6pbgnq3pjusnwk18p8rbjfvf3"  # bot password can be found on https://twitchapps.com/tmi/
BOT = "masoqueeisso"  # Bot's name [NO CAPITALS]
CHANNEL = "axtlol"  # Channal name [NO CAPITALS]
OWNER = "axtlol"  # Owner's name [NO CAPITALS]
 
### Functions
 
def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode())
 
def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user
def getMessage(line):
    global message
    try:
        message = (line.split(":", 2))[2]
    except:
        message = ""
    return message
def joinchat():
    readbuffer_join = "".encode()
    Loading = True
    while Loading:
        readbuffer_join = s.recv(1000000)#Default : 1024
        readbuffer_join = readbuffer_join.decode()
        temp = readbuffer_join.split("\n")
        readbuffer_join = readbuffer_join.encode()
        readbuffer_join = temp.pop()
        for line in temp:
            Loading = loadingCompleted(line)
    #sendMessage(s, "pi pi") #Enviar Mensagem quando conectar-se
    print (BOT + " has joined " + CHANNEL + " Channel!")
 
def loadingCompleted(line):
    if ("End of /NAMES list" in line):
        return False
    else:
        return True
### Code runs
s_prep = socket.socket()
s_prep.connect((SERVER, PORT))
s_prep.send(("PASS " + PASS + "\r\n").encode())
s_prep.send(("NICK " + BOT + "\r\n").encode())
s_prep.send(("JOIN #" + CHANNEL + "\r\n").encode())
s = s_prep
joinchat()
readbuffer = ""
 
def Console(line):
    # gets if it is a user or twitch server
    if "PRIVMSG" in line:
        return False
    else:
        return True
 
 
 
while True:
        try:
            readbuffer = s.recv(1024)
            readbuffer = readbuffer.decode()
            temp = readbuffer.split("\n")
            readbuffer = readbuffer.encode()
            readbuffer = temp.pop()
        except:
            temp = ""
        for line in temp:
            if line == "":
                break
            # So twitch doesn't timeout the bot.
            if "PING" in line and Console(line):
                msgg = "PONG tmi.twitch.tv\r\n".encode()
                s.send(msgg)
                print(msgg)
                break
            # get user
            user = getUser(line)
            # get message send by user
            message = getMessage(line)
            # for you to see the chat from CMD
            print(user + " > " + message)
            # sends private msg to the user (start line)
            PMSG = "/w " + user + " "
 
################################# Command ##################################
############ Here you can add as meny commands as you wish of ! ############
############################################################################
  #  #  ENVIAR MENSAGEMS// COMANDOS
                 
           
            #if "!pi" in message:
                #sendMessage(s, "pi pi pi pi pi")
                #break
			
  
            #//INICIO
            #if user == OWNER and "!command" in message:
                #sendMessage(s, "This can only be used by the owner")
               # break
			#//FINAL
			
			#//INICIO
            #if "!private" in message:
                #sendMessage(s, PMSG + "This is a private message send to the user")
                #break
			#//FINAL
			
			#//INICIO
            #if "!global" in message:
               # sendMessage(s, "This is a global message send to the chat")
                #break
            #//FINAL
############################################################################
