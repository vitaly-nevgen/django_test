from rest_framework import serializers

from library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'author', 'name', 'image')

    def get_image(self, obj):
        image_url = None
        if obj.image:
            image_url = obj.image.url

        return {
            'url': image_url
        }

class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('name', )
