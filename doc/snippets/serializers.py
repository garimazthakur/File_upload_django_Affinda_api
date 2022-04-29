# from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, Affinda


class SnippetSerializer(serializers.ModelSerializer):
    # owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        # fields= ('id', 'title', 'code', 'linenos', 'language', 'style','owner',)
        fields= ('id', 'title', 'code', 'linenos', 'language', 'style',)

# class UserSerializer(serializers.ModelSerializer):
#     snippets= serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#     #https://www.django-rest-framework.org/api-guide/relations/#stringrelatedfield
#     class Meta:
#         model=User
#         fields=('id', 'username', 'snippets')

class AffindaSerializer(serializers.ModelSerializer):
    """
    AffindaSerializer class is created with Affinda Model and added
    all field from AffindaSerializer Model
    """

    class Meta:
        model = Affinda
        fields = "__all__"


