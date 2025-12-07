from django.contrib import admin
from .models import Message, JobData, Pricing, Staff, BeforAfterImg, ServiceDetail, BlogDetailsView, ServiceCategory, AdditionalImage

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'shorter_message')
    search_fields = ('name', 'email')
    list_filter = ['email']
    ordering = ['-id']

    @admin.display(description="Message")   
    def shorter_message(self, obj):
        return (obj.message[:50] + '....') if len(obj.message) > 50 else obj.message



@admin.register(JobData)
class JobDataAdmin(admin.ModelAdmin):
    list_display = ('email', 'service', 'fileformat', 'background', 'file', 'message', 'checked')
    search_fields = ['email']
    list_filter = ['service']
    ordering = ['-id']

    @admin.display(description="JobData")
    def message(self, obj):
        return (obj.message[:20] + "....") if len(obj.message) > 20 else obj.message


@admin.register(ServiceCategory)
class ServiceCategory(admin.ModelAdmin):
    list_display = ('img', 'servicecategory_name')




@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('title', 'simple_category', 'complex_category', 'super_complex')



@admin.register(BeforAfterImg)
class BeforAfterImgAdmin(admin.ModelAdmin):
    list_display = ['before_img', 'after_img']


@admin.register(ServiceDetail)
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'working_process_h2', 'pricing_h2')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)



@admin.register(BlogDetailsView)
class BlogDetailsViewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)



@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'department')
    search_fields = ('name',)



@admin.register(AdditionalImage)
class AdditionalImageAdmin(admin.ModelAdmin):
    list_display = ('intro_image', 'intro_overlay_image') 


