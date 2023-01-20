from fiveth_app.models import *
import datetime
d=datetime.date(1997,10,19)
a=TestTime.objects.create(a=d)
a.save()