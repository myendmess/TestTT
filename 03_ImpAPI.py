import requests
import specialties
import services

def import_and_store_data(api_url, idGroup=None):
    try:
        response = requests.get(api_url, params={'idGroup': idGroup} if idGroup else {})
        data = response.json()

        for activity in data:
            specialty_id = activity['idGroup']
            specialty_name = activity['groupName']
            service_id = activity['idActivity']
            service_name = activity['name']
            service_price = activity['price']

            # Salvataggio delle informazioni sulla base dati di Tuotempo
            specialties.store(specialty_id, specialty_name)
            services.store(service_id, specialty_id, service_name, service_price)

    except Exception as e:
        print(f"Si è verificato un errore durante l'importazione o durante il salvataggio dei dati: {str(e)}")

# Esempio  utilizzo
api_url = "https://extsrv.clinic_x.com/api/activities"
import_and_store_data(api_url)
