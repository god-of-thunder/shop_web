from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Users,SystemConfig,Product
from .serializer import *
from main.email import EMAIL
from .forms import UsersForm,ProductForm

# Create your views here.

def main(request):
    return render(request,'main.html')

def index(request):
    return render(request,'index.html',locals())


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    @action(detail=False,methods=['post'])
    def login(self, request):

        result = {"status": False, "errcode": None, "errmsg": None, "account": None}
        data = request.data
        account = data.get('account')
        password = data.get('password')
        user = Users.objects.filter(account=account,password=password)
        if user:
            request.session['account'] = account  # 使用session來保存用戶登錄信息
            request.session['password'] = password
            result["status"] = True
            result['account'] = account

            return JsonResponse(result)

        elif (Users.objects.filter(account=account).exists()):
            result["errcode"] = 410
            result["errmsg"] = "密碼錯誤"

            return JsonResponse(result)

        else:
            result["errcode"] = 411
            result["errmsg"] = "帳號不存在"

            return JsonResponse(result)

    @action(detail=False,methods=['post'])
    def logout(self, request):
        request.session['account'] = None
        request.session['password'] = None

        return JsonResponse({"status": True})

    @action(detail=False,methods=['post'])
    def regist(self, request):
        result = {"status": False, "errcode": None, "errmsg": None}
        EM = EMAIL()
        if request.method == 'POST':
            login_form = UsersForm(request.POST)
            if login_form.is_valid():  # 表單有效
                name = login_form.cleaned_data.get('name')
                password = login_form.cleaned_data.get('password')
                email = login_form.cleaned_data.get('email')
                phone = login_form.cleaned_data.get('phone')
                account = login_form.cleaned_data.get('account')
                if Users.objects.filter(account=account).exists():
                    result["errcode"] = 410
                    result["errmsg"] = "此帳號已經存在"
                elif Users.objects.filter(email=email).exists():
                    result["errcode"] = 411
                    result["errmsg"] = '此信箱已註冊過'
                elif Users.objects.filter(phone=phone).exists():
                    result["errcode"] = 412
                    result["errmsg"] = '此手機號碼已註冊過'
                else:
                    try:
                        new_user = Users(name=name,
                                         password=password,
                                         email=email,
                                         phone=phone,
                                         account=account,
                                         confirmed=0)
                        new_user.save()
                        result["status"] = True
                        EM.user_send_mail(account)
                    except Exception as e:
                        result["errcode"] = 404
                        result["errmsg"] = str(e)
            else:
                result["errcode"] = 402
                result["errmsg"] = "表單無效"
        else:
            result["errcode"] = 400
            result["errmsg"] = "非GET請求"
        print(result["errmsg"])
        return JsonResponse(result)

@csrf_exempt
def patch_email(request):
    result = {"status": False, "errcode": None, "errmsg": None}
    EM = EMAIL()
    if request.method == "POST":

        try:
            user_email = request.POST.get("user_email")
            EM.user_patch_email(user_email)
            result["status"] = True

        except:
            result["errcode"] = 404
            result["errmsg"] = "找不到信箱，發送失敗。"

    else:
        result["errcode"] = 400
        result["errmsg"] = "非POST請求"

    return JsonResponse(result)

def enable(request, key1:str):
    productForm = ProductForm()
    usersForm = UsersForm()
    account = model_to_dict(SystemConfig.objects.get(key1=key1)).get('account')
    Users.objects.filter(account=account).update(confirmed=1)

    return render(request,'enable.html',locals())

def items(request,id:int):
    usersForm = UsersForm()
    product = Product.objects.get(id=id)
    productForm = ProductForm()
    product_count = model_to_dict(Product.objects.get(id=id)).get('stock') - model_to_dict(
        Product.objects.get(id=id)).get('sold')
    
    return render(request,'item.html',locals())


def search(request,keyword):
    usersForm = UsersForm()
    keyword = str(keyword)
    productForm = ProductForm()
    product = Product.objects.filter(title__contains=keyword)
    productcount = Product.objects.filter(title__contains=keyword).count()

    return render(request,'search.html',locals())

def cart(request):
    usersForm = UsersForm()
    productForm = ProductForm()
    if Users.objects.filter(account=request.session['account']).exists():
        user = Users.objects.get(account=request.session['account'])
    else:
        user = None
    if user == None:
        return HttpResponse("請登入使用購物車")
    else:
        car_product_list = request.session.get("ber_car_list")
        if car_product_list:
            car_count = len(car_product_list)
        else:
            car_count = 0

    product_list = []
    buy_product_money = 0  # 紀錄購買商品的總價格
    buy_product_count = 0  # 紀錄總共買了幾個商品
    if car_product_list:
        for product in car_product_list:
            temp_product = Product.objects.get(id=product[0])
            product_list.append([temp_product, product[1], int(model_to_dict(temp_product)["money"]) * int(product[1])])
            buy_product_money += int(model_to_dict(temp_product)["money"]) * int(product[1])
            buy_product_count += int(product[1])

    return render(request,"cart.html",locals())

def limited_item(request):  # 限時購物的商品頁面
    usersForm = UsersForm()
    productForm = ProductForm()
    return render(request, 'limited_item.html', locals())

    



