from magic import *
from random import randint
import pygame
pygame.init()
import time


luke_stats = {
        'name': 'Lucas', 
        'hp': 20, 
        'mp': 5, 
        'atkstr': range(1, 3),
        'intro_quote': 'Time to get blasted!',
        'outro_quote': 'Guys, I\'m just gonna go walk home.',
        'music': 'Lucas_battle.ogg',
        'bg': 'Lucas_bg.jpg'
}

luke_quotes = ['Lucas complains at you until your ears bleed!', 
        'Lucas beaches you to death!']

dom_stats = {
        'name': 'Dom', 
        'hp': 40, 
        'mp': 20, 
        'atkstr': range(3, 6),
        'intro_quote': 'How do you play this game again?',
        'outro_quote': 'Whatever, I\'m just gonna move to North Carolina',
        'music': 'Dom_battle.ogg',
        'bg': 'Dom_bg.jpg'
}

dom_quotes = ['Dom stumbles into you, mumbling apologies and mentioning something about too much to drink.',
        'Dom locks you into a bearhug, squeezing the life out of you while mentioning\nhow much he loves you, man.',
        'Dom trips and hurls a glass at you. It shatters on your face.',
        'Dom pukes up a ton of blood on you. Like, a metric ton of blood. Then he passes out on the floor.',
        'Dom uses his drunk strength to sock you in the stomach. You fly at least a foot off the ground.']

jim_stats = {
        'name': 'Jim',
        'hp': 30,
        'mp': 40,
        'atkstr': range(4, 7),
        'intro_quote': 'You know I love me the big game!',
        'outro_quote': 'Should\'ve stuck to watching animu...',
        'music': 'Jim_battle.ogg',
        'bg': 'Jim_bg.jpg'
}

jim_quotes = ['Jim blows out your ears with a concentrated blast of deadmau5!',
        'Jim smothers you with his Senjougahara dakimakura!',
        'Final Spark: After gathering energy for half a second, Jim fires a broad and long-range\nbeam of light in a line that deals magic damage!',
        'Jim calls out his stand \'Knife Party\', causing a shower of knives to rain from the sky!'
        'Jim forces you to watch one of his animus about cute girls doing cute things.\nThe cuteness is too overbearing and you suffer a magjor heart attack!']

marshall_stats = {
        'name': 'Marshall',
        'hp': 60,
        'mp': 20,
        'atkstr': range(4, 7),
        'intro_quote': 'Where do I think I am?! Marshall Reed!',
        'outro_quote': 'Man, I don\'t even get a constellation prize...',
        'music': 'Marshall_battle.ogg',
        'bg': 'Marshall_bg.jpg'
}

marshall_quotes = ['Marshall leaps off the top rope and bodyslams you into the dirt!',
        'Marshall takes a running start and charges into you full speed!',
        'Marshall grapples with you, picking you up over his head and slamming you into the ground!',
        'You throw a punch at Marshall, but it reflects back and strikes you instead!']

shane_stats = {
        'name': 'Shane',
        'hp': 50,
        'mp': 25,
        'atkstr': range(6, 9),
        'intro_quote': 'Let\'s rumble you baka gaijin!',
        'outro_quote': 'Oooh, sasuga Lawrence-kun.',
        'music': 'Shane_battle.ogg',
        'bg': 'Shane_bg.jpg'
}

shane_quotes = ['Shane whips his hair around your neck, choking the life out of you!',
        'Shane calls Nikki out to do a x2 double hair attack combo!',
        'Shane gets some of his hair in your food, causing you to take gross out damage!',
        'Shane lashes you with his hair repeatedly!'
        'Shane grabs your hand with his hair and tosses you effortlessly into the distance!']

nanny_stats = {
        'name': 'nanny',
        'hp': 60,
        'mp': 30,
        'atkstr': range(7, 11),
        'intro_quote': 'What\'d you write this in, VIM? How primitive, every knows that EMACs\nis the superior text editor.',
        'outro_quote': 'Say goodbye to Lawrence, Alara.',
        'music': 'nanny_battle.ogg',
        'bg': 'nanny_bg.jpg'
}

