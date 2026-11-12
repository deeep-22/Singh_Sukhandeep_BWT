
def trasforma(string):
    string += "$"

    rotazioni = []

    for i in range (len(string)):
        rotazione = string[i:] + string[:i]
        rotazioni.append(rotazione)

    print(rotazioni)

    n = len(rotazioni)
    temp = ""
    for i in range(n):
        for j in range(0, n-i-1):
            if rotazioni[j] > rotazioni[j+1]:
                temp = rotazioni[j]
                rotazioni[j] = rotazioni[j+1]
                rotazioni[j+1] = temp

    risultato = ""

    for riga in rotazioni:
        risultato += riga[-1]

    return risultato


