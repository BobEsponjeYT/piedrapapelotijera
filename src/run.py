import json
import random

datos = {
    "piedra": "1",
    "papel": "2",
    "tijera": "3"
}

def login():
    
    user = input("Tu nickname: ") ## Nicknames no funcionan bien despues del reinicio!!
    
    if not user:
        
        try:
            
            print("No elegistes un nickname")
            
            return login()
            
        except KeyError:
            
            return 0
        
    else:
        
        print("Tu nickname sera: {0}".format(user))
        start(u=user)

class end:
    def lose():
    
        print("Te gano el bot. Perdistes XD !")
    
        return start()
    def win():
        
        print("Ganastes!!!!")
        
        return start()


def game(con=None):
    piedra = datos["piedra"]
    papel = datos["papel"]
    tijera = datos["tijera"]
    
    bot_selection = random.choice([piedra,papel,tijera])
    
    if(bot_selection == "1"):
        
        selected = "Piedra" 
        
    elif(bot_selection == "2"):
        
        selected = "Papel"
        
    elif(bot_selection == "3"):
        
        selected = "Tijera"
    
    print("Bot: "+selected)
    
    if(con == bot_selection):
        
        print("Empate!!!")
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
    
    print("Piedra (1), Papel (2) o Tijera (3) !")
    
    pptp = input("- ")
    
    if not pptp:
        
        print("No elegistes ninguna opt!!")
        
    else:
        
        if datos["piedra"] in pptp:
            
            print("{0}(Yo): Piedra".format(u))
            
            game(con=datos["piedra"])
            
        elif datos["papel"] in pptp:
            
            print("{0}(Yo): Papel".format(u))
            
            game(con=datos["papel"])
            
        elif datos["tijera"] in pptp:
            
            print("{0}(Yo): Tijera".format(u))
            
            game(con=datos["tijera"])
            
        else:
            
            print("No existe esa opt!!")
            return start()
    
login()

if __name__ == "main":
    
    index = 0 
    points = 0
    
    options = False
