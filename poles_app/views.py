from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from django.contrib.auth import get_user_model


class PollsListView(APIView):

    def get(self, request):
        polls = Poll.objects.filter(active=True)
        serializer = PollsListSerializer(polls, many=True)
        return Response(serializer.data)

class PollDetailView(APIView):

    def get(self, request, pk):
        questions = Question.objects.filter(poll=pk)
        serializer = PollDetailSerializer(questions, many=True)
        return Response(serializer.data)


class QuestionDetailView(APIView):

    def get(self,request, pk):
        variants = AnswerVariant.objects.filter(question=pk)
        serializer = QuestionDetailSerializer(variants, many=True)
        return Response(serializer.data)

class AnswerAddView(APIView):

    def post(self, request):
        serializer = AnswerAddSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

class AnswerView(APIView):
    def get(self, request, user_id):
        answers = Answer.objects.filter(user_id=user_id)
        serializer = AnswerViewSerializer(answers, many=True)
        return Response(serializer.data)