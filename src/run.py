import random
from messages import messages
from os import name, system

datos = {
    "piedra": "1",
    "papel": "2",
    "tijera": "3"
}

def login():
    if name == "nt":
        _ = system('cls')
    elif "nt" in name:
        _ = system('cls')

    else:
        _ = system('clear')

    
    user = input(f"{messages.nick_set}: ") 
    
    if not user:
        
        try:
            
            print(f"{messages.no_nickname}")
            
            return login()
            
        except KeyError:
            
            return 0
        
    else:
        
        print("{} {}".format(messages.nick_seted, user))
        start(u=user)

class end:
    def lose(u=None):
    
        print(f"\u001b[44m\u001b[31;1m{messages.on_lose}\u001b[0m")
    
        return start(u=u)
    def win(u=None):
        
        print(f"\u001b[44m\u001b[32;1m{messages.on_win}\u001b[0m")
        
        return start(u=u)


def game(con=None, nick=None):
    piedra = datos["piedra"]
    papel = datos["papel"]
    tijera = datos["tijera"]
    
    bot_selection = random.choice([piedra,papel,tijera])
    
    if(bot_selection == "1"):
        
        selected = messages.stone 
        
    elif(bot_selection == "2"):
        
        selected = messages.paper
        
    elif(bot_selection == "3"):
        
        selected = messages.scissors
    
    print("Bot: "+selected)
    
    if(con == bot_selection):
        
        print(f"\u001b[36m{messages.on_tie}")
        return start(u=nick)

    else:
        
        if(con == piedra):
            
            if(bot_selection == "2"):
                
                end.lose(u=nick)
            elif(bot_selection == "3"):
            
                end.win(u=nick)
                
        if(con == papel):
            
            if(bot_selection == "3"):
                
                end.lose(u=nick)
            
            elif(bot_selection == "1"):
                
                end.win(u=nick)
                
        if(con == "3"):
            
            if(bot_selection == "1"):
                
                end.lose(u=nick)
            
            elif(bot_selection == "2"):
                
                end.win(u=nick)
    
        ##ordenes = {
        ##    "piedra": {
        ##        "gana": "tijera",
        ##        "pierde": "papel"
        ##    }
        ##    "papel": {
        ##        "gana": "piedra",
        ##        "pierde": "tijera"
        ##    }
        ##    "tijera": {
        ##        "gana": "papel",
        ##        "pierde": "piedra"
        ##    }
        ##}
        
        return start(u=nick)
    
    

def start(u=None):
    while True:
    
        print("\u001b[37;1m\u001b[1m_________________________________________________")
        
        print(f"\u001b[36;1m{messages.stone} (1), {messages.paper} (2) o {messages.scissors} (3) !")
        
        pptp = input("\u001b[33m- \u001b[36m")
        
        if not pptp:
            
            print(f"\u001b[31m{messages.no_option}")
            
        else:
            
            if datos["piedra"] in pptp:
                
                print("\u001b[32m{}(Yo/Me): \u001b[37m{}".format(u, messages.stone))
                
                game(con=datos["piedra"], nick=u)
                
            elif datos["papel"] in pptp:
                
                print("\u001b[32m{}(Yo/Me): \u001b[37m{}".format(u, messages.paper))
                
                game(con=datos["papel"], nick=u)
                
            elif datos["tijera"] in pptp:
                
                print("\u001b[32m{}(Yo/Me): \u001b[37m{}".format(u, messages.scissors))
                
                game(con=datos["tijera"], nick=u)
                
            else:
                
                print(f"{messages.option_null}")
                return start(u=u)
    
login()

if __name__ == "main":
    
    wins = 0
    
    options = False
