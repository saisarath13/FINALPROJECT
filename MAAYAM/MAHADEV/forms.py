from django import forms

class GeeksForm(forms.Form):
	name = forms.CharField()
	event = forms.CharField()
	geeks_field = forms.ImageField()
