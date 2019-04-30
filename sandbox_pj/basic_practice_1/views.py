import sys
import codecs


from django.shortcuts import (render, redirect,)
from .models import Posting
from .forms import PostingForm

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)


def index(request):
    form = PostingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('basic_practice_1:index')
    new_text = Posting.objects.all().order_by('-id')
    contexts = {
        'form': form,
        'new_text': new_text,
    }
    return render(request, 'index.html', contexts)
