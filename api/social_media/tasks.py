from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def clean_soft_deleted_posts():
    """
    Celery task to permanently delete posts that have been soft-deleted
    for more than 30 days.
    """
    from social_media.models import Post
    from django.utils import timezone
    from datetime import timedelta

    threshold_date = timezone.now() - timedelta(days=30)
    posts_to_delete = Post.objects.filter(deleted=True, updated_at__lt=threshold_date)
    count = posts_to_delete.count()
    posts_to_delete.delete()
    msg = f"Deleted {count} soft-deleted posts older than 30 days."
    logger.info(msg)
    
    return msg