def skrivLaks(antallLaks):
    i=0
    while antallLaks > 0:
        i=i+1
        if i == 1:
            print(i, "laks")
        else:
            print(i, "laksar")
        antallLaks = antallLaks-1


    
skrivLaks(5)