from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from rest_framework_jwt.settings import api_settings
    
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class UserDetailSerializer(serializers.ModelSerializer):
    #for login, http://127.0.0.1:8000/dj-rest-auth/login/
    class Meta:
        model = User
        fields = '__all__'
        
class UserRegistrationSerializerWithToken(serializers.ModelSerializer):
    email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
    nickname = serializers.CharField(required=True, allow_blank=False, min_length=5, max_length=30)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    def validate_email(self, email):
        '''custom email validation using allauth utils'''
        if email and email_address_exists(email):
            raise serializers.ValidationError('A user is already registered with this e-mail address.')
        return email
    
    def validate_nickname(self, nickname):
        for n in nickname:
            if n.isdigit() and n.isalpha(): #TODO: if not number or letter 
                raise serializers.ValidationError('Nickname is not a number or letter')
        return nickname

    def validate_password1(self, password):
        #password validation via default allauth adapter
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data
    
    def get_cleaned_data(self):
        print(self.validated_data)
        return {
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'password1': self.validated_data.get('password1', '')
        }

    
    def save(self, request=None):
        #Instantiates  a new user instance
        user = get_user_model()() #extra () for positional argument: 'raw_password'
        cleaned_data = self.get_cleaned_data()

        email = cleaned_data.get('email')
        nickname = cleaned_data.get('nickname')

        user.email = email
        user.nickname = nickname

        if 'password1' in cleaned_data:
            user.set_password(cleaned_data['password1'])
        else:
            user.set_unusable_password()

        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'email',
            'nickname',
            'password1',
            'password2',
        )

