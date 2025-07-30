from django.http import JsonResponse

def hello_word(request):
    return JsonResponse({'1': 'exemplo'})