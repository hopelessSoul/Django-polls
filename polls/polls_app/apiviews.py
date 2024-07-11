from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from polls_app.utils.srializers.serializer import PollSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer

from polls_app.models import Poll, Question, Choice, Answer


class PollCreateView(APIView):
    def post(self, request):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollSerializer(poll).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PollUpdateView(APIView):
    def patch(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        serializer = PollSerializer(poll, data=request.data, partial=True)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollSerializer(poll).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        poll.delete()
        return Response('Poll has been deleted', status=status.HTTP_204_NO_CONTENT)


class PollsView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


class QuestionCreateView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    def patch(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return Response('Question has been deleted', status=status.HTTP_204_NO_CONTENT)


class ChoiceCreateView(APIView):
    def post(self, request):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(ChoiceSerializer(choice).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoiceUpdateView(APIView):
    def patch(self, request, pk):
        choice = get_object_or_404(Choice, pk=pk)
        serializer = QuestionSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(QuestionSerializer(choice).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        choice = get_object_or_404(Choice, pk=pk)
        choice.delete()
        return Response('Choice has been deleted', status=status.HTTP_204_NO_CONTENT)


class AnswerCreateView(APIView):
    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            answer = serializer.save()
            return Response(AnswerSerializer(answer).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerUpdateView(APIView):
    def patch(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            answer = serializer.save()
            return Response(AnswerSerializer(answer).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        answer = get_object_or_404(Choice, pk=pk)
        answer.delete()
        return Response('Answer has been deleted', status=status.HTTP_204_NO_CONTENT)
