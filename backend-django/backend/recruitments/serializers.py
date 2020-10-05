from rest_framework import serializers
from .models import Recruitment
from .models import Introduction
from accounts.serializers import UserSerializer

class RecruitmentListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    images = serializers.ImageField(use_url=True)
    class Meta:
        Model = Recruitment
        fields = ('division', 'title', 'startdate', 'deadline', 'images')

class RecruitmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Recruitment
        fields = '__all__'

class IntroductionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Introduction
        fields = '__all__'
