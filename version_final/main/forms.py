from django import forms



def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')

class ContactForm(forms.Form):
    email = forms.EmailField(label='Email' ,required=True,widget=forms.TextInput(attrs={'class': 'text-center', 'placeholder':'Ingresa tu email', 
    'style':'width:300px; border-radius:12px; border:1px solid; height:40px; border-color:#E6ECF8; min-width:50%; max-width:100%; padding: calc(0.75rem - 1px; '}))
    name = forms.CharField(label='Nombre' ,max_length=80, required=True, widget=forms.TextInput(attrs={'class': 'text-center', 'placeholder':'Ingresa tu nombre',
     'style':'width:300px; border-radius:12px; border:1px solid; height:40px; border-color:#E6ECF8; min-width:50%; max-width:100%; padding: calc(0.75rem - 1px); '}))
    message = forms.CharField(label='Mensaje' , required=True, widget=forms.Textarea(attrs={'class': 'text-center', 'placeholder':'Escribe tu Mensaje aqui', 
    'style':' height:300px; Width:400px; border-radius:12px; border:1px solid; border-color:#E6ECF8; display:flex; flex-direction:column; min-width:100%; max-width:100%; padding: calc(0.75rem - 1px); '}))