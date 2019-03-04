from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
def eggs(request):
    return HttpResponse('<h1>eggs</h1> are cool!')
def count(request):
    view11 = request.GET['fulltext']

    wordlist=view11.split()
    dict={}
    for word in wordlist:
        if word in dict:
            #increase
            dict[word]+=1
        else:
            #add to dictionary
            dict[word]=1

    sortedwords = sorted(dict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'pass':view11,'count':len(wordlist),'sortedwords':sortedwords })

def about(request):
    return render(request,'about.html')
