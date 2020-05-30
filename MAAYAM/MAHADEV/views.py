from django.shortcuts import render
from .forms import GeeksForm
from .models import GeeksModel

# Create your views here.
def hi(request):
	context = {}
	if request.method == "POST":
		form = GeeksForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data.get("name")
			event = form.cleaned_data.get("event")
			img = form.cleaned_data.get("geeks_field")
			obj = GeeksModel.objects.create(
								title = name,
				                event  = event,
								img = img
								)
			obj.save()
			print(obj)
	else:
		form = GeeksForm()
	context['form']= form
	return render(request, "MAHADEV/hi.html", context)

