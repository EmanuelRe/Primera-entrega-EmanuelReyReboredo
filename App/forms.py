from django import forms

class FormularioMascotas(forms.Form):
   
    animal = forms.CharField(max_length=30)
    raza = forms.CharField(max_length=30)
    nombre = forms.CharField(max_length=20)


class FormularioDueños(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    DNI = forms.IntegerField()
    mascota = forms.CharField(max_length=30)

class FormularioEncargados(forms.Form):

    nombre = forms.CharField(max_length=30)
    DNI = forms.IntegerField()
    telefono = forms.IntegerField()

