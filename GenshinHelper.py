# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:20:17 2021

@author: simek
"""

import pygame
import datetime

pygame.init()

wymiaryokna=(800,600)
kolortla=(212, 185, 112)

GH=pygame.display.set_mode(wymiaryokna)
pygame.display.set_caption("GenshinHelper")
#font = pygame.font.Font(None, 23)
font=pygame.font.SysFont("comicsansms",15)
GH.fill(kolortla)


class bohater(object):
    def __init__(self, grafika, dz, ksiazka):
        self.grafika=grafika
        self.miejsce=[0,0] #470,30 pierwszy + 117 kolejny
        self.dz=dz
        self.ksiazka=ksiazka
    def rysuj(self, okno):
        okno.blit(self.grafika, (self.miejsce[0], self.miejsce[1]))
        
class bron(object):
    def __init__(self, grafika, dz, tekst):
        self.grafika=grafika
        self.miejsce=[0,0] #470, 30 pierwszy + 58 kolejny
        self.dz=dz
        self.tekst=tekst
    def rysuj(self, okno):
        okno.blit(self.grafika, (self.miejsce[0], self.miejsce[1]))
    def dymek(self, okno, myszka):
        txt=(len(self.tekst)+1)*9
        pygame.draw.rect(okno, (0,0,0), [myszka[0]-txt-5, myszka[1]-18, txt+5, 32])
        okno.blit(font.render(self.tekst,True,(255,255,255)), (myszka[0]-txt,myszka[1]-13))

albedo=bohater(pygame.image.load('bohaterowie/albedo.jpg'),[2,5],0)
amber=bohater(pygame.image.load('bohaterowie/amber.jpg'),[0,3],2)
barbara=bohater(pygame.image.load('bohaterowie/barbara.jpg'),[0,3],2)
beidou=bohater(pygame.image.load('bohaterowie/beidou.jpg'),[2,5],2)
bennett=bohater(pygame.image.load('bohaterowie/bennett.jpg'),[1,4],5)
chongyun=bohater(pygame.image.load('bohaterowie/chongyun.jpg'),[1,4],1)
diluc=bohater(pygame.image.load('bohaterowie/diluc.jpg'),[1,4],5)
diona=bohater(pygame.image.load('bohaterowie/diona.jpg'),[0,3],2)
fischl=bohater(pygame.image.load('bohaterowie/fischl.jpg'),[2,5],0)
ganyu=bohater(pygame.image.load('bohaterowie/ganyu.jpg'),[1,4],1)
jean=bohater(pygame.image.load('bohaterowie/jean.jpg'),[1,4],5)
kaeya=bohater(pygame.image.load('bohaterowie/kaeya.jpg'),[2,5],0)
keqing=bohater(pygame.image.load('bohaterowie/keqing.jpg'),[0,3],4)
klee=bohater(pygame.image.load('bohaterowie/klee.jpg'),[0,3],2)
lisa=bohater(pygame.image.load('bohaterowie/lisa.jpg'),[2,5],0)
mona=bohater(pygame.image.load('bohaterowie/mona.jpg'),[1,4],5)
ningguang=bohater(pygame.image.load('bohaterowie/ningguang.jpg'),[0,3],4)
noelle=bohater(pygame.image.load('bohaterowie/noelle.jpg'),[1,4],5)
qiqi=bohater(pygame.image.load('bohaterowie/qiqi.jpg'),[0,3],4)
razor=bohater(pygame.image.load('bohaterowie/razor.jpg'),[1,4],5)
sucrose=bohater(pygame.image.load('bohaterowie/sucrose.jpg'),[0,3],2)
tartaglia=bohater(pygame.image.load('bohaterowie/tartaglia.jpg'),[0,3],2)
venti=bohater(pygame.image.load('bohaterowie/venti.jpg'),[2,5],0)
xiangling=bohater(pygame.image.load('bohaterowie/xiangling.jpg'),[1,4],1)
xiao=bohater(pygame.image.load('bohaterowie/xiao.jpg'),[0,3],4)
xingqiu=bohater(pygame.image.load('bohaterowie/xingqiu.jpg'),[2,5],3)
xinyan=bohater(pygame.image.load('bohaterowie/xin-yan.jpg'),[2,5],3)
zhongli=bohater(pygame.image.load('bohaterowie/zhongli.jpg'),[2,5],3)

AlleyHunter=bron(pygame.image.load('bronie/Alley Hunter.png'),[1,4], 'Alley Hunter' )
AmosBow=bron(pygame.image.load('bronie/Amos\' Bow.png'),[2,5], 'Amos\' Bow')
AquilaFavonia=bron(pygame.image.load('bronie/Aquila Favonia.png'),[0,3], 'Aquila Favonia')
BlackcliffAgate=bron(pygame.image.load('bronie/Blackcliff Amulet.png'),[0,3], 'Blackcliff Amulet')
BlackcliffLongsword=bron(pygame.image.load('bronie/Blackcliff Longsword.png'),[1,4], 'Blackcliff Longsword')
BlackcliffPole=bron(pygame.image.load('bronie/Blackcliff Pole.png'),[0,3], 'Blackcliff Pole')
BlackcliffSlasher=bron(pygame.image.load('bronie/Blackcliff Slasher.png'),[1,4], 'Blackcliff Slasher')
BlackcliffWarbow=bron(pygame.image.load('bronie/Blackcliff Warbow.png'),[0,3], 'Blackcliff Warbow')
CompoundBow=bron(pygame.image.load('bronie/Compound Bow.png'),[2,5], 'Compound Bow')
CrescentPike=bron(pygame.image.load('bronie/Crescent Pike.png'),[0,3], 'Crescent Pike')
Deathmatch=bron(pygame.image.load('bronie/Deathmatch.png'),[1,4], 'Deathmatch')
DragonsBane=bron(pygame.image.load('bronie/Dragon\'s Bane.png'),[1,4], 'Dragon\'s Bane')
DragonspineSpear=bron(pygame.image.load('bronie/Dragonspine Spear.png'),[1,4], 'Dragonspine Spear')
DreamofDragonfell=bron(pygame.image.load('bronie/Dream of Dragonfell.png'),[0,3], 'Dream of Dragonfell')
EyeofPerception=bron(pygame.image.load('bronie/Eye of Perception.png'),[1,4], 'Eye of Perception')
FavoniusCodex=bron(pygame.image.load('bronie/Favonius Codex.png'),[0,3], 'Favonius Codex')
FavoniusGreatsword=bron(pygame.image.load('bronie/Favonius Greatsword.png'),[2,5],'Favonius Greatsword')
FavoniusLance=bron(pygame.image.load('bronie/Favonius Lance.png'),[2,5], 'Favonius Lance')
FavoniusSword=bron(pygame.image.load('bronie/Favonius Sword.png'),[0,3], 'Favonius Sword')
FavoniusWarbow=bron(pygame.image.load('bronie/Favonius Warbow.png'),[2,5], 'Favonius Warbow')
FesteringDesire=bron(pygame.image.load('bronie/Festering Desire.png'),[2,5], 'Festering Desire')
IronSting=bron(pygame.image.load('bronie/Iron Sting.png'),[2,5], 'Iron Sting')
LionsRoar=bron(pygame.image.load('bronie/Lion\'s Roar.png'),[0,3], 'Lion\'s Roar')
LithicBlade=bron(pygame.image.load('bronie/Lithic Blade.png'),[0,3], 'Lithic Blade')
LithicSpear=bron(pygame.image.load('bronie/Lithic Spear.png'),[2,5], 'Lithic Spear')
LostPrayertotheSacredWinds=bron(pygame.image.load('bronie/Lost Prayer to the Sacred Winds.png'),[2,5], 'Lost Prayer to the Sacred Winds')
MappaMare=bron(pygame.image.load('bronie/Mappa Mare.png'),[2,5], 'Mappa Mare')
MemoryofDust=bron(pygame.image.load('bronie/Memory of Dust.png'),[2,5], 'Memory of Dust')
PrimordialJadeWingedSpear=bron(pygame.image.load('bronie/Primordial Jade Winged Spear.png'),[0,3], 'Primordial Jade Winged Spear')
PrototypeAminus=bron(pygame.image.load('bronie/Prototype Aminus.png'),[2,5], 'Prototype Aminus')
PrototypeCrescent=bron(pygame.image.load('bronie/Prototype Crescent.png'),[1,4], 'Prototype Crescent')
PrototypeMalicer=bron(pygame.image.load('bronie/Prototype Malice.png'),[1,4], 'Prototype Malice')
PrototypeRancour=bron(pygame.image.load('bronie/Prototype Rancour.png'),[1,4], 'Prototype Rancour')
PrototypeStarglitter=bron(pygame.image.load('bronie/Prototype Starglitter.png'),[2,5], 'Prototype Starglitter')
Rainslasher=bron(pygame.image.load('bronie/Rainslasher.png'),[1,4], 'Rainslasher')
RoyalBow=bron(pygame.image.load('bronie/Royal Bow.png'),[2,5], 'Royal Bow')
RoyalGreatsword=bron(pygame.image.load('bronie/Royal Greatsword.png'),[2,5], 'Royal Greatsword')
RoyalGrimoire=bron(pygame.image.load('bronie/Royal Grimoire.png'),[0,3], 'Royal Grimoire')
RoyalLongsword=bron(pygame.image.load('bronie/Royal Longsword.png'),[0,3], 'Royal Longsword')
RoyalSpear=bron(pygame.image.load('bronie/Royal Spear.png'),[1,4], 'Royal Spear')
RustBow=bron(pygame.image.load('bronie/Rust Bow.png'),[0,3], 'Rust Bow')
SacrificialBow=bron(pygame.image.load('bronie/Sacrificial Bow.png'),[1,4], 'Sacrificial Bow')
SacrificialGreatsword=bron(pygame.image.load('bronie/Sacrificial Greatsword.png'),[1,4], 'Sacrificial Greatsword')
SacrificialSword=bron(pygame.image.load('bronie/Sacrificial Sword.png'),[2,5], 'Sacrificial Sword')
SacrificialFragments=bron(pygame.image.load('bronie/Sacrificial Fragments.png'),[2,5], 'Sacrificial Fragments')
SerpentSpine=bron(pygame.image.load('bronie/Serpent Spine.png'),[2,5], 'Serpent Spine')
SkywardAtlas=bron(pygame.image.load('bronie/Skyward Atlas.png'),[1,4], 'Skyward Atlas')
SkywardBlade=bron(pygame.image.load('bronie/Skyward Blade.png'),[1,4], 'Skyward Blade')
SkywardHarpr=bron(pygame.image.load('bronie/Skyward Harp.png'),[1,4], 'Skyward Harp')
SkywardPride=bron(pygame.image.load('bronie/Skyward Pride.png'),[1,4], 'Skyward Pride')
SkywardSpine=bron(pygame.image.load('bronie/Skyward Spine.png'),[2,5], 'Skyward Spine')
SnowTombedStarsilver=bron(pygame.image.load('bronie/Snow Tombed Starsilver.png'),[0,3], 'Snow Tombed Starsilver')
SolarPearl=bron(pygame.image.load('bronie/Solar Pearl.png'),[0,3], 'Solar Pearl')
SummitShaper=bron(pygame.image.load('bronie/Summit Shaper.png'),[0,3], 'Summit Shaper')
SwordofDescension=bron(pygame.image.load('bronie/Sword of Descension.png'),[1,4], 'Sword of Descension')
TheAlleyFlash=bron(pygame.image.load('bronie/The Alley Flash.png'),[2,5], 'The Alley Flash')
TheBell=bron(pygame.image.load('bronie/The Bell.png'),[0,3], 'The Bell')
TheBlackSword=bron(pygame.image.load('bronie/The Black Sword.png'),[1,4], 'The Black Sword')
TheFlute=bron(pygame.image.load('bronie/The Flute.png'),[1,4], 'The Flute')
TheStringless=bron(pygame.image.load('bronie/The Stringless.png'),[0,3], 'The Stringless')
TheUnforgedr=bron(pygame.image.load('bronie/The Unforged.png'),[1,4], 'The Unforged')
TheVriridescentHunt=bron(pygame.image.load('bronie/The Vriridescent Hunt.png'),[0,3], 'The Vriridescent Hunt')
TheWidsith=bron(pygame.image.load('bronie/The Widsith.png'),[1,4], 'The Widsith')
VortexVanquisher=bron(pygame.image.load('bronie/Vortex Vanquisher.png'),[2,5], 'Vortex Vanquisher')
Whiteblind=bron(pygame.image.load('bronie/Whiteblind.png'),[0,3], 'Whiteblind')
WineandSong=bron(pygame.image.load('bronie/Wine and Song.png'),[1,4], 'Wine and Song')
WolfsGravestone=bron(pygame.image.load('bronie/Wolf\'s Gravestone.png'),[2,5], 'Wolf\'s Gravestone')


bohaterowie=[albedo,amber,barbara,beidou,bennett,chongyun,diluc,diona,fischl,ganyu,jean,kaeya,keqing,klee,lisa,mona,ningguang,noelle,qiqi,razor,sucrose,tartaglia,venti,xiangling,xiao,xingqiu,xinyan,zhongli]

pon=[]
wt=[]
sr=[]
czw=[]
pt=[]
sob=[]
btydz=[pon,wt,sr,czw,pt,sob]

bronie=[AlleyHunter, AmosBow, AquilaFavonia, BlackcliffAgate, BlackcliffLongsword, BlackcliffPole, BlackcliffSlasher, BlackcliffWarbow, CompoundBow, CrescentPike, Deathmatch, DragonsBane, DragonspineSpear, DreamofDragonfell, EyeofPerception, FavoniusCodex, FavoniusGreatsword, FavoniusLance, FavoniusSword, FavoniusWarbow, FesteringDesire, IronSting, LionsRoar, LithicBlade, LithicSpear, LostPrayertotheSacredWinds, MappaMare, MemoryofDust, PrimordialJadeWingedSpear, PrototypeAminus, PrototypeCrescent, PrototypeMalicer, PrototypeRancour, PrototypeStarglitter, Rainslasher, RoyalBow, RoyalGreatsword, RoyalGrimoire, RoyalLongsword, RoyalSpear, RustBow, SacrificialBow, SacrificialFragments, SacrificialGreatsword, SacrificialSword, SkywardAtlas, SkywardBlade, SkywardHarpr, SkywardPride, SkywardSpine, SnowTombedStarsilver, SolarPearl, SummitShaper, SwordofDescension, TheAlleyFlash, TheBell, TheBlackSword,TheFlute,TheStringless,TheUnforgedr,TheVriridescentHunt,TheWidsith, VortexVanquisher, Whiteblind, WineandSong, WolfsGravestone]

ponb=[]
wtb=[]
srb=[]
czwb=[]
ptb=[]
sobb=[]
tydzb=[ponb,wtb,srb,czwb,ptb,sobb]


class dni(object):
    def __init__(self, miejsce, tekst):
        self.miejsce=miejsce
        self.tekst=tekst
        self.rozmiar=(50,25)
        self.ramka=-1
        self.kolor=(195, 140, 30)        
    def rysuj(self, okno):
        pygame.draw.rect(okno, self.kolor, [self.miejsce[0], self.miejsce[1], self.rozmiar[0], self.rozmiar[1]], self.ramka)
        okno.blit(font.render(self.tekst, True, (0,0,0)), (self.miejsce[0]+self.rozmiar[0]/4,self.miejsce[1]+self.rozmiar[1]/4))
        
tydz=[dni((450,0),"Pon."),dni((500,0),"Wt."),dni((550,0),"Sr."),dni((600,0),"Czw."), dni((650,0),"Pt."),dni((700,0),"Sob."), dni((750,0),"Ndz.")]
zakladki=[dni((330,25),"Bohaterowie"), dni((330,50), "Bronie")]
for x in zakladki:
    x.rozmiar=(120,25)

dzien=datetime.date.weekday(datetime.date.today())
tydz[dzien].ramka=0

def buduj_dzien(dz, bohaterowie):
    global btydz
    x=470
    y=30
    for k in bohaterowie:
        if dz in k.dz:
            k.miejsce[0]=x
            k.miejsce[1]=y
            btydz[dz].append(k)
            x+=117
            if x>800:
                x=470
                y+=130

def buduj_dzienb(dz, bronie):
    global tydzb
    x=460
    y=30
    for k in bronie:
        if dz in k.dz:
            k.miejsce[0]=x
            k.miejsce[1]=y
            tydzb[dz].append(k)
            x+=58
            if x>800:
                x=460
                y+=65



mode=0
running=True

class talent(object):
    def __init__(self,tekst,grafika):
        self.miejsce=[0,0]
        self.tekst=tekst
        self.grafika=grafika
    def rysuj(self, okno):
        txt=(len(self.tekst)+1)*7
        pygame.draw.rect(okno, (0,0,0), [self.miejsce[0]-txt-5, self.miejsce[1]-18, txt+5, 32])
        okno.blit(font.render(self.tekst,True,(255,255,255)), (self.miejsce[0]-txt,self.miejsce[1]-13))
        okno.blit(self.grafika,[self.miejsce[0]-txt-70, self.miejsce[1]-18])
        

ballad=talent("Book of Ballad", pygame.image.load('ksiazki/ballad.png'))
diligence=talent("Book of Diligence", pygame.image.load('ksiazki/diligence.png'))
freedom=talent("Book of Freedom", pygame.image.load('ksiazki/freedom.png'))
gold=talent("Book of Gold", pygame.image.load('ksiazki/gold.png'))
prosperity=talent("Book of Prosperity", pygame.image.load('ksiazki/prosperity.png'))
resistance=talent("Book of Resistance", pygame.image.load('ksiazki/resistance.png'))

ksiazki=[ballad,diligence,freedom,gold,prosperity,resistance]

while running:
    myszka=pygame.mouse.get_pos() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False    
        if event.type == pygame.MOUSEBUTTONDOWN:
            i=0
            for x in tydz:
                if x.miejsce[0]<myszka[0] and x.miejsce[0]+x.rozmiar[0]>myszka[0] and x.miejsce[1]<myszka[1] and x.miejsce[1]+x.rozmiar[1]>myszka[1]:
                    dzien=i
                    break
                i+=1
            i=0
            for x in zakladki:
                if x.miejsce[0]<myszka[0] and x.miejsce[0]+x.rozmiar[0]>myszka[0] and x.miejsce[1]<myszka[1] and x.miejsce[1]+x.rozmiar[1]>myszka[1]:
                    mode=i
                    break
                i+=1
    
    GH.fill(kolortla) #Żeby nie zostawał slad na tle
    
    for i in range(len(tydz)):
        tydz[i].ramka=-1
        if i==dzien:
            tydz[i].ramka=0
        tydz[i].rysuj(GH)
        
    for i in range(len(zakladki)):
        zakladki[i].ramka=-1
        if i==mode:
            zakladki[i].ramka=0
        zakladki[i].rysuj(GH)

    pygame.draw.rect(GH, (195, 140, 30), [450, 25, 800-450, 600-25], 0) #Kwadrat do dni
    
    if mode==0:
        if dzien!=6:
            if btydz[dzien]==[]:
                buduj_dzien(dzien, bohaterowie)
            for x in btydz[dzien]:
                x.rysuj(GH)
            for x in btydz[dzien]:
                if x.miejsce[0]<myszka[0] and x.miejsce[0]+100>myszka[0] and x.miejsce[1]<myszka[1] and x.miejsce[1]+120>myszka[1]: 
                    ksiazki[x.ksiazka].miejsce=myszka
                    ksiazki[x.ksiazka].rysuj(GH)
        else:
            GH.blit(font.render("W niedziele dropią wszystkie materiały", True, (0,0,0)), (470,35))
    elif mode==1:
        if dzien!=6:
            if tydzb[dzien]==[]:
                buduj_dzienb(dzien, bronie)
            for x in tydzb[dzien]:
                x.rysuj(GH)
            for x in tydzb[dzien]:
                if x.miejsce[0]<myszka[0] and x.miejsce[0]+50>myszka[0] and x.miejsce[1]<myszka[1] and x.miejsce[1]+60>myszka[1]:
                    x.dymek(GH,myszka)
        else:
            GH.blit(font.render("W niedziele dropią wszystkie materiały", True, (0,0,0)), (470,35))
    
        
    pygame.display.update()
    
pygame.quit()