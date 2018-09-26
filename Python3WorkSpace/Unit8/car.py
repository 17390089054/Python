def make_car(manufactor,size,color='blue',tow_package=True,**info):
    infos={}
    infos['maker']=manufactor
    infos['size']=size
    infos['color']='blue'
    info['tow_package']=True
    for key,value in info.items():
        infos[key]=value
    return infos

car=make_car('Yiqi','Large',output='China',price='1400$')
print(car)
car=make_car('宝马','Large')
print(car)
