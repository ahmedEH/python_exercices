
def game ():
    print("\n\n\n************************************ Game ************************")
    user1 = ""
    user2 = ""
    a = "paper"
    b = "rock"
    c = "scissors"
    while(user1 == user2):
        user1 = input("\n\tEntrer votre nom :")
        user2 = input("\n\tentrer votre nom :")
        if(user1 == user2):
            print("\n\t\tvous avez le meme nom !!!")
    choix = 1


    while(choix != 0):
        i =1
        print("\n\n################## Le tour numero "+ str(i)+" #################")
        if(choix == 0): break
        elif(choix != 0 and choix != 1):
            print("\n\tMauvais choix")
        elif(choix ==1):
            choixg1 = ""
            choixg2 = ""
            while(choixg1 == "" or choixg2 == ""):
                print("\n\t\t1- pour rock ")
                print("\n\t\t2- pour paper")
                print("\n\t\t3-pour scissors")
                choixg1 = int(input("\n\n\t\t\t" + user1 +" votre choix :"))
                choixg2 = int(input("\n\n\t\t\t" + user2 +" votre choix :"))
                if(choixg1 != 1 and choixg1 != 2 and choixg1 != 3):
                    choixg1 = ""
                    print("\n\n\t\t\t" +user1 +" Mauvais choix")
                elif(choixg2 != 1 and choixg2 != 2 and choixg2 != 3):
                    choixg2 = ""
                    print("\n\n\t\t\t" +user2 +" Mauvais choix")
            if(choixg1 == choixg2 and choixg1 != ""):
                print("\n\n\t\t\tVous avez choisis le meme choix")
                continue
            elif(choixg1 == 1 and choixg2 == 2):
                print("\n\n\t\t\t"+ user2 +"  wins")
            elif(choixg1 == 2 and choixg2 == 1):
                print("\n\n\t\t\t"+ user1 +"  wins")
            elif(choixg1 == 1 and choixg2 == 3):
                print("\n\n\t\t\t"+ user1 +"  wins")
            elif(choixg1 == 3 and choixg2 == 1):
                print("\n\n\t\t\t"+ user2 +"  wins")
            elif(choixg1 == 2 and choixg2 == 3):
                print("\n\n\t\t\t"+ user2 +"  wins")
            elif(choixg1 == 3 and choixg2 == 2):
                print("\n\n\t\t\t"+ user1 +"  wins")
        print("\n\t0- pour quitter")
        print("\n\t1- pour continuer")
        choix = int(input("\n\t\tEntrer votre choix"))
        i = i+1
                

game()  




