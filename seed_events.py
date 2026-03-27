import os
import sys
import django

# Add the gestion_even directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gestion_even'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_even.settings')
django.setup()

from django.contrib.auth.models import User
from events.models import Event, EventCategory, JobCategory, Ticket
from datetime import datetime, timedelta
from django.utils import timezone

# Get or create admin user
admin_user, _ = User.objects.get_or_create(
    username='admin',
    defaults={'email': 'admin@eventtickets.com', 'is_staff': True, 'is_superuser': True}
)

# Create event categories with all required fields
categories_data = [
    {'name': 'Music', 'code': 'MUS', 'status': 'active'},
    {'name': 'Sports', 'code': 'SPT', 'status': 'active'},
    {'name': 'Technology', 'code': 'TEC', 'status': 'active'},
    {'name': 'Arts', 'code': 'ART', 'status': 'active'},
    {'name': 'Business', 'code': 'BUS', 'status': 'active'},
]

categories = []
for cat_data in categories_data:
    cat, created = EventCategory.objects.get_or_create(
        name=cat_data['name'],
        defaults={
            'code': cat_data['code'],
            'status': cat_data['status'],
            'created_user': admin_user,
            'updated_user': admin_user,
        }
    )
    categories.append(cat)
    if created:
        print(f"✓ Created category: {cat.name}")

# Get or create job category
job_cat, _ = JobCategory.objects.get_or_create(name='Event Management')

# Define locations (using simple string representation)
locations = [
    '40.7128,-74.0060',  # New York
    '34.0522,-118.2437',  # Los Angeles
    '37.7749,-122.4194',  # San Francisco
    '41.8781,-87.6298',  # Chicago
    '33.7490,-84.3880',  # Atlanta
    '39.7392,-104.9903',  # Denver
    '33.9425,-118.4081',  # Long Beach
    '29.7604,-95.3698',  # Houston
    '47.6062,-122.3321',  # Seattle
    '25.7617,-80.1918',   # Miami
]

