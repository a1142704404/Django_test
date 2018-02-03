from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

from .models import Comment
from .form import CommentForm

def post_comment(request,post_pk):
    '''先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来，
        这里我们使用了Django提供的一个快捷函数get_object_or_404，
        这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回404'''
    post = get_object_or_404(Post,pk = post_pk)
    if request.method == 'POST':
        #用户提交的数据存在requestPOST中，这是一个类字典对象
        form = CommentForm(request.POST)
        if form.is_valid():
            #如果数据合法，调用SAVE存到数据库
            comment = form.save(commit=False)
            comment.post = post #将评论和被评论的文章关联起来
            comment.save() #最终数据存入数据库
            return redirect(post) #重定向回get_absolute_url返回的URL
        else:
            comment_list = post.comment_set.all()
            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            return render(request,'blog/detail.html',context=context)
    return redirect(post)