from flask import Flask,render_template,request,redirect,url_for
from database import db , MenuItem,Message
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///royalbites.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)
@app.route('/setup')
def setup():
    db.create_all()
    return 'Database Created successfully'

@app.route('/admin')
def admin():
    menu_items=MenuItem.query.all()
    messages=Message.query.all()
    menu_count=len(menu_items)
    message_count=len(messages)
    return render_template('admin.html',menu_items=menu_items,messages=messages,menu_count=menu_count,message_count=message_count)

@app.route('/admin/add',methods=['POST'])
def admin_add():
    name=request.form.get('name')
    description=request.form.get('description')
    price=request.form.get('price')
    image_url=request.form.get('image_url')
    category=request.form.get('category')
    new_item=MenuItem(name=name,description=description,price=price,image_url=image_url,category=category)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/admin/delete/<int:id>',methods=['POST'])
def admin_delete(id):
    item=db.session.get(MenuItem,id)
    if item:
        db.session.delete(item)
        db.session.commit()
        print(f"Deleted item: {id}")  
        return redirect(url_for('admin'))
    return "Item not  found",404

@app.route('/check')
def check():
    items=MenuItem.query.all()
    result=""
    for item in items:
        result += f"{item.name} - ₹{item.price} ({item.category})<br>"

    return result
@app.route('/contact',methods=['POST'])
def contact():
    content=request.form['message']
    if content:
        new_message=Message(content=content)
        db.session.add(new_message)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/messages')
def messages():
    all_messages=Message.query.order_by(Message.timestamp.desc()).all()
    result = f"Total messages: {len(all_messages)}<br><br>"
    for msg in all_messages:
        result += f"Message: {msg.content}<br>"
        result += f"Time: {msg.timestamp}<br><br>"
    return result

    
@app.route('/')
def home():
    menu_items=MenuItem.query.all()
    return render_template('index.html',menu_items=menu_items)
if __name__=='__main__':
    app.run(debug=True)