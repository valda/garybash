# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#  This file is part of Wrye Bash.
#
#  Wrye Bash is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  Wrye Bash is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Wrye Bash; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  Wrye Bash copyright (C) 2005, 2006, 2007, 2008, 2009 Wrye
#
# =============================================================================

"""This module defines static data for use by other modules in the Wrye Bash package.
Its use should generally be restricted to large chunks of data and/or chunks of data
that are used by multiple objects."""

# Imports ---------------------------------------------------------------------
import struct
import ctypes

from bolt import _,GPath

# Installer -------------------------------------------------------------------
# ensure all path strings are prefixed with 'r' to avoid interpretation of
#   accidental escape sequences
wryeBashDataFiles = set((
    r'Bashed Patch.esp',
    r'Bashed Patch, 0.esp',
    r'Bashed Patch, 1.esp',
    r'Bashed Patch, 2.esp',
    r'Bashed Patch, 3.esp',
    r'Bashed Patch, 4.esp',
    r'Bashed Patch, 5.esp',
    r'Bashed Patch, 6.esp',
    r'Bashed Patch, 7.esp',
    r'Bashed Patch, 8.esp',
    r'Bashed Patch, 9.esp',
    r'Bashed Patch, CBash.esp',
    r'Bashed Patch, Python.esp',
    r'Bashed Patch, FCOM.esp',
    r'Bashed Patch, Warrior.esp',
    r'Bashed Patch, Thief.esp',
    r'Bashed Patch, Mage.esp',
    r'Bashed Patch, Test.esp',
    r'ArchiveInvalidationInvalidated!.bsa'
    r'Fallout - AI!.bsa'
    ))
wryeBashDataDirs = set((
    r'Bash Patches',
    r'INI Tweaks'
    ))
ignoreDataFiles = set((
#    r'NVSE\Plugins\Construction Set Extender.dll',
#    r'NVSE\Plugins\Construction Set Extender.ini'
    ))
ignoreDataDirs = set((
#    r'NVSE\Plugins\ComponentDLLs\CSE',
    r'LSData'
    ))
bethDataFiles = set((
    #--Vanilla
    'falloutnv.esm',
    r'fallout - meshes.bsa',
    r'fallout - misc.bsa',
    r'fallout - sound.bsa',
    r'fallout - textures.bsa',
    r'fallout - textures2.bsa',
    r'fallout - voices1.bsa',
    #--Preorder Packs
    r'caravanpack.esm',
    r'caravanpack - main.bsa',
    r'classicpack.esm',
    r'classicpack - main.bsa',
    r'mercenarypack.esm',
    r'mercenarypack - main.bsa',
    r'tribalpack.esm',
    r'tribalpack - main.bsa',
    #--DLCs
    r'deadmoney.esm',
    r'deadmoney - main.bsa',
    r'deadmoney - sounds.bsa',
    r'honesthearts.esm',
    r'honesthearts - main.bsa',
    r'honesthearts - sounds.bsa',
    r'oldworldblues.esm',
    r'oldworldblues - main.bsa',
    r'oldworldblues - sounds.bsa',
    r'lonesomeroad.esm',
    r'lonesomeroad - main.bsa',
    r'lonesomeroad - sounds.bsa',
    ))
