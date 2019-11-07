from django import forms
class NewComplainForm(forms.Form):
    complain_id=forms.IntegerField(label='id')
    Name=forms.CharField(label='Name',max_length=100)
    Category=forms.CharField(label='Category')
    Phone_no=forms.IntegerField(label='Phone no.')
    Address=forms.CharField(label='Address')
class SearchForm(forms.Form):
    Category=forms.CharField(label='Category',max_length=100)
