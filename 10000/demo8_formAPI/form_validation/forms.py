from django import forms


class Form1(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()


# class Form1(forms.Form):
#     fname = forms.CharField()
#     lname = forms.CharField()
#     email = forms.EmailField()
#     phone = forms.CharField()

    # def clean_fname(self):
    #     fname = self.cleaned_data.get("fname")
    #     print(fname)
    #     # if len(fname) < 3:
    #     #     raise forms.ValidationError("Please fill >3 chars")
    #     # # print(fname)
    #     return "Mr. "+fname

    # def clean(self):
    #     cleaned_data = super().clean()
    #     fname = cleaned_data.get("fname");
    #     lname = cleaned_data.get("lname");
    #
    #     # It will give only one error msg for all the fields
    #     if len(fname) < 3:
    #         print(fname)
    #         raise forms.ValidationError("enter proper name")
    #
    #     if len(lname) < 3:
    #         # print(lname)
    #         raise forms.ValidationError("enter last name name")