allBethFiles = set((
    #vanilla
    r'Credits.txt',
    r'CreditsWacky.txt',
    r'Fallout - Meshes.bsa',
    r'Fallout - Misc.bsa',
    r'Fallout - Sounds.bsa',
    r'Fallout - Textures.bsa',
    r'Fallout - Textures2.bsa',
    r'Fallout - Voices1.bsa',
    r'FalloutNV.esm',
    r'Update.bsa',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_City_Full.mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_City_Perc.mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Full(alt1).mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Full.mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Perc(alt1).mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Perc(alt2).mp3',
    r'Music\BTTL\Evil1\mus_BTTL_Lp_Evil1_Rural_Perc.mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_City_Full.mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_City_Perc.mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_Rural_Full(alt1).mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_Rural_Full.mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_Rural_Perc(alt1).mp3',
    r'Music\BTTL\Evil2\mus_BTTL_Lp_Evil2_Rural_Perc.mp3',
    r'Music\BTTL\Evil3\mus_BTTL_Lp_Evil3_City_Full.mp3',
    r'Music\BTTL\Evil3\mus_BTTL_Lp_Evil3_City_Perc.mp3',
    r'Music\BTTL\Evil3\mus_BTTL_Lp_Evil3_Rural_Full.mp3',
    r'Music\BTTL\Evil3\mus_BTTL_Lp_Evil3_Rural_Perc.mp3',
    r'Music\BTTL\Evil4\mus_BTTL_Lp_Evil4_City_Full.mp3',
    r'Music\BTTL\Evil4\mus_BTTL_Lp_Evil4_City_Perc.mp3',
    r'Music\BTTL\Evil4\mus_BTTL_Lp_Evil4_Rural_Full.mp3',
    r'Music\BTTL\Evil4\mus_BTTL_Lp_Evil4_Rural_Perc.mp3',
    r'Music\BTTL\Good1\mus_BTTL_Lp_Good1_City_Full.mp3',
    r'Music\BTTL\Good1\mus_BTTL_Lp_Good1_City_Perc.mp3',
    r'Music\BTTL\Good1\mus_BTTL_Lp_Good1_Rural_Full.mp3',
    r'Music\BTTL\Good1\mus_BTTL_Lp_Good1_Rural_Perc.mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_City_Full.mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_City_Perc.mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_Rural_Full(alt1).mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_Rural_Full.mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_Rural_Perc(alt1).mp3',
    r'Music\BTTL\Good2\mus_BTTL_Lp_Good2_Rural_Perc.mp3',
    r'Music\BTTL\Good3\mus_BTTL_Lp_Good3_City_Full.mp3',
    r'Music\BTTL\Good3\mus_BTTL_Lp_Good3_City_Perc.mp3',
    r'Music\BTTL\Good3\mus_BTTL_Lp_Good3_Rural_Full.mp3',
    r'Music\BTTL\Good3\mus_BTTL_Lp_Good3_Rural_Perc.mp3',
    r'Music\BTTL\Good4\mus_BTTL_Lp_Good4_City_Full.mp3',
    r'Music\BTTL\Good4\mus_BTTL_Lp_Good4_City_Perc.mp3',
    r'Music\BTTL\Good4\mus_BTTL_Lp_Good4_Rural_Full.mp3',
    r'Music\BTTL\Good4\mus_BTTL_Lp_Good4_Rural_Perc.mp3',
    r'Music\DNGN\Dungeon1\mus_DNGN_One_1Low(alt).mp3',
    r'Music\DNGN\Dungeon1\mus_DNGN_One_1Low.mp3',
    r'Music\DNGN\Dungeon1\mus_DNGN_One_2Mid.mp3',
    r'Music\DNGN\Dungeon1\mus_DNGN_One_3High.mp3',
    r'Music\DNGN\Dungeon2\mus_DNGN_Two_1Low(alt1).mp3',
    r'Music\DNGN\Dungeon2\mus_DNGN_Two_1Low.mp3',
    r'Music\DNGN\Dungeon2\mus_DNGN_Two_2Mid.mp3',
    r'Music\DNGN\Dungeon2\mus_DNGN_Two_3High.mp3',
    r'Music\DNGN\Dungeon3\mus_DNGN_Three_1Low.mp3',
    r'Music\DNGN\Dungeon3\mus_DNGN_Three_2Mid(alt1).mp3',
    r'Music\DNGN\Dungeon3\mus_DNGN_Three_2Mid.mp3',
    r'Music\DNGN\Dungeon3\mus_DNGN_Three_3High.mp3',
    r'Music\DNGN\Dungeon4\mus_DNGN_Four_1Low.mp3',
    r'Music\DNGN\Dungeon4\mus_DNGN_Four_2Mid.mp3',
    r'Music\DNGN\Dungeon4\mus_DNGN_Four_3High.mp3',
    r'Music\DNGN\Dungeon5\mus_DNGN_Five_1Low.mp3',
    r'Music\DNGN\Dungeon5\mus_DNGN_Five_2Mid(alt1).mp3',
    r'Music\DNGN\Dungeon5\mus_DNGN_Five_2Mid.mp3',
    r'Music\DNGN\Dungeon5\mus_DNGN_Five_3High.mp3',
    r'Music\DNGN\Dungeon6\mus_DNGN_Six_1Low.mp3',
    r'Music\DNGN\Dungeon6\mus_DNGN_Six_2Mid.mp3',
    r'Music\DNGN\Dungeon6\mus_DNGN_Six_3High.mp3',
    r'Music\DNGN\Dungeon7\mus_DNGN_Seven_1Low.mp3',
    r'Music\DNGN\Dungeon7\mus_DNGN_Seven_2Mid.mp3',
    r'Music\DNGN\Dungeon7\mus_DNGN_Seven_3High.mp3',
    r'Music\DNGN\Dungeon8\mus_DNGN_Eight_1Low.mp3',
    r'Music\DNGN\Dungeon8\mus_DNGN_Eight_2Mid.mp3',
    r'Music\DNGN\Dungeon8\mus_DNGN_Eight_3High.mp3',
    r'Music\Fallout1and2\Fallout\01MetallicMonks.mp3',
    r'Music\Fallout1and2\Fallout\02DesertWind.mp3',
    r'Music\Fallout1and2\Fallout\03ATradersLife.mp3',
    r'Music\Fallout1and2\Fallout\04TheVaultoftheFuture.mp3',
    r'Music\Fallout1and2\Fallout\05IndustrialJunk.mp3',
    r'Music\Fallout1and2\Fallout\06MoribundWorld.mp3',
    r'Music\Fallout1and2\Fallout\07VatsofGoo.mp3',
    r'Music\Fallout1and2\Fallout\08CityoftheDead.mp3',
    r'Music\Fallout1and2\Fallout\09SecondChance.mp3',
    r'Music\Fallout1and2\Fallout\10UndergroundTroubles.mp3',
    r'Music\Fallout1and2\Fallout\11CityofLostAngels.mp3',
    r'Music\Fallout1and2\Fallout\12FollowersCredo.mp3',
    r'Music\Fallout1and2\Fallout\13RadiationStorm.mp3',
    r'Music\Fallout1and2\Fallout\14AcolytesoftheNewgod.mp3',
    r'Music\Fallout1and2\Fallout\15FlameoftheAncientWorld.mp3',
    r'Music\Fallout1and2\Fallout\16KhansofNewCalifornia.mp3',
    r'Music\Fallout1and2\Fallout2\Arroyo.mp3',
    r'Music\Fallout1and2\Fallout2\Modoc.mp3',
    r'Music\Fallout1and2\Fallout2\NewReno.mp3',
    r'Music\Fallout1and2\Fallout2\Redding.mp3',
    r'Music\Fallout1and2\Fallout2\SanFrancisco.mp3',
    r'Music\Fallout1and2\Fallout2\VaultCity.mp3',
    r'Music\Fallout1and2\Fallout2\Worldmap1.mp3',
    r'Music\Fallout1and2\Fallout2\Worldmap2.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Day_1Low.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Day_2Mid.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Day_3High.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Night_1Low.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Night_2Mid.mp3',
    r'Music\LOC\CaesarsLegion\mus_LOC_Caesar_Night_3High.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Day_1Low.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Day_2Mid.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Day_3High.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Night_1Low.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Night_2Mid.mp3',
    r'Music\LOC\CorporateRuins\mus_LOC_CorpRuins_Night_3High.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Day_1Low.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Day_2Mid.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Day_3High.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Night_1Low.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Night_2Mid.mp3',
    r'Music\LOC\DesertExploration\mus_LOC_DesExpl_Night_3High.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Day_1Low.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Day_2Mid.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Day_3High.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Night_1Low.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Night_2Mid.mp3',
    r'Music\LOC\DesertSettlement\mus_LOC_DesSttl_Night_3High.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Day_1Low.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Day_2Mid.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Day_3High.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Night_1Low.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Night_2Mid.mp3',
    r'Music\LOC\Freeside\mus_LOC_Freeside_Night_3High.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_Caesar_1Low.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_Caesar_2Mid.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_Caesar_3High.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_NCR_1Low.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_NCR_2Mid.mp3',
    r'Music\LOC\HooverDam\mus_LOC_Hoover_NCR_3High.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Day_1Low.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Day_2Mid.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Day_3High(alt1).mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Day_3High.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Night_1Low.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Night_2Mid.mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Night_3High(alt1).mp3',
    r'Music\LOC\IndustrialCity\mus_LOC_Industrial_Night_3High.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Day_1Low.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Day_2Mid.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Day_3High.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Night_1Low.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Night_2Mid.mp3',
    r'Music\LOC\Jacobstown\mus_LOC_Jacobstown_Night_3High.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Day_1Low.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Day_2Mid.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Day_3High(alt1).mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Day_3High.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Night_1Low.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Night_2Mid.mp3',
    r'Music\LOC\LargerTown\mus_LOC_LrgTown_Night_3High.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Day_1Low.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Day_2Mid.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Day_3High.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Night_1Low.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Night_2Mid.mp3',
    r'Music\LOC\Mountain\mus_LOC_Mountain_Night_3High.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Day_1Low.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Day_2Mid.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Day_3High.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Night_1Low.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Night_2Mid.mp3',
    r'Music\LOC\NewCaliforniaRepublic\mus_LOC_CalRepublic_Night_3High.mp3',
    r'Music\OLD\FO1\mus_FO1_AcolytesOfTheNewGod.mp3',
    r'Music\OLD\FO1\mus_FO1_CityOfLostAngels.mp3',
    r'Music\OLD\FO1\mus_FO1_CityOfTheDead.mp3',
    r'Music\OLD\FO1\mus_FO1_DesertWind.mp3',
    r'Music\OLD\FO1\mus_FO1_FlameOfTheAncientWorld.mp3',
    r'Music\OLD\FO1\mus_FO1_IndustrialJunk.mp3',
    r'Music\OLD\FO1\mus_FO1_MetallicMonks.mp3',
    r'Music\OLD\FO1\mus_FO1_RadiationStorm.mp3',
    r'Music\OLD\FO1\mus_FO1_SecondChance.mp3',
    r'Music\OLD\FO1\mus_FO1_TheVaultOfTheFuture.mp3',
    r'Music\OLD\FO1\mus_FO1_UndergroundTrouble.mp3',
    r'Music\OLD\FO2\mus_FO2_Modoc.mp3',
    r'Music\OLD\FO2\mus_FO2_Redding.mp3',
    r'Music\OLD\FO3\mus_FO3_Base2.mp3',
    r'Music\OLD\FO3\mus_FO3_Base3.mp3',
    r'Music\OLD\FO3\mus_FO3_Base5.mp3',
    r'Music\OLD\FO3\mus_FO3_Death.mp3',
    r'Music\OLD\FO3\mus_FO3_Dungeon1.mp3',
    r'Music\OLD\FO3\mus_FO3_Dungeon2.mp3',
    r'Music\OLD\FO3\mus_FO3_Dungeon3.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore1.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore3.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore4.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore5.mp3',
    r'Music\OLD\FO3\mus_FO3_Explore6.mp3',
    r'Music\SCR\mus_SCR_DeathStinger.mp3',
    r'Music\SCR\mus_SCR_DocMitchell.mp3',
    r'Music\SCR\mus_SCR_GoodspringsStinger.mp3',
    r'Music\SCR\mus_SCR_Muzak.mp3',
    r'Music\SCR\mus_SCR_MuzakRadio.mp3',
    r'Music\SCR\mus_SCR_VegasStinger.mp3',
    r'Music\SCR\mus_SCR_VictorySinger(alt1).mp3',
    r'Music\SCR\mus_SCR_VictorySinger(alt2).mp3',
    r'Music\SCR\mus_SCR_VictorySinger.mp3',
    r'Music\Special\EndCredits.mp3',
    r'Music\Special\MainTitle.mp3',
    r'Music\Special\mus_endgameslideshow.mp3',
    r'Music\Special\mus_endgametransitionstinger.mp3',
    r'Music\Special\mus_hailchief.mp3',
    r'Shaders\shaderpackage002.sdp',
    r'Shaders\shaderpackage003.sdp',
    r'Shaders\shaderpackage004.sdp',
    r'Shaders\shaderpackage006.sdp',
    r'Shaders\shaderpackage007.sdp',
    r'Shaders\shaderpackage009.sdp',
    r'Shaders\shaderpackage010.sdp',
    r'Shaders\shaderpackage011.sdp',
    r'Shaders\shaderpackage012.sdp',
    r'Shaders\shaderpackage013.sdp',
    r'Shaders\shaderpackage014.sdp',
    r'Shaders\shaderpackage015.sdp',
    r'Shaders\shaderpackage016.sdp',
    r'Shaders\shaderpackage017.sdp',
    r'Shaders\shaderpackage018.sdp',
    r'Shaders\shaderpackage019.sdp',
    r'Sound\songs\radionv\MUS_Aint_That_A_Kick_In_the_Head.mp3',
    r'Sound\songs\radionv\MUS_American_Swing.mp3',
    r'Sound\songs\radionv\MUS_Big_Iron.mp3',
    r'Sound\songs\radionv\MUS_Blues_For_You.mp3',
    r'Sound\songs\radionv\MUS_Blue_Moon.mp3',
    r'Sound\songs\radionv\MUS_Cobwebs_and_Rainbows.mp3',
    r'Sound\songs\radionv\MUS_Concerto_For_2_Vl_Str_In_D_Minor.mp3',
    r'Sound\songs\radionv\MUS_Concerto_Grosso_In_B_Minor_Allegro_01.mp3',
    r'Sound\songs\radionv\MUS_Concerto_Grosso_In_B_Minor_Allegro_02.mp3',
    r'Sound\songs\radionv\MUS_EddyArnold_Rca_ItsASin.mp3',
    r'Sound\songs\radionv\MUS_Flower_Duet_Lakm_KPM.mp3',
    r'Sound\songs\radionv\MUS_Four_Seasons_No_4_The_Winter.mp3',
    r'Sound\songs\radionv\MUS_Goin_Under.mp3',
    r'Sound\songs\radionv\MUS_Hallo_Mister_X.mp3',
    r'Sound\songs\radionv\MUS_Happy_Times.mp3',
    r'Sound\songs\radionv\MUS_Heartaches_by_the_Number.mp3',
    r'Sound\songs\radionv\MUS_HomeOnTheWastes.mp3',
    r'Sound\songs\radionv\MUS_In_The_Shadow_Of_The_Valley.mp3',
    r'Sound\songs\radionv\MUS_Its_A_Sin_To_Tell_A_Lie.mp3',
    r'Sound\songs\radionv\MUS_I_m_Movin_Out.mp3',
    r'Sound\songs\radionv\MUS_I_m_So_Blue.mp3',
    r'Sound\songs\radionv\MUS_Jazz_Blues_GT.mp3',
    r'Sound\songs\radionv\MUS_Jazz_Club_Blues_CAS.mp3',
    r'Sound\songs\radionv\MUS_Jingle_Jangle_Jingle.mp3',
    r'Sound\songs\radionv\MUS_Joe_Cool_CAS.mp3',
    r'Sound\songs\radionv\MUS_Johnny_Guitar.mp3',
    r'Sound\songs\radionv\MUS_Lazy_Day_Blues.mp3',
    r'Sound\songs\radionv\MUS_Let_s_Ride_Into_The_Sunset_Together.mp3',
    r'Sound\songs\radionv\MUS_Lone_Star.mp3',
    r'Sound\songs\radionv\MUS_Love_Me_As_Though_No_Tomorrow.mp3',
    r'Sound\songs\radionv\MUS_Mad_About_The_Boy.mp3',
    r'Sound\songs\radionv\MUS_Manhattan.mp3',
    r'Sound\songs\radionv\MUS_NewVegasValley.mp3',
    r'Sound\songs\radionv\MUS_Piano_Concerto_No_21__Elvira_Madigan.mp3',
    r'Sound\songs\radionv\MUS_Ride_Of_The_Valkyries_01.mp3',
    r'Sound\songs\radionv\MUS_Roundhouse_Rock.mp3',
    r'Sound\songs\radionv\MUS_Sit_And_Dream.mp3',
    r'Sound\songs\radionv\MUS_Sleepy_Town_Blues_CAS.mp3',
    r'Sound\songs\radionv\MUS_Slow_Bounce.mp3',
    r'Sound\songs\radionv\MUS_Slow_Sax_KOS.mp3',
    r'Sound\songs\radionv\MUS_Somethings_Gotta_Give.mp3',
    r'Sound\songs\radionv\MUS_Spring_Song_KPMC.mp3',
    r'Sound\songs\radionv\MUS_Stars_Of_The_Midnight_Range.mp3',
    r'Sound\songs\radionv\MUS_Strahlende_Trompete.mp3',
    r'Sound\songs\radionv\MUS_StreetsOfNewReno.mp3',
    r'Sound\songs\radionv\MUS_Von_Spanien_Nach_S_damerika.mp3',
    r'Sound\songs\radionv\MUS_Where_Have_You_Been_All_My_Life.mp3',
    r'Sound\songs\radionv\MUS_Why_Dont_You_Do_Right.mp3',
    r'Video\FNVIntro.bik',
    #Preorder Packs
    r'CaravanPack - Main.bsa',
    r'CaravanPack.esm',
    r'CaravanPack.nam',
    r'ClassicPack - Main.bsa',
    r'ClassicPack.esm',
    r'ClassicPack.nam',
    r'MercenaryPack - Main.bsa',
    r'MercenaryPack.esm',
    r'MercenaryPack.nam',
    r'TribalPack - Main.bsa',
    r'TribalPack.esm',
    r'TribalPack.nam',
    #DLCs
    r'DEADMONEY.NAM',
    r'DeadMoney - Main.bsa',
    r'DeadMoney - Sounds.bsa',
    r'DeadMoney.esm',
    r'HONESTHEARTS.NAM',
    r'HonestHearts - Main.bsa',
    r'HonestHearts - Sounds.bsa',
    r'HonestHearts.esm',
    r'LONESOMEROAD.NAM',
    r'LonesomeRoad - Main.bsa',
    r'LonesomeRoad - Sounds.bsa',
    r'LonesomeRoad.esm',
    r'OLDWORLDBLUES.NAM',
    r'OldWorldBlues - Main.bsa',
    r'OldWorldBlues - Sounds.bsa',
    r'OldWorldBlues.esm',
    r'DLCList.txt',
    ))

