from django.test import TestCase
from django.urls import reverse
from core.models import Reservation

# Create your tests here.


class KhanaPina(TestCase):
    # Test 1 - Homepage loading

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")

    ## Test 2 - Create Reservation via the model

    def test_create_reservation_model(self):
        # Create ONE object with ALL required fields
        reservation = Reservation.objects.create(
            name="Haldar",
            date="2026-01-03",  # Use YYYY-MM-DD format for DateField
            time="15:00",  # Use HH:MM format for TimeField
            guest_number=3,
            mobile="01670267006",
        )

        # Now verify the fields on that one object
        self.assertEqual(reservation.name, "Haldar")
        self.assertEqual(str(reservation.date), "2026-01-03")
        self.assertEqual(reservation.guest_number, 3)

        # Check that only one record exists in the database
        self.assertEqual(Reservation.objects.count(), 1)
