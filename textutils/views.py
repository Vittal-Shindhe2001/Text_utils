from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text',"default")
    removepuc=request.POST.get('removepunc','off')
    capitalyze=request.POST.get('fullcap','off')
    newlineremove=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    countchar=request.POST.get('countchar','off')
    if removepuc=="on":
        punctuatins='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed=''
        for char in djtext:
            if char not in punctuatins:
                analyzed=analyzed+char
        params={'purpose':"Remove Punctuation","analyzed_text":analyzed}
        djtext=analyzed
    if(capitalyze=='on'):
       analyzed=''
       for char in djtext:
           analyzed= analyzed + char.upper()
       params={"purpose":"To Uppercase","analyzed_text":analyzed}
       djtext=analyzed    
    if(newlineremove=='on'):
        analyzed=''
        for char in djtext:
            if char !='\n' and char!="\r":
                analyzed=analyzed+char
        params={"purpose":"Remove new Line","analyzed_text":analyzed}
        djtext=analyzed
    elif(extraspaceremover=='on'):
        analyzed=djtext.rstrip()
        params={"purpose":"Remove space","analyzed_text":analyzed}
        djtext=analyzed
    if(countchar=='on'):
        analyzed=0
        character=djtext.strip()
        for char in character:
            if isinstance(char, str):
                analyzed+=1
        params={"purpose":"Count Character","analyzed_text":analyzed}
        djtext=analyzed
    if(removepuc!="on" and capitalyze!='on' and newlineremove!='on' and extraspaceremover!='on' and countchar!='on'):
        return HttpResponse('ERROR')
    return render(request,'analyze.html',params)
