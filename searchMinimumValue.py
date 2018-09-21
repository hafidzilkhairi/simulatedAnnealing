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

def swap(x,y):
    return x,y

def tampil(a,b,c):
    print("(", a, ",", b, ")", c)

def start():
    T = 1000
    x,y = swap(hasilRandom(),hasilRandom())
    solusi = hasilOperasi(x, y)
    
    while(T>1):
        xNew, yNew = swap(hasilRandom(),hasilRandom())
        solusiNew = hasilOperasi(xNew, yNew)
        delta = solusiNew - solusi
        if(delta < 0):
            x,y = swap(xNew,yNew)
            solusi = solusiNew
        elif ((math.exp(-delta/T) > (random.uniform(0, 1)))):
            x = xNew
            y = yNew
            if(solusi>solusiNew):
                solusi = solusiNew
            T = 0.85 * T
    tampil(x,y,solusi)

start()
