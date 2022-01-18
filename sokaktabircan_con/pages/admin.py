from django.contrib import admin
from django.forms import models
from .models import Adoption, Age, Brand, Breed, ContactUs, FoodType, Gender, Order, OrderItem, Post, Treatment


class PostAdmin(admin.ModelAdmin):
    list_display = ["header","brand","breed","age", "food_type", "price"] # hangi başlıklar gözüksün
    list_display_links = ["header","price"] #verilen alanlara tıklandığında içeriğe erişim sağlar
    list_filter = ["publishing_date", "brand","breed","age", "food_type"]
    search_fields = ["header","breed","age", "food_type"]
    prepopulated_fields = {'slug':('header',)}

    class Meta:
        model = Post

# Register your models here.
admin.site.register(Post, PostAdmin) #olusturulan model admin paneline eklendi

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ["user","header","breed","clinic","cost"] # hangi başlıklar gözüksün
    list_display_links = ["header","breed", "cost"] #verilen alanlara tıklandığında içeriğe erişim sağlar
    list_filter = ["publishing_date", "breed","clinic"]
    search_fields = ["header"]
    prepopulated_fields = {'slug':('header',)}

    class Meta:
        model = Treatment
admin.site.register(Treatment,TreatmentAdmin)

class AdoptionAdmin(admin.ModelAdmin):
    list_display = ["user","name","breed","gender","publishing_date"] # hangi başlıklar gözüksün
    list_display_links = ["user","name","breed","gender","publishing_date"] #verilen alanlara tıklandığında içeriğe erişim sağlar
    list_filter = ["publishing_date","breed","gender","age"]
    search_fields = ["user","breed","gender"]
    prepopulated_fields = {'slug':('header',)}

    class Meta:
        model = Adoption
admin.site.register(Adoption, AdoptionAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["topic","email","publishing_date"] # hangi başlıklar gözüksün
    list_display_links = ["topic","email","publishing_date"] #verilen alanlara tıklandığında içeriğe erişim sağlar
    search_fields = ["topic"]

    class Meta:
        model = Adoption
admin.site.register(ContactUs, ContactUsAdmin)

class BreedAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Breed, BreedAdmin)

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Brand, BrandAdmin)

class AgeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Age, AgeAdmin)

class GenderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Gender, GenderAdmin)

class FoodTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(FoodType, FoodTypeAdmin)

admin.site.register(Order)
admin.site.register(OrderItem)


