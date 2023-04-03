import os

def checkSettingsFile(filepath):
    f = open(filepath, "rt")
    data = f.read()

    if "'DIRS': []," and "'django.contrib.staticfiles'," and "STATIC_URL = '/static/'" in data:
       print("'HELLO world'")
    elif "path('admin/', admin.site.urls)," in data:
        print("'HELLO world Urls'")
    elif '"django.contrib.staticfiles"' and '"DIRS": [],' and 'STATIC_URL = "static/"' in data:
        print('"HELLO world"')
    elif 'path("admin/", admin.site.urls),' in data:
        print('"HELLO world urls"')


checkSettingsFile("test.txt")