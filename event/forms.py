from django import forms
from event.models import Category,Event,Participant



class StyledFormMixin:
    """ Mixing to apply style to form field"""

    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder':  f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-3 m-4 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            else:
                field.widget.attrs.update({
                    'class': self.default_classes
                })
                
                
class Category_form(StyledFormMixin,forms.ModelForm):
    class Meta:
        model=Category
        fields=["name","description"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
        

class Event_form(StyledFormMixin,forms.ModelForm):
    class Meta:
        model=Event
        exclude=["description"]
        widgets = {
            'due_date': forms.SelectDateWidget
            
        }
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
        
        
        
class Participant_form(StyledFormMixin,forms.ModelForm):
    class Meta:
        model=Participant
        fields='__all__'
        widgets = {
            'event': forms.CheckboxSelectMultiple
        }
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
        
        