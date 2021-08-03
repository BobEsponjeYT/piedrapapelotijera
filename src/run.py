import json
import random
from messages import messages

datos = {
    "piedra": "1",
    "papel": "2",
    "tijera": "3"
}

def login():
    
    user = input(f"{messages.nick_set}: ") ## Nicknames no funcionan bien despues del reinicio!!
    
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
    def lose():
    
        print(f"{messages.on_lose}")
    
        return start()
    def win():
        
        print(f"{messages.on_win}")
        
        return start()


def game(con=None):
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
        
        print(f"{messages.on_tie}")
        return start()

    else:
        
        if(con == piedra):
            
            if(bot_selection == "2"):
                
                end.lose()
            elif(bot_selection == "3"):
            
                end.win()
                
        if(con == papel):
            
            if(bot_selection == "3"):
                
                end.lose()
            
            elif(bot_selection == "1"):
                
                end.win()
                
        if(con == "3"):
            
            if(bot_selection == "1"):
                
                end.lose()
            
            elif(bot_selection == "2"):
                
                end.win()
    
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
        
        return start()
    
    

def start(u=None):
    
    print("_________________________________________________")
    
    print(f"{messages.stone} (1), {messages.paper} (2) o {messages.scissors} (3) !")
    
    pptp = input("- ")
    
    if not pptp:
        
        print(f"{messages.no_option}")
        
    else:
        
        if datos["piedra"] in pptp:
            
            print("{}(Yo/Me): {}".format(u, messages.stone))
            
            game(con=datos["piedra"])
            
        elif datos["papel"] in pptp:
            
            print("{}(Yo): {}".format(u, messages.paper))
            
            game(con=datos["papel"])
            
        elif datos["tijera"] in pptp:
            
            print("{}(Yo): {}".format(u, messages.scissors))
            
            game(con=datos["tijera"])
            
        else:
            
            print(f"{messages.option_null}")
            return start()
    
login()

if __name__ == "main":
    
    index = 0 
    points = 0
    
    options = False
