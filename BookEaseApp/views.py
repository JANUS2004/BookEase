from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        origin = request.POST.get("origin")
        destination = request.POST.get("destination")
        transportation_type = request.POST.get("transportation_type")
        
        if transportation_type == 'bus':

            api_url1 = f'http://127.0.0.1:8000/buses/{origin}/{destination}'  # Replace with your API endpoint URL
            response = requests.get(api_url1)
            bus_data = response.json()
            if response.status_code == 200:
                   bus_data = response.json()
                   return render(request, 'bus.html', {'bus_data': bus_data})
            else:
                   return render(request, 'index.html', {'message': 'Failed to fetch bus details. Please try again!'})
       
        elif transportation_type == 'flight':
            
            api_url2 = f'http://127.0.0.1:8000/flights/{origin}/{destination}'  # Replace with your API endpoint URL
            response = requests.get(api_url2)
            flight_data = response.json()
            if response.status_code == 200:
                   flight_data = response.json()

                   return render(request, 'flight.html', {'flight_data': flight_data})
            else:
                   return render(request, 'index.html', {'message': 'Failed to fetch flight details. Please try again!'})
    return render(request, 'index.html')



