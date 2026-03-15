# Personajes
define s = Character("Sergi", color="#4FC3F7")
define g = Character("Gabriel", color="#81C784")
define d = Character("David", color="#FFB74D")

# Variable secreta
default curiositat = 0

# Transiciones
define flash = Fade(0.1, 0.0, 0.3, color="#fff")
define fear = Fade(0.2, 0.0, 0.2, color="#000")

label start:

    play music "audio/ambient_estació.mp3" fadein 2.0

    scene black
    with fade

    "Una nit freda."
    "Tres amics arriben a una estació gairebé buida."

    jump escena1


label escena1:

    scene station
    with dissolve

    s "Ja hem arribat."

    g "El tren hauria d'arribar en deu minuts."

    d "Aquest lloc està massa buit..."

    "Una veu sona per megafonia."

    "El tren patirà un retard de 30 minuts."

    menu:
        "Esperar tranquil·lament":
            jump escena2

        "Investigar l'estació":
            $ curiositat += 1
            jump escena3


label escena2:

    scene waiting_room
    with dissolve

    g "Potser només és un retard normal."

    d "No m'agrada gens aquest lloc."

    menu:
        "Anar a l'andana":
            jump escena4

        "Entrar a la sala d'espera":
            jump escena5


label escena3:

    scene station
    with fade

    play sound "audio/passos.mp3"

    "Sentiu passos darrere vostre..."

    d "He vist algú caminant per l'andana."

    menu:
        "Seguir la persona":
            $ curiositat += 1
            jump escena6

        "Ignorar-la":
            jump escena5


label escena4:

    scene platform
    with dissolve

    g "Escolteu això?"

    play sound "audio/misteri.mp3"

    menu:
        "Investigar el soroll":
            $ curiositat += 1
            jump escena7

        "Tornar enrere":
            jump escena5


label escena5:

    scene waiting_room
    with dissolve

    "A la sala d'espera hi ha una dona misteriosa."

    "Dona" "No hauríeu d'estar aquí aquesta nit."

    menu:
        "Preguntar què passa":
            jump escena8

        "Ignorar-la":
            jump escena6


label escena6:

    scene station
    with fade

    play sound "audio/passos.mp3"

    d "He trobat una porta oberta."

    menu:
        "Entrar":
            $ curiositat += 1
            jump escena9

        "No entrar":
            jump escena7


label escena7:

    scene control_room
    with fear

    play sound "audio/misteri.mp3"

    "El soroll ve de la sala de control."

    s "El sistema del tren està actiu..."

    menu:
        "Tocar els controls":
            jump escena10

        "No tocar res":
            jump final_normal


label escena8:

    scene waiting_room
    with dissolve

    "La dona sospira."

    "Dona" "El tren d'avui no és normal."

    menu:
        "Confiar en ella":
            jump escena9

        "No confiar":
            jump escena7


label escena9:

    scene control_room
    with dissolve

    g "Algú ha manipulat la ruta del tren!"

    if curiositat >= 3:
        jump final_secret

    menu:
        "Intentar arreglar-ho":
            jump final_bo

        "Sortir corrent":
            jump final_dolent


label escena10:

    scene platform
    with flash

    play sound "audio/tren_arriba.mp3"

    with vpunch

    "El tren arriba molt ràpid."

    menu:
        "Pujar al tren":
            jump final_secret

        "Amagar-se":
            jump final_dolent


label final_bo:

    scene black
    with fade

    "Aconseguiu arreglar el sistema."

    "El tren arriba correctament."

    "FINAL BO"

    return


label final_normal:

    scene black
    with fade

    "Decidiu no intervenir."

    "El tren arriba tard però tot sembla normal."

    "FINAL NORMAL"

    return


label final_dolent:

    scene black
    with fear

    play sound "audio/misteri.mp3"

    "Alguna cosa surt malament..."

    "El tren desapareix a la nit."

    "FINAL DOLENT"

    return


label final_secret:

    scene black
    with flash

    play sound "audio/tren_arriba.mp3"

    "El tren en què pugeu no apareix en cap registre."

    "Potser no hauríeu d'haver pujat."

    "FINAL SECRET"

    return