from django import forms
from .models import DemoRequest

class DemoRequestForm(forms.ModelForm):
    class Meta:
        model = DemoRequest
        fields = ['mobile', 'telegram_id', 'email', 'panel_name', 'panel_version', 'robot_status']
        widgets = {
            'mobile': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'مثال: 09123456789',
                'dir': 'ltr'
            }),
            'telegram_id': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'مثال: @username',
                'dir': 'ltr'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'مثال: example@domain.com',
                'dir': 'ltr'
            }),
            'panel_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'مثال: پنل سنایی'
            }),
            'panel_version': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'مثال: V2.001',
                'dir': 'ltr'
            }),
            'robot_status': forms.RadioSelect(attrs={
                'class': 'form-radio'
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email.lower().startswith('www'):
            raise forms.ValidationError('ایمیل نمی‌تواند با www شروع شود')
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.startswith('09'):
            raise forms.ValidationError('شماره موبایل باید با 09 شروع شود')
        if not mobile.isdigit():
            raise forms.ValidationError('شماره موبایل باید فقط شامل اعداد باشد')
        if len(mobile) != 11:
            raise forms.ValidationError('شماره موبایل باید 11 رقم باشد')
        return mobile 