from random import randint
import time

class Magic(object):

    def __init__(self):
        self.heal_mp = 5
        self.greaterheal_mp = 10
        self.sandpaper_mp = 10
        self.chaos_mp = 20

    def heal(self, caster):
        original_hp = caster.hp
        caster.hp += 5
        if caster.hp > caster.maxhp:
            caster.hp = caster.maxhp
        print("{} takes out a bandage and some anitseptic ointment and treats one of his wounds for {} health!".format(caster.name, caster.hp - original_hp))
        caster.mp -= self.heal_mp

    def greaterheal(self,caster):
        original_hp = caster.hp
        caster.hp += 10
        if caster.hp > caster.maxhp:
            caster.hp = caster.maxhp
        print("{} set his broken bone and applies a splint, restoring {} health!".format(caster.name, caster.hp - original_hp))
        caster.mp -= self.heal_mp

    def sandpaper(self, caster, rubbed):
        original_hp = rubbed.hp
        rubbed.hp -= 10
        if original_hp - 10 < 0:
            damage = original_hp
        else:
            damage = original_hp - rubbed.hp
        print("{} acts really abraisive towards {} and it kind of hurts his feelings.\n".format(caster.name, rubbed.name))
        time.sleep(1)
        print("{} takes {} points of emotional damage!\n(Note: Emotional Damage is the same as normal damage.)".format(rubbed.name, damage))
        caster.mp -= self.sandpaper_mp

    def chaos_dunk(self, caster, slammed):
        original_hp = slammed.hp
        slammed.hp -= 25
        if original_hp - 25 < 0:
            damage = original_hp
        else:
            damage = original_hp - slammed.hp
        print("There were no survivors. You monster.")
        caster.mp -= self.chaos_mp
