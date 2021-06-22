import random
def name(n):
    for i in range (n):
        onset = ["b", "c", "d", "ch", "f", "g", "h", "j", "k", "l", "m", "n", "p", "qu", "r", "s", "t", "v", "w", "x", "y", "z", "th", "sh", "wh"]
        clusterb = ["l", "r"]
        clusters = ["l", "r", "n", "m", "g", "c", "k", "p", "qu", "t", "w"]
        clusterth = ["r", "w"]
        vowel = ["a", "e", "i", "o", "u", "y", "ae", "au", "ea", "ee", "eo", "ia", "ie", "io", "oa", "oe", "oi", "oo", "ou",]
        coda = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k", "l", "m", "n", "ng", "o", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ck", "tt"]
        f = random.randint(0, 1)
        e = random.randint(0, 4)
        if e == 0:
            a = ("")
        else:
            h = random.choice(onset)
            if f == 1:
                if h in ["b", "c", "f", "g", "k", "p", "v", "sh"]:
                    g = random.choice(clusterb)
                elif h in ["s"]:
                    g = random.choice(clusters)
                elif h in ["th"]:
                    g = random.choice(clusterth)
                else:
                    g = ("")
            else:
                g = ("")
            a = (h+g)
        exsyl = random.randint(0, 2)
        d = ("")
        while exsyl >= 0:
            j = random.randint(0, 1)
            b = random.choice(vowel)
            h = random.choice(coda)
            if j == 1:
                g = random.choice(onset)
            else:
                g = ("")
            c = (h+g)
            d = d + b + c
            exsyl -= 1
        return (a+d)