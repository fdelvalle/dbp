from django.utils.text import slugify


def slugify_save(model_instance, add=None):
    slug = model_instance.slug
    if not slug:
        slug = slugify(model_instance.name)
        setattr(model_instance, 'slug', slug)
    return slug
