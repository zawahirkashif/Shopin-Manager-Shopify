from send_request_to_update import *
from credentials import *
from get_product_inv import *

def main():
    products_inventory = Product_Request.get_all_products()
    products_inventory_upload = products_inventory[['inv_item_id','shopify_inventory']] 
    print(products_inventory_upload)  
    for inv_item_id, inventory_push in products_inventory_upload.itertuples(index=False):
        Post_Request_Inventory.post_request_inventory(inv_item_id, round(int(inventory_push)))
        print("Sucess") 

if __name__ == "__main__":
    main()