class DataMixin:
    title_page = None
    cat_selected = None
    extra_context = {}
    paginate_by = 3

    def __init__(self):
        self.extra_context['title'] = self.title_page
        self.extra_context['cat_selected'] = self.cat_selected

    def get_mixin_context(self, context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context
