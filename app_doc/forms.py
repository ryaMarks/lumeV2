from django import forms
from .models import Cliente



class ClienteForm(forms.ModelForm):
    disjuntores = (
        ('25A-MONO', '25A - MONO'),
        ('40A-MONO', '40A - MONO'),
        ('63A-MONO', '63A - MONO'),
        ('40A-TRI', '40A - TRI'),
        ('63A-TRI', '63A - TRI'),
        ('80A-TRI', '80A - TRI'),
        ('100A-TRI', '100A - TRI'),
        ('125A-TRI', '125A - TRI'),
    )

    nascimento = forms.DateField(
        label='date',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type':'date'
            }),
        input_formats=('%Y-%m-%d',),
    )

<<<<<<< HEAD
=======
    inicio = forms.DateField(
        label='date',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type':'date'
            }),
        input_formats=('%Y-%m-%d',),
    )

    fim = forms.DateField(
        label='date',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type':'date'
            }),
        input_formats=('%Y-%m-%d',),
    )

>>>>>>> correção view procuração e datefields do modelo cliente
        
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def clean(self):
        data = self.cleaned_data
        cpf = data.get("cpf")
        qs = Cliente.objects.filter(cpf__icontains=cpf)
        if qs.exists():
            self.add_error("cpf",f"{cpf} já possui cadastro.")
        return data



