#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_messages():
    return \
		{
			"0": "Il motore Nettacker è iniziato ...\n\n",
			"1": "python nettacker.py [opzioni]",
			"2": "Mostra il menu di aiuto di Nettacker",
			"3": "Leggere la licenza e gli accordi https://github.com/viraintel/OWASP-Nettacker\n",
			"4": "Motore",
			"5": "Opzioni di ingresso del motore",
			"6": "selezionare una lingua {0}",
			"7": "scansione di tutti gli IP nell'intervallo",
			"8": "trovare e analizzare i sottodomini",
			"9": "numeri di thread per le connessioni ad un host",
			"10": "numeri di thread per gli host di scansione",
			"11": "salvare tutti i registri nel file (results.txt, results.html, results.json)",
			"12": "Bersaglio",
			"13": "Opzioni di ingresso target",
			"14": "elenco target (s), separato con \",\"",
			"15": "leggere i bersagli dal file",
			"16": "Opzioni del metodo di scansione",
			"17": "scegliere il metodo di scansione {0}",
			"18": "scegliere il metodo di scansione per escludere {0}",
			"19": "nome utente, separato da \",\"",
			"20": "leggere il nome utente dal file",
			"21": "elenco delle password, separato con \",\"",
			"22": "leggere le password dal file",
			"23": "elenco delle porte, separato da \",\"",
			"24": "leggere le password dal file",
			"25": "tempo di dormire tra ogni richiesta",
			"26": "Impossibile specificare i target (i)",
			"27": "Impossibile specificare gli obiettivi, impossibile aprire il file: {0}",
			"28": "è meglio utilizzare il numero di thread inferiore a 100, BTW stiamo continuando ...",
			"29": "impostare il timeout a {0} secondi, è troppo grande, non è vero? dal modo in cui stiamo continuando ...",
			"30": "questo modulo di scansione [{0}] non è stato trovato!",
			"31": "questo modulo di scansione [{0}] non è stato trovato!",
			"32": "non è possibile escludere tutti i metodi di scansione",
			"33": "non è possibile escludere tutti i metodi di scansione",
			"34": "il modulo {0} selezionato per escludere non trovato!",
			"35": "inserire gli input di metodi, ad esempio: \"ftp_brute_users = test, admin & ftp_brute_passwds = read_from_file: /tmp/pass.txt&ftp_brute_port=21\"",
			"36": "non riesce a leggere file {0}",
			"37": "Impossibile specificare il nome utente, impossibile aprire il file: {0}",
			"38": "",
			"39": "Impossibile specificare le password, impossibile aprire il file: {0}",
			"40": "file \"{0}\" non è scrivibile!",
			"41": "scelga il metodo di scansione!",
			"42": "rimuovendo file temporanei!",
			"43": "risolvere i risultati!",
			"44": "fatto!",
			"45": "iniziare ad attaccare {0}, {1} di {2}",
			"46": "questo modulo \"{0}\" non è disponibile",
			"47": "purtroppo questa versione del software potrebbe essere eseguita solo su linux / osx / windows.",
			"48": "La tua versione Python non è supportata!",
			"49": "saltare l'obiettivo duplicato (alcuni sottodomini / domini possono avere lo stesso IP e le aree)",
			"50": "tipo sconosciuto di destinazione [{0}]",
			"51": "controlla la gamma {0} ...",
			"52": "controllando {0} ...",
			"53": "OSPITE",
			"54": "NOME UTENTE",
			"55": "PASSWORD",
			"56": "PORTA",
			"57": "TIPO",
			"58": "DESCRIZIONE",
			"59": "livello di modalità verbose (0-5) (impostazione predefinita 0)",
			"60": "mostrare la versione del software",
			"61": "ricerca aggiornamenti",
			"62": "",
			"63": "",
			"64": "Ripeti quando il timeout di connessione (default 3)",
			"65": "ftp a {0}: {1} timeout, saltando {2}: {3}",
			"66": "INCONTATO IN SUCCESSO!",
			"67": "INCONTRATO IN SUCCESSO, PERMISSIONE ANNULLATA PER IL COMANDO ELENCO!",
			"68": "ftp a {0}: {1} non è riuscito, saltando intero passo [processo {2} di {3}]! andando al passo successivo",
			"69": "il target di input per il modulo {0} deve essere DOMAIN, HTTP o SINGLE_IPv4, saltando {1}",
			"70": "utente: {0} pass: {1} host: {2} port: {3} trovato!",
			"71": "(NESSUNA PERMISSIONE PER LE FILE DELLE LISTA)",
			"72": "provando {0} di {1} in processo {2} di {3} {4}: {5}",
			"73": "connessione smtp a {0}: {1} timeout, saltando {2}: {3}",
			"74": "la connessione smtp a {0}: {1} non è riuscita, saltando tutto il passo [processo {2} di {3}]! andando al passo successivo",
			"75": "il target di ingresso per il modulo {0} deve essere HTTP, saltando {1}",
			"76": "ssh a {0}: {1} timeout, saltando {2}: {3}",
			"77": "ssh a {0}: {1} non è riuscito, saltando intero passo [processo {2} di {3}]! andando al passo successivo",
			"78": "connessione ssh a% s:% s non riuscita, saltando intero passo [processo% s di% s]! andando al passo successivo",
			"79": "PORTA APERTA",
			"80": "host: {0} port: {1} trovato!",
			"81": "target {0} inviato!",
			"82": "impossibile aprire il file di elenco proxy: {0}",
			"83": "impossibile trovare il file di elenco proxy: {0}",
			"84": "si esegue la versione OWASP Nettacker {0} {1} {2} {6} con il nome del codice {3} {4} {5}",
			"85": "questa funzione non è ancora disponibile! si prega di eseguire \"clone git https://github.com/viraintel/OWASP-Nettacker.git\" o \"pip install -U OWASP-Nettacker\" per ottenere l'ultima versione.",
			"86": "costruire un grafico di tutte le attività e le informazioni, è necessario utilizzare l'output HTML. grafici disponibili: {0}",
			"87": "per utilizzare il grafico il nome del file di output deve terminare con \".html\" o \".htm\"!",
			"88": "costruzione grafico ...",
			"89": "finire il grafico di costruzione!",
			"90": "Grafici di prova di penetrazione",
			"91": "Questo grafico creato da OWASP Nettacker. Il grafico contiene tutte le attività dei moduli, mappe di rete e informazioni sensibili. Non condividi questo file con nessuno se non è affidabile.",
			"92": "Rapporto OWASP Nettacker",
			"93": "Dettagli del software: versione OWASP Nettacker {0} [{1}] in {2}",
			"94": "non sono state trovate porte aperte!",
			"95": "nessun utente / password trovato!",
			"96": "{0} moduli caricati ...",
			"97": "questo modulo di grafico non è trovato: {0}",
			"98": "questo modulo grafico \"{0}\" non è disponibile",
			"99": "ping prima di eseguire la scansione dell'host",
			"100": "saltando l'intero target {0} e il metodo di scansione {1} a causa di -ping-before-scan è vero e non ha risposto!",
			"101": "non si utilizza l'ultima versione di OWASP Nettacker, si prega di aggiornare.",
			"102": "non riesci a controllare l'aggiornamento, controlla la tua connessione internet.",
			"103": "Stai utilizzando l'ultima versione di OWASP Nettacker ...",
			"104": "elenco directory trovato in {0}",
			"105": "inserire la porta tramite il comando -g o -methods-args anziché url",
			"106": "connessione http {0} timeout!",
			"107": "",
			"108": "nessuna directory o file trovato per {0} nella porta {1}",
			"109": "impossibile aprire {0}",
			"110": "il valore dir_scan_http_method deve essere GET o HEAD, impostare il valore predefinito su GET.",
			"111": "elenca tutti i metodi args",
			"112": "non è possibile ottenere {0} modulo args",
			"113": "",
			"114": "",
			"115": "",
			"116": "",
			"117": ""
		}