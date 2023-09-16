from src.models.user import User
from src.service.service_user import ServiceUser

service = ServiceUser()
resposta = service.add_user(1,"Tester")
print(resposta)

resposta = service.add_user("Jose",1)
print(resposta)

resposta = service.add_user("Jose", "Dev")
print(resposta)