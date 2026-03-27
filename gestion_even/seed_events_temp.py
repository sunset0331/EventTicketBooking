from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model

from events.models import Event, EventCategory, JobCategory


User = get_user_model()
user, _ = User.objects.get_or_create(
    username="seed_admin",
    defaults={
        "first_name": "Seed",
        "last_name": "Admin",
        "email": "seed_admin@example.com",
        "is_staff": True,
        "is_superuser": True,
    },
)
if not user.has_usable_password():
    user.set_password("seedadmin123")
    user.save(update_fields=["password"])

categories = [
    ("Technology", "TECH01"),
    ("Business", "BUS001"),
    ("Design", "DES001"),
]
category_objs = {}
for name, code in categories:
    obj, _ = EventCategory.objects.get_or_create(
        code=code,
        defaults={
            "name": name,
            "created_user": user,
            "updated_user": user,
            "status": "active",
        },
    )
    updated = False
    if obj.created_user_id != user.id:
        obj.created_user = user
        updated = True
    if obj.updated_user_id != user.id:
        obj.updated_user = user
        updated = True
    if obj.status != "active":
        obj.status = "active"
        updated = True
    if updated:
        obj.save()
    category_objs[name] = obj

job_category, _ = JobCategory.objects.get_or_create(name="General Professionals")

seed_events = [
    ("Tech Future Summit 2026", "Technology", "Casablanca Expo Center"),
    ("AI Builders Meetup", "Technology", "Rabat Innovation Hub"),
    ("Cloud Security Bootcamp", "Technology", "Marrakech Tech Campus"),
    ("Startup Growth Forum", "Business", "Casablanca Finance City Hall"),
    ("Women in Leadership Conference", "Business", "Tangier Convention Center"),
    ("Digital Marketing Masterclass", "Business", "Agadir Business Lounge"),
    ("UX Design Sprint Live", "Design", "Rabat Creative House"),
    ("Product Design Circle", "Design", "Marrakech Design Lab"),
    ("Brand Storytelling Workshop", "Design", "Casablanca Art District"),
    ("Innovation & Networking Night", "Business", "Fez Cultural Center"),
]

base_date = date.today() + timedelta(days=7)
created_count = 0
for idx, (name, category_name, venue) in enumerate(seed_events):
    start = base_date + timedelta(days=idx * 3)
    end = start + timedelta(days=1)
    price = Decimal("99.00") + Decimal(idx * 10)
    _, created = Event.objects.get_or_create(
        name=name,
        defaults={
            "category": category_objs[category_name],
            "description": f"<p>{name} is a curated event focused on practical insights, networking, and growth.</p>",
            "job_category": job_category,
            "scheduled_status": "scheduled",
            "venue": venue,
            "start_date": start,
            "end_date": end,
            "location": "33.5731,-7.5898",
            "maximum_attende": 200 + idx * 20,
            "created_user": user,
            "updated_user": user,
            "status": "active",
            "price": price,
        },
    )
    if created:
        created_count += 1

print(f"Seed complete. Created {created_count} new events.")
print(f"Total events in DB: {Event.objects.count()}")
for e in Event.objects.order_by("-id")[:10]:
    print(f"{e.id}|{e.name}|{e.start_date}|{e.status}")