# Balo Canonical Groups -------------------------------------------------------
baloGroups = (
    ('Root',),
    ('Library',1),
    ('Cosmetic',),
    ('Clothing',),
    ('Weapon',),
    ('Tweak',2,-1),
    ('Overhaul',4,-1),
    ('Misc.',1),
    ('Magic',2),
    ('NPC',),
    ('Home',1),
    ('Place',1),
    ('Quest',3,-1),
    ('Last',1,-1),
    )

# Tes3 Group/Top Types -------------------------------------------------------------
groupTypes = [
    _('Top (Type)'),
    _('World Children'),
    _('Int Cell Block'),
    _('Int Cell Sub-Block'),
    _('Ext Cell Block'),
    _('Ext Cell Sub-Block'),
    _('Cell Children'),
    _('Topic Children'),
    _('Cell Persistent Childen'),
    _('Cell Temporary Children'),
    _('Cell Visible Distant Children'),
]

#--Top types in FalloutNV order.
topTypes = ['GMST', 'TXST', 'MICN', 'GLOB', 'CLAS', 'FACT', 'HDPT', 'HAIR', 'EYES',
    'RACE', 'SOUN', 'ASPC', 'MGEF', 'SCPT', 'LTEX', 'ENCH', 'SPEL', 'ACTI', 'TACT',
    'TERM', 'ARMO', 'BOOK', 'CONT', 'DOOR', 'INGR', 'LIGH', 'MISC', 'STAT', 'SCOL',
    'MSTT', 'PWAT', 'GRAS', 'TREE', 'FURN', 'WEAP', 'AMMO', 'NPC_', 'CREA', 'LVLC',
    'LVLN', 'KEYM', 'ALCH', 'IDLM', 'NOTE', 'PROJ', 'LVLI', 'WTHR', 'CLMT', 'REGN',
    'NAVI', 'CELL', 'WRLD', 'DIAL', 'QUST', 'IDLE', 'PACK', 'CSTY', 'LSCR', 'ANIO',
    'WATR', 'EFSH', 'EXPL', 'DEBR', 'IMGS', 'IMAD', 'FLST', 'PERK', 'BPTD', 'ADDN',
    'COBJ', 'AVIF', 'RADS', 'CAMS', 'CPTH', 'VTYP', 'IPCT', 'IPDS', 'ARMA', 'ECZN',
    'MESG', 'RGDL', 'DOBJ', 'LGTM', 'MUSC', 'IMOD', 'REPU', 'RCPE', 'RCCT', 'CHIP',
    'CSNO', 'LSCT', 'MSET', 'ALOC', 'CHAL', 'AMEF', 'CCRD', 'CMNY', 'CDCK', 'DEHY',
    'HUNG', 'SLPD',
    # Unused types in falloutNV. (dummy)
    'SLGM', 'BSGN', 'FLOR', 'SGST', 'CLOT', 'SBSP', 'SKIL', 'LVSP', 'APPA',
    ]

# Fo3 added
# ['BPTD', 'VTYP', 'MUSC', 'FLST', 'PWAT', 'MICN', 'AVIF', 'NOTE', 'TERM', 'ASPC',
#  'PERK', 'HDPT', 'TXST', 'DOBJ', 'NAVI', 'EXPL', 'IPDS', 'IDLM', 'ARMA', 'LVLN',
#  'MSTT', 'IMAD', 'TACT', 'RGDL', 'CPTH', 'IMGS', 'MESG', 'DEBR', 'LGTM', 'SCOL',
#  'ECZN', 'CAMS', 'RADS', 'PROJ', 'IPCT', 'ADDN', 'COBJ' ]
# NV added
# ['IMOD', 'REPU', 'RCPE', 'RCCT', 'CHIP', 'CSNO', 'LSCT', 'MSET', 'ALOC', 'CHAL',
#  'AMEF', 'CCRD', 'CMNY', 'CDCK', 'DEHY', 'HUNG', 'SLPD' ]
# Oblivion specifics
# ['SLGM', 'BSGN', 'FLOR', 'SGST', 'CLOT', 'SBSP', 'SKIL', 'LVSP', 'APPA']

#--Dict mapping 'ignored' top types to un-ignored top types.
topIgTypes = dict([(struct.pack('I',(struct.unpack('I',type)[0]) | 0x1000),type) for type in topTypes])

recordTypes = set(topTypes + 'GRUP,TES4,ROAD,REFR,ACHR,ACRE,PGRD,LAND,INFO,PGRE,NAVM'.split(','))

# Id Functions ----------------------------------------------------------------
def getIdFunc(modName):
    return lambda x: (GPath(modName),x)

ob = getIdFunc('FalloutNV.esm')
cobl = getIdFunc('Cobl Main.esm')

# Race Info -------------------------------------------------------------------
raceNames = {
    0x000019 : _('Caucasian'),
    0x0038e5 : _('Hispanic'),
    0x0038e6 : _('Asian'),
    0x003b3e : _('Ghoul'),
    0x00424a : _('AfricanAmerican'),
    0x0042be : _('AfricanAmerican Child'),
    0x0042bf : _('AfricanAmerican Old'),
    0x0042c0 : _('Asian Child'),
    0x0042c1 : _('Asian Old'),
    0x0042c2 : _('Caucasian Child'),
    0x0042c3 : _('Caucasian Old'),
    0x0042c4 : _('Hispanic Child'),
    0x0042c5 : _('Hispanic Old'),
    0x04bb8d : _('Caucasian Raider'),
    0x04bf70 : _('Hispanic Raider'),
    0x04bf71 : _('Asian Raider'),
    0x04bf72 : _('AfricanAmerican Raider'),
    0x0987dc : _('Hispanic Old Aged'),
    0x0987dd : _('Asian Old Aged'),
    0x0987de : _('AfricanAmerican Old Aged'),
    0x0987df : _('Caucasian Old Aged'),
    }

raceShortNames = {
    0x000019 : 'Cau',
    0x0038e5 : 'His',
    0x0038e6 : 'Asi',
    0x003b3e : 'Gho',
    0x00424a : 'Afr',
    0x0042be : 'AfC',
    0x0042bf : 'AfO',
    0x0042c0 : 'AsC',
    0x0042c1 : 'AsO',
    0x0042c2 : 'CaC',
    0x0042c3 : 'CaO',
    0x0042c4 : 'HiC',
    0x0042c5 : 'HiO',
    0x04bb8d : 'CaR',
    0x04bf70 : 'HiR',
    0x04bf71 : 'AsR',
    0x04bf72 : 'AfR',
    0x0987dc : 'HOA',
    0x0987dd : 'AOA',
    0x0987de : 'FOA',
    0x0987df : 'COA',
    }

raceHairMale = {
    0x000019 : 0x014b90, #--Cau
    0x0038e5 : 0x0a9d6f, #--His
    0x0038e6 : 0x014b90, #--Asi
    0x003b3e : None, #--Gho
    0x00424a : 0x0306be, #--Afr
    0x0042be : 0x060232, #--AfC
    0x0042bf : 0x0306be, #--AfO
    0x0042c0 : 0x060232, #--AsC
    0x0042c1 : 0x014b90, #--AsO
    0x0042c2 : 0x060232, #--CaC
    0x0042c3 : 0x02bfdb, #--CaO
    0x0042c4 : 0x060232, #--HiC
    0x0042c5 : 0x02ddee, #--HiO
    0x04bb8d : 0x02bfdb, #--CaR
    0x04bf70 : 0x02bfdb, #--HiR
    0x04bf71 : 0x02bfdb, #--AsR
    0x04bf72 : 0x0306be, #--AfR
    0x0987dc : 0x0987da, #--HOA
    0x0987dd : 0x0987da, #--AOA
    0x0987de : 0x0987d9, #--FOA
    0x0987df : 0x0987da, #--COA
    }

raceHairFemale = {
    0x000019 : 0x05dc6b, #--Cau
    0x0038e5 : 0x05dc76, #--His
    0x0038e6 : 0x022e50, #--Asi
    0x003b3e : None, #--Gho
    0x00424a : 0x05dc78, #--Afr
    0x0042be : 0x05a59e, #--AfC
    0x0042bf : 0x072e39, #--AfO
    0x0042c0 : 0x05a5a3, #--AsC
    0x0042c1 : 0x072e39, #--AsO
    0x0042c2 : 0x05a59e, #--CaC
    0x0042c3 : 0x072e39, #--CaO
    0x0042c4 : 0x05a59e, #--HiC
    0x0042c5 : 0x072e39, #--HiO
    0x04bb8d : 0x072e39, #--CaR
    0x04bf70 : 0x072e39, #--HiR
    0x04bf71 : 0x072e39, #--AsR
    0x04bf72 : 0x072e39, #--AfR
    0x0987dc : 0x044529, #--HOA
    0x0987dd : 0x044529, #--AOA
    0x0987de : 0x044529, #--FOA
    0x0987df : 0x044529, #--COA
    }

# Default Eyes/Hair -----------------------------------------------------------
#standardEyes = [ob(x) for x in (0x27306,0x27308,0x27309)] + [cobl(x) for x in (0x000821, 0x000823, 0x000825, 0x000828, 0x000834, 0x000837, 0x000839, 0x00084F, )]
standardEyes = [ob(x) for x in (0x4252,0x4253,0x4254,0x4255,0x4256)]

