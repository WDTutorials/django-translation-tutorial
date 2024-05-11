from modeltranslation.translator import translator, TranslationOptions
from .models import Post

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'slug') # specify the fields you want to translate

translator.register(Post, PostTranslationOptions)