# Pull base image
FROM python:3.10
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
## Install dependencies

COPY Pipfile Pipfile.lock /code/
#RUN pip install pipenv && pipenv install --system
#RUN pip install whitenoise
##RUN pip install django-debug-toolbar
#RUN pip install sendgrid
RUN apt-get update
RUN apt-get install expect -y
## Copy project

COPY . /code/
RUN pip install -r /code/requirements.txt

#RUN cp -pr /usr/local/lib/python3.8/site-packages/django/contrib/admin /code/staticfiles/
#RUN cp -pr /usr/local/lib/python3.8/site-packages/django/contrib/admin /app/staticfiles/



#RUN cp -pr /usr/local/lib/python3.8/site-packages/django/contrib/admin /code/staticfiles/
#RUN mkdir /app/staticfiles
#RUN cp -pr /usr/local/lib/python3.8/site-packages/django/contrib/admin /app/staticfiles/


RUN /code/manage.py makemigrations
RUN /code/manage.py migrate
RUN /code/expect
RUN /code/manage.py collectstatic

EXPOSE 8000

CMD ["/code/manage.py", "runserver", "0.0.0.0:8000"]
