#Use the django.test.TestCase class for tests that rely on the back-end database
#Otherwise use the unittest.TestCase class   
from django.test import TestCase
import unittest
from .models import Book
from .models import User
from jot.GoogleBookSearchAPI import getRatings

# Create your tests here.
class ApiSearchTestCase(unittest.TestCase):

    def test_api_search(self):
        #gibberish search should return the default array 
        self.assertEqual(getRatings("sdjbksfgbjqlswdgf2432ssdf"),[0,0])
        #Book has no reviews and so should return the default array - might change should consider mocking
        self.assertEqual(getRatings("the blue book of grammar and punctuation"),[0,0])
        #GetRatings should be able to take numeric titles no problem 
        self.assertNotEqual(getRatings(1984), [0,0])
        #Normal search should renturn a non-deafult result 
        self.assertNotEqual(getRatings("Lord of the Rings"),[0,0])
        
    def test_models_books(self):
        
        keyword = "Inferno"
        books_list = Book.objects.filter(book_title__icontains = keyword)
        self.assertEqual(books_list[0].book_title,"Inferno")

        keyword = "Inferno"
        books_list = Book.objects.filter(book_title__icontains = keyword)
        self.assertEqual(books_list[1].book_title,"Inferno2")


    def test_models_users(self):

        keyword = "OnionGuy34672"
        users_list = User.objects.filter(username__icontains = keyword)
        self.assertEqual(users_list[0].username,"OnionGuy34672")
