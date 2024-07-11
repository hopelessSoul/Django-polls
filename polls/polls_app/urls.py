from django.urls import path
from . import apiviews

app_name = 'polls_app'

urlpatterns = [
    path('all', apiviews.PollsView.as_view(), name='polls_view'),

    path('create', apiviews.PollCreateView.as_view(), name='create_poll'),
    path('update/<int:pk>', apiviews.PollUpdateView.as_view(), name='update_poll'),

    path('question/create', apiviews.QuestionCreateView.as_view(), name="question_create"),
    path('question/update/<int:pk>', apiviews.QuestionUpdateView.as_view(), name="question_update"),

    path('choice/create', apiviews.ChoiceCreateView.as_view(), name="choice_create"),
    path('choice/update/<int:pk>', apiviews.ChoiceUpdateView.as_view(), name="choice_update"),

    path('answer/create', apiviews.AnswerCreateView.as_view(), name="answer_create"),
    path('answer/update', apiviews.AnswerUpdateView.as_view(), name="answer_update"),
]
