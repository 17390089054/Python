from collections import OrderedDict

favorite_languages=OrderedDict()

favorite_languages['a']='python'
favorite_languages['b']='c++'
favorite_languages['c']='c'
favorite_languages['d']='ruby'

for name,language in favorite_languages.items():
    print(name.title()+" 's favorite_language is "+language.title()+" .")

