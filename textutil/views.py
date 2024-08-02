# i have created this
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
       return render(request, 'index.html')

def analyze(request):
        djtext= request.POST.get('text', 'default')
        removepunc= request.POST.get('removepunc', 'off')
        fullcap= request.POST.get('fullcap', 'off')
        nlremove= request.POST.get('nlremove', 'off')
        extraspaceremover = request.POST.get('extraspaceremover', 'off')

        if(removepunc == 'on' and fullcap == 'on')  :
                punctuations = '''.,?!:;'"()[]{}-–—.../\@&*_^~|<>=#$%+'''
                analyzed = ""
                for char in djtext:
                        if char not in punctuations:
                         analyzed = analyzed + char.upper()

                params = {'purpose': 'Removed Punctuations and UPPERCASE ', 'analyzed_text': analyzed}
                djtext = analyzed


        if (removepunc == 'on'):
                punctuations = '''.,?!:;'"()[]{}-–—.../\@&*_^~|<>=#$%+'''
                analyzed = ""
                for char in djtext:
                        if char not in punctuations:
                                analyzed = analyzed + char
                params = {'purpose': 'Removed Punctuations ', 'analyzed_text': analyzed}

                djtext = analyzed

        if (fullcap == 'on'):
                analyzed = ""
                for char in djtext:
                       analyzed= analyzed + char.upper()
                params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}

                djtext = analyzed

        if extraspaceremover == 'on':
                analyzed = ""
                for index, char in enumerate(djtext):
                        if not (djtext[index] == " " and djtext[index + 1] == " "):
                                analyzed = analyzed + char
                params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
                djtext = analyzed

        if(nlremove== 'on'):
                analyzed = ""
                for char in djtext:
                        if char == "\n" or char == "\r":
                                analyzed = analyzed + ' '
                        else:
                                analyzed = analyzed + char
                params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        if (removepunc != 'on' and fullcap != 'on ' and extraspaceremover != 'on' and nlremove != 'on'):
                return HttpResponse('Select the operation')

        return render(request, 'analyze.html', params)