defaultEyes = {
    #--FalloutNV.esm
    ob(0x000019): #--Caucasian
        standardEyes,
    ob(0x0038e5): #--Hispanic
        standardEyes,
    ob(0x0038e6): #--Asian
        standardEyes,
    ob(0x003b3e): #--Ghoul
        [ob(0x35e4f)],
    ob(0x00424a): #--AfricanAmerican
        standardEyes,
    ob(0x0042be): #--AfricanAmerican Child
        standardEyes,
    ob(0x0042bf): #--AfricanAmerican Old
        standardEyes,
    ob(0x0042c0): #--Asian Child
        standardEyes,
    ob(0x0042c1): #--Asian Old
        standardEyes,
    ob(0x0042c2): #--Caucasian Child
        standardEyes,
    ob(0x0042c3): #--Caucasian Old
        standardEyes,
    ob(0x0042c4): #--Hispanic Child
        standardEyes,
    ob(0x0042c5): #--Hispanic Old
        standardEyes,
    ob(0x04bb8d): #--Caucasian Raider
        [ob(0x4cb10)],
    ob(0x04bf70): #--Hispanic Raider
        [ob(0x4cb10)],
    ob(0x04bf71): #--Asian Raider
        [ob(0x4cb10)],
    ob(0x04bf72): #--AfricanAmerican Raider
        [ob(0x4cb10)],
    ob(0x0987dc): #--Hispanic Old Aged
        standardEyes,
    ob(0x0987dd): #--Asian Old Aged
        standardEyes,
    ob(0x0987de): #--AfricanAmerican Old Aged
        standardEyes,
    ob(0x0987df): #--Caucasian Old Aged
        standardEyes,
    }

# Function Info ---------------------------------------------------------------
conditionFunctionData = ( #--0: no param; 1: int param; 2: formid param
    (153, 'CanHaveFlames', 0, 0, 0, 0),
    (127, 'HasBeenEatan', 0, 0, 0, 0),
    ( 14, 'GetActorValue', 1, 0, 0, 0),
    ( 61, 'GetAlarmed', 0, 0, 0, 0),
    (190, 'GetAmountSoldStolen', 0, 0, 0, 0),
    (  8, 'GetAngle', 1, 0, 0, 0),
    ( 81, 'GetArmorRating', 0, 0, 0, 0),
    (274, 'GetArmorRatingUpperBody', 0, 0, 0, 0),
    ( 63, 'GetAttacked', 0, 0, 0, 0),
    (264, 'GetBarterGold', 0, 0, 0, 0),
    (277, 'GetBaseActorValue', 1, 0, 0, 0),
    (229, 'GetClassDefaultMatch', 0, 0, 0, 0),
    ( 41, 'GetClothingValue', 0, 0, 0, 0),
    (122, 'GetCrime', 2, 1, 0, 0),
    (116, 'GetMinorCrimeCount', 0, 0, 0, 0),
    (110, 'GetCurrentAIPackage', 0, 0, 0, 0),
    (143, 'GetCurrentAIProcedure', 0, 0, 0, 0),
    ( 18, 'GetCurrentTime', 0, 0, 0, 0),
    (148, 'GetCurrentWeatherPercent', 0, 0, 0, 0),
    (170, 'GetDayOfWeek', 0, 0, 0, 0),
    ( 46, 'GetDead', 0, 0, 0, 0),
    ( 84, 'GetDeadCount', 2, 0, 0, 0),
    (203, 'GetDestroyed', 0, 0, 0, 0),
    ( 45, 'GetDetected', 2, 0, 0, 0),
    (180, 'GetDetectionLevel', 2, 0, 0, 0),
    ( 35, 'GetDisabled', 0, 0, 0, 0),
    ( 39, 'GetDisease', 0, 0, 0, 0),
    ( 76, 'GetDisposition', 2, 0, 0, 0),
    (  1, 'GetDistance', 2, 0, 0, 0),
    (215, 'GetDefaultOpen', 0, 0, 0, 0),
    (182, 'GetEquipped', 2, 0, 0, 0),
    ( 73, 'GetFactionRank', 2, 0, 0, 0),
    ( 60, 'GetFactionRankDifference', 2, 2, 0, 0),
    (128, 'GetFatiguePercentage', 0, 0, 0, 0),
    (288, 'GetFriendHit', 2, 0, 0, 0),
    (160, 'GetFurnitureMarkerID', 0, 0, 0, 0),
    ( 74, 'GetGlobalValue', 2, 0, 0, 0),
    ( 48, 'GetGold', 0, 0, 0, 0),
    ( 99, 'GetHeadingAngle', 2, 0, 0, 0),
    (318, 'GetIdleDoneOnce', 0, 0, 0, 0),
    (338, 'GetIgnoreFriendlyHits', 0, 0, 0, 0),
    ( 67, 'GetInCell', 2, 0, 0, 0),
    (230, 'GetInCellParam', 2, 2, 0, 0),
    ( 71, 'GetInFaction', 2, 0, 0, 0),
    ( 32, 'GetInSameCell', 2, 0, 0, 0),
    (310, 'GetInWorldspace', 2, 0, 0, 0),
    ( 91, 'GetIsAlerted', 0, 0, 0, 0),
    ( 68, 'GetIsClass', 2, 0, 0, 0),
    (228, 'GetIsClassDefault', 2, 0, 0, 0),
    ( 64, 'GetIsCreature', 0, 0, 0, 0),
    (161, 'GetIsCurrentPackage', 2, 0, 0, 0),
    (149, 'GetIsCurrentWeather', 2, 0, 0, 0),
    (237, 'GetIsGhost', 0, 0, 0, 0),
    ( 72, 'GetIsID', 2, 0, 0, 0),
    (254, 'GetIsPlayableRace', 0, 0, 0, 0),
    (224, 'GetVATSMode', 0, 0, 0, 0),
    ( 69, 'GetIsRace', 2, 0, 0, 0),
    (136, 'GetIsReference', 2, 0, 0, 0),
    ( 70, 'GetIsSex', 1, 0, 0, 0),
    (246, 'GetIsUsedItem', 2, 0, 0, 0),
    (247, 'GetIsUsedItemType', 1, 0, 0, 0),
    ( 47, 'GetItemCount', 2, 0, 0, 0),
    (107, 'GetKnockedState', 0, 0, 0, 0),
    ( 80, 'GetLevel', 0, 0, 0, 0),
    ( 27, 'GetLineOfSight', 2, 0, 0, 0),
    (  5, 'GetLocked', 0, 0, 0, 0),
    ( 65, 'GetLockLevel', 0, 0, 0, 0),
    (320, 'GetNoRumors', 0, 0, 0, 0),
    (255, 'GetOffersServicesNow', 0, 0, 0, 0),
    (157, 'GetOpenState', 0, 0, 0, 0),
    (193, 'GetPCExpelled', 2, 0, 0, 0),
    (199, 'GetPCFactionAttack', 2, 0, 0, 0),
    (195, 'GetPCFactionMurder', 2, 0, 0, 0),
    (197, 'GetPCEnemyofFaction', 2, 0, 0, 0),
    (132, 'GetPCInFaction', 2, 0, 0, 0),
    (129, 'GetPCIsClass', 2, 0, 0, 0),
    (130, 'GetPCIsRace', 2, 0, 0, 0),
    (131, 'GetPCIsSex', 1, 0, 0, 0),
    (312, 'GetPCMiscStat', 1, 0, 0, 0),
    (225, 'GetPersuasionNumber', 0, 0, 0, 0),
    ( 98, 'GetPlayerControlsDisabled', 0, 0, 0, 0),
    (365, 'IsChild', 0, 0, 0, 0),
    (362, 'GetPlayerHasLastRiddenHorse', 0, 0, 0, 0),
    (  6, 'GetPos', 1, 0, 0, 0),
    ( 56, 'GetQuestRunning', 2, 0, 0, 0),
    ( 79, 'GetQuestVariable', 2, 1, 0, 0),
    ( 77, 'GetRandomPercent', 0, 0, 0, 0),
    (244, 'GetRestrained', 0, 0, 0, 0),
    ( 24, 'GetScale', 0, 0, 0, 0),
    ( 53, 'GetScriptVariable', 2, 1, 0, 0),
    ( 12, 'GetSecondsPassed', 0, 0, 0, 0),
    ( 66, 'GetShouldAttack', 2, 0, 0, 0),
    (159, 'GetSitting', 0, 0, 0, 0),
    ( 49, 'GetSleeping', 0, 0, 0, 0),
    ( 58, 'GetStage', 2, 0, 0, 0),
    ( 59, 'GetStageDone', 2, 1, 0, 0),
    ( 11, 'GetStartingAngle', 1, 0, 0, 0),
    ( 10, 'GetStartingPos', 1, 0, 0, 0),
    ( 50, 'GetTalkedToPC', 0, 0, 0, 0),
    (172, 'GetTalkedToPCParam', 2, 0, 0, 0),
    (361, 'GetTimeDead', 0, 0, 0, 0),
    (315, 'GetTotalPersuasionNumber', 0, 0, 0, 0),
    (144, 'GetTrespassWarningLevel', 0, 0, 0, 0),
    (242, 'GetUnconscious', 0, 0, 0, 0),
    (259, 'GetUsedItemActivate', 0, 0, 0, 0),
    (258, 'GetUsedItemLevel', 0, 0, 0, 0),
    ( 40, 'GetVampire', 0, 0, 0, 0),
    (142, 'GetWalkSpeed', 0, 0, 0, 0),
    (108, 'GetWeaponAnimType', 0, 0, 0, 0),
    (109, 'IsWeaponSkillType', 1, 0, 0, 0),
    (147, 'GetWindSpeed', 0, 0, 0, 0),
    (154, 'HasFlames', 0, 0, 0, 0),
    (214, 'HasMagicEffect', 2, 0, 0, 0),
    (227, 'HasCannibal', 0, 0, 0, 0),
    (353, 'IsActor', 0, 0, 0, 0),
    (314, 'IsActorAVictim', 0, 0, 0, 0),
    (313, 'IsActorEvil', 0, 0, 0, 0),
    (306, 'IsActorUsingATorch', 0, 0, 0, 0),
    (280, 'IsCellOwner', 2, 2, 0, 0),
    (267, 'IsCloudy', 0, 0, 0, 0),
    (150, 'IsContinuingPackagePCNear', 0, 0, 0, 0),
    (163, 'IsCurrentFurnitureObj', 2, 0, 0, 0),
    (162, 'IsCurrentFurnitureRef', 2, 0, 0, 0),
    (354, 'IsEssential', 0, 0, 0, 0),
    (106, 'IsFacingUp', 0, 0, 0, 0),
    (125, 'IsGuard', 0, 0, 0, 0),
    (282, 'IsHorseStolen', 0, 0, 0, 0),
    (112, 'IsIdlePlaying', 0, 0, 0, 0),
    (289, 'IsInCombat', 0, 0, 0, 0),
    (332, 'IsInDangerousWater', 0, 0, 0, 0),
    (300, 'IsInInterior', 0, 0, 0, 0),
    (146, 'IsInMyOwnedCell', 0, 0, 0, 0),
    (285, 'IsLeftUp', 0, 0, 0, 0),
    (278, 'IsOwner', 2, 0, 0, 0),
    (176, 'IsPCAMurderer', 0, 0, 0, 0),
    (175, 'IsPCSleeping', 0, 0, 0, 0),
    (358, 'IsPlayerMovingIntoNewSpace', 0, 0, 0, 0),
    (339, 'IsPlayersLastRiddenHorse', 0, 0, 0, 0),
    (266, 'IsPleasant', 0, 0, 0, 0),
    ( 62, 'IsRaining', 0, 0, 0, 0),
    (327, 'IsRidingHorse', 0, 0, 0, 0),
    (287, 'IsRunning', 0, 0, 0, 0),
    (103, 'IsShieldOut', 0, 0, 0, 0),
    (286, 'IsSneaking', 0, 0, 0, 0),
    ( 75, 'IsSnowing', 0, 0, 0, 0),
    (223, 'IsSpellTarget', 2, 0, 0, 0),
    (185, 'IsSwimming', 0, 0, 0, 0),
    (141, 'IsTalking', 0, 0, 0, 0),
    (265, 'IsTimePassing', 0, 0, 0, 0),
    (102, 'IsTorchOut', 0, 0, 0, 0),
    (145, 'IsTrespassing', 0, 0, 0, 0),
    (111, 'IsWaiting', 0, 0, 0, 0),
    (101, 'IsWeaponOut', 0, 0, 0, 0),
    (309, 'IsXBox', 0, 0, 0, 0),
    ( 36, 'MenuMode', 1, 0, 0, 0),
    ( 42, 'SameFaction', 2, 0, 0, 0),
    (133, 'SameFactionAsPC', 0, 0, 0, 0),
    ( 43, 'SameRace', 2, 0, 0, 0),
    (134, 'SameRaceAsPC', 0, 0, 0, 0),
    ( 44, 'SameSex', 2, 0, 0, 0),
    (135, 'SameSexAsPC', 0, 0, 0, 0),
    (323, 'WhichServiceMenu', 0, 0, 0, 0),
    (449, 'HasPerk', 2, 1, 1, 2),
    (546, 'GetQuestCompleted', 2, 0, 0, 0),
    (427, 'GetIsVoiceType', 2, 0, 0, 0),
    (523, 'IsPS3', 0, 0, 0, 0),
    (524, 'IsWin32', 0, 0, 0, 0),
    (372, 'IsInList', 2, 0, 0, 0),
    (382, 'GetHasNote', 2, 1, 1, 2),
    (492, 'GetMapMakerVisible', 1, 1, 1, 2),
    (446, 'GetInZone', 2, 1, 1, 2),
    ( 25, 'IsMoving', 0, 0, 0, 0),
    ( 26, 'IsTurning', 0, 0, 0, 0),
    (451, 'IsLastIdlePlayed', 2, 0, 0, 0),
    (399, 'IsWeaponInList', 2, 0, 0, 0),
    (408, 'GetVATSValue', 1, 2, 0, 0),
    (435, 'GetDialogueEmotion', 0, 0, 0, 0),
    (235, 'GetVatsTargetHeight', 0, 0, 0, 0),
    (391, 'GetHitLocation', 0, 0, 0, 0),
    (392, 'IsPC1stPerson', 0, 0, 0, 0),
    (226, 'GetSandman', 0, 0, 0, 0),
    (428, 'GetPlantedExplosive', 0, 0, 0, 0),
    (304, 'IsWaterObject', 0, 0, 0, 0),
    (123, 'IsGreetingPlayer', 0, 0, 0, 0),
    (438, 'GetIsCreatureType', 1, 0, 0, 0),
    (503, 'GetRadiationLevel', 0, 0, 0, 0),
    (431, 'GetHealthPercentage', 0, 0, 0, 0),
    (411, 'GetFactionCombatReaction', 2, 2, 0, 0),
    (515, 'IsCombatTarget', 2, 0, 0, 0),
    (495, 'GetPermanentActorValue', 1, 0, 0, 0),
    (474, 'GetIsAlignment', 1, 0, 0, 0),
    (454, 'GetPlayerTeammate', 0, 0, 0, 0),
    (522, 'GetIsLockBroken', 0, 0, 0, 0),
    (433, 'GetIsObjectType', 1, 0, 0, 0),
    (500, 'GetWeaponHealthPerc', 0, 0, 0, 0),
    (368, 'IsPlayerActionActive', 1, 0, 0, 0),
    (416, 'GetGroupMemberCount', 0, 0, 0, 0),
    (417, 'GetGroupTargetCount', 0, 0, 0, 0),
    (510, 'GetLastHitCritical', 0, 0, 0, 0),
    (450, 'GetFactionRelation', 1, 0, 0, 0),
    (455, 'GetPlayerTeammateCount', 0, 0, 0, 0),
    (219, 'GetAnimAction', 0, 0, 0, 0),
    (430, 'IsActorTalkingThroughActivator', 0, 0, 0, 0),
    (480, 'GetIsUsedItemEquipType', 1, 0, 0, 0),
    (398, 'IsLimbGone', 1, 0, 0, 0),
    (550, 'IsGoreDisabled', 0, 0, 0, 0),
    (420, 'GetObjectiveCompleted', 2, 1, 0, 0),
    (421, 'GetObjectiveDisplayed', 2, 1, 0, 0),
    (397, 'GetCauseofDeath', 0, 0, 0, 0),
    (415, 'Exists', 2, 0, 0, 0),
    (117, 'GetMajorCrimeCount', 0, 0, 0, 0),
    (471, 'GetDestructionStage', 0, 0, 0, 0),
    (460, 'GetActorFactionPlayerEnemy', 0, 0, 0, 0),
    (586, 'IsHardcore', 0, 0, 0, 0),
    (575, 'GetReputationThreshold', 2, 1, 0, 0),
    (610, 'GetCasinoWinningStage', 2, 0, 0, 0),
    (573, 'GetReputation', 2, 1, 0, 0),
    (612, 'PlayerInRegion', 2, 0, 0, 0),
    (601, 'GetForceHitReaction', 0, 0, 0, 0),
    (118, 'GetActorAggroRadiusViolated', 0, 0, 0, 0),
    (192, 'GetIgnoreCrime', 0, 0, 0, 0),
    (367, 'GetLastPlayerAction', 0, 0, 0, 0),
    (370, 'IsTalkingActivatorActor', 2, 0, 0, 0),
    (403, 'HasFriendDisposition', 0, 0, 0, 0),
    (409, 'IsKiller', 2, 0, 0, 0),
    (410, 'IsKillerObject', 2, 0, 0, 0),
    (436, 'GetDialogueEmotionValue', 0, 0, 0, 0),
    (459, 'GetActorCrimePlayerEnemy', 0, 0, 0, 0),
    (462, 'IsPlayerTagSkill', 1, 0, 0, 0),
    (464, 'IsPlayerGrabbedRef', 1, 0, 0, 0),
    (478, 'GetThreatRatio', 2, 0, 0, 0),
    (489, 'GetConcussed', 0, 0, 0, 0),
    (496, 'GetKillingBlowLimb', 0, 0, 0, 0),
    (518, 'GetVATSRightAreaFree', 1, 0, 0, 0),
    (519, 'GetVATSLeftAreaFree', 1, 0, 0, 0),
    (520, 'GetVATSBackAreaFree', 1, 0, 0, 0),
    (521, 'GetVATSFrontAreaFree', 1, 0, 0, 0),
    (525, 'GetVATSRightTargetVisible', 1, 0, 0, 0),
    (526, 'GetVATSLeftTargetVisible', 1, 0, 0, 0),
    (527, 'GetVATSBackTargetVisible', 1, 0, 0, 0),
    (528, 'GetVATSFrontTargetVisible', 1, 0, 0, 0),
    (531, 'IsInCriticalStage', 1, 0, 0, 0),
    (533, 'GetXPForNextLevel', 0, 0, 0, 0),
    (555, 'GetSpellUsageNum', 2, 0, 0, 0),
    (557, 'GetActorsInHigh', 0, 0, 0, 0),
    (558, 'HasLoaded3D', 0, 0, 0, 0),
    (574, 'GetReputationPct', 2, 1, 0, 0),
    (607, 'ChallengeLocked', 2, 0, 0, 0),
    (614, 'GetChallengeCompleted', 2, 0, 0, 0),
    (619, 'IsAlwaysHardcore', 0, 0, 0, 0),

    # extended by NVSE
    (1024, 'GetNVSEVersion', 0, 0, 0, 0),
    (1025, 'GetNVSERevision', 0, 0, 0, 0),
    (1213, 'GetNVSEBeta', 0, 0, 0, 0),
    (1082, 'IsKeyPressed', 1, 0, 0, 0),
    (1166, 'IsControlPressed', 1, 0, 0, 0),
    (1028, 'GetWeight', 2, 0, 0, 0),
    (1165, 'GetWeaponHasScope', 0, 0, 0, 0),
    )
