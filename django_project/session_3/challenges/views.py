from typing import Text
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect , Http404
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.


# def jan(request):
#     return HttpResponse("yaay")

# def feb(request):
#     return HttpResponse("yaay2")

# def mar(request):
#     return HttpResponse("yaay3")


month_challenges =  {
"january": " jan it is",
"february" : " feb it is",
"march" : None
}



def index(request):
    months  = list(month_challenges.keys())
    # list_items = ""
    # for mon in months:
    #     reverse_path = reverse("my_challenge_function",args=[mon])
    #     list_items+=f"<li><a href=\"{reverse_path}\">{mon}</a></li>"
    # responsedata  = f"<ul>{list_items}</ul>"
    #return HttpResponse(response_data)
    kwargs_dict = {"months":months}
    return render(request,"challenges/index.html", kwargs_dict)
    # return HttpResponse(responsedata)

    


def month_caller_by_number_redirect_reverse(request, month_param):
    month_list = list(month_challenges.keys())
    redirect_url = ""
    try:
        month_val = month_list[month_param-1]
        redirect_url = reverse("my_challenge_function", args=[month_val])
        # print ("hi   "+redirect_url)
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound("not supported number")




def month_caller_by_number_redirect(request, month_param):
    month_list = list(month_challenges.keys())
    try:
        month_val = month_list[month_param-1]
        return HttpResponseRedirect("/challenges/"+month_val)
    except:
        return HttpResponseNotFound("not supported")



def month_caller_by_number(request, month_param):
    text= None
    if month_param == 1:
        text = "jan it is "
    elif month_param == 2:
        text = "feb it is "
    else:
        return HttpResponseNotFound("not supported")

    return HttpResponse(text)
        


def month_caller(request, month_param): 
    # try:
    text = month_challenges[month_param]
    month_list = list(month_challenges.keys())
    # response_data = f"<h1>{text}</h1>"
    #return HttpResponse(response_data)
    kwargs_dict = {"html_text":text,"html_month": month_param, "months":month_list}
    return render(request,"challenges/challenge.html", kwargs_dict)
    # response_text = render_to_string("challenges/challenge.html")
    # return HttpResponse(response_text)
    # except:
    #     raise Http404()
    #     return HttpResponseNotFound("not supported")

        

