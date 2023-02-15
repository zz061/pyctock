from django.urls import path
from book.views import index


urlpatterns = [
        # path('admin/', admin.site.urls),
        path('index/',index)
]
