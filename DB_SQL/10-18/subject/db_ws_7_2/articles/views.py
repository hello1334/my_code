from .models import Article
from .serializers import ArticlelistSerializers, ArticleSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticlelistSerializers(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializers(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializers(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        a = {'delete':f'데이터 {article_pk}번 글이 삭제되었습니다.'}
        article.delete()
        return Response(a, status=status.HTTP_204_NO_CONTENT)