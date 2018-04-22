from django import forms
from .models import Comment

# 继承自forms.ModelsForm
class CommentForm(forms.ModelForm):
    # 要写class Meta
    class Meta:
        # 用Comment这个model创建form
        model = Comment
        # 创建form用哪些字段.对应Comment模型的字段
        fields = ['name','email','url','text']