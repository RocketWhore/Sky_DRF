import stripe

from config import settings
from course.models import Subscription


def get_payment(price, title, pk):
    stripe.api_key = settings.STRIPE_API_KEY

    product = stripe.Product.create(name=title)
    price = stripe.Price.create(
        unit_amount=price,
        currency="usd",
        recurring={"interval": "month"},
        product=product['id'],
    )
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price['id'],
                "quantity": 2,
            },
        ],
        mode="subscription",
    )
    subscription = Subscription.objects.get(pk=pk)
    subscription.is_subscribed = True
    subscription.save()
    return session['url']
