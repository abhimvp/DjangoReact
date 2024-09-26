from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"] # fileds we want to serialize when we accept a new user & returning a new user
        extra_kwargs = {"password":{"write_only":True}} # we dont want to return the password when we return a user , write_only means no one can read this

    def create(self,validated_data):
        """ Accept the validated data , this is the data we have already have passed all of the validation checks that the serializers does for us.
        Looks for valid username , passowrd , serializer will look at User Model , it will look at all of the fields on that Model and the one's we have specified in fields above
        it will make sure they are valid & pass the data below to validated_data"""
        user = User.objects.create_user(**validated_data) # ** is used to unpack the dictionary
        # validated_data contains the username and password 
        return user # all this is doing is implement a method that will be called when we want to create a new version of user 
    

# let's create a serializer for the Note model
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id","title","content","created_at","author"] # fields we want to serialize
        extra_kwargs = {"author":{"read_only":True}} # only read the author is & not write
        # read_only_fields = ["created_at","author"] # fields we dont want to be able to change , read only fields