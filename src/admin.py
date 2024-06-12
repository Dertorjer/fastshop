from sqladmin import ModelView
from src.company.models.sqlalchemy_models import Basket

class BasketAdmin(ModelView, model=Basket):
    icon = "/static/icons/chart-simple-solid.svg"

    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]

    column_searchable_list = [Basket.user_id, Basket.status]

    category = "Shop Management"

    column_labels = {
        Basket.id: "ID",
        Basket.user_id: "User ID",
        Basket.price: "Price",
        Basket.status: "Status"
    }
