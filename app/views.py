from django.shortcuts import *

def index(request):
    return render_to_response('index.html')
