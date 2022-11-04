from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render


def index(request):		
	return render(
		request=request,
		context={},
		template_name="home/index.html",
	)
