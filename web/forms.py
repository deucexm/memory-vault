from django import forms
from web.models import Console, Domain, Game, Cheat, MyModelChoiceField

class ConsoleForm(forms.ModelForm):
    class Meta:
        model = Console
        fields = ['name', 'short_name', 'release_year']

class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ['name', 'console_id']
        field_classes = {
            'console_id': MyModelChoiceField,
        }

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'release_year', 'source', 'console_id']
        field_classes = {
            'console_id': MyModelChoiceField,
        }

class CheatForm(forms.ModelForm):
    class Meta:
        model = Cheat
        fields = ['domain_id', 'address', 'name', 'notes', 'game_id']
        field_classes = {
            'domain_id': MyModelChoiceField,
            'game_id': MyModelChoiceField,
        }