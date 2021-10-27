#I have created this file: Tushar

from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
 #   return HttpResponse('</h1>Hello Tushar</h1> <a href="https://www.facebook.com"> Facebook.com</a>')

#def about(request):
 #   return HttpResponse('Tushar is a Network Automation Engineer')

def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text from user
    djtext= request.GET.get('text','default')
    removepunc=request.GET.get("removepunc","off")
    createuppercase=request.GET.get("createuppercase","off")
    newlineremover=request.GET.get("newlineremover","off")
    extraspaceremover=request.GET.get("extraspaceremover","off")
    charcount=request.GET.get("charcount","off")
    print(removepunc)
    print(djtext)
    #analyzed=djtext
    punctuations= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,"analyze.html",params)

    elif(createuppercase == "on"):
        analyzed = ""
        for letter in djtext:
                analyzed = analyzed + letter.upper()
        params={'purpose':'Converted to Uppercase','analyzed_text':analyzed}
        return render(request,"analyze.html",params)

    elif(newlineremover == "on"):
        analyzed = ""
        for letter in djtext:
            if letter != "\n":
                analyzed = analyzed + letter
        params={'purpose':'New line char has been removed','analyzed_text':analyzed}
        return render(request,"analyze.html",params)


    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params={'purpose':'Extra space has been removed','analyzed_text':analyzed}
        return render(request,"analyze.html",params)

    elif(charcount=="on"):
        count = 0
        for char in djtext:
            count = count + 1
        params = {'purpose': 'Total char count is calculated', 'analyzed_text': count}
        return render(request, "analyze.html", params)

    else:
        return HttpResponse("Error")


def navigator(request):
    return HttpResponse('''</h3>Welcome to Navigator</h3>
    <li><a href="https://www.facebook.com"> Facebook.com</a>)</li>
    <li><a href="https://www.youtube.com"> Youtube.com</a>)</li>
    <li><a href="https://www.linkedin.com"> Linkedin.com</a>)</li>

    ''')



'''
def capfirst(request):
    return HttpResponse("capfirst")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaceremove <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount")
'''