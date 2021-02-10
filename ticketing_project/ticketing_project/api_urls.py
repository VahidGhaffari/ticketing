from rest_framework import routers
from send_client.api_views import ticketViewset, answerticketViewset

router = routers.SimpleRouter()
router.register('ticket', ticketViewset, basename='ticket')
router.register('answer_ticket', answerticketViewset, basename='answer_ticket')
