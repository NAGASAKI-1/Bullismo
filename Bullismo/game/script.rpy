#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define Preside = Character("Preside", color="#4e7239")
define Luca = Character("Luca", color="#2b13b6")
define Marco = Character("Marco", color="#f72323")
define Andrea = Character("Andrea", color="#fffb00")
define Giulia = Character("Giulia", color="#fd0bc9")
define Simone = Character("Simone", color="#00ffdd")


# Il gioco comincia qui.

label start:

    # Mostra uno sfondo. Al momento mostra una sagoma generica, ma puoi
    # aggiungere un file (chiamato "bg room.png" oppure "bg room.jpg")
    # alla directory 'images' per cambiarla.

    scene bg room

    # Mostra lo sprite di un personaggio.
    # Al momento mostra una sagoma generica, ma puoi aggiungere un file
    # (chiamato "eileen_happy.png") alla directory 'images' per cambiarla.

    show eileen happy

    # Questo mostra linee di dialogo.

    "Funziona davvero!"

    Preside "Hai creato un nuovo gioco Ren'Py."

    Preside "Quando aggiungerai una storia, immagini e musica, potrai distribuirlo nel mondo!"

    # Questo termina il gioco.

    return

