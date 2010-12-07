# Create your views here.
from django.http import HttpResponse
import json
from models import TimelineVisitor


def timeline(request, user_id):
    visitor = TimelineVisitor(user_id)
    timeline = visitor.get_timeline()

    return HttpResponse(json.dumps(timeline),
                        mimetype='application/json')
