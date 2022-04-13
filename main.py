import statClass as status
import evClass as evs
import os

while True:
    
        
    def statcal():
        print("STAT CALCULATOR")
        basehp = int(input("input Pokemon Base HP: "))
        iv = int(input("Input Pokemon Individual Value (0-31): "))
        if iv < 0 or iv >31 :
            print("This input is not in range")
            exit()
        ev = int(input("Input Pokemon Effort Value: (0-255): "))
        if ev < 0 or ev >255 :
            print("This input is not in range")
            exit()
        lvl = int(input("Input Pokemon Level: "))
        print("""
        0 Hardy     1 Lonely    2 brave     3 adamant      4 naughty    5 bold
        6 Docile    7 Relaxed   8 Impish    9 Lax          10 Timid     11 Hasty
        12 Serious  13 Jolly    14 Naive    15 Modest      16 Mild      17 Quiet
        18 Bashful  19 Rash     20 Calm     21 Gentle      22 Sassy     23 Careful
        24 Quirky
        """)
        nature = int(input("please choose a nature: " ))
        

        hp = status.stat_class.hp_stat(basehp,iv,ev,lvl)
        attack = status.stat_class.attack_stat(basehp,iv,ev,lvl,nature)
        defens = status.stat_class.def_stat(basehp,iv,ev,lvl,nature)
        sp_attack = status.stat_class.sp_attack_stat(basehp,iv,ev,lvl,nature)
        sp_defense = status.stat_class.sp_def_stat(basehp,iv,ev,lvl,nature)
        speed = status.stat_class.spd_stat(basehp,iv,ev,lvl,nature)

        print("HP:      "+str(round(hp,2)))
        print("ATTACK:  "+str(round(attack,2)))
        print("DEFENSE: "+str(round(defens,2)))
        print("SP ATTK: "+str(round(sp_attack,2)))
        print("SP DEF:  "+str(round(sp_defense,2)))
        print("SPEED:   "+str(round(speed,2)))

    def evcal():
        print("EV CALCULATIOR")
        ch = int(input("what would you like to do?\n1 Single Stat Calculator\n2 Multiple stat Calculator\n"))
        if ch < 1 or ch > 2:
            print("Invalid Input")
            
        elif ch == 1:
            os.system('cls')
            print("""
            Please select the stat you want to calculate

            1 ATTACK
            2 DEFENSE
            3 SP ATTACK
            4 SP DEF
            5 SPEED
            """)
            opt = int(input("your choice : "))
        
        bstat = int(input("Input Pokemon Base Stat: "))
        ev_iv = int(input("Input Pokemon Individual Value (0-31): "))
        if ev_iv < 0 or ev_iv >31:
            print("This input is not in range")
        ev_ev = int(input("Input Pokemon Effort Value: (0-255): "))
        if ev_iv < 0 or ev_iv > 255:
            print("This input is not in range")
        lvl = int(input("Input Pokemon Level: "))
        print("""
            0 Hardy     1 Lonely    2 brave     3 adamant      4 naughty    5 bold
            6 Docile    7 Relaxed   8 Impish    9 Lax          10 Timid     11 Hasty
            12 Serious  13 Jolly    14 Naive    15 Modest      16 Mild      17 Quiet
            18 Bashful  19 Rash     20 Calm     21 Gentle      22 Sassy     23 Careful
            24 Quirky
        """)
        nature = int(input("please choose a nature: " ))

        evattack = evs.ev_class.EVattack_stat(bstat,ev_iv,ev_ev,lvl,nature)
        evdef = evs.ev_class.EVdef_stat(bstat,ev_iv,ev_ev,lvl,nature)
        evspattack = evs.ev_class.EVspattack_stat(bstat,ev_iv,ev_ev,lvl,nature)
        evspdef = evs.ev_class.EVspdef_stat(bstat,ev_iv,ev_ev,lvl,nature)
        evspd = evs.ev_class.EVspd_stat(bstat,ev_iv,ev_ev,lvl,nature)

        
        if ch == 1:
            if opt == 1:
                print("ATTACK = ",round(evattack,2))
            elif opt == 2:
                print("DEFENSE = ",round(evdef,2))
            elif opt == 3:
                print("SP ATTACK = ",round(evspattack,2))
            elif opt == 4:
                print("SP DEF = ",round(evspdef,2))
            elif opt == 5:
                print("SPEED = ",round(evspd,2))
            else:
                print("Invalid Input")
                exit()
        if ch == 2:
            print("ATTACK =     "+str(round(evattack,2)))
            print("DEFENSE =    "+str(round(evdef,2)))
            print("SP ATTACK =  "+str(round(evspattack,2)))
            print("SP DEF =     "+str(round(evspdef,2)))
            print("SPEED =      "+str(round(evspd,2)))




    print("Welcome to My Pokemon Stat and EV Calculator")

    ch = int(input("what would you like to do?\n1 Stat Calculator\n2 Ev Calculator\n"))
    if ch < 1 or ch > 2:
        print("Invalid Input")
    if ch == 1:
        os.system('cls')
        statcal()
    elif ch == 2: 
        os.system('cls')
        evcal()
    else:
       exit()
    check = input("Input y to continue or input any key to exit: ")
    if check == "y":
        os.system('cls')
        continue
    else:
        break

  
   


