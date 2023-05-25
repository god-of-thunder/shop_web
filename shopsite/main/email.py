from main.base_url import *
from main.models import SystemConfig,Users
from django.conf import settings
from django.core.mail import send_mail
from django.forms.models import model_to_dict
import json,hashlib,datetime

class EMAIL:
    def __init__(self):
        self.title = "Vincent Shop 您好！帳號驗證啟用信"

    def hash_code(self,account):
        h = hashlib.sha256()
        account += str(datetime.datetime.now())
        h.update(account.encode())
        return h.hexdigest()

    def user_send_email(self,account:str):
        account_code = self.hash_code(account=account)
        account_email = model_to_dict(Users.objects.get(account=account)).get('email')
        account_name = model_to_dict(Users.objects.get(account=account)).get('name')
        system_config = SystemConfig(key1=account_code,
                                     account=account)
        system_config.save()
        email_url = base_url + 'enable/'+ account_code
        send_mail(self.title,
                  '''{}您好！\n\n　　歡迎您加入 Vincent Shop！請點擊以下連結以啟用帳號享受全部的功能！\n\n　　{}\n\n祝 順心\n\n Vincent Shop 營運團隊敬上'''.format(account_name,email_url),
                  settings.EMAIL_HOST_USER,
                  [account_email],
                  fail_silently = False
                  )
        
    def user_patch_email(self,email):
        account=model_to_dict(Users.objects.get(email=email)).get("account")
        account_name = model_to_dict(Users.objects.get(email=email)).get("name")
        account_code = self.hash_code(account)
        SystemConfig.objects.filter(account=account).update(key1=account_code)
        email_url=base_url + "enable/"+account_code
        send_mail(self.title,
                  '''{}您好！\n\n　　歡迎您加入 Vincent Shop！請點擊以下連結以啟用帳號享受全部的功能！\n\n　　{}\n\n祝 順心\n\n Vincent Shop 營運團隊敬上'''.format(account_name,email_url),
                  settings.EMAIL_HOST_USER,
                  [email],
                  fail_silently = False
                  )
