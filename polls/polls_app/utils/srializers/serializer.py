from rest_framework import serializers

from polls_app.models import Poll, Question, Choice, Answer

from users.utils.serializers.serializer import ProfileSerializer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['name', 'start_date', 'end_date', 'description']

    def create(self, data):
        return Poll.objects.create(**data)

    def update(self, instance, validated_data):
        if 'start_date' in validated_data:
            raise serializers.ValidationError({'start_date': "You can't change that field"})
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionSerializer(serializers.ModelSerializer):
    poll = PollSerializer()

    class Meta:
        model = Question
        fields = "__all__"

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Choice
        fields = "__all__"

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    poll = PollSerializer()
    choice = ChoiceSerializer()

    class Meta:
        model = Answer
        fields = "__all__"

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
