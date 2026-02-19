from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send Email Logic
            try:
                # Email to Admin
                # Email to Admin
                from django.core.mail import EmailMessage
                email = EmailMessage(
                    subject=f"New Contact Message: {contact_message.subject}",
                    body=f"Name: {contact_message.name}\nEmail: {contact_message.email}\n\nMessage:\n{contact_message.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.ADMIN_EMAIL],
                    reply_to=[contact_message.email],
                )
                email.send(fail_silently=False)
                # Confirmation to User
                send_mail(
                    subject="Thank you for contacting me",
                    message=f"Hi {contact_message.name},\n\nI have received your message regarding '{contact_message.subject}' and will get back to you shortly.\n\nBest regards,\nKeerthana",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[contact_message.email],
                    fail_silently=False,
                )
            except Exception as e:
                # Log the error (in a real app, use logging)
                print(f"Email sending failed: {e}")
                # We still consider the message "sent" to the DB, but maybe warn the user?
                # For now, we'll just proceed as success creates a better UX than crashing, 
                # and the admins can check the DB.

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'contact_app/contact.html', {'form': form})
