style mm_button:
    size_group "mm"
    xalign 0.5
    ysize 70

screen main_menu():

    tag menu

    add "images/station.jpg"

    frame:
        xalign 0.5
        yalign 0.7

        vbox:
            spacing 20

            text "L'ÚLTIM TREN" size 70

            textbutton "Jugar" action Start()
            textbutton "Carregar partida" action ShowMenu("load")
            textbutton "Opcions" action ShowMenu("preferences")
            textbutton "Sortir" action Quit(confirm=True)