allConditions = set(entry[0] for entry in conditionFunctionData)
fid1Conditions = set(entry[0] for entry in conditionFunctionData if entry[2] == 2)
fid2Conditions = set(entry[0] for entry in conditionFunctionData if entry[3] == 2)
fid3Conditions = set(entry[0] for entry in conditionFunctionData if entry[4] == 2)
fid4Conditions = set(entry[0] for entry in conditionFunctionData if entry[5] == 2)

# Magic Info ------------------------------------------------------------------
weaponTypes = (
    _('Big gun'),
    _('Energy'),
    _('Small gun'),
    _('Melee'),
    _('Unarmed'),
    _('Thrown'),
    _('Mine'),
    )

magicEffects = {
    'ABAT': [5,_('Absorb Attribute'),0.95],
    'ABFA': [5,_('Absorb Fatigue'),6],
    'ABHE': [5,_('Absorb Health'),16],
    'ABSK': [5,_('Absorb Skill'),2.1],
    'ABSP': [5,_('Absorb Magicka'),7.5],
    'BA01': [1,_('Bound Armor Extra 01'),0],#--Formid == 0
    'BA02': [1,_('Bound Armor Extra 02'),0],#--Formid == 0
    'BA03': [1,_('Bound Armor Extra 03'),0],#--Formid == 0
    'BA04': [1,_('Bound Armor Extra 04'),0],#--Formid == 0
    'BA05': [1,_('Bound Armor Extra 05'),0],#--Formid == 0
    'BA06': [1,_('Bound Armor Extra 06'),0],#--Formid == 0
    'BA07': [1,_('Bound Armor Extra 07'),0],#--Formid == 0
    'BA08': [1,_('Bound Armor Extra 08'),0],#--Formid == 0
    'BA09': [1,_('Bound Armor Extra 09'),0],#--Formid == 0
    'BA10': [1,_('Bound Armor Extra 10'),0],#--Formid == 0
    'BABO': [1,_('Bound Boots'),12],
    'BACU': [1,_('Bound Cuirass'),12],
    'BAGA': [1,_('Bound Gauntlets'),8],
    'BAGR': [1,_('Bound Greaves'),12],
    'BAHE': [1,_('Bound Helmet'),12],
    'BASH': [1,_('Bound Shield'),12],
    'BRDN': [0,_('Burden'),0.21],
    'BW01': [1,_('Bound Order Weapon 1'),1],
    'BW02': [1,_('Bound Order Weapon 2'),1],
    'BW03': [1,_('Bound Order Weapon 3'),1],
    'BW04': [1,_('Bound Order Weapon 4'),1],
    'BW05': [1,_('Bound Order Weapon 5'),1],
    'BW06': [1,_('Bound Order Weapon 6'),1],
    'BW07': [1,_('Summon Staff of Sheogorath'),1],
    'BW08': [1,_('Bound Priest Dagger'),1],
    'BW09': [1,_('Bound Weapon Extra 09'),0],#--Formid == 0
    'BW10': [1,_('Bound Weapon Extra 10'),0],#--Formid == 0
    'BWAX': [1,_('Bound Axe'),39],
    'BWBO': [1,_('Bound Bow'),95],
    'BWDA': [1,_('Bound Dagger'),14],
    'BWMA': [1,_('Bound Mace'),91],
    'BWSW': [1,_('Bound Sword'),235],
    'CALM': [3,_('Calm'),0.47],
    'CHML': [3,_('Chameleon'),0.63],
    'CHRM': [3,_('Charm'),0.2],
    'COCR': [3,_('Command Creature'),0.6],
    'COHU': [3,_('Command Humanoid'),0.75],
    'CUDI': [5,_('Cure Disease'),1400],
    'CUPA': [5,_('Cure Paralysis'),500],
    'CUPO': [5,_('Cure Poison'),600],
    'DARK': [3,_('DO NOT USE - Darkness'),0],
    'DEMO': [3,_('Demoralize'),0.49],
    'DGAT': [2,_('Damage Attribute'),100],
    'DGFA': [2,_('Damage Fatigue'),4.4],
    'DGHE': [2,_('Damage Health'),12],
    'DGSP': [2,_('Damage Magicka'),2.45],
    'DIAR': [2,_('Disintegrate Armor'),6.2],
    'DISE': [2,_('Disease Info'),0], #--Formid == 0
    'DIWE': [2,_('Disintegrate Weapon'),6.2],
    'DRAT': [2,_('Drain Attribute'),0.7],
    'DRFA': [2,_('Drain Fatigue'),0.18],
    'DRHE': [2,_('Drain Health'),0.9],
    'DRSK': [2,_('Drain Skill'),0.65],
    'DRSP': [2,_('Drain Magicka'),0.18],
    'DSPL': [4,_('Dispel'),3.6],
    'DTCT': [4,_('Detect Life'),0.08],
    'DUMY': [2,_('Mehrunes Dagon'),0], #--Formid == 0
    'FIDG': [2,_('Fire Damage'),7.5],
    'FISH': [0,_('Fire Shield'),0.95],
    'FOAT': [5,_('Fortify Attribute'),0.6],
    'FOFA': [5,_('Fortify Fatigue'),0.04],
    'FOHE': [5,_('Fortify Health'),0.14],
    'FOMM': [5,_('Fortify Magicka Multiplier'),0.04],
    'FOSK': [5,_('Fortify Skill'),0.6],
    'FOSP': [5,_('Fortify Magicka'),0.15],
    'FRDG': [2,_('Frost Damage'),7.4],
    'FRNZ': [3,_('Frenzy'),0.04],
    'FRSH': [0,_('Frost Shield'),0.95],
    'FTHR': [0,_('Feather'),0.1],
    'INVI': [3,_('Invisibility'),40],
    'LGHT': [3,_('Light'),0.051],
    'LISH': [0,_('Shock Shield'),0.95],
    'LOCK': [0,_('DO NOT USE - Lock'),30],
    'MYHL': [1,_('Summon Mythic Dawn Helm'),110],
    'MYTH': [1,_('Summon Mythic Dawn Armor'),120],
    'NEYE': [3,_('Night-Eye'),22],
    'OPEN': [0,_('Open'),4.3],
    'PARA': [3,_('Paralyze'),475],
    'POSN': [2,_('Poison Info'),0],
    'RALY': [3,_('Rally'),0.03],
    'REAN': [1,_('Reanimate'),10],
    'REAT': [5,_('Restore Attribute'),38],
    'REDG': [4,_('Reflect Damage'),2.5],
    'REFA': [5,_('Restore Fatigue'),2],
    'REHE': [5,_('Restore Health'),10],
    'RESP': [5,_('Restore Magicka'),2.5],
    'RFLC': [4,_('Reflect Spell'),3.5],
    'RSDI': [5,_('Resist Disease'),0.5],
    'RSFI': [5,_('Resist Fire'),0.5],
    'RSFR': [5,_('Resist Frost'),0.5],
    'RSMA': [5,_('Resist Magic'),2],
    'RSNW': [5,_('Resist Normal Weapons'),1.5],
    'RSPA': [5,_('Resist Paralysis'),0.75],
    'RSPO': [5,_('Resist Poison'),0.5],
    'RSSH': [5,_('Resist Shock'),0.5],
    'RSWD': [5,_('Resist Water Damage'),0], #--Formid == 0
    'SABS': [4,_('Spell Absorption'),3],
    'SEFF': [0,_('Script Effect'),0],
    'SHDG': [2,_('Shock Damage'),7.8],
    'SHLD': [0,_('Shield'),0.45],
    'SLNC': [3,_('Silence'),60],
    'STMA': [2,_('Stunted Magicka'),0],
    'STRP': [4,_('Soul Trap'),30],
    'SUDG': [2,_('Sun Damage'),9],
    'TELE': [4,_('Telekinesis'),0.49],
    'TURN': [1,_('Turn Undead'),0.083],
    'VAMP': [2,_('Vampirism'),0],
    'WABR': [0,_('Water Breathing'),14.5],
    'WAWA': [0,_('Water Walking'),13],
    'WKDI': [2,_('Weakness to Disease'),0.12],
    'WKFI': [2,_('Weakness to Fire'),0.1],
    'WKFR': [2,_('Weakness to Frost'),0.1],
    'WKMA': [2,_('Weakness to Magic'),0.25],
    'WKNW': [2,_('Weakness to Normal Weapons'),0.25],
    'WKPO': [2,_('Weakness to Poison'),0.1],
    'WKSH': [2,_('Weakness to Shock'),0.1],
    'Z001': [1,_('Summon Rufio\'s Ghost'),13],
    'Z002': [1,_('Summon Ancestor Guardian'),33.3],
    'Z003': [1,_('Summon Spiderling'),45],
    'Z004': [1,_('Summon Flesh Atronach'),1],
    'Z005': [1,_('Summon Bear'),47.3],
    'Z006': [1,_('Summon Gluttonous Hunger'),61],
    'Z007': [1,_('Summon Ravenous Hunger'),123.33],
    'Z008': [1,_('Summon Voracious Hunger'),175],
    'Z009': [1,_('Summon Dark Seducer'),1],
    'Z010': [1,_('Summon Golden Saint'),1],
    'Z011': [1,_('Wabba Summon'),0],
    'Z012': [1,_('Summon Decrepit Shambles'),45],
    'Z013': [1,_('Summon Shambles'),87.5],
    'Z014': [1,_('Summon Replete Shambles'),150],
    'Z015': [1,_('Summon Hunger'),22],
    'Z016': [1,_('Summon Mangled Flesh Atronach'),22],
    'Z017': [1,_('Summon Torn Flesh Atronach'),32.5],
    'Z018': [1,_('Summon Stitched Flesh Atronach'),75.5],
    'Z019': [1,_('Summon Sewn Flesh Atronach'),195],
    'Z020': [1,_('Extra Summon 20'),0],
    'ZCLA': [1,_('Summon Clannfear'),75.56],
    'ZDAE': [1,_('Summon Daedroth'),123.33],
    'ZDRE': [1,_('Summon Dremora'),72.5],
    'ZDRL': [1,_('Summon Dremora Lord'),157.14],
    'ZFIA': [1,_('Summon Flame Atronach'),45],
    'ZFRA': [1,_('Summon Frost Atronach'),102.86],
    'ZGHO': [1,_('Summon Ghost'),22],
    'ZHDZ': [1,_('Summon Headless Zombie'),56],
    'ZLIC': [1,_('Summon Lich'),350],
    'ZSCA': [1,_('Summon Scamp'),30],
    'ZSKA': [1,_('Summon Skeleton Guardian'),32.5],
    'ZSKC': [1,_('Summon Skeleton Champion'),152],
    'ZSKE': [1,_('Summon Skeleton'),11.25],
    'ZSKH': [1,_('Summon Skeleton Hero'),66],
    'ZSPD': [1,_('Summon Spider Daedra'),195],
    'ZSTA': [1,_('Summon Storm Atronach'),125],
    'ZWRA': [1,_('Summon Faded Wraith'),87.5],
    'ZWRL': [1,_('Summon Gloom Wraith'),260],
    'ZXIV': [1,_('Summon Xivilai'),200],
    'ZZOM': [1,_('Summon Zombie'),16.67],
    }
