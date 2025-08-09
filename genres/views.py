from django.http import JsonResponse
from genres.models import Genre
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

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
        print(request)
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

@csrf_exempt
def genre_detail_view(request, pk):
    if request.method == "GET":
        data = get_object_or_404(Genre, id=pk)
        return JsonResponse(
                {
                    "id" :data.id, "name": data.name
                }
            )

@csrf_exempt
def genre_delete_view(request, pk):
    if request.method == "DELETE":

        data = get_object_or_404(Genre, id=pk)
        data.delete()
        return JsonResponse(
            {'message': 'Deletado com sucesso'}
            )
    


    


