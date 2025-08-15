from django.http import JsonResponse, HttpResponse
from genres.models import Genre
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework import generics
from genres.serializers import GenreSerializer

# sem rest - serializer "na mao"

# mudar pra class-based view
#@csrf_exempt
'''def genre_view(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        data = []
        #for genre in genres:
        #    data.append(
        #        {'id': genre.id, "name": genre.name}
        #    )
        #print(request)
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

    genre = get_object_or_404(Genre, id=pk)

    if request.method == "GET":
        return JsonResponse(
                {
                    "id" :genre.id, "name": genre.name
                }
            )
    

    elif request.method == "PUT":
        payload = json.loads(request.body.decode('utf-8'))
        new_name = payload.get('name')
        if new_name:
            genre.name = new_name
            genre.save()
            return JsonResponse(
                
                    {}, status=200
                

            )
        
    elif request.method == "DELETE":
        genre.delete()
        return HttpResponse(
            status=204
            )'''



class GenreView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
    


    


