# About Shopin Manager 💻
Do you have multiple stores? Are You sharing your inventory with others? Is your Shopify is not integrated with your database? Or you are facing product not found issue if your inventory is less? 🤔
Worry not Shopin Manager is the best solution for all of these problems.
### What Shopin Manager Do?
Let’s say you have thousands of products and hundreds of thousands of variants.Isn't it hard to keep track on your low inventory product variants?
**Shopin Manager will help you to set your low inventory variant quantity to zero so you never loose a sale.😊** So sit back and enjoy a glass of coke with some popcorns and let Shopin Manager do all the work for you. 👍
### How It Works?
Shopin Manager is the best solution for your inventory management problem. It is made for those who have a huge amount of products. With the idea to turn all the manual work into one click.
#### Here's Why
- Shopin Manager go through each of your product variants/skus and check your inventory.
- Checks if any product variant inventory is less than two Shopin Manager gonna put a zero their.
- Because if a product variant inventory level is less than two you can not just draft the product **right?**
### Build With
Shopin Manager is bulit with love ❤️ using python and Shopify API a reference to the shopify documentation is attached below 👇
- [Python 🐍](https://www.python.org/)
- [Shopify Product API](https://shopify.dev/api/admin-rest/2021-10/resources/product)
- [Shopify Inventory API](https://shopify.dev/api/examples/product-inventory)

# Getting Started

Let dive a little more deeper in the Shopin Manager To get a local copy up and running follow these simple example steps.

### Prerequisites

- Python
```
https://www.python.org/
```
- If you already have the python installed in your device check the version.
```
python --version
```

### Installation

1- Open visual studio code or any code editor select a folder where you want to clone the repo

2- Clone the Repo

 ```
 git clone https://github.com/zawahirkashif/Shopin-Manager-Shopify.git
 ```

3- Install all the required packages
```
pip install -r requirnments.txt
```
4- Create a private app on your Shopify Store
```
https://youtube.com/clip/UgkxHA0lZFT2LIwIi_cWc1W3ujoclTHLgs4N
```
5 Add API key
```
 API_KEY = ""
```
6 Add Admin API 
```
 ADMIN_API = ""
```
7 Add your store url e.g example.myshopify.com
```
  STORE_URL = ""
```
8 Add API version most probably it will be 2022-04
```
  API_VERSION = ""
```
9 Filter your products **oldest created** open the top most product and copy the id in the end of url
```
   LAST_PRODUCT_ID = ""
```
### Usage
Right now it set variant inventory zero if the current variant quantity is less than 2 even you can set a condition if you want to keep track on specific vendors or if you don’t have any vendors it is completely of you just need change the code below.


![Actual](https://github.com/zawahirkashif/Set-Inventory-Zero-If-Quantity-Less-Than-Two-Shopify/blob/b064e17afbe56d6ef2eab395ff874b1b0fc8a98d/images/carbon.png)

#### But I Don't Have Any Specific Vendor

Worry not just cange the above code with this

![No Vendor](https://github.com/zawahirkashif/Set-Inventory-Zero-If-Quantity-Less-Than-Two-Shopify/blob/b064e17afbe56d6ef2eab395ff874b1b0fc8a98d/images/carbon%20(1).png)

#### But I Have More Than One Vendor

Change your code with this condition

![Multi Vendor](https://github.com/zawahirkashif/Set-Inventory-Zero-If-Quantity-Less-Than-Two-Shopify/blob/b064e17afbe56d6ef2eab395ff874b1b0fc8a98d/images/carbon%20(2).png)

##### How To Run This Code?

```
python main.py
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes 
4. Push to the Branch 
5. Open a Pull Request


## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact

Your Name - [@SMZawahir1](https://twitter.com/SMZawahir1) - zawahirkashif@gmail.com

Project Link: [https://github.com/zawahirkashif/Shopin-Manager-Shopify]([https://github.com/your_username/repo_name](https://github.com/zawahirkashif/Shopin-Manager-Shopify.git))



