favorite_language={
    "jen":['python','java'],
    "sarah":['c'],
    "edward":['ruby','go'],
    "phil":['python',"haskell"]
    }
for name,languages in favorite_language.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t"+language.title())
