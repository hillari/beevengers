# from django.contrib.auth.base_user import BaseUserManager
#
#
# class CustomUserManager(BaseUserManager):
#
#     def create_user(self, username, email, password ):
#         if not username:
#             raise ValueError("Username is required")
#         if not password:
#             raise ValueError("Password is required")
#
#         user = self.model(
#             username = username,
#             email = self.normalize_email(email),
#         )
#         user.set_password(password)
#         user.save() # may need to do user.save(using=self._db)?
#         return user
#
#     def create_superuser(self, username, email, password):
#         user = self.create_user(username, email, password)
#         user.is_superuser = True  # maybe do .setdefault?
#         user.is_staff = True
#         user.is_active = True


