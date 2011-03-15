from django.shortcuts import *
from django.template import RequestContext
from django.core.paginator import Paginator
from util import paginate

from models import *

def galleries(request):
    return render_to_response('gallery/gallery_list.html')


def gallery(request):
    return render_to_response('gallery/gallery_detail.html')

