from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .models import ContactMessage

class ContactTests(TestCase):
    def test_contact_page_load(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_app/contact.html')

    def test_contact_form_submission(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Inquiry',
            'message': 'Hello there'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302) # Redirects to home on success
        
        # Verify message saved
        self.assertEqual(ContactMessage.objects.count(), 1)
        
        # Verify emails sent (one to admin, one confirmation)
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].subject, "New Contact Message: Inquiry")
        self.assertEqual(mail.outbox[1].subject, "Thank you for contacting me")

