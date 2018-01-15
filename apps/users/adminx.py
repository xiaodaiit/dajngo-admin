# -*- coding: utf-8 -*

import xadmin
from xadmin import views
# from xadmin.plugins.auth import UserAdmin
# from xadmin.layout import Fieldset, Main, Side, Row
# from django.utils.translation import ugettext as _

from .models import EmailVerifyRecord, Banner, UserProfile

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"  #(设置左侧


class EmailVerifyRecorAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']  #(自定义显示列)
    search_fields = ['code', 'email', 'send_type',]  #(自定义显示列)
    list_filter = ['code', 'email', 'send_type', 'send_time']  #(自定义显示列)

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecorAdmin)

xadmin.site.register(views.CommAdminView, GlobalSettings) #(全局配置
xadmin.site.register(views.BaseAdminView, BaseSetting)#(主题功能)