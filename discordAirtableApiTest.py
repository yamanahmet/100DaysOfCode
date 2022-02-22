from pyairtable import Api, Base, Table

api = Api('keyTRu7XDdf9Ky5Q0')  #apikey
api.all('appZg83GywzAAXvlu', 'Contacts') #base_id, table_name

base = Base('keyTRu7XDdf9Ky5Q0', 'appZg83GywzAAXvlu')
base.all('Contacts')

table = Table('keyTRu7XDdf9Ky5Q0', 'appZg83GywzAAXvlu', 'Contacts')
table.all()

#Belirli bir özelliğe göre arama ve tüm datasını alma
from pyairtable.formulas import match
formula = match({"Phone Number": "136-130-4036"})
table.all(formula=formula)

#ID'yi girerek veri güncelleme
table.update('rec0PV4pfANoIjocD', {"Email": "a@gmail.com"})

#Belirli bir özelliğe göre arayıp eşleşme sonucundaki diğer veriyi çekme
formula = match({"Phone Number": "136-130-4036"})
table.all(formula = formula)
print(table.first(fields = "Email" ))
