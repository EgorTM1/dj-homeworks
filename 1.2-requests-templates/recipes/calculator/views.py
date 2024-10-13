from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,  
        'молоко, л': 0.1,  
        'соль, ч.л.': 0.5,  
    },
    'pasta': {
        'макароны, г': 0.3,  
        'сыр, г': 0.05,  
    },
    'buter': {
        'хлеб, ломтик': 1,  
        'колбаса, ломтик': 1,  
        'сыр, ломтик': 1,  
        'помидор, ломтик': 1,  
    },
}

def all_recipes_view(request, recipe_name=None):  
    if recipe_name is None:  
        context = {'recipes': list(DATA.keys())}  
        
    elif recipe_name in DATA:  
        context = {
            'recipe': DATA[recipe_name],
            'servings': request.GET.get('servings'),
            'recipe_name': recipe_name
        }

        if context['servings']:
            try:
                servings = int(context['servings'])
                for ingredient in context['recipe']:  
                    context['recipe'][ingredient] = DATA[recipe_name][ingredient] * servings

            except ValueError:
                pass
    else:
        context = {'error_message': f'Рецепт "{recipe_name}" не найден'}  

    return render(request, 'calculator/index.html', context=context)  
    