# Sample events data
events_data = [
    {
        'name': 'Django Tech Conference 2026',
        'description': '<p>Learn the latest Django best practices and frameworks from industry experts worldwide.</p>',
        'category_idx': 2,  # Technology
        'venue': 'San Francisco Convention Center',
        'start_date': (timezone.now() + timedelta(days=15)).date(),
        'end_date': (timezone.now() + timedelta(days=15)).date(),
        'location': locations[2],
        'maximum_attende': 500,
        'price': 299,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
    {
        'name': 'Summer Music Festival 2026',
        'description': '<p>Three-day outdoor music festival featuring top international artists and live performances.</p>',
        'category_idx': 0,  # Music
        'venue': 'Central Park',
        'start_date': (timezone.now() + timedelta(days=45)).date(),
        'end_date': (timezone.now() + timedelta(days=47)).date(),
        'location': locations[0],
        'maximum_attende': 5000,
        'price': 150,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
    {
        'name': 'Annual Tech Hackathon',
        'description': '<p>Build innovative solutions in 24 hours with prizes worth $50,000 for winning teams.</p>',
        'category_idx': 2,  # Technology
        'venue': 'Tech Hub Downtown',
        'start_date': (timezone.now() + timedelta(days=20)).date(),
        'end_date': (timezone.now() + timedelta(days=20)).date(),
        'location': locations[3],
        'maximum_attende': 300,
        'price': 75,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
    {
        'name': 'Marathon Championship 2026',
        'description': '<p>Full marathon race through scenic city routes. Open to all fitness levels.</p>',
        'category_idx': 1,  # Sports
        'venue': 'City Marathon Route',
        'start_date': (timezone.now() + timedelta(days=30)).date(),
        'end_date': (timezone.now() + timedelta(days=30)).date(),
        'location': locations[1],
        'maximum_attende': 1000,
        'price': 50,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
    {
        'name': 'Contemporary Art Exhibition',
        'description': '<p>Showcasing works from 50 emerging contemporary artists from around the world.</p>',
        'category_idx': 3,  # Arts
        'venue': 'Metropolitan Art Gallery',
        'start_date': (timezone.now() + timedelta(days=10)).date(),
        'end_date': (timezone.now() + timedelta(days=35)).date(),
        'location': locations[0],
        'maximum_attende': 800,
        'price': 25,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
    {
        'name': 'Business Leaders Summit',
        'description': '<p>Network with C-suite executives and discuss future business trends and innovations.</p>',
        'category_idx': 4,  # Business
        'venue': 'Grand Hotel Ballroom',
        'start_date': (timezone.now() + timedelta(days=25)).date(),
        'end_date': (timezone.now() + timedelta(days=25)).date(),
        'location': locations[4],
        'maximum_attende': 400,
        'price': 500,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
    {
        'name': 'Electronic Music Night',
        'description': '<p>High-energy electronic dance music from world-renowned DJs and producers.</p>',
        'category_idx': 0,  # Music
        'venue': 'Downtown Nightclub',
        'start_date': (timezone.now() + timedelta(days=7)).date(),
        'end_date': (timezone.now() + timedelta(days=7)).date(),
        'location': locations[5],
        'maximum_attende': 1200,
        'price': 40,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
    {
        'name': 'Web Development Workshop',
        'description': '<p>Hands-on workshop covering React, Django, and modern web development practices.</p>',
        'category_idx': 2,  # Technology
        'venue': 'Code Academy Downtown',
        'start_date': (timezone.now() + timedelta(days=12)).date(),
        'end_date': (timezone.now() + timedelta(days=12)).date(),
        'location': locations[8],
        'maximum_attende': 150,
        'price': 120,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
    {
        'name': 'Basketball Tournament',
        'description': '<p>City-wide amateur basketball tournament. Teams of 5 players each competing for championship.</p>',
        'category_idx': 1,  # Sports
        'venue': 'City Sports Arena',
        'start_date': (timezone.now() + timedelta(days=35)).date(),
        'end_date': (timezone.now() + timedelta(days=42)).date(),
        'location': locations[6],
        'maximum_attende': 2000,
        'price': 60,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
    {
        'name': 'Photography Masterclass',
        'description': '<p>Learn professional photography techniques from award-winning photographers and industry experts.</p>',
        'category_idx': 3,  # Arts
        'venue': 'Creative Studio Space',
        'start_date': (timezone.now() + timedelta(days=18)).date(),
        'end_date': (timezone.now() + timedelta(days=18)).date(),
        'location': locations[9],
        'maximum_attende': 50,
        'price': 200,
        'scheduled_status': 'scheduled',
        'status': 'active',
    },
]

# Create events
created_count = 0
for idx, event_data in enumerate(events_data):
    cat_idx = event_data.pop('category_idx')
    category = categories[cat_idx]
    
    event, created = Event.objects.get_or_create(
        name=event_data['name'],
        defaults={
            'category': category,
            'job_category': job_cat,
            'description': event_data['description'],
            'venue': event_data['venue'],
            'start_date': event_data['start_date'],
            'end_date': event_data['end_date'],
            'location': event_data['location'],
            'maximum_attende': event_data['maximum_attende'],
            'price': event_data['price'],
            'scheduled_status': event_data['scheduled_status'],
            'status': event_data['status'],
            'created_user': admin_user,
            'updated_user': admin_user,
        }
    )
    if created:
        # Create a ticket for each event
        ticket, _ = Ticket.objects.get_or_create(
            name=f"{event_data['name']} Ticket",
            defaults={
                'description': f"Ticket for {event_data['name']}",
                'price': event_data['price'],
                'nbr_ticket': event_data['maximum_attende'],
            }
        )
        event.ticket = ticket
        event.save()
        
        created_count += 1
        print(f"✓ Created event {idx+1}: {event.name}")
    else:
        print(f"⚠ Event already exists: {event.name}")

print(f"\n✅ Seeding complete! {created_count}/10 events created successfully!")
