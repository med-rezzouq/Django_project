from django.shortcuts import render,get_object_or_404, redirect
from myApp.models import Book,Review
from django.views.generic import ListView,DetailView
import json


# booksData = open('C:/Users/medre/OneDrive/Bureau/python/djangoProject/books.json').read()
# data = json.loads(booksData)


class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()

# def index(request):
#     dbData= Book.objects.all()
#     context = {'books':dbData}
#     return render(request,'myApp/index.html',context)



class BookDetailView(DetailView):
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        return context    
# def show(request,id):

#     #we did first because the result of filter is another array so we need to select 0 index
#     # singleBook = Book.objects.filter(id=id).first()
   
#     singleBook = get_object_or_404(Book,pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book':singleBook, 'reviews' : reviews}
#     return render(request,'myApp/show.html',context)    

def review(request,id):
      review = request.POST['review']
      newReview = Review(body=review,book_id=id)  
      newReview.save()
      return redirect("/myApp")
# def show(request,id):
#     singleBook = list()
#     for book in data:
#         if book['id']==id:
#             singleBook = book

#     context = {'book':singleBook}
#     return render(request,'myApp/show.html',context)    
