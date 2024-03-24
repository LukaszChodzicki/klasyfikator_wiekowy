print("Witamy w programie - Klasyfikator wiekowy")
while True:
    print("Podaj wiek użytownika")
    wiek = int(input())
    if wiek<0:
        print("Podano nieprawidłowy wiek, spróbuj ponownie")
    else:
        break
if wiek<13:
    print("Podany Wiek użytkownika to", wiek)
    print("Użytkownik został sklasyfikowany jako dziecko", wiek)
elif wiek>=13 and wiek<=19:
    print("Podany Wiek użytkownika to", wiek)
    print("Użytkownik został sklasyfikowany jako nastolatek", wiek)
elif wiek>=20 and wiek<=65:
    print("Podany Wiek użytkownika to", wiek)
    print("Użytkownik został sklasyfikowany jako dorosły", wiek)
elif wiek>65:
    print("Podany Wiek użytkownika to", wiek)
    print("Użytkownik został sklasyfikowany jako senior", wiek)
