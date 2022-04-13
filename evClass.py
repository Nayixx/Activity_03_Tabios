class ev_class():

    def EVattack_stat(pokemon_base,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 1.0
        if pnature == 1 or pnature == 2 or pnature == 3 or pnature == 4:
            n = 1.1
        elif pnature == 5 or pnature == 10 or pnature == 15 or pnature == 20:
            n = 0.9
        else: 
            n = 0.9
        d = ((2*pokemon_base+pokemon_iv+(pokemon_ev/4))*pokemon_lvl/100)
        total = (((((pokemon_base/n)-d)*400)/pokemon_lvl)/4)*4
        return total

    def EVdef_stat(pokemon_base,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 1.0
        if pnature == 5 or pnature == 7 or pnature == 8 or pnature == 9:
            n = 1.1
        elif pnature == 1 or pnature == 11 or pnature == 16 or pnature == 21:
            n = 0.9
        else :
            n = 0.9
        d = ((2*pokemon_base+pokemon_iv+(pokemon_ev/4))*pokemon_lvl/100)
        total = (((((pokemon_base/n)-d)*400)/pokemon_lvl)/4)*4
        return total

    def EVspattack_stat(pokemon_base,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 1.0
        if pnature == 15 or pnature == 16 or pnature == 17 or pnature == 19:
            n = 1.1
        elif pnature == 3 or pnature == 8 or pnature == 13 or pnature == 23:
            n = 0.9
        else :
            n = 0.9
        d = ((2*pokemon_base+pokemon_iv+(pokemon_ev/4))*pokemon_lvl/100)
        total = (((((pokemon_base/n)-d)*400)/pokemon_lvl)/4)*4
        return total
    
    def EVspdef_stat(pokemon_base,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 1.0
        if pnature == 20 or pnature == 21 or pnature == 22 or pnature == 23:
            n = 1.1
        elif pnature == 4 or pnature == 9 or pnature == 14 or pnature == 19:
            n = 0.9
        else :
            n = 0.9
        d = ((2*pokemon_base+pokemon_iv+(pokemon_ev/4))*pokemon_lvl/100)
        total = (((((pokemon_base/n)-d)*400)/pokemon_lvl)/4)*4
        return total

    def EVspd_stat(pokemon_base,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 1.0
        if pnature == 10 or pnature == 11 or pnature == 13 or pnature == 14:
            n = 1.1
        elif pnature == 2 or pnature == 7 or pnature == 17 or pnature == 22:
            n = 0.9
        else :
            n = 0.9
        d = ((2*pokemon_base+pokemon_iv+(pokemon_ev/4))*pokemon_lvl/100)
        total = (((((pokemon_base/n)-d)*400)/pokemon_lvl)/4)*4
        return total