mgef_school = dict((x,y) for x,[y,z,a] in magicEffects.items())
mgef_name = dict((x,z) for x,[y,z,a] in magicEffects.items())
mgef_basevalue = dict((x,a) for x,[y,z,a] in magicEffects.items())
mgef_school.update(dict((ctypes.cast(x, ctypes.POINTER(ctypes.c_ulong)).contents.value ,y) for x,[y,z,a] in magicEffects.items()))
mgef_name.update(dict((ctypes.cast(x, ctypes.POINTER(ctypes.c_ulong)).contents.value,z) for x,[y,z,a] in magicEffects.items()))
mgef_basevalue.update(dict((ctypes.cast(x, ctypes.POINTER(ctypes.c_ulong)).contents.value,a) for x,[y,z,a] in magicEffects.items()))

hostileEffects = set((
    'ABAT', #--Absorb Attribute
    'ABFA', #--Absorb Fatigue
    'ABHE', #--Absorb Health
    'ABSK', #--Absorb Skill
    'ABSP', #--Absorb Magicka
    'BRDN', #--Burden
    'DEMO', #--Demoralize
    'DGAT', #--Damage Attribute
    'DGFA', #--Damage Fatigue
    'DGHE', #--Damage Health
    'DGSP', #--Damage Magicka
    'DIAR', #--Disintegrate Armor
    'DIWE', #--Disintegrate Weapon
    'DRAT', #--Drain Attribute
    'DRFA', #--Drain Fatigue
    'DRHE', #--Drain Health
    'DRSK', #--Drain Skill
    'DRSP', #--Drain Magicka
    'FIDG', #--Fire Damage
    'FRDG', #--Frost Damage
    'FRNZ', #--Frenzy
    'PARA', #--Paralyze
    'SHDG', #--Shock Damage
    'SLNC', #--Silence
    'STMA', #--Stunted Magicka
    'STRP', #--Soul Trap
    'SUDG', #--Sun Damage
    'TURN', #--Turn Undead
    'WKDI', #--Weakness to Disease
    'WKFI', #--Weakness to Fire
    'WKFR', #--Weakness to Frost
    'WKMA', #--Weakness to Magic
    'WKNW', #--Weakness to Normal Weapons
    'WKPO', #--Weakness to Poison
    'WKSH', #--Weakness to Shock
    ))
