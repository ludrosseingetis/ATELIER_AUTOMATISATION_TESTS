import requests
import time
import statistics
import storage # Importe le fichier storage.py au dessus

def run_tests():
    url = "https://api.frankfurter.app/latest?from=EUR&to=USD"
    latencies = []
    passed = 0
    response = requests.get(url)
    data = response.json()
        taux_usd = data['rates']['USD']
        storage.save_run(100, 150, f"1 EUR = {taux_usd} USD")
    
    for i in range(5): # On fait 5 tests pour la QoS
        try:
            start = time.perf_counter()
            r = requests.get(url, timeout=3)
            lat = (time.perf_counter() - start) * 1000
            latencies.append(lat)
            
            if r.status_code == 200 and "rates" in r.json():
                passed += 1
        except:
            pass

    success_rate = (passed / 5) * 100
    avg_lat = statistics.mean(latencies) if latencies else 0
    
    # On enregistre dans la BDD
    storage.save_run(success_rate, avg_lat, "Test automatique Frankfurter")

if __name__ == "__main__":
    run_tests()
