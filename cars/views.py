#from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cars.models import Car
from .forms import CarForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class HomeView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search) 
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "new_car.html"
    success_url = "/cars/"


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = "car_update.html"
    #success_url = "/cars/"
    
    def get_success_url(self):
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = "/cars/"


#def new_car_view(request):
#    if request.method == "POST":
#        form = CarForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect("home")
#    else:
#        form = CarForm()
#    return render(request, "new_car.html",{"form": form})



#def home(request):
#    search=request.GET.get('search')
#    if search:
#        cars = Car.objects.filter(model__icontains=search)
#    else:
#        cars = Car.objects.all()
#    pessoa={
#        'nome':'Anderson Vieira',
#        'idade':40,
#        'profissao':'Desenvolvedor Web'
#    }
#    return render(request, "cars.html",{'cars':cars,'pessoa':pessoa})