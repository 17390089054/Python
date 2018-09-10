from django.contrib import admin
from learning_logs.models import Topic,Entry
from learning_logs.models import Pizza,Topping
# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Pizza)
admin.site.register(Topping)
