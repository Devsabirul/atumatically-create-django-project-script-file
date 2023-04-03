# f = open("D://Programming//Django//blog//blog//settings.py", "r")
# f = open("t.txt", "r")

# line_index = 2
# lines = None

# lines = f.readlines()
# lines.insert(line_index, 'import os')

# f = open('t.txt', 'w')
# f.writelines(lines)


# data = f.read()
# data = data.replace(
#     '"DIRS": [],', '"DIRS": [os.path.join(BASE_DIR,"templates")],')
# # f = open("t.txt", "w")
# f = open("D://Programming//Django//blog//blog//settings.py", "w")
# f.write(data)
# f.close()

# import fileEdit

import os
print(os.getcwd())
# fileEdit.add_text(
#     'D://Programming//Django//blogproject//blogproject//settings.py', 'import os', 13)
# fileEdit.replace('D://Programming//Django//blogproject//blogproject//settings.py',
#                  "'DIRS': [],", '"DIRS": [os.path.join(BASE_DIR, "templates")],')

# fileEdit.replace('D://Programming//Django//blogproject//blogproject//settings.py',
#                  "STATIC_URL = '/static/'", "STATIC_URL = '/static/'\nSTATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')\nSTATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]\n\n\nMEDIA_ROOT = os.path.join(BASE_DIR, 'media')\nMEDIA_URL = '/media/'")

# fileEdit.add_text(
#     'D://Programming//Django//blogproject//blogproject//urls.py', 'from django.conf import settings\nfrom django.conf.urls.static import static\n', 17)

# fileEdit.replace('D://Programming//Django//blogproject//blogproject//urls.py',
#                  ']', '] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)')

# os.chdir('D://Programming//Django//blog')
# os.system("python manage.py startapp core")
# fileEdit.replace('D://Programming//Django//blog//blog//settings.py',
#                  "'django.contrib.staticfiles',", "'django.contrib.staticfiles',\n    'core',")
# open("D://Programming//Django//blog//core//urls.py", 'w')
# url = '''from django.urls import path\nfrom .views import *\nurlpatterns = [\n   path('', home, name="Home"),\n]
# '''

# viewFunction = '''from django.http import HttpResponse\n\n
# def home(request):
#     return HttpResponse("<div style='text-align:center;margin-top:150px'><h1>The install worked successfully! Congratulations! </h1></div>")
# '''
# fileEdit.add_text(
#     "D://Programming//Django//blog//core//views.py", viewFunction, 1)


# path('admin/', admin.site.urls),
# fileEdit.replace('D://Programming//Django//blog//blog//urls.py',
#                  'from django.urls import path', 'from django.urls import path,include')


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


checkSettingsFile("testfolder/test.txt")


