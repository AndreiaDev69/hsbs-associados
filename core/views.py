from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .chatbot import chatbot_response

def chat_page(request):
    return render(request, "chat.html")

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        resposta = chatbot_response(data.get("message", ""))
        return JsonResponse({"response": resposta})
    return JsonResponse({"error": "Método não permitido."}, status=405)

