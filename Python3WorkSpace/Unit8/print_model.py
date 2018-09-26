#若要保留unprinted_model 可以将参数替换成unprinted_model[:]
def print_model(unprinted_model,finished_model):
    while unprinted_model:
        current_model=unprinted_model.pop()
        print("Printing model:"+current_model)
        finished_model.append(current_model)
def show_completed_models(finished_model):
    print("\nThe following models have been printed:")
    for completed_model in finished_model:
        print(completed_model)
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_model(unprinted_designs, completed_models)
show_completed_models(completed_models)

        
