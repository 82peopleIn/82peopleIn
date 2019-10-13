
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Question, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']

    widgets = {
        'title': forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목'}
        ),
        'content': forms.CharField(widget=CKEditorUploadingWidget()),
}



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message',]

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'style': 'width:100%', 'rows': 5, 'placeholder': '', }
        ),
        label=''
    )

