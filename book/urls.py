from rest_framework import routers
from book.views import *
router =routers.SimpleRouter()
router.register(r'books',BookOperations)

urlpatterns=router.urls