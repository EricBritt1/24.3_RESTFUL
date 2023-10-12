from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="lemon",
    size="large",
    rating=9,
    image="https://i2.wp.com/lifemadesimplebakes.com/wp-content/uploads/2017/05/Lemon-Cupcakes-with-Lemon-Cream-Cheese-Frosting.jpg"
)

c2 = Cupcake(
    flavor="Red Velvet",
    size = "medium",
    rating=10,
    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrp5nUDWrkMHldT2rghFt9gBg_1wTBEl_g8Q&usqp=CAU"
)


c3 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c4 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)



db.session.add_all([c1, c2, c3, c4])
db.session.commit()