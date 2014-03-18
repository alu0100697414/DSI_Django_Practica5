# Create your views here.

from django.http import HttpResponse
 
def quick_test(request):
	return HttpResponse("Hello testing world!");
