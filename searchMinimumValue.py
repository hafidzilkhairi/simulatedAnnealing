import math
import random
import time
def hasilOperasi(x,y):
    sinus = math.sin(x)
    cosinus = math.cos(y)
    dalam = math.sqrt(x*x+y*y)/math.pi
    eksponen = math.exp(math.fabs(1-dalam))
    hasil = -(math.fabs(sinus*cosinus*eksponen))
    return hasil


def hasilRandom():
    return (-10 + 20 * random.uniform(0,1))


def start():
    T = 1000000
    x = hasilRandom()
    y = hasilRandom()
    solusi = hasilOperasi(x, y)
    T = 1000000
    while(T>1):
        xNew = hasilRandom()
        yNew = hasilRandom()
        solusiNew = hasilOperasi(xNew, yNew)
        delta = solusiNew - solusi
        if(delta < 0):
            x = xNew
            y = yNew
            solusi = solusiNew
            print("Masuk if")
        elif ((math.exp(-delta/T) > (random.uniform(0, 1)))):
            x = xNew
            y = yNew
            solusi = solusiNew
            T = 0.6 * T
            print("Masuk else")
    print(solusi)

start()
