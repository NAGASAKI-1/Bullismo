#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define Preside = Character("Preside", color="#4e7239")
define Luca = Character("Luca", color="#2b13b6")
define Marco = Character("Marco", color="#f72323")
define Andrea = Character("Andrea", color="#fffb00")
define Giulio = Character("Giulio", color="#fd0bc9")
define Simone = Character("Simone", color="#00ffdd")
define narrator = nvl_narrator



# Il gioco comincia qui.

label start:

    # Mostra uno sfondo. Al momento mostra una sagoma generica, ma puoi
    # aggiungere un file (chiamato "bg room.png" oppure "bg room.jpg")
    # alla directory 'images' per cambiarla.

    scene bg black

    # Mostra lo sprite di un personaggio.
    # Al momento mostra una sagoma generica, ma puoi aggiungere un file
    # (chiamato "eileen_happy.png") alla directory 'images' per cambiarla.

    # Questo mostra linee di dialogo.

    """
    Durante il cambio dell’ora, vicino alla palestra, si è verificato un episodio confuso.

    Alcuni studenti parlano di una lite, altri di uno scherzo, altri ancora non sanno spiegare cosa sia successo.

    Pochi minuti dopo, uno studente, Luca, viene trovato chiuso nel ripostiglio della palestra.

    La porta era chiusa a chiave dall’esterno.

    Non ci sono insegnanti presenti al momento dei fatti.

    Tu, il preside, dovrai interrogare cinque studenti che si trovavano nei pressi della palestra in quell’orario e decidere chi è responsabile dell’atto più grave.
    
    Decidi di parlare, prima di tutto, con la vittima, Luca.
    """

    scene bg classroom

    show luca

    Luca """
    Io e Marco stavamo discutendo vicino alla palestra.
    
    Non era la prima volta: è tutto l’anno che lui e i suoi amici mi prendono di mira,
    
    fanno battute,
    
    mi spingono,
    
    mi fanno sentire sbagliato.
    
    Quel giorno non ce la facevo più e ho risposto.
    
    All’inizio c’erano diverse persone intorno a noi, poi pian piano se ne sono andate.
    
    A un certo punto credo fossimo rimasti solo in tre.
    
    Ho sentito una spinta improvvisa alle spalle e sono caduto all’indietro, proprio dentro il ripostiglio. 
    
    È successo tutto in un attimo, non ho fatto in tempo a capire chi mi avesse spinto.
    """

    scene bg black

    "Dopo quello che ti ha detto Luca, ritirni opportuno sentire la versione di Marco"

    scene bg classroom

    show marco

    Marco """
    Sì, è vero, stavamo discutendo. 
    
    Luca era molto agitato e mi urlava contro senza motivo. 
    
    Io cercavo solo di calmarlo, non capisco perché ce l’avesse con me. 
    
    Non abbiamo mai avuto veri problemi, 
    
    a parte qualche battuta come capita a tutti.
    """

    scene bg black

    "Dopo aver chiesto un po in giro, trovi alcuni testimoni che potrebbero aiutarti."

    scene bg classroom

    show andrea

    Andrea """
    È stato Luca a iniziare tutto. 
    
    Ha perso il controllo, ha spinto Marco e ha attirato l’attenzione di tutti. 
    
    Fa sempre la vittima ma poi è lui che provoca. 
    
    Se succede qualcosa è perché se l’è cercata.
    """

    show giulio
    with fade

    Giulio """
    Ho visto Luca e Marco urlarsi contro vicino alla palestra.
    
    Era una discussione pesante, 
    
    non una semplice lite. 
    
    Luca sembrava davvero provato, quasi sul punto di scoppiare a piangere. 
    
    Marco e i suoi amici spesso lo prendono di mira, lo vedono come uno su cui scherzare.
    """

    show simone
    with fade

    Simone """
    C’era molta confusione. 
    
    Luca era fuori di sé e stava insultando pesantemente Marco, che è un mio amico. 
    
    Io sono intervenuto solo per difenderlo 
    
    e cercare di farlo smettere. 
    
    Non volevo che degenerasse.
    """


    # Questo termina il gioco.

    return

