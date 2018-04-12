from django import forms
from .models import Post, Category, Tag


class PostForm(forms.ModelForm):
    model = Post

    def clean_title(self):
        title = self.cleaned_data['title']
        cleaned = self.cleaned_data

        if not self.instance:
            count_posts = Post.objects.filter(title__unaccent__icontains=title).count()
        else:
            id = self.instance
            count_posts = Post.objects.filter(title__unaccent__icontains=title).exclude(id=self.instance.id).count()

        if count_posts > 0:
            raise forms.ValidationError("Ya existe una entrada con este titulo")

        return title

    class Meta:
        help_texts = {
            'description': ('Máximo 300 caracteres'),
        }


class CategoryForm(forms.ModelForm):
    model = Category

    def clean_name(self):
        name = self.cleaned_data['name']
        if not self.instance:
            count_category = Category.objects.filter(name__unaccent__icontains=name).count()
        else:
            count_category = Category.objects.filter(name__unaccent__icontains=name).exclude(id=self.instance.id).count()

        if count_category > 0:
            raise forms.ValidationError("Ya existe una categoría con este nombre")

        return name.lower()


class TagForm(forms.ModelForm):
    model = Tag

    def clean_tag(self):
        tag = self.cleaned_data['tag']
        if not self.instance:
            count_tag = Tag.objects.filter(tag__unaccent__icontains=tag).count()
        else:
            count_tag = Tag.objects.filter(tag__unaccent__icontains=tag).exclude(id=self.instance.id).count()

        if count_tag > 0:
            raise forms.ValidationError("Ya existe un tag con este nombre")

        return tag.lower()
