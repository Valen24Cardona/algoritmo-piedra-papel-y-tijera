print("Bienvenido al juego piedra papel o tijera, tiene tres posibles posiciones P. piedra, PA. papel, T.tijera, elija una de estas")
opcion1= input("ines escriba su opcion")
opcion2= input("juan escriba su opcion")
if opcion1 == "P" and opcion2 == "T":
    print("a ganado ines")
elif opcion1 == "T" and opcion2 == "PA":
    print("a ganado ines")
elif opcion1 == "PA" and opcion2 == "P":
    print("a ganado ines")
elif opcion1 == opcion2:
    print("los jugadores empataron")
else: 
    print("a ganado juan")

    


