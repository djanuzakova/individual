from transliterate import slugify
import re


def slug_generator_name(name):
    slug = name.lower()
    if bool(re.search('[a-z]+[A-Z]', slug)):
        slug = slugify(slug)
    else:
        slug = slug.replace(" ", " ")
    return slug
