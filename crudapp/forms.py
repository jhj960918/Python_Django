from django import forms
from .models import Blog
class BlogUpdate(forms.ModelForm):#model을 기반으로 forms클래스의 modelform을 인자로 넘겨준다
    class Meta:
        model = Blog
        fields=['title','body']