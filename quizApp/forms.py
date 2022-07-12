from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import *


class addQuestionForm(ModelForm):
    class Meta:
        model = QuizModel
        fields = "__all__"