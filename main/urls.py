from django.urls import path
from main.views import create_item_flutter, show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id,add_item, reduce_item, remove_item, get_item_json, add_item_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_item, delete_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-item/<int:item_id>/', add_item, name='add_item'),
    path('reduce-item/<int:item_id>/', reduce_item, name='reduce_item'),
    path('remove-item/<int:item_id>/',remove_item, name='remove_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('delete-item/<int:id>', delete_item, name='delete_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
]