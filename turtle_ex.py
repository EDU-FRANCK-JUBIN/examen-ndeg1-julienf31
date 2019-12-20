import turtle as tu
import random

# Initialisation du jeu
ts = tu.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup(width=1400, height=800, startx=0, starty=0)

# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs

michelangelo = tu.Turtle("turtle")
michelangelo.up()
michelangelo.color("orange")
michelangelo.setpos(-620, 320)
michelangelo.down()

leonardo = tu.Turtle("turtle")
leonardo.up()
leonardo.color("deep sky blue")
leonardo.setpos(-620, 165)
leonardo.down()

raphael = tu.Turtle("turtle")
raphael.up()
raphael.color("red")
raphael.setpos(-620, 0)
raphael.down()

donatello = tu.Turtle("turtle")
donatello.up()
donatello.color("purple")
donatello.setpos(-620, -145)
donatello.down()

splinter = tu.Turtle("turtle")
splinter.up()
splinter.color("Dark Slate Gray")
splinter.setpos(-620, -300)
splinter.down()

# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3
player1 = input("Joueur 1 : Saisissez votre pronostic")
player2 = input("Joueur 2 : Saisissez votre pronostic")

turtles = [
    michelangelo,
    leonardo,
    raphael,
    donatello,
    splinter
]
wins = [

]

# Mon écran est trop petit je ne voit pas la ligne d'arrivée ni même les polygones de départ en entier donc je l'ai simulée moins loin
# Mais changez la variable ci dessous en fonction de votre écran
arrival = 300


def allTurtleFinished():
    all_ok = True
    for turtle in turtles:
        if (turtle.xcor() < arrival):
            all_ok = False
    return all_ok

def checkResults():
    p1_point = 0
    p2_point = 0
    for i in wins[0:3]:
        p1 = 30
        for p in player1.split(','):
            if int(p) == i:
                p1_point += p1
            p1-=10
        p2 = 30
        for p in player2.split(','):
            if int(p) == i:
                p2_point += p2
            p2 -= 10
    return p1_point, p2_point


# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite
while (not allTurtleFinished()):
    i = 1
    for turtle in turtles:
        if turtle.xcor() < arrival:
            turtle.fd(random.randint(0, 5))
            if turtle.xcor() >= arrival:
                wins.append(i)
        i += 1



player1, player2 = checkResults()
print(wins)

# Comparer les rÃ©sultats de la course avec les pronostics des joueurs
# et afficher le rÃ©sultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0
# A IMPLEMENTER

turtle_arbitre = tu.Turtle()
turtle_arbitre.color("Black")
if player1 > player2:
    turtle_arbitre.write("Le joueur 1 a  gagné", move=True, align="left", font=("Arial", 16, "normal"))

elif player2 > player1:
    turtle_arbitre.write("Le joueur 2 a  gagné", move=True, align="left", font=("Arial", 16, "normal"))

elif player1 == player2:
    turtle_arbitre.write("Egalité", move=True, align="left", font=("Arial", 16, "normal"))

tu.mainloop()
