from django.http import JsonResponse
from genres.models import Genre
import json
from django.views.decorators.csrf import csrf_exempt


# sem rest - serializer "na mao"
@csrf_exempt
def genre_view(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        data = []
        '''for genre in genres:
            data.append(
                {'id': genre.id, "name": genre.name}
            )'''
        
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    
  
    elif request.method == "POST":
        payload = json.loads(request.body.decode('utf-8'))
        data = payload.get("name")
        new_register = Genre(name = data)
        new_register.save()
        return JsonResponse(
            {'id' : new_register.id, "name": new_register.name}, status=201,
        )


