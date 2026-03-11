import requests
import time
import statistics
import storage 

def run_tests():
    url = "https://api.frankfurter.app/latest?from=EUR&to=USD"
    latencies = []
    passed = 0
    dernier_taux = "N/A" # Variable pour stocker le taux récupéré
    
    for i in range(5): 
        try:
            start = time.perf_counter()
            r = requests.get(url, timeout=3)
            lat = (time.perf_counter() - start) * 1000
            latencies.append(lat)
            
            if r.status_code == 200:
                data = r.json()
                if "rates" in data:
                    passed += 1
                    dernier_taux = data['rates']['USD'] # On récupère le taux ici
        except Exception as e:
            print(f"Erreur itération {i}: {e}")

    # Calcul des métriques finales
    success_rate = (passed / 5) * 100
    avg_lat = statistics.mean(latencies) if latencies else 0
    
    # Message de détail pour la BDD
    message_detail = f"Taux récupéré : 1 EUR = {dernier_taux} USD"
    
    # On enregistre UNE SEULE FOIS à la fin du run
    storage.save_run(success_rate, avg_lat, message_detail)

if __name__ == "__main__":
    run_tests()