hostileEffects |= set((ctypes.cast(x, ctypes.POINTER(ctypes.c_ulong)).contents.value for x in hostileEffects))

#Doesn't list mgefs that use actor values, but rather mgefs that have a generic name
#Ex: Absorb Attribute becomes Absorb Magicka if the effect's actorValue field contains 9
#    But it is actually using an attribute rather than an actor value
#Ex: Burden uses an actual actor value (encumbrance) but it isn't listed since its name doesn't change
genericAVEffects = set([
    'ABAT', #--Absorb Attribute (Use Attribute)
    'ABSK', #--Absorb Skill (Use Skill)
    'DGAT', #--Damage Attribute (Use Attribute)
    'DRAT', #--Drain Attribute (Use Attribute)
    'DRSK', #--Drain Skill (Use Skill)
    'FOAT', #--Fortify Attribute (Use Attribute)
    'FOSK', #--Fortify Skill (Use Skill)
    'REAT', #--Restore Attribute (Use Attribute)
    ])
genericAVEffects |= set((ctypes.cast(x, ctypes.POINTER(ctypes.c_ulong)).contents.value for x in genericAVEffects))

actorValues = [
    _('Strength'), #--00
    _('Intelligence'),
    _('Willpower'),
    _('Agility'),
    _('Speed'),
    _('Endurance'),
    _('Personality'),
    _('Luck'),
    _('Health'),
    _('Magicka'),

    _('Fatigue'), #--10
    _('Encumbrance'),
    _('Armorer'),
    _('Athletics'),
    _('Blade'),
    _('Block'),
    _('Blunt'),
    _('Hand To Hand'),
    _('Heavy Armor'),
    _('Alchemy'),

    _('Alteration'), #--20
    _('Conjuration'),
    _('Destruction'),
    _('Illusion'),
    _('Mysticism'),
    _('Restoration'),
    _('Acrobatics'),
    _('Light Armor'),
    _('Marksman'),
    _('Mercantile'),

    _('Security'), #--30
    _('Sneak'),
    _('Speechcraft'),
    'Aggression',
    'Confidence',
    'Energy',
    'Responsibility',
    'Bounty',
    'UNKNOWN 38',
    'UNKNOWN 39',

    'MagickaMultiplier', #--40
    'NightEyeBonus',
    'AttackBonus',
    'DefendBonus',
    'CastingPenalty',
    'Blindness',
    'Chameleon',
    'Invisibility',
    'Paralysis',
    'Silence',

    'Confusion', #--50
    'DetectItemRange',
    'SpellAbsorbChance',
    'SpellReflectChance',
    'SwimSpeedMultiplier',
    'WaterBreathing',
    'WaterWalking',
    'StuntedMagicka',
    'DetectLifeRange',
    'ReflectDamage',

    'Telekinesis', #--60
    'ResistFire',
    'ResistFrost',
    'ResistDisease',
    'ResistMagic',
    'ResistNormalWeapons',
    'ResistParalysis',
    'ResistPoison',
    'ResistShock',
    'Vampirism',

    'Darkness', #--70
    'ResistWaterDamage',
    ]

acbs = {
    'Armorer': 0,
    'Athletics': 1,
    'Blade': 2,
    'Block': 3,
    'Blunt': 4,
    'Hand to Hand': 5,
    'Heavy Armor': 6,
    'Alchemy': 7,
    'Alteration': 8,
    'Conjuration': 9,
    'Destruction': 10,
    'Illusion': 11,
    'Mysticism': 12,
    'Restoration': 13,
    'Acrobatics': 14,
    'Light Armor': 15,
    'Marksman': 16,
    'Mercantile': 17,
    'Security': 18,
    'Sneak': 19,
    'Speechcraft': 20,
    'Health': 21,
    'Strength': 25,
    'Intelligence': 26,
    'Willpower': 27,
    'Agility': 28,
    'Speed': 29,
    'Endurance': 30,
    'Personality': 31,
    'Luck': 32,
    }

 # Save File Info --------------------------------------------------------------
saveRecTypes = {
    6 : _('Faction'),
    19: _('Apparatus'),
    20: _('Armor'),
    21: _('Book'),
    22: _('Clothing'),
    25: _('Ingredient'),
    26: _('Light'),
    27: _('Misc. Item'),
    33: _('Weapon'),
    35: _('NPC'),
    36: _('Creature'),
    39: _('Key'),
    40: _('Potion'),
    48: _('Cell'),
    49: _('Object Ref'),
    50: _('NPC Ref'),
    51: _('Creature Ref'),
    58: _('Dialog Entry'),
    59: _('Quest'),
    61: _('AI Package'),
    }

# Alchemical Catalogs ---------------------------------------------------------
ingred_alchem = (
    (1,0xCED,_('Alchemical Ingredients I'),250),
    (2,0xCEC,_('Alchemical Ingredients II'),500),
    (3,0xCEB,_('Alchemical Ingredients III'),1000),
    (4,0xCE7,_('Alchemical Ingredients IV'),2000),
    )
effect_alchem = (
    (1,0xCEA,_('Alchemical Effects I'),500),
    (2,0xCE9,_('Alchemical Effects II'),1000),
    (3,0xCE8,_('Alchemical Effects III'),2000),
    (4,0xCE6,_('Alchemical Effects IV'),4000),
    )

# Power Exhaustion ------------------------------------------------------------
orrery = getIdFunc('DLCOrrery.esp')
id_exhaustion = {
    ob(0x014D23): 9, # AbPilgrimsGrace
    ob(0x022A43): 7, # BSLoverKiss
    ob(0x022A3A): 7, # BSRitualMaraGift
    ob(0x022A63): 7, # BSSerpent
    ob(0x022A66): 7, # BSShadowMoonshadow
    ob(0x022A6C): 7, # BSTower
    ob(0x0CB623): 7, # BSTowerWarden
    ob(0x06B69D): 7, # DoomstoneAetherius
    ob(0x06A8EE): 7, # DoomstoneApprentice
    ob(0x06A8EF): 7, # DoomstoneAtronach
    ob(0x06B6A3): 7, # DoomstoneDragon
    ob(0x06B69F): 7, # DoomstoneJode
    ob(0x06B69E): 7, # DoomstoneJone
    ob(0x06A8F2): 7, # DoomstoneLady
    ob(0x06A8F3): 7, # DoomstoneLord
    ob(0x06A8F5): 7, # DoomstoneLover
    ob(0x06A8ED): 7, # DoomstoneMage
    ob(0x06B6A1): 7, # DoomstoneMagnus
    ob(0x06B6B1): 7, # DoomstoneNirn
    ob(0x06A8EC): 7, # DoomstoneRitualMarasMercy
    ob(0x06A8EB): 7, # DoomstoneRitualMarasMilk
    ob(0x06A8F8): 7, # DoomstoneSerpent
    ob(0x06A8F6): 7, # DoomstoneShadow
    ob(0x06B6A2): 7, # DoomstoneShezarr
    ob(0x06B6A0): 7, # DoomstoneSithian
    ob(0x06A8F1): 7, # DoomstoneSteed
    ob(0x06A8F4): 7, # DoomstoneThief
    ob(0x06A8F7): 7, # DoomstoneTower
    ob(0x008E53): 7, # DoomstoneTowerArmor
    ob(0x06A8F0): 7, # DoomstoneWarrior
    ob(0x047AD0): 7, # PwRaceBretonShield
    ob(0x047AD5): 7, # PwRaceDarkElfGuardian
    ob(0x047ADE): 7, # PwRaceImperialAbsorbFatigue
    ob(0x047ADD): 7, # PwRaceImperialCharm
    ob(0x047ADF): 7, # PwRaceKhajiitDemoralize
    ob(0x047AE4): 7, # PwRaceNordFrostDamage
    ob(0x047AE3): 7, # PwRaceNordShield
    ob(0x047AD3): 7, # PwRaceOrcBerserk
    ob(0x047AE7): 7, # PwRaceRedguardFortify
    ob(0x047AE9): 7, # PwRaceWoodElfCommandCreature
    ob(0x03BEDB): 7, # VampireEmbraceofShadows
    ob(0x03BEDC): 7, # VampireReignofTerror
    ob(0x03BED9): 7, # VampireSeduction
    #--Shivering Isles
    ob(0x08F024): 7, # SE02BlessingDementia
    ob(0x08F023): 7, # SE02BlessingMania
    ob(0x03161E): 5, # SE07SaintSpell
    ob(0x03161D): 5, # SE07SeducerSpell
    ob(0x05DD22): 3, # SE14WeatherSpell
    ob(0x081C35): 7, # SE44Frenzy
    ob(0x018DBD): 6, # SEPwSummonDarkSeducer
    ob(0x014B35): 6, # SEPwSummonFleshAtronach
    ob(0x018DBC): 6, # SEPwSummonGoldenSaint
    ob(0x050C76): 3, # SE09PwGKHead1
    ob(0x050C77): 3, # SE09PwGKHead2
    ob(0x050C78): 3, # SE09PwGKHeart1
    ob(0x050C79): 3, # SE09PwGKHeart2
    ob(0x050C7A): 3, # SE09PwGKLeftArm1
    ob(0x050C7B): 3, # SE09PwGKLeftArm2
    ob(0x050C7C): 3, # SE09PwGKLeftArm3
    ob(0x050C82): 3, # SE09PwGKLegs1
    ob(0x050C83): 3, # SE09PwGKLegs2
    ob(0x050C7D): 3, # SE09PwGKRightArm1
    ob(0x050C7E): 3, # SE09PwGKRightArm2
    ob(0x050C7F): 3, # SE09PwGKRightArm3
    ob(0x050C80): 3, # SE09PwGKTorso1
    ob(0x050C81): 3, # SE09PwGKTorso2
    ob(0x08E93F): 3, # SESuicidePower

    #--Orrery
    orrery(0x11DC5F): 7, # Masser's Might
    orrery(0x11DC60): 7, # Masser's Grace
    orrery(0x11DC62): 7, # Secunda's Will
    orrery(0x11DC64): 7, # Secunda's Opportunity
    orrery(0x11DC66): 7, # Masser's Alacrity
    orrery(0x11DC68): 7, # Secunda's Magnetism
    orrery(0x11DC6A): 7, # Secunda's Brilliance
    orrery(0x11DC6C): 7, # Masser's Courage
    }

