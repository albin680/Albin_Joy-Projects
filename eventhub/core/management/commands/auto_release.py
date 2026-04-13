from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from core.models import Booking

class Command(BaseCommand):
    help = "Auto release vendor payments after 2 days"

    def handle(self, *args, **kwargs):

        two_days_ago = timezone.now().date() - timedelta(days=2)

        bookings = Booking.objects.filter(
            event_date__lte=two_days_ago,
            status='confirmed',
            payout_released=False
        )

        for booking in bookings:
            booking.status = 'released'
            booking.payout_released = True
            booking.payout_date = timezone.now()
            booking.save()

        self.stdout.write("Auto payout completed")