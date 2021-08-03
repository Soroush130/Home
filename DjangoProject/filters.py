"""
این فایل مربوط به تنظیمات فیلتر کردن بر روی فیلد های مدل خانه است .
"""
import django_filters
from django_filters import DateFilter, CharFilter
from homes.models import *


class HomeFilter(django_filters.FilterSet):
    """
      فیلد(متغییر پایین) برای فیلتر کردن قیمت خانه است --->> یعنی حداقل قیمت
    """
    # price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    """
      فیلد(متغییر پایین) برای فیلتر کردن قیمت خانه است --->> یعنی حداکثر قیمت
    """
    # price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    status = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Home
        fields = ['home_type', 'city', 'bedroom', 'baths', 'garage']


"""
نکته مهم این است که اگر بخواهیم برای یک فیلد یک بازه تعیین کنیم مثلا برای فیلد قیمت یعنی بگیم از حداقل
قیمتی که کاربر وارد میکند تا حداکثر قیمتی که کاربر وارد میکند بیا شی های مورد نظر رو بگردون باید به 
صورت زیر عمل کنیم :

    
      فیلد(متغییر پایین) برای فیلتر کردن قیمت خانه است --->> یعنی حداقل قیمت
    
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')

    فیلد(متغییر پایین) برای فیلتر کردن قیمت خانه است --->> یعنی حداکثر قیمت
    
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

"""

"""
لیست لوک آپ ها در آموزش سایت کویِرا در فصل اول - قسمت orm جنگو و در فایل جستجو در فیلد موجود است ..
"""