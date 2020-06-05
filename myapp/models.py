from django.db import models

class Snippet(models.Model) :
    sentence = models.CharField(max_length=100)

    def __str__(self):
        return(self.sentence)


#{% load crispy_forms_tags %}
#        <label for="placeholder">Please enter your sentence</label>
