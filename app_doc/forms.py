from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):

    nascimento = forms.DateField(
        label='data',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type':'date'
            }),
        input_formats=('%Y-%m-%d',),
    )
        
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



