from django.shortcuts import render, redirect
from .forms import MemoForm
from .models import Memo
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request):
    memos = Memo.objects.all()
    context = {
        'memos':memos,
    }
    return render(request, 'memos/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save()
            return redirect('memos:index')
    else:
        form = MemoForm()
    context = {
        'form':form,
    }
    return render(request, 'memos/create.html', context)


def detail(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    context = {
        'memo':memo,
    }
    return render(request, 'memos/detail.html', context)


def delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memos:index')