# Create your views here.
from django.http import HttpResponse
import json
from models import TimelineVisitor
from time import time


def timeline(request, user_id):
    visitor = TimelineVisitor(user_id)
    count = request.GET.get('count', '100')
    timeline = visitor.range(count=int(count))
    callback = request.GET.get('callback', None)
    response_text = json.dumps(timeline)
    if callback:
        response_text = '%s(%s);' % (callback, response_text)
    return HttpResponse(response_text,
                        mimetype='application/json')
