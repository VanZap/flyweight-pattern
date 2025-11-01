import time

class Order:
    def __init__(self, name):
        self.name = name
        print(f"Cooking {name} order...")
        time.sleep(3)  # simulate time-consuming creation
        print(f"Done cooking {name} order!")

class OrderFactory:
    _cache = {}

    @classmethod
    def get_order(cls, name):
        if name not in cls._cache:
            cls._cache[name] = Order(name)
        return cls._cache[name]

class RestaurantView:
    def show_order(self, order):
        print(f"Order for: {order.name} | ID: {id(order)}\n")

    def show_message(self, message):
        print(message)

class RestaurantController:
    def __init__(self):
        self.view = RestaurantView()

    def create_order(self, food_name):
        order = OrderFactory.get_order(food_name)
        self.view.show_order(order)
        return order

if __name__ == "__main__":
    controller = RestaurantController()
    pizza1 = controller.create_order("Pizza")
    pizza2 = controller.create_order("Pizza")
    pizza3 = controller.create_order("Pizza")

    burger1 = controller.create_order("Burger")
    burger2 = controller.create_order("Burger")
    burger3 = controller.create_order("Burger")