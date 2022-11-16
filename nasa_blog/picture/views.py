from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from picture.forms import CommentForm
from picture.forms import PictureForm
from picture.models import Comment
from picture.models import Picture

class PictureListView(ListView):
    model = Picture
    paginate_by = 4
    template_name = "picture/picture_list.html"

class PictureDetailView(DeleteView):
    model = Picture
    template_name = "picture/picture_detail.html"
    fields = ["title_name", "taken_by", "taken_date", "image"]

    def get(self, request, pk):
        picture = Picture.objects.get(id=pk)
        comments = Comment.objects.filter(picture=picture).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "picture": picture,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)

class PictureCreateView(LoginRequiredMixin, CreateView):
    model = Picture
    success_url = reverse_lazy("picture:picture-list")
    form_class = PictureForm
    #fields = ["title_name", "taken_by", "taken_date", "image"]

    def form_valid(self, form):
        #para evitar usar mismo título y autor
        data = form.cleaned_data
        form.instance.owner = self.request.user
        #validación que solo pueda modificar el superuser
        print(self.request.user.is_staff)
        if not self.request.user.is_staff:
            messages.error(
                self.request,
                f"El ususario no esta habilitado para realizar esta operación",
            )
            form.add_error("title_name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
            #finaliza la validación de superuser
        actual_objects = Picture.objects.filter(
            title_name=data["title_name"], taken_by=data["taken_by"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"Ya existe la imagen {data['title_name']} de {data['taken_by']}",
            )
            form.add_error("title_name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Imagen {data['title_name']} (de {data['taken_by']}) añadida exitosamente",
            )
            return super().form_valid(form)

class PictureUpdateView(LoginRequiredMixin, UpdateView):
    model = Picture
    form_class = PictureForm
    #fields = ["title_name", "taken_by", "taken_date", "image"]
    
    def get_success_url(self):
        picture_id = self.kwargs["pk"]
        return reverse_lazy("picture:picture-detail", kwargs={"pk": picture_id})

    #def post(self):
    #    pass

class PictureDeleteView(LoginRequiredMixin, DeleteView):
    model = Picture
    success_url = reverse_lazy("picture:picture-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        picture = get_object_or_404(Picture, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, picture=picture
        )
        comment.save()
        return redirect(reverse("picture:picture-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        picture = self.object.picture
        return reverse("picture:picture-detail", kwargs={"pk": picture.id})
