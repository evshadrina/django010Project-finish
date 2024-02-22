from django.http import HttpResponse
from django.shortcuts import render
import  datetime


def def_path_element(request):
    path_elements = request.path.split("/")
    print("path_elements: ", path_elements)
    elements_amount = path_elements.__len__()
    print("elements_amount: ", elements_amount)
    path_element = path_elements[elements_amount - 1]
    print("path_element: ", path_element)
    return (path_element)


def index(request):
    path_element = def_path_element(request)
    return render(request, "AppStaticSite/index.html", {"path_element": path_element})


def home(request):
    path_element = def_path_element(request)
    data = {"radius": 55, "width": 77, "height": 105}  # словарь
    date_now=datetime.datetime.now()
    print(date_now)
    my_person = {'name': 'Elena', 'last_name': 'Viktorovna', 'fam': 'Shadrina', 'img': 'images/vally.jpg'}
    context = {'data': data, 'my_person': my_person, 'path_element': path_element, 'date_now': date_now}
    return render(request, "AppStaticSite/home.html", context)

def store (request):
    path_element = def_path_element(request)
    objects_array = [
        {
            "id": "1",
            "title": "Товар 1",
            "vendor_code": "VC111",
            "description": "Описание  товара 1 Это лучший товар месяца",
            "price": 100.34,
            "img": "images/img_1.png"
        },
        {
            "id": "2",
            "title": "Товар 2",
            "vendor_code": "VC222",
            "description": "Описание 2",
            "price": 200.56,
            "img": "images/img.png"
        },
        {
            "id": "3",
            "title": "Товар 3",
            "vendor_code": "VC333",
            "description": "Описание 3",
            "price": 300,
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_003.jpg"
        },
        {
            "id": "4",
            "title": "Товар 4",
            "vendor_code": "VC444",
            "description": "Описание 4",
            "price": 400,
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_004.jpg"
        }
    ]
    dict_of_array = {'objects_array': objects_array}
    context = {'path_element': path_element,
               'dict_of_array': dict_of_array}
    return render(request, "AppStaticSite/store.html", context)

def store_result(request): # http://127.0.0.1:8000/renderApp/greet/Иванов
    print(request.__dir__())
    req = dict(request.GET)
    print (req)
    vendor_code = req.get("vendor_code")
    amount = req.get("amount")
    print(vendor_code, amount)
    i=0
    d = {}
    for key in vendor_code:
        print(vendor_code[i], amount[i])
        d[vendor_code[i]] = amount[i]
        i+=1
    print(d)
    return render(request, "AppStaticSite/store_result.html", {'d':d})


def form(request):
    path_element = def_path_element(request)
    return render(request, "AppStaticSite/form.html", {"path_element": path_element})


def form_abc(request):
    path_element = def_path_element(request)

    context={"path_element": path_element}
    return render(request, "AppStaticSite/form_abc.html", context)

def abc_result(request):
    path_element = def_path_element(request)
    print(request.__dir__())
    req = dict(request.GET)
    print(req)

    # amount = req.get("amount")

    a = int(req.get("a")[0])
    print(a)
    b = int(req.get("b")[0])
    c = int(req.get("c")[0])

    result = ''
    if c>a and c<b:
        result='принадлежит'
        print(result)
    else:
        result= "не принадлежит"
        print(result)

    context = {'result': result, "path_element": path_element, 'a':a, 'b':b, 'c':c}
    return render(request, "AppStaticSite/abc_result.html", context)

#
# def f_str(request, str_value):
#     print("type(request), request: ", type(request), request.path)
#     print("request.META:", request.META.get("HTTP_HOST"))
#     path_elements = request.path.split("/")
#     elements_amount = path_elements.__len__()
#     path_element = path_elements[elements_amount - 2]
#     print("type(str_value), str_value: ", type(str_value), str_value)
#     return HttpResponse(
#         f"<p>f_str, str_value.capitalize():  {str_value.capitalize()}; \n<br>path_element: {path_element} \n</p>")
#
#
# def f_int(request, int_value):
#     print(type(int_value), int_value)
#     return HttpResponse(f"f_int, int_value: {int_value} ")
#
#
# def f_slug(request, slug_value):
#     print(type(slug_value), slug_value)
#     return HttpResponse(f"f_slug, slug_value: {slug_value}")
#
#
# def f_path(request, path_value):
#     print(type(path_value), path_value)
#     return HttpResponse(f"f_path, path_value: {path_value}")
