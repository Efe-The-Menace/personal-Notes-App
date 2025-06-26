from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Note_data
from .forms import note_form

@login_required
def list_view(request):
     list = Note_data.objects.filter(user=request.user)
     return render(request, 'Notes/note_list.html', {'list': list})
 
@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note_data, pk=pk, user=request.user)
    return render(request, 'Notes/note_detail.html', {'note': note})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = note_form(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = note_form()

    return render(request, 'Notes/form.html', {'form': form})

@login_required
def update_view(request, pk):
    note = get_object_or_404(Note_data, pk=pk, user = request.user)
    if request.method == 'POST':
        form = note_form(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = note_form(instance=note)
    return render(request, 'Notes/form.html', {'form': form})


@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note_data, pk=pk, user= request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'Notes/note_confirm_delete.html', {'note':note})