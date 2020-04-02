from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.db import connection
from .models import Prec
from django.db.models import Q
import csv
import json
import sqlite3
from prec_word2vec import precUsingModel
from graph_event_type import draw_graph
from django.http import HttpResponse

@csrf_exempt
def index(request) :
    if request.method == "GET":
        # with open('C:/Users/admin/Documents/pansago/law_list_detail_2.csv', 'r', encoding='utf-8') as f:
        #     csv.field_size_limit(100000000)
        #     rdr = csv.reader(f)
        #     for line in rdr:
        #         law_no = line[0]
        #         law_title = line[1]
        #         law_event_no  = line[2]
        #         law_date	 = line[3]
        #         law_seongo  = line[4]
        #         law_court_name = line[5]
        #         law_event_type  = line[7]
        #         law_result   = line[9]
        #         law_content   = line[14]

        #         print(law_no)

        #         prec = Prec(law_no=law_no, law_title=law_title, law_event_no=law_event_no, law_date=law_date, law_seongo=law_seongo, law_court_name=law_court_name, law_event_type=law_event_type, law_result=law_result, law_content=law_content)
        #         prec.save()

        return render(request, 'index.html')  ## templates 밑에 바로 읽음  

def preclist(request) :
    if request.method == "GET":
        searchtype = request.GET.get('type','')
        searchkeyword = request.GET.get('text','')
        indexsearch = request.GET.get('indexsearch','')

        if indexsearch != '':
            precList = Prec.objects.filter( Q(law_title__icontains=indexsearch) | Q(law_event_type__icontains=indexsearch) ).order_by('-law_date')
        
        else :
            if searchtype =='law_title':
                precList = Prec.objects.filter(law_title__icontains=searchkeyword).order_by('-law_date')
        
            elif searchtype =='law_event_type':
                precList = Prec.objects.filter(law_event_type__icontains=searchkeyword).order_by('-law_date')

            if searchkeyword == '':
                precList = Prec.objects.raw('SELECT * FROM LAW_PREC ORDER BY LAW_DATE DESC')


        paginator = Paginator(precList, 10)
        page = request.GET.get('page')
        posts = paginator.get_page(page)    # 페이지에 해당되는 값만

        

        return render(request, 'precList.html', {'precList' : precList, 'posts':posts, 'searchtype':searchtype, 'searchkeyword':searchkeyword, 'indexsearch':indexsearch})

def showChart(request):
    if request.method == "GET":
        graphType = request.GET.get('graphType','')

        return render(request, 'chart.html', {'graphType': graphType})

@csrf_exempt
def chartSearch(request):
    if request.method == 'GET':
        return render(request, 'chart_search.html')

    elif request.method == 'POST':
        search_keyword = request.POST.get('search_keyword','')
        # print(search_keyword)

        if search_keyword != '':
            graph = draw_graph(search_keyword)
            # print(graph)

        context = {'graph': graph}

        return HttpResponse(json.dumps(context), content_type='application/json')

def precDetail(request):
    if request.method == "GET":
        no = request.GET.get('no','')  # no=209151
        print(no)
        indexsearch = request.GET.get('indexsearch','')

        if no != '':
            precDetail = Prec.objects.get(law_no = no)
            # precDetail = get_object_or_404(Prec, law_no = no)
            # print(type(precDetail))

        similar_words = []
        if indexsearch != '':
            result = precUsingModel(indexsearch)
            # print(result)
            for tmp in result:
                similar_words.append(tmp[0])

        return render(request, 'precDetail.html', {'precDetail' : precDetail, 'indexsearch' : indexsearch, 'similar_words' : similar_words})

@csrf_exempt
def dictionaryhome(request) :
    if request.method == "GET" :

        return render(request, 'dictionaryhome.html')

@csrf_exempt
def showwc(request) :
    if request.method == "GET" :
        event_type = request.GET.get('event_type','')

        return render(request, 'showwc.html', {'event_type':event_type})