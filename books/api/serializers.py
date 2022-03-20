# https://labcodes.com.br/blog/pt-br/development/como-usar-serializers-de-django-rest-framework/
#https://youtu.be/wtl8ZyCbTbg?t=787

import rest_framework import serializers
from Books import models

class BooksSerializer(serializers.ModelSeriealizer):
  class Meta:
    model = models.Books
    fields = [
      'id_book',
      'title',
      'author',
      'release_year',
      'state',
      'pages',
      'publish_company',
      'create_at',
    ]
    # fields = '__ALL__'