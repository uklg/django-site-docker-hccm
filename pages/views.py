from django.views.generic import TemplateView
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
import boto3

from django.urls import resolve


# TODO add expect to docker compose




def contactViewD(request):
    current_url = resolve(request.path_info).url_name
    if request.method == 'GET':
        form = ContactForm()

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            submit_name = form.cleaned_data['submit_name']
            submit_email = form.cleaned_data['submit_email']
            submit_number = form.cleaned_data['submit_number']
            submit_message = form.cleaned_data['submit_message']
            try:
                if settings.DEBUG:
                    print(submit_name, submit_email, submit_number, submit_message, ['admin@example.com'])
                else:
                    #pass
                    def getsendmailapikey():
                        fd=open('aws.env','r')
                        keyline=fd.readlines()[0].strip()
                        delimiter=":"

                        splitkey=keyline.split(delimiter)
                        keyid=splitkey[0].strip()
                        keypass=splitkey[1].strip()
                        return(keyid,keypass)

                    #message = Mail(
                    #    from_email='richmurdo@gmail.com',
                    #    to_emails='richmurdo@gmail.com',
                    #    subject='Message from holly website',
                    #    html_content=f"<strong>Name: {submit_name} <br> From email: {submit_email} \
                    #                   <br> {submit_number} <br> {submit_message} </strong>")
                    try:
                        creds=getsendmailapikey()
                        client = boto3.client(
                            'ses',
                            region_name='us-east-1',
                            aws_access_key_id=creds[0],
                            aws_secret_access_key=creds[1]
                        )


                        response = client.send_email(
                            Destination={
                                'ToAddresses': ['richmurdo@gmail.com'],
                            },
                            Message={
                                'Body': {
                                    'Text': {
                                        'Charset': 'UTF-8',
                                        'Data': 'email body string',
                                    },
                                },
                                'Subject': {
                                    'Charset': 'UTF-8',
                                    'Data': 'email subject string',
                                },
                            },
                            Source='richmurdo@gmail.com',
                        )




                        print(response)
                    except Exception as e:
                        print(e.message)

                    print('not debug no email api setup') 
                    print(submit_name, submit_email, submit_number, submit_message, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('demolition')
            #form='blah'
    return render(request, "index.html", {'form': form, 'current_url': current_url})


#todo  add a success that says thanks we will be in touch

# todo add logs

