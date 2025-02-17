from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, Steps, Like
from users.models import Profile
from django.contrib import messages
from .forms import RecipeForm
from django.http import JsonResponse
from django.db.models import F

def posts(request):
    post = Posts.objects.all().order_by('-created_at')
    profiles = Profile.objects.all()

    liked_posts = []
    if request.user.is_authenticated:
        liked_posts = Like.objects.filter(user=request.user).values_list('post_id', flat=True)

    content = {
        'form': post,
        'profiles': profiles,
        'liked_posts': liked_posts
    }
    return render(request, 'posts.html', content)


@login_required
def new_post(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.views = 1
            recipe.save()
            recipe.viewed_users.add(request.user)

            total_forms = int(request.POST.get('steps-TOTAL_FORMS'))

            for i in range(total_forms):
                step_description = request.POST.get(f'steps-{i}-step_des')
                step_image = request.FILES.get(f'steps-{i}-step_image')

                if step_description:
                    Steps.objects.create(
                        recipe=recipe,
                        step_des=step_description,
                        step_image=step_image,
                    )

            messages.success(request, 'Рецепт успешно создан!')
            return redirect('posts')

    else:
        recipe_form = RecipeForm()

    return render(request, 'new_post.html', {'recipe_form': recipe_form})

def PostView(request, id):
    post = get_object_or_404(Posts, pk=id)
    steps = Steps.objects.filter(recipe=post.id)
    profiles = Profile.objects.all()

    liked_posts = []
    if request.user.is_authenticated:
        liked_posts = Like.objects.filter(user=request.user).values_list('post_id', flat=True)

    content = {
        'post': post,
        'formset': steps,
        'profiles': profiles,
        'liked_posts': liked_posts
    }
    return render(request, 'post_view.html', content)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    
    like_exists = Like.objects.filter(user=request.user, post=post).exists()
    
    if like_exists:
        Like.objects.filter(user=request.user, post=post).delete()
        liked = False
    else:
        Like.objects.create(user=request.user, post=post)
        liked = True

    like_count = post.likes.count()

    return JsonResponse({'like_count': like_count, 'liked': liked})

def PostViewIncrement(request, id):
    post = get_object_or_404(Posts, pk=id)

    if request.user.is_authenticated:
        if request.user not in post.viewed_users.all():
            post.viewed_users.add(request.user)
            Posts.objects.filter(pk=id).update(views=F('views') + 1)
    
    else:
        viewed_posts = request.session.get('viewed_posts', [])
        
        if id not in viewed_posts:
            Posts.objects.filter(pk=id).update(views=F('views') + 1)
            
            viewed_posts.append(id)
            request.session['viewed_posts'] = viewed_posts

    post.refresh_from_db()
    return JsonResponse({'views': post.views})
