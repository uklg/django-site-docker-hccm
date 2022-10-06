diff --git a/Dockerfile b/Dockerfile
index 1b49a55..34a400b 100644
--- a/Dockerfile
+++ b/Dockerfile
@@ -6,6 +6,7 @@ ENV PYTHONUNBUFFERED 1
 # Set work directory
 WORKDIR /code
 ## Install dependencies
+
 COPY Pipfile Pipfile.lock /code/
 RUN pip install pipenv && pipenv install --system
 RUN pip install whitenoise
@@ -15,3 +16,6 @@ RUN apt-get update
 RUN apt-get install expect -y
 ## Copy project
 COPY . /code/
+
+#RUN cp -pr /usr/local/lib/python3.8/site-packages/django/contrib/admin /code/staticfiles/
+
diff --git a/config/urls.py b/config/urls.py
index a982b23..6a329c5 100644
--- a/config/urls.py
+++ b/config/urls.py
@@ -15,9 +15,17 @@ Including another URLconf
 """
 from django.contrib import admin
 from django.urls import path, include
+from django.views.static import serve 
+from django.conf import settings
+
+from django.conf.urls.static import static
+
+
 
 urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('pages.urls')),
     path('__debug__/', include('debug_toolbar.urls')),
+    path('static/', serve,{'document_root': settings.STATIC_ROOT}),
+    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
 ]
diff --git a/db.sqlite3 b/db.sqlite3
index bf5949c..7ca8f84 100644
Binary files a/db.sqlite3 and b/db.sqlite3 differ
