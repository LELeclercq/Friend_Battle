from character import *
from magic import *
from sys import exit
import time



class Engine(object):

    def __init__(self, setup, guy, guymagic):
        # Use these for moving_on()
        self.guy = guy
        self.guymagic = guymagic
        self.setup = setup
        


    def disp_stat(self, good_guy, bad_guy):
        time.sleep(1)
        print "\nHP: %d\t MP: %d" % (good_guy.hp, good_guy.mp)
        print "%s\'s HP: %d\n" % (bad_guy.name, bad_guy.hp)

    def disp_magic(self, protag):
        if protag.lvl < 3:
            print "Which spell?"
            print "\n[H]eal:5MP [S]andpaper:10MP [B]ack"
        else:
            print "Which spell?"
            print "\n[H]eal:5MP [S]andpaper:10MP [C]haos_Dunk:20MP [B]ack"

    def moving_on(self, setup):
    # increments to the next fighter in FightOrder.fighter and goes through run with the new enemy
        new_enemy = setup.next_battle(self.guy)
        self.run(self.guy, self.guymagic, new_enemy)
    
    def retry(self, enemy):
        print 'You died! So sad. A host of sorrows.\n\nWanna try again?'
        my_answer = 1
        while my_answer == 1:
            print '[Y]es [N]o'
            answer = raw_input("> ")
            if answer in ("y", "yes"):
                my_answer = 0
                self.guy.hp = self.guy.maxhp
                self.guy.mp = self.guy.maxmp
                enemy.hp = enemy.maxhp
                enemy.mp = enemy.maxmp
                self.run(self.guy, self.guymagic, enemy)
            elif answer in ('n', 'no'):
                print "\n\nQuitter\n\n"
                time.sleep(1)
                exit(1)
            else:
                print "Just [Y]es or [N]o, please."

    def run(self, hero, heromagic, enemy):
        # the meat and potatoes. plays the enemy intro, then a while loop so it goes back to the players turn.
        enemy.enemy_intro()
        combat = True
        while combat== True:

            if hero.hp  > 0: # Check if hero is alive

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
                        my_turn = 0 # break out of prompt loop

                    elif action in ("m", "magic"):

                        magic_turn = 1
                        while magic_turn == 1:

                            self.disp_magic(hero)
                            spell = raw_input("> ")
                            spell = spell.lower()
                            print ""

                            if spell in ("h", "heal"):
                                if hero.hp == hero.maxhp:
                                    print "I'm already at full health!"
                                else:
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

                    elif action in ("y", "mystery"):
                        print "This doesn't work yet, sorry!"

                    elif action in ("r", "run"):
                        hero.run()
                    else:
                        print "Please type one of the words listed or simply the letter in the brackets."

            else:
                self.disp_stat(hero, enemy)
                time.sleep(1)

                hero.deathmusic()
                self.retry(enemy)

            if enemy.hp < 0:
                enemy.hp = 0 #that way he doesnt have negative health

            self.disp_stat(hero, enemy)
            time.sleep(1)

            if enemy.hp > 0:
                print "And now %s!" % enemy.name
                time.sleep(1)
                enemy.ai(hero)
                if hero.hp < 0:
                    hero.hp = 0 # if hero dies, go to 0 health

            else:
                hero.LevelUp(enemy)
                combat = False
       
        self.moving_on(self.setup) 


class FightOrder(object):
  
    def __init__(self):
        self.fight_num = 0
        self.fighter = [Character(luke_stats, luke_quotes),
                Character(dom_stats, dom_quotes),
                Character(jim_stats, jim_quotes),
                Character(marshall_stats, marshall_quotes),
                Character(shane_stats, shane_quotes),
                Character(nanny_stats, nanny_quotes),
                Character(chris_stats, chris_quotes),
                Character(dave_stats, dave_quotes)]
   
    def next_battle(self, protagonist):
        self.fight_num += 1
        if self.fight_num >= len(self.fighter):
            protagonist.winmusic()
            print "\nCongratulations! You've defeated all of your friends!\n\n\n"
            raw_input('--Press ENTER to exit--')
            exit(1)
        else:
            return self.fighter[self.fight_num]

    def opening_battle(self):
        return self.fighter[self.fight_num]

hero = Character(hero_stats, hero_quotes)
heromagic = Magic()
setup = FightOrder()
enemy = setup.opening_battle()
a = Engine(setup, hero, heromagic)
a.run(hero, heromagic, enemy)
