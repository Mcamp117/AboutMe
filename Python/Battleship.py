#Title
print("""
                         Welcome To
===================================================================
|  __      _     ___    ___            _    _           ___    _  |
| |__)    /_\     |      |     |      |_   |_    |__|    |    |_) |
| |__)   /   \    |      |     |__    |_   __|   |  |   _|_   |   |
===================================================================
                     1  2  3  4  5
                  A|__|__|__|__|__|
                  B|__|__|__|__|__|
                  C|__|__|__|__|__|
                  D|__|__|__|__|__|
                  E|__|__|__|__|__|
""")

#Tells player how to play
print("How to play the game.\n\ttype in the coordinates for you ship to be locted before you start the game\n\ttype in the coordinates to try to hit the other player ship (ex: A4)\n\tto win the game you have to sink all the other player ships")

#What player wins
player1Win=0
player2Win=0

#Lists of coordinates for the Player 2 ships compiled into one big list
player1CarrierCordinates=[]
player1BattleshipCordinates=[]
player1CruiserCordinates=[]
player1SubmarineCordinates=[]
player1DestroyerCordinates=[]
player1HitList=[]
player1CordinateList=[player1CarrierCordinates,player1BattleshipCordinates,player1CruiserCordinates,player1SubmarineCordinates,player1DestroyerCordinates]

#Lists of coordinates for the Player 2 ships compiled into one big list
player2CarrierCordinates=[]
player2BattleshipCordinates=[]
player2CruiserCordinates=[]
player2SubmarineCordinates=[]
player2DestroyerCordinates=[]
player2HitList=[]
player2CordinateList=[player2CarrierCordinates,player2BattleshipCordinates,player2CruiserCordinates,player2SubmarineCordinates,player2DestroyerCordinates]

#tells which player is playing
player=1
#How many ships there are
shipList=5
def shipPlacement():
  #The name of the ships
  print("""
Name:
  Carrier(C)     
  Battleship(B)  
  Cruiser(Cr)    
  Submarine(S)   
  Destroyer(D)   

""")
  while shipList!=0:
    #Asks the player what ship the want to place
    player1ShipSelector=input("Player 1: What ship would you like to place, use the letters in the paranthesis to select your ship ")
    if player1ShipSelector=="C":
      shipList-1
      p1CarrierRow=ord(input("What row would you like (A-E) "))
      p1CarrierCollumn=int(input("What collumn would you like (1-5) "))
      #appends the coordinates to a list
      player1CarrierCordinates.append(p1CarrierRow)
      player1CarrierCordinates.append(p1CarrierCollumn)

    elif player1ShipSelector=="B":
      shipList-1
      p1BattleshipRow=ord(input("What row would you like "))
      p1BattleshipCollumn=int(input("What collumn would you like "))
      player1BattleshipCordinates.append(p1BattleshipRow)
      player1BattleshipCordinates.append(p1BattleshipCollumn)

    elif player1ShipSelector=="Cr":
      shipList-1
      p1CruiserRow=ord(input("What row would you like "))
      p1CruiserCollumn=int(input("What collumn would you like "))
      player1CruiserCordinates.append(p1CruiserRow)
      player1CruiserCordinates.append(p1CruiserCollumn)

    elif player1ShipSelector=="S":
      shipList-1
      p1SubmarineRow=ord(input("What row would you like "))
      p1SubmarineCollumn=int(input("What collumn would you like "))
      player1SubmarineCordinates.append(p1SubmarineRow)
      player1SubmarineCordinates.append(p1SubmarineCollumn)

    elif player1ShipSelector=="D":
      shipList-1
      p1DestroyerRow=ord(input("What row would you like "))
      p1DestroyerCollumn=int(input("What collumn would you like "))
      player1DestroyerCordinates.append(p1DestroyerRow)
      player1DestroyerCordinates.append(p1DestroyerCollumn)

    else:
      print("Incorrect input, try again")
      player1ShipSelector=input("Player 1: What ship would you like to place, use the letters in the paranthesis to select your ship ")

    player2ShipSelector=input("Player 2: What ship would you like to place, use the letters in the paranthesis to select your ship ")
    if player2ShipSelector=="C":
      shipList-1
      p2CarrierRow=ord(input("What row would you like "))
      p2CarrierCollumn=int(input("What collumn would you like "))
      player2CarrierCordinates.append(p2CarrierRow)
      player2CarrierCordinates.append(p2CarrierCollumn)

    elif player2ShipSelector=="B":
      shipList-1
      p2BattleshipRow=ord(input("What row would you like "))
      p2BattleshipCollumn=int(input("What collumn would you like "))
      player2BattleshipCordinates.append(p2BattleshipRow)
      player2BattleshipCordinates.append(p2BattleshipCollumn)

    elif player2ShipSelector=="Cr":
      shipList-1
      p2CruiserRow=ord(input("What row would you like "))
      p2CruiserCollumn=int(input("What collumn would you like "))
      player2CruiserCordinates.append(p2CruiserRow)
      player2CruiserCordinates.append(p2CruiserCollumn)

    elif player2ShipSelector=="S":
      shipList-1
      p2SubmarineRow=ord(input("What row would you like "))
      p2SubmarineCollumn=int(input("What collumn would you like "))
      player2SubmarineCordinates.append(p2SubmarineRow)
      player2SubmarineCordinates.append(p2SubmarineCollumn)

    elif player2ShipSelector=="D":
      shipList-1
      p2DestroyerRow=ord(input("What row would you like "))
      p2DestroyerCollumn=int(input("What collumn would you like "))
      player2DestroyerCordinates.append(p2DestroyerRow)
      player2DestroyerCordinates.append(p2DestroyerCollumn)

    else:
      print("Incorrect input, try again")
      player2ShipSelector=input("Player 2: What ship would you like to place, use the letters in the paranthesis to select your ship ")

#tells if the game has been won
win=False

#plays the ship placement class
shipPlacement()

#creates a loop until game equals true
while win!=True:
  #Checks what player is playing
  if player==1:
    player1AttackRow=ord(input("Which row would you like to hit (A-E) "))
    player1AttackCollumn=int(input("Which Collumn would you like to hit (1-5) "))
    #If the row and collumn is in the other players list
    if player1AttackRow and player1AttackCollumn in player2CordinateList:
      player1Win+=1
      player1HitList.append(player1AttackRow)
      player1HitList.append(player1AttackCollumn)
      #Go again
      print("Hit Successful, prepare another attack")
      player1AttackRow=ord(input("Which row would you like to hit (A-E) "))
      player1AttackCollumn=int(input("Which Collumn would you like to hit (1-5) "))
    else:
      print("Hit Missed, Player 2's turn")
      #switches players
      player=2
  #checks to see if the player is player 2
  elif player==2:
    player2AttackRow=ord(input("Which row would you like to hit (A-J) "))
    player2AttackCollumn=int(input("Which Collumn would you like to hit (1-10) "))
    
    if player2AttackRow and player2AttackCollumn in player1CordinateList:
      player2HitList.append(player2AttackRow)
      player2HitList.append(player2AttackCollumn)

      player2Win+=1
      print("Hit Successful, prepare another attack")
      player2Win+=1
      player2AttackRow=ord(input("Which row would you like to hit (A-J) "))
      player2AttackCollumn=int(input("Which Collumn would you like to hit (1-10) "))
      
    else:
      print("Hit Missed, Player 2's turn")
      player=1
  #If the player gets to 5 hits, they win
  if player1Win==5:
    print("Player 1 Wins")
    win=True
  elif player2Win==5:
    win=True
    print("Player 2 Wins")