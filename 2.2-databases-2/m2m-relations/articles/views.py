from django.shortcuts import render
from .models import Article
from datetime import datetime

def articles_list(request):
    template = "articles/news.html"

    object_list = Article.objects.all().order_by("-published_at").prefetch_related('scopes')
    
    print("Запрос к базе данных:", object_list.query)

    main_tags = []
    for article in object_list:
        scopes = article.scopes.all()
        for scope in scopes:
            if scope.is_main:
                main_tags.append(scope.tag)
                break

    context = {
        "articles": object_list,
        "main_tags": main_tags,
    }

    for article in object_list:
        print(f"Заголовок: {article.title}")
        print(f"Текст: {article.text[:50]}...")
        print(f"Изображение: {article.image}")

    print("Основные теги:", context["main_tags"])

    if not context["main_tags"]:
        print("Основные теги не найдены")
    if not context["articles"]:
        print("Статьи не найдены")

    if "articles" in context and "main_tags" in context:
        print("Переменные передаются в шаблон правильно")
    else:
        print("Переменные не передаются в шаблон")

    return render(request, template, context)

last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Последнее изменение: {last_modified}")
