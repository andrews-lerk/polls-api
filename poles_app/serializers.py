from rest_framework import serializers

from .models import *

class DefaultUser(object):
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id


class PollsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class PollDetailSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerVariant
        fields = '__all__'


class AnswerViewSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(slug_field='title', read_only=True)
    question = serializers.SlugRelatedField(slug_field='text', read_only=True)

    class Meta:
        model=Answer
        fields = '__all__'

class AnswerAddSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(default=DefaultUser())

    class Meta:
        model = Answer
        fields = ('id', 'poll', 'question', 'variant', 'user_id')

