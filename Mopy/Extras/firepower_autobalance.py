# -*- coding: utf-8-dos; mode: python -*-
# This script generates a FWE balance patch for weapon mods.
import sys
import time
from optparse import OptionParser
import bosh
from bosh import formatInteger,formatDate
from bolt import GPath

parser = OptionParser(usage="usage: %prog [options] FILENAME(esm/p, without directory path)")
parser.add_option("-o", dest="outfile", help="output file", default="a.esp", metavar="FILE")
parser.add_option("-q", dest="quiet", help="quiet mode", default=False)
(opts, args) = parser.parse_args(sys.argv)
if len(args) != 2:
    parser.print_help()
    exit()

# init subsystem
bosh.initDirs()
bosh.initSettings(readOnly=True)
bosh.falloutIni = bosh.FalloutIni()
bosh.modInfos = bosh.ModInfos()
bosh.modInfos.refresh()

# create patch
patchInfo = bosh.ModInfo(bosh.modInfos.dir, GPath(opts.outfile))
patchInfo.mtime = max([time.time()]+[info.mtime for info in bosh.modInfos.values()])
loadFactory = bosh.LoadFactory(True,bosh.MreWeap)
patchFile = bosh.ModFile(patchInfo,loadFactory)
patchFile.tes4.author = 'firepower_autobalance.py'
patchFile.tes4.masters = [GPath('Fallout3.esm')]
patchFile.longFids = True

# source mod
fileInfo = bosh.ModInfo(bosh.modInfos.dir, GPath(args[1]))
readFactory = bosh.LoadFactory(False,bosh.MreWeap)
modFile = bosh.ModFile(fileInfo,readFactory)
modFile.load(True)

# scanModFile
mapper = modFile.getLongMapper()
patchRecords = patchFile.WEAP
for record in modFile.WEAP.getActiveRecords():
    record = record.getTypeCopy(mapper)
    patchRecords.setRecord(record)

# buildPatch
weaponType= (
    'Biggun',
    'Energy',
    'Smallgun',
    'Melee',
    'Unarmed',
    'Thrown',
    'Mine',
    )
animationType = {
    0:'Hand to Hand',
    1:'Melee (1 Hand)',
    2:'Melee (2 Hand)',
    3:'Pistol - Balistic (1 Hand)',
    4:'Pistol - Energy (1 Hand)',
    5:'Rifle - Balistic (2 Hand)',
    6:'Rifle - Automatic (2 Hand)',
    7:'Rifle - Energy (2 Hand)',
    8:'Handle (2 Hand)',
    9:'Launcher (2 Hand)',
    10:'Grenade Throw (1 Hand)',
    11:'Land Mine (1 Hand)',
    12:'Mine Drop (1 Hand)',
    }
registType = {
    19:'Poison Resistance',
    52:'Fire Resistance',
    60:'Energy Resistance',
    61:'EMP Resistance',
    4294967295:'None'
    }

def update_attribute(record, attr, multiplier):
    oldValue = record.__getattribute__(attr)
    if isinstance(oldValue, int):
        newValue = int(oldValue * multiplier + 0.5)
        print("  %s: %d (* %f) -> %d" % (attr, oldValue, multiplier, newValue))
    else:
        newValue = oldValue * multiplier
        print("  %s: %f (* %f) -> %f" % (attr, oldValue, multiplier, newValue))
    record.__setattr__(attr, newValue)

