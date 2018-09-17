import math
import random
def hasilOperasi(x,y):
    sinus = math.sin(x)
    cosinus = math.cos(y)
    dalam = math.sqrt(x*x+y*y)/math.pi
    eksponen = math.exp(math.fabs(1-dalam))
    hasil = -(math.fabs(sinus*cosinus*eksponen))
    return hasil


def hasilRandom():
    return (-10 + 20 * random.uniform(0,1))

print(hasilRandom())