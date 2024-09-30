from telegram import Update
import json
from django.http import JsonResponse
from apps.telegram.dispatcher import dispatcher, bot
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def message_handler(request):
    update = Update.de_json(json.loads(request.body), bot)
    dispatcher.process_update(update)
    return JsonResponse({"ok": True})