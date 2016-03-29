# coding: utf-8

from django.core.urlresolvers import reverse
from django.contrib import admin

from django_tinymce.widgets import TinyMCE

from .models import TestPage, TestInline


class TinyMCETestInlineAdmin(admin.StackedInline):
    model = TestInline
    extra = 1

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content1', 'content2'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'external_link_list_url': reverse('django_tinymce.views.flatpages_link_list'),
                },
            ))
        return super(TinyMCETestInlineAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class TinyMCETestPageAdmin(admin.ModelAdmin):
    inlines = [TinyMCETestInlineAdmin]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content1', 'content2'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('django_tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCETestPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(TestPage, TinyMCETestPageAdmin)
