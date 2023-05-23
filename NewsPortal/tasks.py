from django.core.mail import send_mail
from django.utils import timezone

from NewsPortal.models import Post


def send_post_per_week(self):
    categories = Post.categories.all()
    post = Post.objects.all()
    now = timezone.now()
    since_week = now - timezone.timedelta(days=7)
    posts_count = []
    posts_urls = []
    for category in categories:
        posts_count.append(category.post)
        posts_urls.append(self.request.build_absolute_uri(reverse('post_detail', args=[post.pk])))
        if post.time_in >= since_week:
            send_mail(
                subject=f'',
                message=f'Здравствуй {self.request.user.username}. Новая статья в твоём любимом разделе! {post.text[:50]}\n\n Ссылка на новый пост: {post_url}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=subscribers_emails,
            )
