import re

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import CreateView, UpdateView, DeleteView

from notice.forms import NoticeForm
from notice.models import Notice


from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView

# 공지사항

def notice_list(request):
    qs = Notice.objects.all()
    paginate_by = 10
    return render(request, 'notice/notice_list.html',
                  {'notice_list': qs})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    is_liked = False
    if notice.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'notice': notice,
        'is_liked': is_liked,
        'total_likes': notice.total_likes(),
    }
    return render(request, 'notice/notice_detail.html',
                  context)

def notice_new(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            return redirect('notice:notice_detail', pk=notice.pk)
    else:
        form = NoticeForm()
    return render(request, 'notice/notice_form.html', {'form':form})

def notice_edit(request, pk):
    item = get_object_or_404(Notice, pk=pk)
    form = NoticeForm(request.POST or None, instance=item)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()  # 저장하기
        return redirect('/notice/' + str(item.id))
    return render(request, 'notice/notice_form.html', {'form':form})


def notice_remove(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('notice:notice_list')
#


def like_notice(request):
    notice = get_object_or_404(Notice, id=request.POST.get('notice_id'))
    is_liked = False
    if notice.likes.filter(id=request.user.id).exists():
        notice.likes.remove(request.user)
        is_liked = False
    else:
        notice.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(notice.get_absolute_url())

#
#
#
#
