class stat_class():


    def hp_stat(pokemon_hp,pokemon_iv,pokemon_ev,pokemon_lvl):
        total_hp = (((2*pokemon_hp+pokemon_iv*(pokemon_ev/4))*pokemon_lvl)/100)+pokemon_lvl+10
        return total_hp


    def attack_stat(pokemon_hp,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 0
        if pnature == 1 or pnature == 2 or pnature == 3 or pnature == 4:
            n = 1.1
        elif pnature == 5 or pnature == 10 or pnature == 15 or pnature == 20:
            n = 0.9
        else: 
            n = 1.0
        attk = ((((2*pokemon_hp+pokemon_iv+(pokemon_ev/4))*pokemon_lvl)/100)+5)*n
        return attk

    def def_stat(pokemon_hp,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 0
        if pnature == 5 or pnature == 7 or pnature == 8 or pnature == 9:
            n = 1.1
        elif pnature == 1 or pnature == 11 or pnature == 16 or pnature == 21:
            n = 0.9
        else :
            n = 1.0
        defense = ((((2*pokemon_hp+pokemon_iv+(pokemon_ev/4))*pokemon_lvl)/100)+5)*n
        return defense
        
    def sp_attack_stat(pokemon_hp,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 0
        if pnature == 15 or pnature == 16 or pnature == 17 or pnature == 19:
            n = 1.1
        elif pnature == 3 or pnature == 8 or pnature == 13 or pnature == 23:
            n = 0.9
        else :
            n = 1.0
        sp_attack = ((((2*pokemon_hp+pokemon_iv+(pokemon_ev/4))*pokemon_lvl)/100)+5)*n
        return sp_attack

    def sp_def_stat(pokemon_hp,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 0
        if pnature == 20 or pnature == 21 or pnature == 22 or pnature == 23:
            n = 1.1
        elif pnature == 4 or pnature == 9 or pnature == 14 or pnature == 19:
            n = 0.9
        else :
            n = 1.0
        sp_def = ((((2*pokemon_hp+pokemon_iv+(pokemon_ev/4))*pokemon_lvl)/100)+5)*n
        return sp_def

    def spd_stat(pokemon_hp,pokemon_iv,pokemon_ev,pokemon_lvl,pnature):
        n = 0
        if pnature == 10 or pnature == 11 or pnature == 13 or pnature == 14:
            n = 1.1
        elif pnature == 2 or pnature == 7 or pnature == 17 or pnature == 22:
            n = 0.9
        else :
            n = 1.0
        spd = ((((2*pokemon_hp+pokemon_iv+(pokemon_ev/4))*pokemon_lvl)/100)+5)*n
        return spd