def biggun(record):
    if record.animationType == 8 or record.animationType == 9: # Handle (2 Hand) / Launcher (2 Hand)
        if record.dnamFlags1.isAutomatic:
            if 52 == record.resistType: # fire resist
                # Flamer
                update_attribute(record, "damage", 1.5625)
                #update_attribute(record, "minSpread", 1)
                #update_attribute(record, "spread", 1)
                #update_attribute(record, "health", 1)
                #update_attribute(record, "value", 1)
                #update_attribute(record, "projectileCount", 1)
                #update_attribute(record, "fireRate", 1)
                #update_attribute(record, "attackShotsPerSec", 1)
                return True
            elif 60 == record.resistType: # energy resist
                # Gat Las
                update_attribute(record, "damage", 2.875)
                update_attribute(record, "minSpread", 2)
                update_attribute(record, "spread", 2.75)
                update_attribute(record, "health", 0.6666)
                return True
            elif 4294967295 == record.resistType: # no resist
                # Minigan
                update_attribute(record, "damage", 4.2)
                update_attribute(record, "minSpread", 0.6)
                update_attribute(record, "spread", 1.1)
                update_attribute(record, "health", 1.3333)
                return True
        else:
            # Rock-it
            update_attribute(record, "damage", 1.1)
            update_attribute(record, "minSpread", 0.5)
            update_attribute(record, "spread", 0.6)
            update_attribute(record, "health", 1.6666)
            return True
    elif record.animationType == 5 or record.animationType == 6: # Rifle - Balistic (2 Hand) / Rifle - Automatic (2 Hand)
        ## The same multipliers as Smallgun/rifle. (temporarily)
        if record.dnamFlags1.isAutomatic:
            # Assault Rifle
            update_attribute(record, "damage", 3.25)
            update_attribute(record, "minSpread", 0.4666)
            #update_attribute(record, "spread", 1)
            update_attribute(record, "health", 0.916)
            return True
        else:
            if record.projectileCount > 1:
                # Combat Shotgun
                update_attribute(record, "damage", 1.3091)
                #update_attribute(record, "minSpread", 1)
                update_attribute(record, "spread", 0.6)
                update_attribute(record, "health", 1.4583)
                update_attribute(record, "projectileCount", 1.3333)
                return True
            elif 4294967295 == record.resistType: # no resist
                if record.damage > 30:
                    # Sniper Rifle
                    update_attribute(record, "damage", 1.875)
                    update_attribute(record, "minSpread", 0)
                    #update_attribute(record, "spread", 1)
                    update_attribute(record, "health", 3)
                elif record.damage > 10:
                    # Med. Rifle (Hunting Rifle)
                    update_attribute(record, "damage", 1.6)
                    update_attribute(record, "minSpread", 0.5)
                    update_attribute(record, "spread", 3.3333)
                    update_attribute(record, "health", 0.8)
                else:
                    # Light Rifle (BB Gun)
                    update_attribute(record, "damage", 2.5)
                    update_attribute(record, "minSpread", 0.6666)
                    update_attribute(record, "spread", 0.3333)
                    #update_attribute(record, "health", 1)
                return True
    return False

def energy(record):
    if record.animationType == 3  or record.animationType == 4: # Pistol - Balistic (1 Hand) / Pistol - Energy (1 Hand)
        if record.dnamFlags1.isAutomatic:
            pass
        else:
            if record.projectileCount > 1:
                pass
            elif 60 == record.resistType: # energy resist
                if record.damage > 20:
                    # Plasma Pistol
                    update_attribute(record, "damage", 1.8)
                    #update_attribute(record, "minSpread", 1)
                    update_attribute(record, "spread", 0.6818)
                    update_attribute(record, "health", 0.375)
                else:
                    # Laser Pistol
                    update_attribute(record, "damage", 2.9166)
                    update_attribute(record, "minSpread", 0)
                    #update_attribute(record, "spread", 1)
                    update_attribute(record, "health", 0.5)
                return True
    elif record.animationType == 6 or record.animationType == 7: # Rifle - Automatic (2 Hand) / Rifle - Energy (2 Hand)
        if record.dnamFlags1.isAutomatic:
            pass
        else:
            if record.projectileCount > 1:
                pass
            elif 60 == record.resistType: # energy resist
                if record.damage > 40:
                    # Plasma Rifle
                    update_attribute(record, "damage", 1.5555)
                    #update_attribute(record, "minSpread", 1)
                    update_attribute(record, "spread", 7.5)
                    update_attribute(record, "health", 0.2222)
                else:
                    # Laser Rifle
                    update_attribute(record, "damage", 2.4782)
                    update_attribute(record, "minSpread", 0)
                    update_attribute(record, "spread", 8.3333)
                    update_attribute(record, "health", 0.225)
                return True
    return False

