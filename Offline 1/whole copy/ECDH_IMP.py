import random
import time
from prettytable import PrettyTable
#curve : # Secp256k1: y^2 = x^3 + ax + b = y^2 = x^3 + 7
a=0; b=7

#base point
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240, 
     32670510020758816978083085130507043184471273380659243275938904335757337482424)

# modulo
p = pow(2, 256) - pow(2, 32) - pow(2, 9) - pow(2, 8) - pow(2, 7) - pow(2, 6) - pow(2, 4) - pow(2, 0)
 
# order of the elliptic curve group
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

def add_points(P, Q, p):
    x1, y1 = P
    x2, y2 = Q


    if x1 == x2 and y1 == y2: #same point
        S = (3*x1*x2 + a) * pow(2*y1, -1, p)
    else:
        S = (y2 - y1) * pow(x2 - x1, -1, p)
     
    x3 = (S*S - x1 - x2) % p
    y3 = (S * (x1 - x3) - y1) % p
     
    is_on_curve((x3, y3), p) 

    return x3, y3

def is_on_curve(P, p):
    x, y = P
    assert (y*y) % p == ( pow(x, 3, p) + a*x + b ) % p

def double_and_add(G, k, p):
    target_point = G
     
    k_binary = bin(k)[2:] #0b1111111001
     
    for i in range(1, len(k_binary)):
        current_bit = k_binary[i: i+1]
         
        # doubling - always
        target_point = add_points(target_point, target_point, p)
         
        if current_bit == "1":
            target_point = add_points(target_point, G, p)
     
    is_on_curve(target_point, p)
     
    return target_point

# def calculateKey(key_size):
#     #key generation
#     K_a=random.getrandbits(key_size) #privateKey of alice
#     K_b=random.getrandbits(key_size) #privateKey of bob

#     time0=time.time()
#     A=double_and_add(G,K_a,p) #publicKey of alice
#     time1=time.time()
#     B=double_and_add(G,K_b,p) #publickey of Bob
#     time2=time.time()
#     RAlice=double_and_add(B,K_a,p)
#     RBob=double_and_add(A,K_b,p)
#     time3=time.time()

#     R=RAlice

def calculatePublicKey(key_size):
    global privateKey
    privateKey=random.getrandbits(key_size)
    publicKey=double_and_add(G,privateKey,p)
    return publicKey

def calculateSharedKey(otherPublicKey):
    sk=double_and_add(otherPublicKey,privateKey,p)
    sharedKey=str(sk[0])
    return sharedKey[:16]
