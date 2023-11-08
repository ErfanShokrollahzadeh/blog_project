from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'Sun_learning',
        'title': 'Sun Inform',
        'author': 'Erfan Shokrollahzadeh',
        'image': 'sun.jpeg',
        'date': date(2021, 8, 21),
        'short_description': 'this is sun information in my blog',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.
        """,
    },
    {
        'slug': 'Galaxy_learning',
        'title': 'Galaxy Inform',
        'author': 'Erfan Shokrollahzadeh',
        'image': 'galaxy.png',
        'date': date(2021, 4, 5),
        'short_description': 'this is Galaxy information in my blog',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.
        """,
    },
    {
        'slug': 'Earth_learning',
        'title': 'Earth Inform',
        'author': 'Erfan Shokrollahzadeh',
        'image': 'erth.png',
        'date': date(2021, 2, 1),
        'short_description': 'this is earth information in my blog',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consectetur debitis est et excepturi ipsam iste iure,
            magnam natus nemo neque nihil officiis quidem quod sequi tempore! Accusantium laborum nisi veritatis.
        """,
    },
]


def get_date(post):
    return post['date']

def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', context={'posts': latest_posts})

def posts(request):
    context = {
        'all_posts': all_posts,
}
    return render(request, 'blog/all-post.html', context)

def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {'post': post})
