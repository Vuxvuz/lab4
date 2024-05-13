import http.client
from urllib.parse import urlencode
import time

key = "2QACR5MRWUQ9JY6Z"  # Put your API Key here

def thermometer():
    # Calculate CPU temperature of Raspberry Pi in Degrees C
    temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000  # Get Raspberry Pi CPU temp
    
    # Create parameters for the request
    params = urlencode({'field1': temp, 'key': key}) 
    
    # Headers for the request
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    
    # Create a connection to ThingSpeak
    conn = http.client.HTTPSConnection("api.thingspeak.com")
    
    try:
        # Send POST request to update ThingSpeak channel
        conn.request("POST", "/update", params, headers)
        
        # Get response from ThingSpeak
        response = conn.getresponse()
        
        # Print temperature, response status, and reason
        print(temp)
        print(response.status, response.reason)
        
        # Read and print data from the response
        data = response.read()
        
        # Close the connection
        conn.close()
        
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    while True:
        # Call the thermometer function
        thermometer()
        # Wait for 15 seconds before next reading
        time.sleep(15)
