from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
import datetime

def get(request):
        #Get current timestamp
        now = datetime.datetime.now()
        today = now.strftime('%d-%m-%Y')
        time = now.strftime('%H:%M:%S')
        #Serialize it to a JSON object
        obj = {"time": time, "today": today}
        #Return the JSON object
        return JsonResponse(obj)