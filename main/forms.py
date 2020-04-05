from django import forms
from .models import Room


class CreateRoomForm(forms.ModelForm):

    class Meta:
        model = Room

        fields = ['title', 'game']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': '방 제목',
            }),
            # 'game': forms.Select(attrs={
            # }),
        }
