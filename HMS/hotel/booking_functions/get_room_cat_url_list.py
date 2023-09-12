from hotel.models import Room
from django.urls import reverse



def get_room_cat_url_list():
    room = Room.objects.all()[0]
    room_list = []
    room_categories = dict(room.ROOM_CATEGORIES)
    
    room_cat_url_list = []
    
          
    for category in room_categories:
        room_category = room_categories.get(category)
        room_url = reverse('hotel:RoomDetailView', kwargs={
            'category': category})
        
        #print(room, room_url)
        room_cat_url_list.append((room_category, room_url))
        
        return room_cat_url_list