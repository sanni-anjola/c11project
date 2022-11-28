class BasketSize:
    def __init__(self, size: int) -> None:
        self.size = size
        self.basket = []

    def add_item(self, item: str) -> None:
        self.basket.append(item)
        if len(self.basket) > self.size:
            self.basket.pop(0)

