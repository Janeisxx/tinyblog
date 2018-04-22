from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms



class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','nickname',
                  'headshot','signature']


class EditForm(forms.ModelForm):
    class Meta:
        model = User
        # 这样headshot在修改页面只会显示地址,不会显示图片
        # 提交也提交不上去
        # fields = ['username','email','signature','headshot']

        fields = ['username','email','signature']





