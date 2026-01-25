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
    
    $ vinto = False

    scene bg black


    """
    Durante il cambio dell’ora, vicino alla palestra, si è verificato un episodio confuso.

    Alcuni studenti parlano di una lite, altri di uno scherzo, altri ancora non sanno spiegare cosa sia successo.

    Pochi minuti dopo, uno studente, Luca, viene trovato chiuso nel ripostiglio della palestra.

    La porta era chiusa a chiave dall’esterno.

    Non ci sono insegnanti presenti al momento dei fatti.

    Tu, il preside, dovrai interrogare cinque studenti che si trovavano nei pressi della palestra in quell’orario e decidere chi è responsabile dell’atto più grave.
    
    Decidi di parlare, prima di tutto, con la vittima: Luca.
    """

    scene bg classroom
    show luca
    with fade

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
    with fade

    "Dopo quello che ti ha detto Luca, ritieni opportuno sentire la versione di Marco"

    scene bg classroom
    show marco
    with fade

    Marco """
    Sì, è vero, stavamo discutendo. 
    
    Luca era molto agitato e mi urlava contro senza motivo. 
    
    Io cercavo solo di calmarlo, non capisco perché ce l’avesse con me. 
    
    Non abbiamo mai avuto veri problemi, 
    
    a parte qualche battuta come capita a tutti.
    """

    scene bg black
    with fade

    "Dopo aver chiesto un po in giro, trovi alcuni testimoni che potrebbero aiutarti."

    scene bg classroom
    show andrea
    with fade

    Andrea """
    È stato Luca a iniziare tutto. 
    
    Ha perso il controllo, ha spinto Marco e ha attirato l’attenzione di tutti. 
    
    Fa sempre la vittima ma poi è lui che provoca. 
    
    Se succede qualcosa è perché se l’è cercata.
    """

    hide andrea
    show giulio
    with fade

    Giulio """
    Ho visto Luca e Marco urlarsi contro vicino alla palestra.
    
    Era una discussione pesante, 
    
    non una semplice lite. 
    
    Luca sembrava davvero provato, quasi sul punto di scoppiare a piangere. 
    
    Marco e i suoi amici spesso lo prendono di mira, lo vedono come uno su cui scherzare.
    """

    hide giulio
    show simone
    with fade

    Simone """
    C’era molta confusione. 
    
    Luca era fuori di sé e stava insultando pesantemente Marco, che è un mio amico. 
    
    Io sono intervenuto solo per difenderlo 
    
    e cercare di farlo smettere. 
    
    Non volevo che degenerasse.
    """

    scene bg black
    with fade

    "C'è qualcosa che non ti convince, decidi di fare altre domande ai cinque interrogati"

    scene bg classroom
    show luca
    with fade

    Luca """
    Dopo la caduta ero stordito. 
    
    Ho sentito delle risate fuori, qualcuno rideva come se fosse uno scherzo. 
    
    Poi la porta si è chiusa di colpo. Ho sentito il rumore metallico della chiave che girava, ma ero a terra e non vedevo nulla. 
    
    Ho urlato e ho bussato, ma nessuno mi ha risposto.
    """

    hide luca
    show marco
    with fade

    Marco """
    Io non l’ho toccato e non ho spinto nessuno. 
    
    A un certo punto me ne sono andato perché non volevo guai. 
    
    Quando ho lasciato il corridoio non stava succedendo niente di grave.
    """

    hide marco
    show andrea
    with fade

    Andrea """
    Io non so esattamente cosa sia successo dopo, perché me ne sono andato prima. 
    
    Però sono sicuro che Marco non farebbe mai una cosa del genere. 
    
    Lo conosco da sempre, non è capace di cattiverie. 
    
    Luca invece è strano, sempre isolato.
    """

    hide andrea
    show giulio
    with fade

    Giulio """
    Quando la situazione è peggiorata me ne sono andato. 
    
    Avevo paura di finire nei guai per qualcosa che non avevo fatto. 
    
    Non ho visto cosa è successo dopo e non voglio essere coinvolto più del necessario.
    """

    hide giulio
    show simone
    with fade

    Simone """
    Quando me ne sono andato non c’era più nessuno in giro. 
    
    Eravamo rimasti solo io e Marco. 
    
    A un certo punto Luca non c’era più, era sparito. Non so davvero cosa sia successo dopo.
    """

    scene bg black
    with fade

    """
    Le informazioni sono poche e confuse, ma devi arrivare a una conclusione. I bulli non possono rimanere inpuniti.
    
    Cos'è successo?
    """

    menu:
        "Nessuno ha spinto Luca, se l'è inventato":
            jump perso
        "Marco ha spinto Luca senza che se ne rendesse conto":
            jump perso
        "Andrea, complice di Marco, ha spinto Luca":
            jump perso
        "Simone, complice di Marco, ha spinto Luca":
            jump vinto
        "Giulio, complice di Marco, ha spinto Luca":
            jump perso


    label vinto:
        $ vinto = True

        """
        Dopo aver ascoltato attentamente le versioni dei fatti e analizzato le contraddizioni emerse, è chiaro che l’episodio non può essere liquidato come uno scherzo o una semplice lite.

        Luca è stato vittima di un atto grave: è stato chiuso a chiave in un ripostiglio, isolato e lasciato solo. 
        
        Questo è un atto di bullismo.

        Marco viene sanzionato per il comportamento reiterato di provocazione e intimidazione nei confronti di un compagno. Le parole, le prese in giro e l’atteggiamento di gruppo sono forme di violenza.

        Tuttavia, l’atto materiale di chiudere la porta a chiave è stato compiuto da Simone, colui che ha approfittato della confusione e del silenzio degli altri.

        Il vero colpevole non è solo chi provoca, ma anche chi agisce nell’ombra e chi sceglie di non intervenire.

        Il bullismo non vive solo di urla e spintoni.

        Vive nel gruppo che ride, nel testimone che si gira dall’altra parte, in chi approfitta di un momento per fare del male.

        Punire non basta. Capire sì.

        Questa scuola non tollera il bullismo, in nessuna delle sue forme.
        """

        jump fine

    label perso:
        $ vinto = False

        """
        Non sei riuscito a scoprire il colpevole. Il caso viene chiuso.

        Troppe versioni diverse, troppe incertezze. Nessuno è colpevole abbastanza.

        Luca rientra a scuola, ma non è più lo stesso.

        Cammina con lo sguardo basso, come se cercasse di occupare meno spazio possibile.

        Nessuno lo prende più in giro apertamente.

        Ma nessuno gli siede accanto.

        Ogni risata nei corridoi gli sembra rivolta a lui.

        Ogni porta che si chiude gli fa trattenere il respiro.

        Marco continua la sua vita.

        Ride, scherza, viene promosso.

        Dice che “ormai è acqua passata”.

        Andrea racconta la storia come una leggenda da corridoio.

        Uno scherzo finito male.

        Una cosa da dimenticare.

        Giulio evita di incrociare lo sguardo di Luca.

        Ogni tanto pensa di parlargli.

        Poi si convince che ormai è troppo tardi.

        Simone non viene mai chiamato in causa.

        Ha imparato una lezione importante:

        se nessuno guarda, nessuno chiede.

        Passano le settimane.

        Luca smette di alzare la mano.

        Smette di uscire all’intervallo.

        Smette di parlare.

        I professori annotano: “Studente silenzioso, poco partecipe.”

        Un pomeriggio, la madre di Luca entra a scuola.

        Ha il viso stanco, gli occhi gonfi.

        Ti parla a bassa voce.

        Il giorno dopo, la sedia di Luca è vuota.

        Non c’è nessun annuncio ufficiale.

        Solo voci.

        Solo silenzi più lunghi del solito.

        Qualcuno dice che Luca si è trasferito.

        Qualcuno dice che stava male da tempo.

        Nessuno dice il suo nome ad alta voce.

        La porta del ripostiglio della palestra viene sostituita.

        Una serratura nuova.

        Come se bastasse cambiare una chiave per cancellare tutto.

        Gli anni passano.

        Gli studenti crescono, se ne vanno.

        Ma chi c’era quel giorno, ogni tanto, quando sente una porta chiudersi troppo forte,

        si ricorda.

        Si ricorda di aver visto.

        Di aver sentito.

        E di non aver fatto nulla.
        """

        jump fine

    label fine:
        """
        Il bullismo non è sempre evidente.
        A volte il vero responsabile è chi approfitta del silenzio degli altri.
        """

        if not vinto:
            """
            Non tutte le storie di bullismo finiscono con una punizione.
            Alcune finiscono con un silenzio che dura per sempre.
            """

        """
        «Alla fine, non ricorderemo le parole dei nostri nemici, ma il silenzio dei nostri amici.»
        - Martin Luther King Jr.
        """

    return

