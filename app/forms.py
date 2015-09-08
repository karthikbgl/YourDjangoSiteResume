from django import forms

GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))
WHO_CHOICES = (('me', 'Self'), ('child', 'Child'), ('someone', 'Someone else'))

class HealthFinderForm(forms.Form):

    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    who = forms.ChoiceField(choices=WHO_CHOICES)
    age = forms.IntegerField()

    # is_pregnant = forms.BooleanField(initial=False, required=False)


