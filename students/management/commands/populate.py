from django.core.management import BaseCommand

from students.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        students= [{"id":1,"first_name":"Brianna","last_name":"Ainslie","roll_number":73,"class_name":"Female"},
{"id":2,"first_name":"Junie","last_name":"Smowton","roll_number":96,"class_name":"Female"},
{"id":3,"first_name":"Merwyn","last_name":"Rennenbach","roll_number":79,"class_name":"Male"},
{"id":4,"first_name":"Katheryn","last_name":"Blant","roll_number":83,"class_name":"Female"},
{"id":5,"first_name":"Angele","last_name":"Barrell","roll_number":58,"class_name":"Female"},
{"id":6,"first_name":"Claire","last_name":"McIver","roll_number":69,"class_name":"Female"},
{"id":7,"first_name":"Winnie","last_name":"Lamminam","roll_number":88,"class_name":"Non-binary"},
{"id":8,"first_name":"Bambi","last_name":"Vuitton","roll_number":80,"class_name":"Female"},
{"id":9,"first_name":"Anson","last_name":"McRamsey","roll_number":73,"class_name":"Male"},
{"id":10,"first_name":"Vivienne","last_name":"Yard","roll_number":93,"class_name":"Female"},
{"id":11,"first_name":"Cazzie","last_name":"Michieli","roll_number":56,"class_name":"Male"},
{"id":12,"first_name":"Gayle","last_name":"Ryhorovich","roll_number":89,"class_name":"Female"},
{"id":13,"first_name":"Susann","last_name":"Rance","roll_number":85,"class_name":"Female"},
{"id":14,"first_name":"Blake","last_name":"Pawels","roll_number":82,"class_name":"Male"},
{"id":15,"first_name":"Alexia","last_name":"Stripling","roll_number":80,"class_name":"Female"}]
        for s in students:
            student = Student(**s)
            student.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated.'))