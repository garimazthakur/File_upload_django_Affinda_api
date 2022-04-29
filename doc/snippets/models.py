# Create your models here.
from ssl import Options
from django.db import models
from pygments import highlight
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from affinda import AffindaAPI, TokenCredential
# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    linenos=models.BooleanField(default=False)
    language=models.CharField(choices=LANGUAGE_CHOICES, default="python", max_length=100)
    style= models.CharField(choices=STYLE_CHOICES, default='friendly', max_length= 100)
    # owner= models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    # highlighted=models.TextField(blank= True, null= True)

    class Meta:
        ordering=['created']
    def __str__(self):
        return self.title
        
# class ChildSnippet(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     first_name= models.CharField(max_length=100)
#     last_name= models.CharField(max_length=100)
#     title = models.CharField(max_length=100, blank=True, null=True)
#     snippet= models.ForeignKey(Snippet, on_delete=models.CASCADE)
#     class Meta:
#         ordering=["created"]
#         def __str__(self):
#             return "%s %s" %(self.first_name, self.last_name)
   
class Affinda(models.Model):
    """
    Affinda class created in model and fields are added to upload media, media name, field name
    eith unicode functions
    """
     
    file = models.FileField(upload_to="affinda_files/", blank=True, null=True, help_text="Select file")
    file_name = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        help_text="Enter the file name",
    )
    field_name = models.CharField(max_length=250, blank=True, null=True, help_text="Enter field name")
    file_type = models.CharField(max_length=120, blank=True, null=True, help_text="Enter file type")
    is_active = models.BooleanField(default=True, help_text="Select your prefrences")
    is_deleted = models.BooleanField(default=False, help_text="Select your prefrences")
    can_delete = models.BooleanField(default=True, help_text="Select your prefrences")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Select your prefrences")
    updated_at = models.DateTimeField(auto_now=True, help_text="updated time")


    # history = HistoricalRecords(table_name="media_history")

    def __unicode__(
        self,
    ):  # get a bunch of garbage that is not really informative.
        return self.id  # id will show who use this function