import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates roons"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        print(room_models, all_users)
        seeder.add_entity(room_models.Room, number, {
            "host": lambda x: random.choice(all_users), "room_type": lambda x: random.choice(room_types),
            "name": lambda x: seeder.faker.company(),
            "price": lambda x: random.randint(1, 1000),
            "beds": lambda x: random.randint(1, 10),
            "guests": lambda x: random.randint(1, 100),
            "bedrooms": lambda x: random.randint(1, 10),
            "baths": lambda x: random.randint(1, 5),
        })
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenity.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facility.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_Rule.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} created!"))