# Repair Factions -------------------------------------------------------------
#--Formids for npcs which legitimately have no faction membership
repairFactions_legitNullSpells = set((
    #--MS47 Aleswell Invisibility
    0x0002F85F, #Sakeepa
    0x0002F861, #ShagolgroBumph
    0x0002F864, #DiramSerethi
    0x0002F865, #AdosiSerethi
    0x0002F866, #UrnsiSerethi
    ))

repairFactions_legitNullFactions = set((
    #0x00012106, #SEThadon (Between SE07 and SE12) Safer to leave in.
    #0x00012107, #SESyl (Between SE07 and SE12) Safer to leave in.
    #0x00031540, #Mirisa (Only in Cropsford, but doesn't hurt to leave her in it.)
    ))

repairFactions_legitDroppedFactions = set((
    (0x000034CC,0x000034B9), #UlrichLeland CheydinhalGuardFaction
    (0x000034CC,0x000034BB), #UlrichLeland CheydinhalCastleFaction
    (0x000055C2,0x00090E31), #CheydinhalGuardCastlePostDay01 CheydinhalCorruptGuardsFactionMS10
    (0x000055C4,0x00090E31), #CheydinhalGuardCastlePostNight01 CheydinhalCorruptGuardsFactionMS10
    (0x000055C5,0x00090E31), #CheydinhalGuardCastlePostNight02 CheydinhalCorruptGuardsFactionMS10
    (0x000055C7,0x00090E31), #CheydinhalGuardCityPatrolDay02 CheydinhalCorruptGuardsFactionMS10
    (0x000055C8,0x00090E31), #CheydinhalGuardCityPatrolNight01 CheydinhalCorruptGuardsFactionMS10
    (0x000055C9,0x00090E31), #CheydinhalGuardCityPatrolNight02 CheydinhalCorruptGuardsFactionMS10
    (0x000055CB,0x00090E31), #CheydinhalGuardCityPostDay02 CheydinhalCorruptGuardsFactionMS10
    (0x000055CC,0x00090E31), #CheydinhalGuardCityPostNight01 CheydinhalCorruptGuardsFactionMS10
    (0x000055CD,0x00090E31), #CheydinhalGuardCityPostNight02 CheydinhalCorruptGuardsFactionMS10
    (0x000055D2,0x00090E31), #CheydinhalGuardCastlePatrolDay01 CheydinhalCorruptGuardsFactionMS10
    (0x000055D3,0x00090E31), #CheydinhalGuardCastlePatrolNight01 CheydinhalCorruptGuardsFactionMS10
    (0x000055D4,0x00090E31), #CheydinhalGuardCountEscort CheydinhalCorruptGuardsFactionMS10
    (0x000055D5,0x00090E31), #CheydinhalGuardJailorDay CheydinhalCorruptGuardsFactionMS10
    (0x000055D6,0x00090E31), #CheydinhalGuardJailorNight CheydinhalCorruptGuardsFactionMS10
    (0x0000BD60,0x00091ADB), #Larthjar Prisoners
    (0x00012106,0x0001557F), #SEThadon SENewSheothBliss
    (0x00012106,0x0001AD45), #SEThadon SEManiaFaction
    (0x00012106,0x00056036), #SEThadon SE07ManiaHouseFaction
    (0x00012107,0x00013A69), #SESyl SENewSheothFaction
    (0x00012107,0x00015580), #SESyl SENewSheothCrucible
    (0x00012107,0x0001723D), #SESyl SE07ASylFaction
    (0x00012107,0x0001AD46), #SESyl SEDementiaFaction
    (0x00012107,0x0007E0CB), #SESyl SE07DementiaHouseFaction
    (0x0001CF76,0x00009275), #Seridur ICFaction
    (0x0001CF76,0x000947B9), #Seridur SeridurHouseFaction
    (0x0001CF76,0x000980DD), #Seridur OrderoftheVirtuousBlood
    (0x000222A8,0x00028D98), #ReynaldJemane ChorrolFaction
    (0x00023999,0x00028D98), #Jauffre ChorrolFaction
    (0x00023E86,0x000034B7), #GuilbertJemane NewlandsLodgeFaction
    (0x00023E86,0x000034BA), #GuilbertJemane CheydinhalFaction
    (0x00023F2A,0x0001EE1E), #Baurus BladesCG
    (0x00024165,0x0002228F), #Maglir FightersGuild
    (0x00024E0A,0x000272BE), #Jeelius MythicDawnPrisoner
    (0x00026D9A,0x00009275), #AudensAvidius ICFaction
    (0x00026D9A,0x0003486F), #AudensAvidius ImperialWatch
    (0x00026D9A,0x00083595), #AudensAvidius CourierCustomers
    (0x00026D9A,0x0018B117), #AudensAvidius ImperialLegion
    (0x0002AB4E,0x0002AB4D), #Umbacano UmbacanoFaction
    (0x0002AF3E,0x0002AEFA), #Srazirr ClaudeMaricThugFaction
    (0x0002CD21,0x00022296), #Falcar MagesGuild
    (0x0002D01E,0x00035EA9), #Jskar BrumaFaction
    (0x0002D8C0,0x00022296), #Kalthar MagesGuild
    (0x00032940,0x000C48A1), #MG16NecromancerMale1 MG16FortOntusMageFaction
    (0x00032941,0x000C48A1), #MG16NecromancerFemale2 MG16FortOntusMageFaction
    (0x00032943,0x000C48A1), #MG16NecromancerMale2 MG16FortOntusMageFaction
    (0x00033907,0x0003B3F6), #Martin KvatchFaction
    (0x00033B8B,0x000C48A1), #MG16NecromancerFemale3 MG16FortOntusMageFaction
    (0x00033B8D,0x000C48A1), #MG16NecromancerMale3 MG16FortOntusMageFaction
    (0x0003486E,0x00009275), #HieronymusLex ICFaction
    (0x0003486E,0x0003486F), #HieronymusLex ImperialWatch
    (0x00034E86,0x00029F82), #Cingor MythicDawn
    (0x00034EAD,0x00022296), #Caranya MagesGuild
    (0x0003529A,0x00024164), #MyvrynaArano ThievesGuild
    (0x0003529A,0x0003AB39), #MyvrynaArano ICWaterfrontResident
    (0x0003563B,0x00028E77), #Amusei SkingradFaction
    (0x00035649,0x00028E77), #MercatorHosidus SkingradFaction
    (0x00035649,0x0002A09C), #MercatorHosidus SkingradCastleFaction
    (0x00035ECB,0x00035EA9), #Jearl BrumaFaction
    (0x0003628D,0x00009274), #VelwynBenirus AnvilFaction
    (0x0004EF69,0x00090E31), #CheydinhalGuardCityPostDay03 CheydinhalCorruptGuardsFactionMS10
    (0x0004EFF9,0x00090E31), #CheydinhalGuardCityPostDay04 CheydinhalCorruptGuardsFactionMS10
    (0x0004EFFA,0x00090E31), #CheydinhalGuardCityPostNight04 CheydinhalCorruptGuardsFactionMS10
    ))

# Messages Text ===============================================================
messagesHeader = """<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
	<title>Private Message Archive</title>
	<style type="text/css">
		html{
			overflow-x: auto;
		}

		body{
			background-color: #fff;
			color: #000;
			font-family: Verdana, Tahoma, Arial, sans-serif;
			font-size: 11px;
			margin:0px;
			padding:0px;
			text-align:center;
			}

		a:link, a:visited, a:active{
			color: #000;
			text-decoration: underline;
		}

		a:hover{
			color: #465584;
			text-decoration:underline;
		}

		img{
			border: 0;
			vertical-align: middle;
		}

		#ipbwrapper{
			margin: 0 auto 0 auto;
			text-align: left;
			width: 95%;
		}

		.post1{
			background-color: #F5F9FD;
		}

		.post2{
			background-color: #EEF2F7;
		}

		/* Common elements */
		.row1{
			background-color: #F5F9FD;
		}

		.row1{
			background-color: #DFE6EF;
		}

		.row3{
			background-color: #EEF2F7;
		}

		.row2{
			background-color: #E4EAF2;
		}

		/* tableborders gives the white column / row lines effect */
		.plainborder{
			background-color: #F5F9FD
			border: 1px solid #345487;
		}

		.tableborder{
			background-color: #FFF;
			border: 1px solid #345487;
			margin: 0;
			padding: 0;
		}

		.tablefill{
			background-color: #F5F9FD;
			border: 1px solid #345487;
			padding: 6px;
		}

		.tablepad{
			background-color: #F5F9FD;
			padding:6px;
		}

		.tablebasic{
			border: 0;
			margin: 0;
			padding: 0;
			width:100%;
		}

		.pformstrip{
			background-color: #D1DCEB;
			color: #3A4F6C;
			font-weight: bold;
			margin-top:1px
			padding:7px;
		}

		#QUOTE{
			background-color: #FAFCFE;
			border: 1px solid #000;
			color: #465584;
			font-family: Verdana, Arial;
			font-size: 11px;
			padding: 2px;
		}

		#CODE{
			background-color: #FAFCFE;
			border: 1px solid #000;
			color: #465584;
			font-family: Courier, Courier New, Verdana, Arial;
			font-size: 11px;
			padding: 2px;
		}
		/* Main table top (dark blue gradient by default) */
		.maintitle{
			background-color: #D1DCEB;
			color: #FFF;
			font-weight: bold;
			padding:8px 0px 8px 5px;
			vertical-align:middle;
		}

		.maintitle a:link, .maintitle  a:visited, .maintitle  a:active{
			color: #fff;
			text-decoration: none;
		}

		.maintitle a:hover{
			text-decoration: underline;
		}

		/* Topic View elements */
		.signature{
			color: #339;
			font-size: 10px;
			line-height:150%;
		}

		.postdetails{
			font-size: 10px;
		}

		.postcolor{
			font-size: 12px;
			line-height: 160%;
		}
		/* Quote/Code formatting */
		.quotetop {
			color: #fff;
			background-color: #B1C9ED;
			margin: 1em;
			margin-bottom: 0;
			padding: 0.5em;
		}

        .quotemain {
            margin: 0 1em;
            padding: 0.5em;
            border: solid 1px #000;
        }

        .codetop {
            font-family: monospace;
            color: #fff;
            background-color: #A0A0A0;
            margin: 1em;
            margin-bottom: 0;
            padding: 0.5em;
        }

        .codemain {
            font-family: monospace;
            margin: 0 1em;
            padding: 0.5em;
            border: solid 1px #000;
        }
    </style>
</head>
<body><div id="ipbwrapper">\n"""
