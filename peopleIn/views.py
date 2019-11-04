from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
# from userExtends.forms import UserForm

# from notice.models import Notice
from forSale.models import Item
from userExtends.forms import ProfileForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['item_list'] = Item.objects.order_by('-price')[:4]

        return context

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    # form_class = ProfileForm
    success_url = reverse_lazy('register_done')



class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view
                                  )

