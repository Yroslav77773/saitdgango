from  django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class CarForm(forms.Form):
    car_brand = forms.CharField(max_length=255, label="Car Brand")
    car_model = forms.CharField(max_length=255, label="Car Model", required=False)
    car_body = forms.CharField(max_length=255, label="Car Body")
    horse_power = forms.IntegerField(label="Horse Power", min_value=0)
    car_drive = forms.CharField(max_length=255, label="Car Drive")
    tax = forms.FloatField(label="Tax", min_value=0)
    description = forms.CharField(max_length=255, required=False, label="Description", widget=forms.Textarea)