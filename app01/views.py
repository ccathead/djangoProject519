# from django.forms.formsets.BaseFormSet import forms
from django.shortcuts import render, redirect
from app01 import models
from app01.models import UserInfo


# Create your views here.
def depart_list(request):
    queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {'departments': queryset})


def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')
    else:
        # 获取数据并保存到保存到数据库
        models.Department.objects.create(title=request.POST.get('title'))
        return redirect("depart_list")


def depart_delete(request):
    nid = request.GET.get('nid')
    print(nid)
    models.Department.objects.filter(id=nid).delete()
    return redirect("depart_list")


def depart_edit(request, nid):
    if request.method == "GET":
        row_obj = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row_obj': row_obj})
    models.Department.objects.filter(id=nid).update(title=request.POST.get('title'))
    return redirect("depart_list")


def user_list(request):
    queryset = models.UserInfo.objects.all()
    # for user in queryset:
    # print(user.id, user.name, user.password, user.age, user.create_time.strftime('%Y-%m-%d'),
    #       user.get_gender_display(), user.depart_id.title)
    # print(user.name)
    # print(user.password)
    # print(user.age)
    # print(user.create_time)
    return render(request, 'user_list.html', {'users': queryset})


from django import forms


class UserModelForm(forms.ModelForm):
    # name = forms.CharField(max_length=3, label="用户名")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", 'age', 'account', 'create_time', 'depart_id', 'gender']

        #自定义样式
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }

        # 循环找到所有的插件，应用class="form-control"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 使用小括号
        for name, field in self.fields.items():  # 使用 items()
            field.widget.attrs = {'class': 'form-control', "placeholder": field.label}


def user_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})
        # context = {
        #     'gender_choices': models.UserInfo.gender_choices,
        #     'depart_list': models.Department.objects.all(),
        # }
        # return render(request, 'user_add.html', context)
    """获取用户提交的数据"""
    """要提供校验"""
    if request.method == "POST":

        form = UserModelForm(request.POST)
        if form.is_valid():
            """数据合法就保存到数据库"""
            form.save()
            return redirect("/user/list/")
        else:
            """校验失败"""
            return render(request, 'user_add.html', {'form': form})


def user_edit(request, nid):
    """编辑用户"""
    """根据id去数据库获取要编辑的那一行"""
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        """instance 就是当前操作的对象"""
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form, 'nid': nid})
    """不新提交数据，而是将数据更新到这一行"""
    if request.method == "POST":
        form = UserModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            # save默认保存的是用户输入的所有数据，如果想要再用户输入以外增加一点值
            # form.instance.字段名=值
            form.save()
            return redirect("/user/list/")
        else:
            return render(request, 'user_edit.html', {'form': form, 'nid': nid})


def user_delete(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")