import re

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from django.views.generic import CreateView, UpdateView, DeleteView

from question.forms import QuestionForm, CommentForm
from question.models import Question, Comment

from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView

# 공지사항

def question_list(request):
    qs = Question.objects.all()
    return render(request, 'question/question_list.html',
                  {'question_list': qs})


# 정상적으로 작동되는 댓글 기능 코드 ------------------------------------------------------------
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    # comments = Comment.objects.filter(post=question).order_by('-id')
    comments = Comment.objects.filter(post=question)[:1]

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)

        if comment_form.is_valid():
            message = request.POST.get('message')
            comment = Comment.objects.create(post=question, message=message)
            comment.save()
            return HttpResponseRedirect(question.get_absolute_url())

    else:
        comment_form = CommentForm()

    context = {
        'question': question,

        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'question/question_detail.html', context)



def question_new(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('question:question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'question/question_form.html', {'form':form})

def question_edit(request, pk):
    item = get_object_or_404(Question, pk=pk)
    form = QuestionForm(request.POST or None, instance=item)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()  # 저장하기
        return redirect('/question/' + str(item.id))
    return render(request, 'question/question_form.html', {'form':form})


def question_remove(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('question:question_list')
#



