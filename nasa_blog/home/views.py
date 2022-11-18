import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from home.forms import UserRegisterForm
from home.forms import UserUpdateForm
from new.models import New
from home.models import About


def index(request):		
	return render(
		request=request,
		context={},
		template_name="home/index.html",
	)

def register(request):
    form = UserRegisterForm(request.POST) if request.POST else UserRegisterForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente!")
            return redirect("login")

    return render(
        request=request,
        context={"form": form},
        template_name="registration/register.html",
    )


@login_required
def user_update(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home:index")

    form = UserUpdateForm(model_to_dict(user))
    return render(
        request=request,
        context={"form": form},
        template_name="registration/user_form.html",
    )


def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(title__contains=search_param)
        query.add(Q(header__contains=search_param), Q.OR)
        news = New.objects.filter(query)
        context_dict.update(
            {
                "news": news,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )

# def about(request):
#     about = About.objets.all()
#     context_dict = {"about": about}
#     return render (
#         request=request,
#         context=context_dict,
#         template_name="home/about.html",
#     )

# class AboutDetailView(DetailView):
#     model = About
#     template_name = "home/about.html"
#     fields = ["description"]

#     def get(self, request, pk):
#         description = About.objets.get(id=pk)
#         context = {
#             "description": description,
#         }
#         return render(request, self.template_name, context)

class AboutListView(ListView):
    model = About
    paginate_by = 1
    template_name ="home/about_list.html"