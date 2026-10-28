# Python'da datetime — sana va vaqtni olish, saqlash, hisoblash va formatlash uchun ishlatiladigan modul.

# import datetime

# hozir = datetime.datetime.now()
# print(hozir)
# print(hozir.year)
# print(hozir.month)
# print(hozir.day)

# import datetime

# def yoshhisoblash(yosh):
#     vaqt = datetime.datetime.now()
#     print(vaqt.year - yil)

# yil = int(input("Yilizi kiriting : "))
# yoshhisoblash(yil)

# import datetime

# yil = int(input("Yil : "))
# oy = int(input("Oy : "))
# kun = int(input("Kun : "))

# tugilgan_kun = datetime.datetime(yil,oy,kun)
# hozir = datetime.datetime.now()

# farq = hozir - tugilgan_kun

# print("Hozirgi yashab turilgan vaqt", hozir.strftime("%d.%m.%Y %H:%M:%S"))
# print("Yashagan kun",int(farq.days))
# print("Yashagan soat",int(farq.total_seconds() // 3600))

# Necha minut yashagan 1 soatda 60 minut
# Necha sekund yashagan 

# Resultati resultatini chiqaradi qaytarmaydi
def qoshish(a,b):
    print(a + b)

qoshish(5,3)

# return - funksiya hisoblagan natijani 
# tashqariga qaytarish uchun
# def kopaytirish(a,b):
#     return a * b

# x = kopaytirish(4,7)
# print(x)

def a():
    print("Hello my function")

def b():
    return "Hello world"

print(a())
print(b())

# print() - faqat ekranga chiqaradi
# return - qiymatni funksiyadan tashqariga qaytaradi


# Pyhton MATH
# Matematika

import math
# Sonni ildizini chiqarish
print(math.sqrt(25))
print(math.sqrt(144))
print(math.sqrt(81))

# Sonni darajasi
print(math.pow(2,5))
print(math.pow(7,2))

# Faktorial sonlar
# 5 * 4 * 3 * 2 * 1
print(math.factorial(5))
print(math.factorial(7))
print(math.factorial(3))

# yaxlitlash
print(math.ceil(5.1))
print(math.ceil(7.8))
print(math.ceil(8.99))
print(math.ceil(12.5))

# Pastga qarab yaxlitlash
print(math.floor(7.8))
print(math.floor(3.7))

# Math PI 3,14
import math
print(math.pi)

# # Doira yuzi
# # r = 7
# # yuza = math.pi * r**2
# # print(yuza)
# # print(math.ceil(yuza))

# # r = float(input("Radius kiriting : "))
# # Doirani yuzasi

# # JSON - bu malumotlarni saqlash va almashish

# import json
# odam = {
#     "ism" : "Ali",
#     "yosh" : 22,
#     "manzil" : "Asaka",
# }
# natija = json.dumps(odam)
# print(natija)
# # Python obyektni JSON matnga aylantirish
# # dump - Fayl bilan ishlayd

# with open("odam.json", "w") as fayl:
#     json.dump(odam, fayl)

import math
son = float(input("Son kritiing"))

if son.is_integer():
    print("Son allaqachon butun")   
else:
    print(math.ceil(son))

from django.db.models import Q, Avg # Avg ni import qilishni unutmang
from .models import Mahsulot, Catgeory, Review
from .forms import RegisterForm, ReviewForm # ReviewForm ni import qilamiz

def product_detail(request, slug):
    mahsulot = get_object_or_404(Mahsulot, slug=slug)
    
    # Mahsulotga tegishli sharhlar
    reviews = mahsulot.reviews.all().order_by('-created_at')
    
    # O'rtacha reytingni hisoblash (masalan: 4.5)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if average_rating:
        average_rating = round(average_rating, 1)
    else:
        average_rating = 0

    # Sharh yuborishni qayta ishlash
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Sharh qoldirish uchun tizimga kirishingiz kerak!")
            return redirect('login')
            
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.mahsulot = mahsulot
            review.user = request.user
            review.save()
            messages.success(request, "Sharhingiz muvaffaqiyatli qo'shildi!")
            return redirect('product_detail', slug=mahsulot.slug)
    else:
        form = ReviewForm()

    context = {
        "mahsulot": mahsulot,
        "reviews": reviews,
        "average_rating": average_rating,
        "form": form,
    }
    return render(request, "product_detail.html", context)