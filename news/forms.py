from django import forms  #Import forms from django
from .models import Article

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
class NewArticleForm(forms.ModelForm):   #create a form class inheriting Form class from forms module
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }