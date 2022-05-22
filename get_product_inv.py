import requests
from credentials import Authrization
import pandas as pd
from pandas import DataFrame

class Product_Request:
    def get_all_products():
        inventory_data_dataframe = []
        products=pd.DataFrame()
        inventory_data=pd.DataFrame()
        while True:
            url = f"https://{Authrization.API_KEY}:{Authrization.ADMIN_API}@{Authrization.STORE_URL}/api/{Authrization.API_VERSION}/{Authrization.END_POINT}={Authrization.LAST_PRODUCT_ID}"
            response = requests.request("GET", url)
            for access_list_data in response.json()['products']:
                inv_variants = access_list_data['variants']
                vendor_name=access_list_data['vendor']
                for access_inner_list_data in inv_variants:
                    product_id=access_list_data['id']
                    inv_item_id=access_inner_list_data['inventory_item_id']
                    
                    sku=access_inner_list_data['sku']
                    inventory_quantity = access_inner_list_data['inventory_quantity']
                    if vendor_name == 'Adidas' and inventory_quantity <=1:
                        inventory_quantity = 0
                        inventory_data=pd.DataFrame({'product':[product_id], 'inv_item_id':[inv_item_id],'sku':[sku], 'shopify_inventory':[inventory_quantity], 'vendor_name':[vendor_name]})
                    else:
                        inventory_data=pd.DataFrame({'product':[product_id], 'inv_item_id':[inv_item_id],'sku':[sku], 'shopify_inventory':[inventory_quantity], 'vendor_name':[vendor_name]})                        
                    inventory_data_dataframe.append(inventory_data)
            df=pd.DataFrame(response.json()['products'])
            products=pd.concat([products,df])
            Authrization.LAST_PRODUCT_ID=df['id'].iloc[-1]
            if len(df)<250:
                break
        inventory_data_dataframe = pd.concat(inventory_data_dataframe).reset_index()        
        return(inventory_data_dataframe)


