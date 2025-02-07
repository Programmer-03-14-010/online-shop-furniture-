from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from orders.models import OrderModel


@receiver(post_save, sender=OrderModel)
def send_order_confirmation(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Buyurtmangiz qabul qilindi!",
            message=f"Hurmatli {instance.full_name}, sizning buyurtmangiz qabul qilindi!\n"
                    f"Yetkazib berish manzili: {instance.address}\n"
                    f"Jami summa: {instance.total_amount} so‘m",
            from_email="noreply@shop.com",
            recipient_list=[instance.email],
            fail_silently=False,
        )