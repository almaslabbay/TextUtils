#I have created this file-Almas
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request,"index.html")
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc=='on':
        punctuations ='''!()-[]:;'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params = {'purpose':'Removed Punctuation','analyzed_text': analyzed}
        djtext=analyzed

    if(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'UpperCase', 'analyzed_text': analyzed}
        djtext=analyzed

    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext=analyzed

    if(extraspaceremover=='on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]== " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
    if(removepunc!='on'and fullcaps!='on' and newlineremover != 'on' and extraspaceremover!='on'):
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)

    #Analyze the text
    # return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")