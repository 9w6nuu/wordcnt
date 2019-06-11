from django.shortcuts import render

# Create your views here.

# request, template 이름, 사전형객체(딕셔너리형 인자)를 받음
def home(request):
    return render(request, 'home.html')

# request가 들어오면 about.html을 반환
def about(request):
    return render(request, 'about.html')


def result(request):
    # 원문 글 전체를 가져와 변수 text에 담기게 된다 '지은 이름'
    text = request.GET['fulltext']

    # string 문자열을 공백을 기준으로 나눠서 리스트로 저장
    # 워드 변수에 리스트를 담음   
    words = text.split()
    word_dic = {}
    # <단어: 횟수 단어: 횟수>

    for word in words:
        if word in word_dic:
            # increse
            word_dic[word]+=1
        else:
            # add to word_dic
            word_dic[word]=1

    
    # render 함수에 3 번째 인자를 사전형(key와 value) 객체를 등록하는데 이때 key 값은 full로 임의로 지정
    # {'full':text}, {'length': len(words)}) 오류남
    return render(request, 'result.html', {'full':text, 'length': len(words), 'dic':word_dic.items})