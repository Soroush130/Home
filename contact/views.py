from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from contact.forms import ContactForm
from contact.models import Contact


def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_subject = form.cleaned_data["subject"]
            new_message = form.cleaned_data["message"]

            new_contact = Contact.objects.create(name=new_name, email=new_email, subject=new_subject,
                                                 message=new_message)
            new_contact.save()
            return HttpResponse("پیام شما با موفقیت ارسال شد.")
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