nanny_quotes = ['nanny hacks the code itself and lowers your current_health stat!',
        'nanny tags out and lets Alara use her superior physical strength to just wail on you!',
        'nanny creates a mecha out of spare computer parts and fire his Rocket Fist\n directly into your chest!',
        'nanny brings you up to his highest roof deck and kicks you off!',
        'nanny writes a virus that causes your computer to blow up in your face!']

chris_stats = {
        'name': 'Chris',
        'hp': 50,
        'mp': 20,
        'atkstr': range(10, 16),
        'intro_quote': 'It\'s time you knew the truth. The Jews control everything.',
        'outro_quote': 'Curses! Foiled again by God\'s chosen people!',
        'music': 'Chris_battle.ogg',
        'bg': 'Chris_bg.jpg'
}

chris_quotes = ['Chris stabs you 9 times with a shiv!',
        'Chris cleaves into you with his Kukri!',
        'Chris slices and dices you with an ordinary set of kitchen knives!',
        'Chris stabs you in the back with a butterfly knife!',
        'Chris uses his superior knowledge of the outdoors to set up a man-trap for you. You fall for it hook, line, and sinker!',
        'Chris swings a shovel at you! Even though he\s 10 feet away, it still connects!']

dave_stats = {
        'name': 'Dave',
        'hp': 100,
        'mp': 30,
        'atkstr': range(15, 21),
        'intro_quote': 'When you die it\'ll be funny, becaus we knew you!',
        'outro_quote': 'Too much bulking, not enough cutting...',
        'music': 'Dave_battle.ogg',
        'bg': 'Dave_bg.jpg'
}

dave_quotes = ['Dave deadlifts you a couple times before crushing you into the ground!',
        'Dave delivers a heart break shot, stopping your heart for a second or two!',
        'Daves takes a wide stance and begins swaying in a figure-eight motion.\nSuddenly, he explodes with puches from both sides, using his\nmomentum to deliver his full body weight into each punch!',
        'Dave picks up a barbell and hurls it into you!',
        'Dave swallows some protein powder, Popeye-style, delivers a punch\nso hard you fly out of your clothes!',
        'You cannot grasp the true form of Dave\'s attack!']

hero_stats = {
        'name': 'Lawrence',
        'hp': 20,
        'mp': 10,
        'atkstr': range(4, 7),
        'intro_quote': 'none',
        'outro_quote': 'none',
        'music': 'none',
        'bg': 'none'
}

hero_quotes = ['Lawrence says the opponent took damage, and Lawrence\'s always right,\nso that means he must have!',
        'Lawrence strkes at precisely the right angle!',
        'Lawrence prattles on and on for hours talking about Zelda!',
        'Lawrence channels his love of animation into a really nice fountain pen and\nthen stabs it into his opponent!',
        'Lawrence delivers a roundhouse kick to the head!',
        'Lawrence spends a full hour on the finer points of JoJo\'s Bizarre Adventure\n exaplaining each character in depth as well as his disdain for the\n english translations. Eventually his opponent just punches himself\nin the face to get it over with.']

