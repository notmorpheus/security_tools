import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_requests_basic(n):
    for _ in range(n):
        response = requests.get("https://api.linode.com", timeout=2)
        print (response.json())

#this should be about twice as fast as basic 
def send_requests_session(n):
    new_session=requests.session()
    for _ in range(n):
        response= new_session.get("https://api.linode.com")
        print(response.json())

def send_requests_threaded(n): 
    
    def send_requests_session(session):
        
        for _ in range(n):
            response= session.get("https://api.linode.com/")
            return response

    new_session=requests.session()
    
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_index = { executor.submit(send_requests_session, new_session): i for i in range (n)}
        for future in as_completed(future_to_index): 
            data = future.result()
            print(data)
    new_session.close()
    
    
if __name__ == "__main__" : 

    start_time = time.time()

    no_of_requests = 6000
    #send_requests_basic(no_of_requests)
    #send_requests_session(no_of_requests)
    send_requests_threaded(no_of_requests)
    total_time = time.time()-start_time
    print(f"\nTotal Time took: {total_time} seconds\n\n Rate: {float(no_of_requests/total_time)} r/s")