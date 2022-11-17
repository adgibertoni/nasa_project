from django.shortcuts import render
from top10.models import Top10
from django.views.generic import ListView, DetailView
# Create your views here.

class Top10ListView(ListView):
    model = Top10
    paginated_by = 3
    template_name = "picture/top10_list.html"

class Top10DetailView(DetailView):
    model = Top10
    template_name = "top10/top10_detail.html"

    def get(self, request, pk):
        top10 = Top10.objects.get(id=pk)
        context = {
            "top10": top10,
        }
        return render(request, self.template_name, context)
