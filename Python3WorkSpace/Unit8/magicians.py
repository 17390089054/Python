def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for i in range(0,len(magicians)):
        magicians[i]="the Great "+magicians[i]
    show_magicians(magicians)
       
mgicians=['Harry','Shelly','July','Parsa']
make_great(mgicians)
