from example.models import Company, Programmer, Language


apple = Company.objects.get(pk=2)
alphabet = Company.objects.get(pk=1)
microsoft = Company.objects.get(pk=3)

lisa = Programmer.objects.get(pk=3)
ann = Programmer.objects.get(pk=1)
steve = Programmer.objects.get(pk=5)
allen = Programmer.objects.get(pk=4)
kim = Programmer.objects.get(pk=2)


>> > from example.models import Company, Programmer, Language
>> > apple = Company.objects.get(pk=2)
>> > alphabet = Company.objects.get(pk=1)
>> > microsoft = Company.objects.get(pk=3)
>> > kim = Programmer.objects.get(pk=2)
>> > ann = Programmer.objects.get(pk=1)
>> > python = Language(name='Python')
>> > nodejs = Language(name='Nodejs')
>> > sql = Language(name='Sql')
>> > c = Language(name='C')
>> > pyhton.save()
>> > python.save()
>> > c.save()
>> > nodejs.save()
>> > sql.save()
>> > kim.languages.add(c)
>> > kim.languages.add(python)
>> > lisa.languages.add(nodejs)
Traceback(most recent call last):
    File "<console>", line 1, in <module >
NameError: name 'lisa' is not defined
>> > ann.languages.add(nodejs)
>> > ann.languages.add(sql)
>> > kim.languages.all()
<QuerySet [ < Language: Python > , < Language: C > ] >
>> > ann.languages.all()
<QuerySet [ < Language: Nodejs > , < Language: Sql > ] >
>> > python.programmer_set.all()
<QuerySet [< Programmer: Kim > ] >
>> > sql.programmer_set.all()
<QuerySet [< Programmer: Ann > ] >
