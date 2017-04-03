from flask import *
import mlab
from models.FoodItem import FoodItem
from models.user import User
import os
from werkzeug.utils import *
from flask_login import *
from sessionuser import SessionUser

app = Flask(__name__)

# connect to mlab
mlab.connect()

app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
if not os.path.exists(app.config['UPLOAD_PATH']):
    os.makedirs(app.config['UPLOAD_PATH'])

app.secret_key = 'phamtien'

login_manager = LoginManager()
login_manager.init_app(app)

# admin_user = User()
# admin_user.username = 'admin'
# admin_user.password = 'admin'
# admin_user.save()


@login_manager.user_loader
def user_loader(user_token):
    found_user = User.objects(token=user_token).first()
    if found_user:
        session_user = SessionUser(found_user.id)
        return session_user

girl_list = [
    {
        "src": "http://68.media.tumblr.com/c2b359d90b868247565a37b4f70ea2d9/tumblr_omu6agTv6b1qbd81ro1_1280.jpg",
        "title": "12343 by Đinh Văn Linh ♥",
        "tags": "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography",
        "price": "135. 500 đ"
    },
    {
        "src": "http://68.media.tumblr.com/fdce8d90185f8f38a5f36a69b198a271/tumblr_ojqkfv1h7c1qbd81ro1_1280.jpg",
        "title": "lightstudio | 0966726996 by Leo White | 0966 72 6996 | 0164 960 8794 ♥",
        "tags": "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    },
    {
        "src": "http://68.media.tumblr.com/333c275f13f585bb49a55f9e7b8fa9c8/tumblr_of8kztZ3QA1qbd81ro1_1280.jpg",
        "title": "DSC_2180 by mrSun_vn ♥",
        "tags": "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    },
    {
        "src": "http://68.media.tumblr.com/6707567f4007a0ebb6e342f37692da0b/tumblr_of8kzf8gMp1qbd81ro1_1280.jpg",
        "title": "IMG_7340 by Hải Nguyễn | Tell 0902990341 ♥",
        "tags": "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    }
]

food_list1 = [
    {
        "src": "http://liztraks.com/ltphotography/wp-content/uploads/2016/01/2-1-450x675.jpg",
        "name_food": "Bánh rán chanh vắt khổng lồ",
        "title": "Món bánh rán đậm chất vỉa hè Việt Nam được đưa vào chế biến cùng nguyên liệu tinh túy từ sữa dừa và hoa nhài, tạo nên sự khác biện giữa không gian và thời gian.",
        "price": "135. 500 đ"
    },
    {
        "src": "http://lovelyindeed.com/wp-content/uploads/2016/10/pumpkin-donut-holes-1-450x675.jpg",
        "name_food": "Xiên nướng tẩm bột mỳ Ấn Độ",
        "title": "Được làm từ thịt bò Kobe, xay nhuyễn cùng bột mỳ nhập khẩu nguyên túi từ Ấn Độ tạo nên một hương vị khó cưỡng nổi.",
        "price": "148. 000 đ"
    },
    {
        "src": "http://gapps.pl/wp-content/uploads/2017/01/IMG_0229-450x675.jpg",
        "name_food": "Cà phê trứng Quảng Đông",
        "title": "Không cần nói gì nhiều, chỉ việc nhấc cốc lên và thưởng thức ly cà phê thơm ngon, đậm đà và bổ dưỡng.",
        "price": "102. 000 đ"
    },
    {
        "src": "http://tattebakery.com/wp-content/uploads/2013/10/Q6A2524-450x675.jpg",
        "name_food": "Cupcake Sờ cha beo di",
        "title": "Vị ngọt của bánh, độ ngậy của bơ, hòa quyện cùng vị thơm của dâu, phù hợp với thưởng thức bữa sáng cùng lý cà phê kể trên.",
        "price": "112. 000đ"
    }
    ]
food_list2 = [
    {
        "src": "http://www.jenniephaneufphotography.com/wp-content/uploads/2016/07/Pumpkin-Spice-Donuts-1-450x675.jpg",
        "name_food": "Donuts Australia",
        "title": "ĐÔ NÚT CỦA ÚC, đóng gói và làm nóng trong hộp sắt không bóc hoàn toàn",
        "price": "62. 000 đ"
    },
    {
        "src": "http://www.glorykitchen.com/wp-content/uploads/2017/01/Vegetable-Chicken-and-Orzo-Soup5-450x675.jpg",
        "name_food": "Soup Ve ge tơ bờ lồ",
        "title": "Món súp dân dã được chính các đầu bếp Việt Nam chế biến",
        "price": "160. 000 đ"
    },
    {
        "src": "http://www.jenniephaneufphotography.com/wp-content/uploads/2016/07/Mesquite-Chicken-Tacos-1-450x675.jpg",
        "name_food": "Taco Mexico",
        "title": "Lấy công thức từ dân bản địa của thung lũng Mexico trứ danh, rất khỏ để bỏ qua món này trong thực đơn",
        "price": "300. 000 đ"
    },
    {
        "src": "https://www.legacyoftaste.com/wp-content/uploads/2017/02/TsingtaoSkewerChicken-450x675.jpg",
        "name_food": "Chicken Skewers",
        "title": "Gà xé phay nướng than hồng hoạt tính không khói, nhâm nhi cùng chút bia TSINGTAO từ Thanh Đảo Trung Quốc là khẩu vị tuyệt vời cho thực dân châu Á",
        "price": "250. 000 đ"
    }
]

# for food in food_list2:
#     new_food = FoodItem()
#     new_food.src = food["src"]
#     new_food.title = food["name_food"]
#     new_food.description = food["title"]
#     new_food.save()


@app.route('/')
def hello_world():
    return redirect(url_for("foodblog1"))

number_of_visiter = 0


@app.route('/login1', methods=["GET", "POST"])
def login1():
    if request.method == "GET":
        return render_template("login1.html")
    elif request.method == "POST":
        user = User.objects(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            session_user = SessionUser(user.id)
            user.update(set__token=str(user.id))
            login_user(session_user)

            return redirect(url_for('add_food'))
        else:
            return render_template("login1.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login1'))


@app.route('/login')
def login():
    global number_of_visiter
    number_of_visiter += 1
    return render_template("login.html", girl_list=girl_list, number_visiter=number_of_visiter)


@app.route('/oingonqua')
def oingonqua():
    return render_template("oingonqua.html", girl_list=girl_list)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/css_demo')
def css_demo():
    return render_template("cssdemo.html")


@app.route('/w3cssdemo')
def w3css_demo():
    return render_template("w3cssdemo.html")


@app.route('/foodblog')
def foodblog():
    return render_template("foodblog.html", food_list1=food_list1, food_list2=food_list2)


@app.route('/foodblog1')
def foodblog1():
    return render_template("foodblog1.html", food_list=FoodItem.objects())


@app.route('/addFood', methods=["GET", "POST"])
@login_required
def add_food():
    if request.method == "GET":
        return render_template("addfood.html")
    elif request.method == "POST":
        file = request.files['source']
        if file:
            filename = secure_filename(file.filename)
            if os.path.exists(os.path.join(app.config['UPLOAD_PATH'], filename)):
                name_index = 0
                original_name = filename.rsplit('.', 1)[0]
                original_extension = filename.rsplit('.', 1)[1]
                while os.path.exists(os.path.join(app.config['UPLOAD_PATH'], filename)):
                    name_index += 1
                    filename = "{0} ({1}).{2}".format(original_name, name_index, original_extension)
            file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            new_food = FoodItem()
            new_food.src = url_for('uploaded_file', filename=filename)
            new_food.title = request.form["title"]
            new_food.description = request.form["description"]
            new_food.save()
            return render_template("addfood.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@app.route('/deleteFood', methods=["GET", "POST"])
def delete_food():
    if request.method == "GET":
        return render_template("deletefood.html")
    elif request.method == "POST":
        new_food = FoodItem.objects(title=request.form["title"]).first()
        if new_food is not None:
            new_food.delete()
        return render_template("deletefood.html")


@app.route('/updateFood', methods=["GET", "POST"])
def update_food():
    if request.method == "GET":
        return render_template("updatefood.html")
    elif request.method == "POST":
        new_food = FoodItem.objects(title=request.form["title_old"]).first()
        if new_food is not None:
            new_food.delete()
            new_food = FoodItem()
            new_food.src = request.form["source"]
            new_food.title = request.form["title"]
            new_food.description = request.form["description"]
            new_food.save()
        return render_template("updatefood.html")


if __name__ == '__main__':
    app.run()
