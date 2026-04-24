from django import forms    # formulários Django
from .models import Projeto, Tecnologia, Formacao

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Projeto.


class TecnologiaForm(forms.ModelForm):
  class Meta:
    model = Tecnologia        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Tecnologia.


class FormacaoForm(forms.ModelForm):
  class Meta:
    model = Formacao
    fields = '__all__'
