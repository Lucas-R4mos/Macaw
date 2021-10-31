import json
from flask import Response

def check_json_return_data(request):
    if request.is_json and request.data:
        return json.loads(request.data)
    else:
        return None