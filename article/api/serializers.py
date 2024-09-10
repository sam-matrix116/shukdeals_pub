from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from article.models import News
from account.api.serializers import CreatorProfileSerializer


class NewsSerializer(ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = '__all__'

    def get_category_name(self, news):
        return news.category.name
    
    

class NewsDetailSerializer(ModelSerializer):

    category_name = serializers.SerializerMethodField()
    related_news = serializers.SerializerMethodField()
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = '__all__'

    def get_category_name(self, news):
        return news.category.name
    
    def get_related_news(self, news):

        related_news = News.objects.filter(deleted = False, category = news.category)
        serializer = NewsSerializer(related_news, many=True)
        return serializer.data
    
    def get_user_details(self,job):
        user = self.context.get('user')
        serializer = CreatorProfileSerializer(job.user, context={"user": user})
        return serializer.data