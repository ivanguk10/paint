from django import forms
from .models import Comment


class CommentForm(forms.Form):
    comment_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'placeholder': "Имя"}), max_length=50, label="")
    comment_email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'email', 'placeholder': "Email"}), max_length=100, label="")
    comment_theme = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'type': 'text', 'placeholder': 'Тема'}), max_length=50, label="")
    comment_body = forms.CharField(min_length=10, widget=forms.Textarea(
        attrs={'class': 'textarea', 'placeholder': 'Ваш отзыв', 'rows': 4}), label="")

    def save(self):
        new_comment = Comment.objects.create(
            comment_name=self.cleaned_data['comment_name'],
            comment_email=self.cleaned_data['comment_email'],
            comment_theme=self.cleaned_data['comment_theme'],
            comment_body=self.cleaned_data['comment_body']
            )
        return new_comment
