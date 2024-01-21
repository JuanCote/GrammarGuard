from django import forms


class TextForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "outline-none bg-[#ebecf5] font-semibold rounded-lg outline-offset-0 ease-out duration-300 border border-gray-400 w-full p-3 outline-3 focus:outline-[#c38d9d]"
            }
        )
    )
