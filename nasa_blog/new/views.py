from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from new.forms import NewForm
from new.forms import CommentNewForm
from new.models import New
from new.models import CommentNew

class NewListView(ListView):
    model = New
    paginated_by = 3
    template_name = "picture/new_list.html"

class NewDetailView(DetailView):
    model = New
    template_name = "new/new_detail.html"

    def get(self, request, pk):
        new = New.objects.get(id=pk)
        commentsnew = CommentNew.objects.filter(new=new).order_by("-updated_at")
        commentnew_form = CommentNewForm()
        context = {
            "new": new,
            "commentsnew": commentsnew,
            "commentnew_form": commentnew_form,
        }
        return render(request, self.template_name, context)

class NewCreateView(LoginRequiredMixin, CreateView):
    model = New
    success_url = reverse_lazy("new:new-list")
    form_class = NewForm
    
    def form_valid(self, form):
        #para evitar usar mismo título y autor
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = New.objects.filter(
            title=data["title"], header=data["header"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"{data['title']} ya fue creada",
            )
            form.add_error("title", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Noticia {data['title']} agregada exitosamente",
            )
            return super().form_valid(form)

class NewUpdateView(LoginRequiredMixin, UpdateView):
    model = New
    form_class = NewForm
    
    def get_success_url(self):
        new_id = self.kwargs["pk"]
        return reverse_lazy("new:new-detail", kwargs={"pk": new_id})

class NewDeleteView(LoginRequiredMixin, DeleteView):
    model = New
    success_url = reverse_lazy("new:new-list")


class CommentNewCreateView(LoginRequiredMixin, CreateView):
    #model = CommentNew
    def post(self, request, pk):
        new = get_object_or_404(New, id=pk)
        commentnew = CommentNew(
            text=request.POST["commentnew_text"], owner=request.user, new=new
        )
        commentnew.save()
        return redirect(reverse("new:new-detail", kwargs={"pk": pk}))


class CommentNewDeleteView(LoginRequiredMixin, DeleteView):
    model = CommentNew

    def get_success_url(self):
        new = self.object.new
        return reverse("new:new-detail", kwargs={"pk": new.id})
