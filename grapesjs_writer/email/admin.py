from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import EmailTemplate

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'template_id', 'name', 'created_at', 'updated_at']
    add_form_template = 'grapesjs_writer/email_template_change_form.html'
    change_form_template = 'grapesjs_writer/email_template_change_form.html'
    fieldsets = [
        (
            _("template metadata"),
            {
                "fields": ["name", "template_id"],
                "classes": ["collapse", "wide"]
            },
        ),
        (
            None,
            {
                "fields": ["template_code", "template_data"],
                "classes": ["hide-raw-data"]
            }
        )
    ]
