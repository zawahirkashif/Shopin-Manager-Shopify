import requests
from credentials import *
class Post_Request_Inventory:  
    def post_request_inventory(inventory_item_id, onhand: int):
        post_url=f"https://{Authrization.API_KEY}:{Authrization.ADMIN_API}@{Authrization.STORE_URL}/api/{Authrization.API_VERSION}/"
        requests.post(post_url+Authrization.POST_URL_END_POINT, json={"inventory_item_id": inventory_item_id,"location_id": Authrization.INVENTORY_LOCATION_ID,"available": onhand})
        

    