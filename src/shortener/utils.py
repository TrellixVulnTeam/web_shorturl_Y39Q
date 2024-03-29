import random
import string

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code
    # or can use
    # return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    #print(instance)                      # created object from the class
    #print(instance.__class__)            # getting the actual information from object class
    #print(instance.__class__.__name__)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code