class Character(object):

    def __init__(self, stats, battle_quotes):
        self.lvl = 1
        self.name = stats['name']
        self.hp = stats['hp']
        self.maxhp = stats['hp']
        self.mp = stats['mp']
        self.maxmp = self.mp
        self.atkstr = stats['atkstr']
        self.intro = stats['intro_quote']
        self.outro = stats['outro_quote']
        self.quips = battle_quotes
        self.music = stats['music']
        self.bg = stats['bg']

    def enemy_intro(self):
        pic = pygame.image.load('bg\\' + self.bg) # pygame is awful, and i need to find a substitute one day
        background = pygame.display.set_mode(pic.get_size())
        background.blit(pic,(0,0))
        pygame.display.flip()

        pygame.mixer.music.load('music\\' + self.music)
        pygame.mixer.music.play(-1)

        print "A wild %s has appeared!" % self.name
        time.sleep(1)
        print "\'%s\'" % self.intro

    def attack(self, opponent):
        print self.quips[randint(0, len(self.quips) - 1)]
        time.sleep(1)
        original_hp = opponent.hp
        strike = self.atkstr[randint(0, len(self.atkstr) - 1)]
        opponent.hp -= strike
        if original_hp - strike < 0:
            damage = original_hp
        else:
            damage = original_hp - opponent.hp
        print "%s takes %d damage!" % (opponent.name, damage)

    def run(self):
        run_loop = 1
        while run_loop == 1:
            really = raw_input("Are you sure? [Y]es [No]\n> ")
            really = really.lower()
            if really in ("y", "yes"):
                
                pygame.mixer.music.load('music\quit.ogg')  # super buggy. pygame sucks.
                pygame.mixer.music.set_volume(.5)
                pygame.mixer.music.play(-1)
                print "You run from the fight. But it doesn\'t end there. "
                print "The rest of your life you're branded a coward; someone who turns tail at\nthe slightest provacation. Your friends"
                print "gradually grow distant from you, and you\nend your days as an old, bitter man who curses"
                print "the world instead of himself.\n\n\nGAME OVER\n\n\n"
                raw_input("--Press ENTER to exit--")
                exit(1)
            elif really in ("n", "no"):
                print "Then why'd you choose Run, silly?"
                run_loop = 0
            else:
                print "Just [Y]es or [N]o, thank you.\n"

    def LevelUp(self, enemy):
        pygame.mixer.music.load('music\lvlup.ogg')  # super buggy. pygame sucks.
        pygame.mixer.music.play(-1)
        print "\'%s\'" % enemy.outro
        print ""
        print "You win! I mean it was an obvious outcome, since you're %s, but y\'know." % self.name
        time.sleep(3)

        self.lvl += 1
        self.hp = (self.lvl * 10) + 10
        self.maxhp = self.hp
        self.mp = ((self.lvl - 1) * 4) + 10
        self.atkstr = [((self.lvl - 1) * 2) + x for x in self.atkstr]
        print "%s has reached Level %d!" % (self.name, self.lvl)
        time.sleep(1)
        print "HP rose to %d!" % self.hp
        time.sleep(1)
        print "MP rose to %d!" % self.mp
        time.sleep(1)
        print "ATK rose by 2!"
        time.sleep(1)
        if self.lvl == 3:
            time.sleep(1)
            print "%s has learned Chaos_Dunk!" % self.name

        print "\n\n"
        raw_input("--Press ENTER to continue--\n")
        time.sleep(2)

    def deathmusic(self):
        pygame.mixer.music.load('music\death.ogg')
        pygame.mixer.music.play(-1)

    def winmusic(self):
        pygame.mixer.music.load('music\win.ogg')
        pygame.mixer.music.play(-1)

    def ai(self, hero):
        if self.name == 'Lucas':
            return self.lucas_ai(hero)
        elif self.name == 'Dom':
            return self.dom_ai(hero)
        elif self.name == 'Jim':
            return self.jim_ai(hero)
        elif self.name == 'Marshall':
            return self.marshall_ai(hero)
        elif self.name == 'Shane':
            return self.shane_ai(hero)
        elif self.name == 'nanny':
            return self.nanny_ai(hero)
        elif self.name == 'Chris':
            return self.chris_ai(hero)
        elif self.name == 'Dave':
            return self.dave_ai(hero)

    def lucas_ai(self, hero):
        lucas_magic = Magic()
        if self.hp < 11:
            outcome = randint(1,3)
            if (outcome == 1) and (self.mp >= lucas_magic.heal_mp):
                lucas_magic.heal(self)
            else:
                self.attack(hero)
        else:
            self.attack(hero)

    def dom_ai(self, hero):
        dom_magic = Magic()
        if (self.hp < 31) and (self.hp >= 20):
            outcome = randint(1, 3)
            if (outcome == 1) and (self.mp >= dom_magic.heal_mp):
                dom_magic.heal(self)
            else:
                self.attack(hero)
        elif self.hp < 20:
            outcome1 = randint(1,4)
            if (outcome1 == 1) and (self.mp >= dom_magic.greaterheal_mp):
                dom_magic.greaterheal(self)
            else:
                self.attack(hero)
        else:
            self.attack(hero)

    def jim_ai(self, hero):

        jim_magic = Magic()

        if self.hp >= 21:
            joutcome2 = randint(1, 4)
            if (joutcome2 == 1) and (self.mp >= jim_magic.sandpaper_mp):
                jim_magic.sandpaper(self, hero)
            else:
                self.attack(hero)

        elif (self.hp < 21) and (self.hp > 15):
            joutcome = randint(1, 4)
            if (joutcome == 1) and (self.mp >= jim_magic.greaterheal_mp):
                jim_magic.greaterheal(self)
            elif (houtcome == 2) and (self.mp >= jim_magic.sandpaper_mp):
                jim_magic.sanpaper(self, hero)
            else:
                self.attack(hero)
        
        else:
            joutcome3 = rand(1, 4)
            if ((joutcome3 == 1) or (joutcome3 == 2)) and (self.mp >= jim_magic.greaterheal_mp):
                jim_magic.greaterheal(self)
            else:
                self.attack(hero)


    def marshall_ai(self, hero):
        marshall_magic = Magic()
        if self.hp < 40:
            outcome = randint(1, 4)
            if (outcome == 1) and (self.mp >= marshall_magic.heal_mp):
                marshall_magic.heal(self)
            else:
                self.attack(hero)
        else:
            self.attack(hero)


    def shane_ai(self, hero):
        shane_magic = Magic()
        if (self.hp < 41) and (self.hp >= 30):
            outcome = randint(1, 3)
            if (outcome == 1) and (self.mp >= shane_magic.heal_mp):
                shane_magic.heal(self)
            else:
                self.attack(hero)
        elif self.hp < 30:
            outcome1 = randint(1,4)
            if (outcome1 == 1) and (self.mp >= shane_magic.greaterheal_mp):
                shane_magic.greaterheal(self)
            else:
                self.attack(hero)
        else:
            self.attack(hero)


    def nanny_ai(self, hero):
        nanny_magic = Magic()
        if (self.hp < 51) and (self.hp >= 40):
            outcome = randint(1, 3)
            if (outcome == 1) and (self.mp >= nanny_magic.heal_mp):
                nanny_magic.heal(self)
            else:
                self.attack(hero)
        elif self.hp < 40:
            outcome1 = randint(1,4)
            if (outcome1 == 1) and (self.mp >= nanny_magic.greaterheal_mp):
                nanny_magic.greaterheal(self)
            else:
                self.attack(hero)
        else:
            self.attack(hero)


    def chris_ai(self, hero):
        chris_magic = Magic()
        if (self.hp < 41) and (self.hp >= 30):
            outcome = randint(1, 3)
            if (outcome == 1) and (self.mp >= chris_magic.heal_mp):
                chris_magic.heal(self)
            else:
                self.attack(hero)
        elif self.hp < 30:
            outcome1 = randint(1,4)
            if (outcome1 == 1) and (self.mp >= chris_magic.greaterheal_mp):
                chris_magic.greaterheal(self)
            else:
                self.attack(hero)
        else:
            self.attack(hero)


    def dave_ai(self, hero):
        shane_magic = Magic()
        if (self.hp < 61) and (self.hp >= 50):
            outcome = randint(1, 3)
            if (outcome == 1) and (self.mp >= dave_magic.heal_mp):
                dave_magic.heal(self)
            else:
                self.attack(hero)
        elif self.hp < 50:
            outcome1 = randint(1,4)
            if (outcome1 == 1) and (self.mp >= dave_magic.greaterheal_mp):
                dave_magic.greaterheal(self)
            else:
                self.attack(hero)
        else:
            self.attack(hero)
