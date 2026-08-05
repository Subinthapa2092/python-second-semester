import sys
sys.path.append("C:/Users/Lenovo/Desktop/python programming")
from Game.Characters.players import play 
from Game.Weapons.guns import fire 
from Game.Weapons.knife import fight 
from Game.Characters.boss import playNegative
play()
fire()
fight()
playNegative()