kicsi = []
kozepes = []
nagy = []

csomag = float(input("Hany kilos a csomag? "))

while csomag != 0:

    csomag = float(input("Hany kilos a csomag? "))

    if csomag == 0: break
    
    if csomag >= 0.1 and csomag < 5.0:
        kicsi.append(csomag)

    elif csomag >= 5.1 and csomag < 15.0:
            kozepes.append(csomag)

    elif csomag >= 15.1 and csomag < 30.0:
                nagy.append(csomag)

    else:
           print("a csomag tul nagy")

print( len(kicsi), len(kozepes), len(nagy))