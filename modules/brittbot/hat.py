#!/usr/bin/env python
# encoding: utf-8

import random
from modules.brittbot.filters import smart_ignore

hats = [
    "Alien Swarm Parasite",
    "Bounty Hat",
    "Ellis' Cap",
    "Ghastly Gibus",
    "Hat of Undeniable Wealth and Respect",
    "Horrific Headsplitter",
    "Mann Co Cap",
    "Max's Severed Head",
    "Modest Pile of Hat",
    "Noble Amassment of Hats",
    "Saxton Hale Maks",
    "Spine-Chilling Skull",
    "The Athletic Supporter",
    "Towering Pillar of Hats",
    "Treasure Hat",
    "Voodoo Juju",
    "Wiki Cap",
    "World Traveler's Hat",
    "Baseball Bill's Sports Shine",
    "Batter's Helmet",
    "Bombing Run",
    "Bonk Helm",
    "Flipped Trilby",
    "The Milkman",
    "The Superfan",
    "Whoopee Cap",
    "Ye Old Baker Boy",
    "Chieftain's Challenge",
    "Defiant Spartan",
    "Dr's Dapper Topper",
    "Exquisite Rack",
    "Grenadier's Softcap",
    "Hero's Hachimaki",
    "Killer's Kabuto",
    "Lumbricus Lid",
    "Sergeant's Drill Hat",
    "Soldier's Stash",
    "Stainless Pota",
    "Stout Shako",
    "Tyrant's Helm",
    "Carouser's Capotain",
    "Demoman's Fro",
    "Glengarry Bonnet",
    "Hustler's Hallmark",
    "Prince Tavish's Crown",
    "Rimmed Raincatcher",
    "Samur-Eye",
    "Scotch Bonnet",
    "Scotsman's Stove Pipe",
    "Sober Stuntman",
    "Tippler's Tricorne",
    "Brigade Helm",
    "Foster's Facade",
    "Handyman's Handle",
    "Madame Dixie",
    "Napper's Respite",
    "Old Guadalajara",
    "Pyro's Beanie",
    "Pyromancer's Mask",
    "Respectless Rubber Glove",
    "The Attendant",
    "Triboniophorus Tyrannus",
    "Vintage Merryweather",
    "Big Chief",
    "Cadaver's Cranium",
    "Coupe D'Isaster",
    "Dealer's Visor",
    "Dread Knot",
    "Football Helmet",
    "Hard Counter",
    "Heavy-Duty Rag",
    "Hound Dog",
    "Magnificent Mongolian",
    "Officer's Ushanka",
    "Pugilist's Protector",
    "Tough Guy's Toque",
    "Berliner's Bucket Helm",
    "Blighted Beak",
    "Geisha Boy",
    "Gentleman's Gatsby",
    "German Gonzila",
    "Otolaryngologist's Mirror",
    "Physician's Procedure Mask",
    "Prussian Pickelhaube",
    "Vintage Tyrolean",
    "Buckaroo's Hat",
    "Engineer's Cap",
    "Hotrod",
    "Industrial Festivizer",
    "Mining Light",
    "Safe'n'Sound",
    "Texas Slim's Dome Shine",
    "Texas Ten Gallon",
    "Trophy Belt",
    "Professional's Panama",
    "Master's Yellow Belt",
    "Shooter's Sola Topi",
    "Bloke's Bucket Hat",
    "Ritzy Rick's Hair Fixative",
    "Ol' Snaggletooth",
    "Larrikin Robin",
    "Fancy Fedora",
    "Backbiter's Billycock",
    "Magistrate's Mullet",
    "Frenchman's Beret",
    "Familiar Fez",
    "Detective Noir",
    "Le Party Phantom",
    "Noh Mercy",
]


@smart_ignore
def hat(jenni, input):
    '''.hat <nick> -- have jenni give someone a hat'''
    index = random.choice(range(len(hats)))
    txt = input.group(2)
    if not txt:
        msg = '{0} has put on a {1}'.format(
            input.nick,
            hats[index],
        )
        return jenni.msg(input.sender, msg, x=True)
    else:
        msg = '{0} is now wearing a {1}'.format(
        input.group(2),
        hats[index],
        )
        jenni.msg(input.sender, msg, x=True)

hat.commands = ['hat', 'hats']

if __name__ == '__main__':
    print __doc__.strip()
