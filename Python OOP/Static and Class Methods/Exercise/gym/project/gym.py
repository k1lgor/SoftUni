from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        self.__add_entity(self.customers, customer)

    def add_trainer(self, trainer: Trainer):
        self.__add_entity(self.trainers, trainer)

    def add_equipment(self, equipment: Equipment):
        self.__add_entity(self.equipment, equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_entity(self.plans, plan)

    def add_subscription(self, subscription: Subscription):
        self.__add_entity(self.subscriptions, subscription)

    def subscription_info(self, subscription_id):
        sub = self.__find_entity(self.subscriptions, subscription_id)
        customer = self.__find_entity(self.customers, sub.customer_id)
        trainer = self.__find_entity(self.trainers, sub.trainer_id)
        plan = self.__find_entity(self.plans, sub.exercise_id)
        equipment = self.__find_entity(self.equipment, plan.equipment_id)

        return f'{repr(sub)}\n' \
               f'{repr(customer)}\n' \
               f'{repr(trainer)}\n' \
               f'{repr(equipment)}\n' \
               f'{repr(plan)}\n'

    def __add_entity(self, collection, entity):
        if entity in collection:
            return
        collection.append(entity)

    def __find_entity(self, collection, entity_id):
        for entity in collection:
            if entity_id == entity.id:
                return entity
