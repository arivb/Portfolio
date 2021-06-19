from django import forms
from .models import Login,SignUp
class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUp
        fields="__all__"
        widgets={
            "name":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),
            "facebookid":forms.TextInput(
               attrs={
                   "class":"form-control"
               }
           ),
             "email":forms.EmailInput(
                attrs={
                    "class":"form-control"
                }
            ),
             "phonenumber":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),
           
           "age":forms.TextInput(
               attrs={
                   "class":"form-control"
               }
           ) 
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"
        widgets={
            "name":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            ),
             "email":forms.EmailInput(
                attrs={
                    "class":"form-control"
                }
            ),
             "phonenumber":forms.TextInput(
                attrs={
                    "class":"form-control"
                }
            )
            
        }