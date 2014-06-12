from character import *
from magic import *
from sys import exit
import time



class Engine(object):

    def __init__(self, setup, fighter, guy, guymagic):
        self.guy = guy
        self.guymagic = guymagic
        self.setup = setup
        


    def disp_stat(self, good_guy, bad_guy):
        print ""
        print "HP: %d\t MP: %d" % (good_guy.hp, good_guy.mp)
        print "%s\'s HP: " % bad_guy.name, bad_guy.hp
        print ""

    def disp_magic(self, protag):
        if protag.lvl < 3:
            print "Which spell?"
            print "\n[H]eal:5MP [S]andpaper:10MP [B]ack"
        else:
            print "Which spell?"
            print "\n[H]eal:5MP [S]andpaper:10MP [C]haos_Dunk:20MP [B]ack"

    def moving_on(self, setup):
        new_enemy = setup.next_battle()
        self.run(self.guy, self.guymagic, new_enemy)
        

    def run(self, hero, heromagic, enemy):
        
        print "A wild %s has appeared!" % enemy.name
        time.sleep(1)
        print "\'%s\'" % enemy.intro
        time.sleep(1)
        
        combat = True
        while combat== True:

            if hero.hp  > 0:

                my_turn = 1
                while my_turn == 1: #allows me to loop prompt until a satisfactory answer is given

                    self.disp_stat(hero, enemy)
                    time.sleep(1)
                    print "What will you do?"
                    print "\n[A]ttack [M]agic M[y]stery [Run]"
                    action = raw_input("> ")
                    action = action.lower()
                    print ""

                    if action in ("a", "attack"):
                        hero.attack(enemy)
                        time.sleep(1)
                        my_turn = 0 # break out of prompt loop

                    elif action in ("m", "magic"):

                        magic_turn = 1
                        while magic_turn == 1:

                            self.disp_magic(hero)
                            spell = raw_input("> ")
                            spell = spell.lower()
                            print ""

                            if spell in ("h", "heal"):
                                if hero.mp >= heromagic.heal_mp:
                                    heromagic.heal(hero)
                                    my_turn = 0 # break out of promt loop
                                    magic_turn = 0
                                else:
                                    print "Not enough MP"

                            elif spell in ("s", "sandpaper"):
                                if hero.mp >= heromagic.sandpaper_mp:
                                    heromagic.sandpaper(hero, enemy)
                                    my_turn = 0 # break out of prompt loop
                                    magic_turn = 0
                                else:
                                    print "Not enough MP"

                            elif (spell in ("c", "chaos", "chaos_dunk", "chaos dunk")) and (hero.lvl >= 3):
                                if hero.mp >= heromagic.chaos_mp:
                                    heromagic.chaos_dunk(hero, enemy)
                                    my_turn = 0 # break out of prompt loop
                                    magic_turn = 0
                                else:
                                    print "Not enough MP"

                            elif spell in ("b", "back"):
                                magic_turn = 0

                            else:    
                                print "404 error: The spell you are looking for cannot be found."

                    elif action in ("r", "run"):
                        hero.run()
                    else:
                        print "Please type one of the words listed or simply the letter in the brackets."

            else:
                self.disp_stat(hero, enemy)
                time.sleep(1)
                print "You've died! So sad."
                exit(1)
            #print ""

            if enemy.hp < 0:
                enemy.hp = 0 #that way he doesnt have negative health
           # time.sleep(1)    
            self.disp_stat(hero, enemy)
            time.sleep(1)
            if enemy.hp > 0:
                print "And now %s!" % enemy.name
                time.sleep(1)
                enemy.ai(hero)
                if hero.hp < 0:
                    hero.hp = 0 # if hero dies, go to 0 health
                time.sleep(1)

            else:
                print "\'%s\'" % enemy.outro
                print ""
                print "You win! Brllnt!"
                hero.LevelUp(hero)
                combat = False
       
        self.moving_on(self.setup) 


class FightOrder(object):
  
    def __init__(self):
        self.fight_num = 0
        self.fighter = [Character(luke_stats, luke_quotes), Character(dom_stats, dom_quotes)]
   
    def next_battle(self):
        self.fight_num += 1
        if self.fight_num >= len(self.fighter):
            print "Congratulations! You've defeated all of your friends!\n\n\n"
            exit(1)
        else:
            return self.fighter[self.fight_num]

    def opening_battle(self):
        return self.fighter[self.fight_num]

hero = Character(hero_stats, hero_quotes)
heromagic = Magic()
setup = FightOrder()
enemy = setup.opening_battle()
a = Engine(setup, enemy, hero, heromagic)
a.run(hero, heromagic, enemy)