def smallgun(record):
    if record.animationType == 3: # Pistol - Balistic (1 Hand)
        if record.dnamFlags1.isAutomatic:
            # SMG
            update_attribute(record, "damage", 2.8571)
            update_attribute(record, "minSpread", 0.5)
            update_attribute(record, "spread", 0.8)
            update_attribute(record, "health", 0.9)
            return True
        else:
            if record.projectileCount > 1:
                # Sawnoff
                update_attribute(record, "damage", 1.68)
                update_attribute(record, "minSpread", 0.6428)
                update_attribute(record, "spread", 0.3)
                update_attribute(record, "health", 1.6)
                update_attribute(record, "projectileCount", 1.3333)
                return True
            elif 4294967295 == record.resistType: # no resist
                if record.damage > 25:
                    # Heavy Pistol
                    update_attribute(record, "damage", 1.2857)
                    update_attribute(record, "minSpread", 0.6666)
                    #update_attribute(record, "spread", 1)
                    update_attribute(record, "health", 1.4583)
                elif record.damage > 7:
                    # Med. Pistol
                    update_attribute(record, "damage", 2.2222)
                    update_attribute(record, "minSpread", 0.6)
                    update_attribute(record, "spread", 6)
                    update_attribute(record, "health", 1.6666)
                else:
                    # Light Pistol
                    update_attribute(record, "damage", 4.6666)
                    #update_attribute(record, "minSpread", 1)
                    #update_attribute(record, "spread", 1)
                    update_attribute(record, "health", 3.25)
                return True
    elif record.animationType == 5 or record.animationType == 6: # Rifle - Balistic (2 Hand) / Rifle - Automatic (2 Hand)
        if record.dnamFlags1.isAutomatic:
            # Assault Rifle
            update_attribute(record, "damage", 3.25)
            update_attribute(record, "minSpread", 0.4666)
            #update_attribute(record, "spread", 1)
            update_attribute(record, "health", 0.916)
            return True
        else:
            if record.projectileCount > 1:
                # Combat Shotgun
                update_attribute(record, "damage", 1.3091)
                #update_attribute(record, "minSpread", 1)
                update_attribute(record, "spread", 0.6)
                update_attribute(record, "health", 1.4583)
                update_attribute(record, "projectileCount", 1.3333)
                return True
            elif 4294967295 == record.resistType: # no resist
                if record.damage > 30:
                    # Sniper Rifle
                    update_attribute(record, "damage", 1.875)
                    update_attribute(record, "minSpread", 0)
                    #update_attribute(record, "spread", 1)
                    update_attribute(record, "health", 3)
                elif record.damage > 10:
                    # Med. Rifle (Hunting Rifle)
                    update_attribute(record, "damage", 1.6)
                    update_attribute(record, "minSpread", 0.5)
                    update_attribute(record, "spread", 3.3333)
                    update_attribute(record, "health", 0.8)
                else:
                    # Light Rifle (BB Gun)
                    update_attribute(record, "damage", 2.5)
                    update_attribute(record, "minSpread", 0.6666)
                    update_attribute(record, "spread", 0.3333)
                    #update_attribute(record, "health", 1)
                return True
    return False

def melee(record):
    if record.dnamFlags1.isAutomatic:
        # Ripper
        record.damage = int(record.damage * 1.5 + 0.5)
        return True
    else:
        if record.animationType == 1: # Melee (1 Hand)
            if record.damage > 20:
                # Shishkebab
                #update_attribute(record, "damage", 1)
                return False
            elif record.damage >= 10:
                # Sword
                update_attribute(record, "damage", 2.5)
            elif record.damage > 5:
                # Blade
                update_attribute(record, "damage", 2.1428)
            else:
                # Improvised (Knife)
                update_attribute(record, "damage", 2.5)
            return True
        elif record.animationType == 2: # Melee (2 Hand)
            if record.damage >= 20:
                # Hammer
                update_attribute(record, "damage", 1.5)
            elif record.damage > 5:
                # Club
                update_attribute(record, "damage", 2.5)
            else:
                # Improvised (Pool Cue)
                update_attribute(record, "damage", 5)
            return True
    return False

def unarmed(record):
    if record.animationType == 0: # Hand to Hand
        if record.damage > 15:
            # Power Fist
            update_attribute(record, "damage", 2.25)
        else:
            # Knuckles
            update_attribute(record, "damage", 2.5)
        return True
    return False

def thrown(record):
    return False

def mine(record):
    return False

def put_stats(record):
    print("  weaponType: %s\n  animationType: %s\n  damage: %d\n  isAutomatic: %d\n  projectileCount: %d\n  resistType: %s" %
          (weaponType[record.etype],
           animationType[record.animationType],
           record.damage,
           record.dnamFlags1.isAutomatic,
           record.projectileCount,
           registType[record.resistType]))

for record in patchFile.WEAP.records:
    name = record.full
    print "%s:%s" % (name, bosh.strFid(record.fid))
    put_stats(record)
    func = (biggun,energy,smallgun,melee,unarmed,thrown,mine)[record.etype]
    if func(record):
        print "  >> patched!!"
    else:
        print "  >> skip"

# postprocess
patchFile.tes4.masters = patchFile.getMastersUsed()
patchFile.convertToShortFids()
numRecords = sum([x.getNumRecords(False) for x in patchFile.tops.values()])
patchFile.tes4.description = "{{BASH:NoMerge,Stats}}\nUpdated: %s\n\nRecords Changed: %d" % (formatDate(time.time()),numRecords)
patchFile.safeSave()
print "\nWrote to '%s'..." % opts.outfile

