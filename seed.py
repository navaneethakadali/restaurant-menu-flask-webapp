from app import app
from database import db,MenuItem
menu_items=[
    {
        "name": "Veg Manchurian",
        "description": "A delicious Indo-Chinese dish of veggie balls dunked into a sauce with hot, sweet, sour and salty flavors.",
        "price": 169,
        "image_url": "https://pbs.twimg.com/media/DydrW5IWwAEjGUQ.jpg",
        "category": "Starter"
    },
    {
        "name": "Apollo Fish",
        "description": "A popular restaurant appetizer made with boneless fish, spices and curry leaves.",
        "price": 599,
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBG6QC7DWanwEen2u755fNUdOZ6PnRe6EkzQ&s",
        "category": "Starter"
    },
    {
        "name": "Chicken Curry",
        "description": "Indian chicken curry has an unbeatable combination of flavors.",
        "price": 250,
        "image_url": "https://tse2.mm.bing.net/th?id=OIP.nTT5tvHk0Up59zRcC6oEygAAAA&pid=Api&P=0&h=180",
        "category": "Main Course"
    },
    {
        "name": "Butter Naan",
        "description": "Butter naan is a popular leavened, oven-baked flatbread from India, traditionally cooked in a clay tandoor oven and generously brushed with melted butter or ghee.",
        "price": 59,
        "image_url": "https://vaya.in/recipes/wp-content/uploads/2018/03/Butter-Naan-1.jpg",
        "category": "Main Course"
    },
    {
        "name": "Roti",
        "description": "Roti is an unleavened flatbread made with just a handful of ingredients.",
        "price": 49,
        "image_url": "https://werecipes.com/app/uploads/2015/04/phulka-roti-chappati-recipe.jpg",
        "category": "Main Course"
    },
    {
        "name": "Chicken Tikka",
        "description": "A popular curried dish made with boneless chicken and ground spices.",
        "price": 199,
        "image_url": "https://tse3.mm.bing.net/th?id=OIP.I8b9lb4qxYZuLx3Oy3eMPgAAAA&pid=Api&P=0&h=180",
        "category": "Main Course"
    },
    {
        "name": "Mutton Roast",
        "description": "A tasty, soft side dish cum gravy made by cooking minced meat with spices.",
        "price": 299,
        "image_url": "https://www.archanaskitchen.com/images/archanaskitchen/1-Author/naseerawazir-gmail.com/Mutton_Varattiyad__Malabar_Mutton_Roast.jpg",
        "category": "Main Course"
    },
    {
        "name": "Samosa",
        "description": "A deep fried triangular shape fried dough filled with a spiced potato peas filling.",
        "price": 99,
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6fXEwGgYtfXXvk4ia-3LFCjN5U6hdutQzwA&s",
        "category": "Starter"
    },
    {
        "name": "Pav Bhaji",
        "description": "A spicy curry of mixed vegetables cooked in a special blend of spices.",
        "price": 149,
        "image_url": "https://images.unsplash.com/photo-1606491956689-2ea866880c84",
        "category": "Main Course"
    },
    {
        "name": "Kachori",
        "description": "A deep-fried, spicy, stuffed pastry originating from the Marwar region of Rajasthan, India.",
        "price": 49,
        "image_url": "https://blog.swiggy.com/wp-content/uploads/2024/06/Image-5_-Aloo-Kachori-1024x538.png",
        "category": "Starter"
    },
    {
        "name": "Paneer Biryani",
        "description": "A mildly spiced and delicately flavored dum cooked traditional biryani recipe.",
        "price": 299,
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzTkFwrC9PqVXBOIWXMHMrb1lpetG4NHYYBw&s",
        "category": "Main Course"
    },
    {
        "name": "Chicken Biryani",
        "description": "A savory chicken and rice dish including aromatics steamed together.",
        "price": 399,
        "image_url": "https://www.licious.in/blog/wp-content/uploads/2022/06/chicken-hyderabadi-biryani-01.jpg",
        "category": "Main Course"
    },
    {
        "name": "Sizzling Brownie",
        "description": "A chocolate brownie with ice cream on top served with melted chocolate.",
        "price": 149,
        "image_url": "https://www.cookwithkushi.com/wp-content/uploads/2017/01/sizzling_brownie_sundae_ice_cream.jpg",
        "category": "Desserts"
    },
    {
        "name": "Chocolate Chocochip Ice Cream",
        "description": "Creamy vanilla ice cream packed with tiny melt-in-your-mouth chocolate chips.",
        "price": 199,
        "image_url": "https://afoodloverskitchen.com/wp-content/uploads/chocolate-chocolate-chip-ice-cream-featured.jpg",
        "category": "Desserts"
    },
    {
        "name": "Blueberry Lemonade",
        "description": "A refreshing cocktail perfect for a lazy summer afternoon.",
        "price": 149,
        "image_url": "https://i.pinimg.com/originals/28/e4/43/28e4437ee258d31e9690c11708e5bb73.jpg",
        "category": "Beverages"
    },
    {
        "name": "Watermelon Smoothie",
        "description": "A beautiful beverage that plays nicely with fresh summer flavors.",
        "price": 149,
        "image_url": "https://tse4.mm.bing.net/th?id=OIP.Zji90eoj0tlvKtY2IihDPQHaFm&pid=Api&P=0&h=180",
        "category": "Beverages"
    }
]
with app.app_context():
    MenuItem.query.delete()
    for item in menu_items:
        menu_item=MenuItem(
            name=item['name'],
            description=item['description'],
            price=item['price'],
            image_url=item['image_url'],
            category=item['category']


        )
        db.session.add(menu_item)
    db.session.commit()
    print("Items added successfully")
