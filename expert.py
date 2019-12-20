from easygui import *
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, saigne, choquee, malaise, brulure, inconscient,noPouls')
pyDatalog.create_terms('pansement, pls,defibriller')

defibriller(X) <= inconscient(X) & noPouls(X)
pansement(X) <= saigne(X)
pls(X) <= malaise(X)

msg = "Informations"
fields = ('Prénom','Nom','Lieu','Nombre de victimes','Etat des victimes','Obstacles potentiels')
informations = multenterbox(msg,msg,fields)

victimes = informations[3]
print(victimes)

etats = [
    'bien',
    'pas bien',
    'vraiment pas bien'
]

victime_count = 1;
for p in range(int(victimes)):
    choice = choicebox('Etat victime ' + str(victime_count),'Choisir dans la liste :',etats)
    victime_count += 1
