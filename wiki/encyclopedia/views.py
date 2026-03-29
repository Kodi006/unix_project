from django.shortcuts import render
import re
from . import util
from django import forms
import random


def converti(f):
    f = re.sub(r'###### (\w*?)\n',r'<h6>\1</h6>',f)
    f = re.sub(r'##### (\w*?)\n',r'<h5>\1</h5>',f)
    f = re.sub(r'#### (\w*?)\n',r'<h4>\1</h4>',f)
    f = re.sub(r'### (\w*?)\n',r'<h3>\1</h3>',f)
    f = re.sub(r'## (\w*?)\n',r'<h2>\1</h2>',f)

    f = re.sub(r'# (\w*?)\n',r'<h1>\1</h1>',f)

    f = re.sub(r'\n(\w[^\n]+)',r'<p>\1</p>',f)
    f=re.sub(r'\*\*([\w\W]+?)\*\*',r'<strong>\1</strong>',f)

    f = re.sub(r'\* (\w[^\n]+)',r'<ul><li>\1</li></ul>',f)
    f=re.sub(r'\(([\w\W]+?)\)',r'<a href="/\1">\1</a>',f)
    return f


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })
def search(request):
    s=[]
    if request.method=='POST':
        k=request.POST.get('q')
            
        for i in util.list_entries():
            if k in i:
                s.append(i)
    else:
        return(request,'encyclopedia/layout.html')
    return render(request,'encyclopedia/search.html',{'s':s})        
        
def text(request,text):
    if text in util.list_entries():
        h=[]
        f=open(f"entries/{text}.md",'r+')
        f=f.readlines()
        
        for i in f:
            i=converti(i)
            h.append(i)
    else:
        h=[]
        
    return render(request,"encyclopedia/text.html",{'k':h ,'title':text})

def newpage(request):
    s=1
    if request.method=='POST':
        
        title=request.POST.get('title')
        for i in util.list_entries():
            if i==title:
                s=0
                return render(request,'encyclopedia/error.html')

        if s==1:
        
            cont=request.POST.get('content')
            
            util.save_entry(title,cont)
            return render(request,'encyclopedia/index.html')
    else:
        return render(request,'encyclopedia/newpage.html')
def edit(request,title):
    if request.method=='POST':
        cont=request.POST.get('content')
        util.save_entry(title,cont)
        return render(request,'encyclopedia/index.html')
    else:
        h=[]
        f=open(f"entries/{title}.md",'r')
        f=f.readlines()
        for i in f:
            h.append(i)
        return render(request,'encyclopedia/edit.html',{"title":title,'contents':h})
def rando(request):
    t=random.choice(util.list_entries())
    h=[]
    f=open(f"entries/{t}.md",'r+')
    f=f.readlines()
        
    for i in f:
            i=converti(i)
            h.append(i)
    return render(request,"encyclopedia/text.html",{'k':h ,'title':t})

