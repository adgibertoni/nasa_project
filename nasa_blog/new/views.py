from django.shortcuts import render
from new.models import New
from django.views.generic import ListView, DetailView
# Create your views here.´

class NewListView(ListView):
    model = New
    paginated_by = 3
    template_name = "picture/new_list.html"

class NewDetailView(DetailView):
    model = New
    template_name = "new/new_detail.html"

    def get(self, request, pk):
        new = New.objects.get(id=pk)
        context = {
            "new": new,
        }
        return render(request, self.template_name, context)
