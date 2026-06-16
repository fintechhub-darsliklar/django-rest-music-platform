from rest_framework.serializers import ModelSerializer
from apps.users.models import Favourite
from rest_framework.exceptions import ValidationError


class FavouriteListSeralizer(ModelSerializer):

    class Meta:
        model = Favourite
        fields = '__all__'


class FavouriteCreateSeralizer(ModelSerializer):
    user = None
    class Meta:
        model = Favourite
        fields = '__all__'

    def validate_music(self, music):

        favourite = Favourite.objects.filter(user=self.user, music=music)
        if favourite.exists():
            raise ValidationError("this music already exists in your favourite list.")
        elif not music.is_public:
            raise ValidationError("You can't add this playlist to your favourite.")
        return music

