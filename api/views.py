from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Books
import json

def get_api_books(requests):
    try:
        books=Books.objects.all()
        names = [books.name for book in books]
        if(len(names)==0):
            my_string="No books found"
            return JsonResponse({'my_string':my_string})
        return JsonResponse({'names': names})
    except Exception as e:
        return JsonResponse({'error':str(e)})
    #return JsonResponse({'error': 'Invalid request method'})
def post_api_books(requests):
    try:
        data=json.loads(requests.body.decode('utf-8'))
        required_fields=['name']
        for f in required_fields:
            if f not in data:
                return JsonResponse({'error':'missing required fields'})
        return JsonResponse({'message':'succesfully saved data'})
    except json.JSONDecodeError:
        return JsonResponse({'error':'Invalid Json data'})
    except Exception as e:
        return JsonResponse({'error':str(e)})
    #we can also give role based access control so that not everybody could post data

def put_api_books(request,id):
    try:
        book=Books.objects.get(pk=id)
        data=json.loads(request.body.decode('utf-8'))
        if 'name' in data:
            book.name=data['name']
        if 'container_name' in data:
            book.book_container=data['container_name']
        if 'registered' in data:
            book.registered=data['registered']
        if 'reg_under' in data:
            book.reg_under=data['reg_under']
        book.save()
        return JsonResponse({'message':' Data updated succesfully'})
    except Books.DoesNotExist:
        return JsonResponse({'error':'Book not found'})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

# Create your views here.
