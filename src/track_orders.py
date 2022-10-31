from typing import Counter


class TrackOrders:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        new_order = {"customer": customer, "order": order, "day": day}
        return self._data.append(new_order)

    def get_most_ordered_dish_per_customer(self, customer):
        foods = []
        for rows in self._data:
            if rows["customer"] == customer:
                foods.append(rows["order"])
        return Counter(foods).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        foods_in_general = set()
        foods_of_customer = set()
        for rows in self._data:
            foods_in_general.add(rows["order"])
            if rows["customer"] == customer:
                foods_of_customer.add(rows["order"])
        return foods_in_general.difference(foods_of_customer)

    def get_days_never_visited_per_customer(self, customer):
        days_in_general = set()
        days_of_customer = set()
        for rows in self._data:
            days_in_general.add(rows["day"])
            if rows["customer"] == customer:
                days_of_customer.add(rows["day"])
        return days_in_general.difference(days_of_customer)

    def get_busiest_day(self):
        day_of_busiet = []
        for rows in self._data:
            day_of_busiet.append(rows["day"])
        return Counter(day_of_busiet).most_common(1)[0][0]

    def get_least_busy_day(self):
        least_busy_day = []
        for rows in self._data:
            least_busy_day.append(rows["day"])
        return Counter(least_busy_day).most_common()[-1][0]
