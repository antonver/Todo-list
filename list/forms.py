from django import forms

from list.models import Task, Tag


class TaskForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date", "class": "datepicker"}))
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type": "date", "class": "datepicker"}),
                               required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        fields = "__all__"
        model = Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"