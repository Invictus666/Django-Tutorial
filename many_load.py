import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, Region, States, Iso, Site

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    Region.objects.all().delete()
    States.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

## Continue from here

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        r, created = Region.objects.get_or_create(name=row[9])
        s, created = States.objects.get_or_create(name=row[8])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
          y = int(row[3])
        except:
          y = None

        try:
          long = float(row[4])
        except:
          long = None

        try:
          lang = float(row[5])
        except:
          lang = None

        try:
          area = float(row[6])
        except:
          area = None

        site = Site(name=row[0], description=row[1], justification=row[2], year = y, longitude=long, latitude=lang, area_hectares=area, category=c,states=s,region=r,iso=i)
        site.save()
