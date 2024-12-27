from rest_framework import serializers
from .models import ProductsModel, AdministrationModel, CategoryModel

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = "__all__"






"""class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrationModel
        fields = ['name', 'achievement', 'experience', 'skills', 'bio', 'image']

    def create(self, validated_data):
        return AdministrationModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.skills = validated_data.get('skills', instance)
        instance.name = validated_data.get('name', instance)
        instance.image = validated_data.get('image', instance)
        instance.achievement = validated_data.get('achievement', instance)
        instance.experience = validated_data.get('experience', instance)
        instance.bio = validated_data.get('bio', instance)
        instance.save()
        return instance"""

