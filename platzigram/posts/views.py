from django.shortcuts import render

from datetime import datetime

posts =[
     {
        'title' : 'At woods',
        'user':{
        'name' : 'Leonardo Latorre',
        'picture' : 'https://picsum.photos/id/1003/60/60',
    },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/id/1003/800/600',
    },
    {   'title' : 'Cute Pug',
        'user':{
        'name' : 'Francesca Latorre',
        'picture' : 'https://picsum.photos/id/1025/60/60'
    },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/id/1025/800/600',
    },
    {
        'title':'Amazing Landscape',
        'user':{
        'name' : 'Angela Fandino',
        'picture' : 'https://picsum.photos/id/1015/60/60',
        },
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo' : 'https://picsum.photos/id/1015/800/600',
    },
]
def list_posts(request):
    return render (request, 'feed.html', {'posts':posts})