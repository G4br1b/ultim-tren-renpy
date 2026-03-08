define s = Character("Sergi")
define g = Character("Gabriel")
define d = Character("David")

label start:

    play music "audio/ambient_estacio.mp3"

    scene black
    "Una nit freda."
    "Tres amics arriben a una estació gairebé buida."

    jump escena1


label escena1:

    scene bg room

    s "Ja hem arribat."

    g "El tren hauria d'arribar en deu minuts."

    d "Aquest lloc està massa buit..."

    "Una veu sona per megafonia."

    "El tren patirà un retard de 30 minuts."

    menu:
        "Esperar tranquil·lament":
            jump escena2

        "Investigar l'estació":
            jump escena3


label escena2:

    g "Potser només és un retard normal."

    d "No m'agrada gens aquest lloc."

    menu:
        "Anar a l'andana":
            jump escena4

        "Entrar a la sala d'espera":
            jump escena5


label escena3:

    "Decidiu investigar."

    play sound "audio/passos.mp3"

    s "He vist algú caminant per l'andana."

    menu:
        "Seguir la persona":
            jump escena6

        "Ignorar-la":
            jump escena5


label escena4:

    "L'andana està buida."

    g "Escolteu això?"

    play sound "audio/misteri.mp3"

    menu:
        "Investigar el soroll":
            jump escena7

        "Tornar enrere":
            jump escena5


label escena5:

    "A la sala d'espera hi ha una dona misteriosa."

    "Dona" "No hauríeu d'estar aquí aquesta nit."

    menu:
        "Preguntar què passa":
            jump escena8

        "Ignorar-la":
            jump escena6


label escena6:

    "Seguiu caminant per l'estació."

    d "He trobat una porta oberta."

    menu:
        "Entrar":
            jump escena9

        "No entrar":
            jump escena7


label escena7:

    "El soroll ve de la sala de control."

    s "El sistema del tren està actiu..."

    menu:
        "Tocar els controls":
            jump escena10

        "No tocar res":
            jump final_normal


label escena8:

    "La dona sospira."

    "Dona" "El tren d'avui no és normal."

    menu:
        "Confiar en ella":
            jump escena9

        "No confiar":
            jump escena7


label escena9:

    "Descobriu que algú ha manipulat el sistema del tren."

    g "Algú ha canviat la ruta!"

    menu:
        "Intentar arreglar-ho":
            jump final_bo

        "Sortir corrent":
            jump final_dolent


label escena10:

    "Accidentalment activeu el sistema."

    play sound "audio/tren_arriba.mp3"

    "El tren arriba molt ràpid."

    menu:
        "Pujar al tren":
            jump final_secret

        "Amagar-se":
            jump final_dolent


label final_bo:

    scene black

    "Aconseguiu arreglar el sistema."

    "El tren arriba correctament."

    "FINAL BO"

    return


label final_normal:

    scene black

    "Decidiu no intervenir."

    "El tren arriba tard però tot sembla normal."

    "FINAL NORMAL"

    return


label final_dolent:

    scene black

    "Alguna cosa surt malament."

    "El tren desapareix a la nit."

    "FINAL DOLENT"

    return


label final_secret:

    scene black

    "El tren en què pugeu no apareix en cap registre."

    "Potser no hauríeu d'haver pujat."

    "FINAL SECRET"

    return