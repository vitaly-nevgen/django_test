from rest_framework import serializers

from library.models import Book


class BookSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('name', 'image')

    def get_image(self, obj):
        return {
            'url': obj.image.url if obj.image else None
        }

class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('name', )
