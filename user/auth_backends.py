from django.contrib.auth import views as auth_views
from django.contrib.auth.backends import ModelBackend

# ########
# # 토큰으로 이메일인증하고 이메일등록하기
# class EmailBackend(ModelBackend):

#     def authenticate(self, request, **kwargs):
#         UserModel = auth_views.UserModel()
#         try:
#             email = kwargs.get('email', None)
#             if email is None: # comment 1)
#                 email = kwargs.get('username', None)

#             user = UserModel.objects.get(email=email)
#             if user.check_password(kwargs.get('password', None)):
#                 return user

#         except UserModel.DoesNotExist:
#             return None
#         return None
        