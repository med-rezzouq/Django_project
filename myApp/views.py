from django.shortcuts import render,get_object_or_404
from myApp.models import Book
import json


booksData = open('C:/Users/medre/OneDrive/Bureau/python/djangoProject/books.json').read()
data = json.loads(booksData)

def index(request):
    dbData= Book.objects.all()
    context = {'books':dbData}
    return render(request,'myApp/index.html',context)


def show(request,id):

    #we did first because the result of filter is another array so we need to select 0 index
    # singleBook = Book.objects.filter(id=id).first()
   
    singleBook = get_object_or_404(Book,pk=id)

    context = {'book':singleBook}
    return render(request,'myApp/show.html',context)    


# def show(request,id):
#     singleBook = list()
#     for book in data:
#         if book['id']==id:
#             singleBook = book

#     context = {'book':singleBook}
#     return render(request,'myApp/show.html',context)    
