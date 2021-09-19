Templateview
from django.views.generic import Templateview


class  MyTemplateView(Templateview):
    template_name = "index.html"

    def  get_context_data(self, **kwargs):(あたいに何かを指定したい時、必要)
        context = super(ViewName, self).get_context_data(**kwargs)
        context["foo"] = "bar"
        return context
<div class="sample">{{foo}}-> bar</div>


class MyBookList(ListView):
    model = Books
    # デフォルトでobject_list,モデル名_listは使えるが、自分でtemplateで使う変数名
    # を指定できる
#     {%for object in my_books%}
#     <li>{object.name}</li>
# {%endfor%}
 # paginate_by:1ページに表示する数
# queryset:ソートしたり、フィルタリングする
# def get_queryset(self):
#     return model.objects.filter(some_column=foo)と同じ
#  def  get_context_data(self, **kwargs):(あたいに何かを指定したい時、必要)
#         context = super(ViewName, self).get_context_data(**kwargs)
#         context["foo"] = "bar"
#         return contextもかける
    context_object_name = "my_books"
    paginate_by = 5
    queryset = model.objects.filter(some_column=foo)


class OnDetailView(DetailView):
    model = MyModel
urlpattterns = [
    path('<int:pk>',OnDetailView.as_view()),
]


class MyCreateView(CreateView):
    model = MyModel
    template_name =
    fields("name",)
    作成成功した後のページをどこに遷移させるか
    success_url = reverse_lazy('list')
    # フォームのフィールドにname項目入れる
    # form変数をCreateView,UpdateViewは自動生成してくれる
#     <form method="post">
# {%csrf_token%}
# <table>
# {{form}}
# </table>
# <input type="submit"/>
# </form>
フォームのフィールド名変更したい時(forms.py)
class MyModelForm (forms.ModelForm):
    class Meta:
        model = MyModel
        field = ["name"]

(views.py)
class MyCreateView(CreateView):
    form_class = MyModelForm


追加したデータがちゃんと処理されたかユーザに伝えないと心配するので、伝えるバリデーション機能追加
from django.views.generic.edit import CreateView
from django.contrib import messages  # メッセージフレームワーク


class MyCreateView(CreateView):
    model =

    def form_valid(self,form):
        message.success(self.request,"保存しました")
        return super().form_valid(form)

    def form_invalid(self,form):
        message.warning(self.request,"保存されませんでした")
        return super().form_invalid(form)

{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}


class MyDeleteView(DeleteView):
    model =
    template_name = delete.html
    success_url = reverse_lazy('list')

解除確認画面(delete.html)
<form method="post">{% csrf_token %}

<p>本当に "{{ object }}" を削除しますか?</p>

<input type="submit" value="削除する">

</form>



共通項目のview作って継承したいと時

objectのimportは必要ない

class MyCommonView(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["SITE_NAME"] = "SITE-NAME"
        return context


class MyListView(ListView, MyCommonView):
    model = MyModel
