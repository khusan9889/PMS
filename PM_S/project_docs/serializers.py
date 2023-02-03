from rest_framework import serializers
from .models import Project_docs

class Project_docsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_docs
        fields =  '__all__'

    