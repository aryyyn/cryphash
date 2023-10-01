#hash function to be implemented here:
import data #importing all the data from data.py


def hash(word): #creating a function to convert the text into encrypted text
    
    encrypted = []
    for letter in word:
        for item in (data.a, data.b, data.c, data.d, data.e, data.f, data.g, data.h, data.i, data.j, data.k, data.l, data.m, data.n, data.o, data.p, data.q, data.r, data.s, data.t, data.u, data.v, data.w, data.x, data.y, data.z):
            if letter in item:
                print("found")
            else:
                item.index(letter)
            
    

