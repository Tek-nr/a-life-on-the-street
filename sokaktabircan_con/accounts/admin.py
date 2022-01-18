from django.contrib import admin
from .models import FeedBanks, VeterinaryClinic


class FeedBanksAdmin(admin.ModelAdmin):
    list_display = ["user","feedbank_name","phone_number","publishing_date"] # hangi başlıklar gözüksün
    list_display_links = ["user","feedbank_name"] #verilen alanlara tıklandığında içeriğe erişim sağlar
    list_filter = ["user","feedbank_name"]
    search_fields = ["feedbank_name"]
    prepopulated_fields = {'slug':('feedbank_name',)}


    class Meta:
        model = FeedBanks

admin.site.register(FeedBanks, FeedBanksAdmin)

class VeterinaryClinicAdmin(admin.ModelAdmin):
    list_display = ["name","phone_number","account","publishing_date"] # hangi başlıklar gözüksün
    list_display_links = ["name","phone_number"] #verilen alanlara tıklandığında içeriğe erişim sağlar
    list_filter = ["name","phone_number"]
    search_fields = ["name","phone_number"]
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model = VeterinaryClinic

admin.site.register(VeterinaryClinic, VeterinaryClinicAdmin)
