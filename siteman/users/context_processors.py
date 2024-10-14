menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить страницу', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
]


def get_man_context(request):
    return {'mainmenu': menu}
