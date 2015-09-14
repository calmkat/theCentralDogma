import random
import turtle
# DNA Replication
base = turtle.Turtle()
wn = turtle.Screen()
dna = []
base.speed(1)

def g(x):
    x.color("green")
def c(x):
    x.color("yellow")
def a(x):
    x.color("red")
def t(x):
    x.color("blue")
def u(x):
    x.color("lightblue")
    
    

base.shape("turtle")
base.penup()
base.write("DNA will exist as two strands, the template and the coding strand")
base.left(180)
base.forward(80)
base.left(90)
base.forward(10)

for i in range(9):
    x = random.randint(0,10)
    if x <= 10 and x > 7:
        g(base)
        dna.append("g")
    elif x <= 7 and x > 5:
        c(base)
        dna.append("c")
    elif x <= 5 and x > 2:
        a(base)
        dna.append("a")
    elif x <= 2 and x > 0:
        t(base)
        dna.append("t")
    base.stamp()
    base.left(90)
    base.forward(20)
    base.right(90)
#Transcription
base.clear()
base.write("RNA Polymerse (not shown) adds complimentary RNA nucleotides to a template strand of DNA. This strand of RNA is similar to the DNA except t is replaced by u")
base.forward(30)
base.left(180)
rna = dna[::-1]
for i in rna:
    if i == "g":
        c(base)
        i = "c"
    elif i == "c":
        g(base)
        i = "g"
    elif i == "a":
        u(base)
        i = "u"
    elif i == "t":
        a(base)
        i = "a"
    base.left(90)
    base.forward(20)
    base.right(90)
    base.stamp()
#translation
base.clearstamps(9)
base.forward(30)
base.right(90)
base.forward(20)
base.right(90)
base.color("black")
rna = rna[::-1]
#this for loop reads all characters, but it needs to read three at a time then print for each three, then stop after nine.
#Maybe we can set up the range differently?
rr = [0, 3, 6]
def codrr (x) :
    for i in x:
        if rna[i] == "g":
            i += 1
            if rna[i] == "g":
                base.write("glycine")
            elif rna[i] == "c":
                base.write("alanine")
            elif rna[i] == "a":
                i += 1
                if rna[i] == "g" or rna[i] == "a":
                    base.write("glutamic acid")
                elif rna[i] == "c" or rna[i] == "u":
                    base.write("aspartic acid")
            elif rna[i] == "u":
                base.write("valine")
        elif rna[i] == "c":
            i += 1
            if rna[i] == "g":
                base.write("arginine")
            elif rna[i] == "c":
                base.write("proline")
            elif rna[i] == "a":
                i += 1
                if rna[i] == "g" or rna[i] == "a":
                    base.write("glutamine")
                elif rna[i] == "c" or rna[i] == "u":
                    base.write("histidine")
            elif rna[i] == "u":
                base.write("leucine")
        if rna[i] == "a":
            i += 1
            if rna[i] == "g":
                i += 1
                if rna[i] == "g" or rna[i] == "a":
                    base.write("arginine")
                elif rna[i] == "c" or rna[i] == "u":
                    base.write("serine")
            elif rna[i] == "c":
                base.write("threonine")
            elif rna[i] == "a":
                i += 1
                if rna[i] == "g" or rna[i] == "a":
                    base.write("lysine")
                elif rna[i] == "c" or rna[i] == "u":
                    base.write("asparagine")
            elif rna[i] == "u":
                i += 1
                if rna[i] == "g":
                    base.write("methionine")
                elif rna[i] == "c" or rna[i] == "a" or rna[i] == "u":
                    base.write("isoleucine")
        if rna[i] == "u":
            i += 1
            if rna[i] == "g":
                i += 1
                if rna[i] == "g":
                    base.write("tryptophan")
                elif rna[i] == "c" or rna[i] == "u":
                    base.write("cysteine")
                elif rna[i] == "a":
                    base.write("stop")
            elif rna[i] == "c":
                base.write("serine")
            elif rna[i] == "a":
                i += 1
                if rna[i] == "g" or rna[i] == "a":
                    base.write("stop")
                elif rna[i] == "c" or rna[i] == "u":
                    base.write("tyrosine")
            elif rna[i] == "u":
                i += 1
                if rna[i] == "g" or rna[i] == "a":
                    base.write("leucine")
                elif rna[i] == "c" or rna[i] == "u":
                    base.write("phenylalanine")
        base.left(90)
        base.forward(60)
        base.right(90)
print(rna)
codrr(rr)

wn.exitonclick()
