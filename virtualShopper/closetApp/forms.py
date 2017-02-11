from django import forms
from models import ClothingType, UserProfile
from django.contrib.auth.models import User




class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('username', 'password', 'email')


class ClothingForm(forms.ModelForm):
	class Meta:
		model = ClothingType

class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.CharField(widget=forms.EmailInput(), required=True)
	subject = forms.CharField(required=True)
	body = forms.CharField(widget=forms.Textarea(), required=True)

	def send_message(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		subject = self.cleaned_data['subject']
		body = self.cleaned_data['body']

		message = '''
		New Message from {name} @ {email}
		Subject: {Subject}
		Message: 
		{body}
		'''.format(name=name,
			email=email,
			subject=subject,
			body=body)
		email_msg = EmailMessage('New Contact Form Submission',
			message,
			email,
			['mbrunson84@gmail.com'])
		email_msg.send()

class PasswordRecoveryForm(forms.Form):
	email = forms.EmailField(required=False)

	def clean_email(self):
		try: 
			return User.objects.get(email=self.cleaned_data['email'])
		except User.DoesNotExist:
			raise forms.ValidationError("Can't Find a user based on this email")
		return self.cleaned_data['email']

	def reset_password(self):
		user = self.clean_email()

		password = get_random_string(length=8)

		user.set_password(password)

		user.save()
		body = """
				Sorry you are having issues with your account! Below is your username and new password
				Username: {username}
				Password: {password}
				You can log in here: http://localhost:8000/login/
				You can change your password here: http://localhost:8000/settings/
				""".format(username=user.username, password=password)
		pw_msg = EmailMessage('Your new password', body, 'joeknows718@gmail.com', [user.email])
		pw_msg.send()