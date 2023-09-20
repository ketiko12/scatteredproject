from django.contrib import admin
from .models import Post , Category


# mymodels=[Post, Category]
# admin.site.register(mymodels)(admin.ModelAdmin)
admin.site.register(Post)
admin.site.register(Category)