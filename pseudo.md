funzione importaPrestazioniDaAPI(idGroupOpzionale):
    // Effettua una chiamata GET all'API
    rispostaAPI = chiamataGET("https://extsrv.clinica_x.com/api/activities", { "idGroup": idGroupOpzionale })

    // Analizza la risposta dell'API
    per ogni prestazione in rispostaAPI:
        service_id = prestazione.idActivity
        specialty_id = prestazione.idGroup
        service_name = prestazione.name
        service_price = prestazione.price

        // Salva o aggiorna le informazioni sulle specialità
        prova:
            specialties.store(specialty_id, prestazione.groupName)
        cattura Eccezione:
            // Gestisci l'eccezione in caso di errori nell'inserimento o aggiornamento

        // Salva o aggiorna le informazioni sui servizi
        prova:
            services.store(service_id, specialty_id, service_name, service_price)
        cattura Eccezione:
            // Gestisci l'eccezione in caso di errori nell'inserimento o aggiornamento

// Chiamata all'API senza specificare idGroup per ottenere tutte le prestazioni
importaPrestazioniDaAPI()

// Chiamata all'API con specifica specialità (idGroup) per ottenere prestazioni di una specifica specialità
// importaPrestazioniDaAPI(123456)
