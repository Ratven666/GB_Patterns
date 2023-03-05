from threading import local


class CRUDMapper:
    current = local()

    def __init__(self):
        self.new_objects = []
        self.dirty_objects = []
        self.removed_objects = []
        self.MapperRegistry = None

    def set_mapper_registry(self, mapper_registry):
        self.MapperRegistry = mapper_registry

    def register_new(self, obj):
        self.new_objects.append(obj)

    def register_dirty(self, obj):
        self.dirty_objects.append(obj)

    def register_removed(self, obj):
        self.removed_objects.append(obj)

    def commit(self):
        self.insert_new()
        self.update_dirty()
        self.delete_removed()

        self.new_objects.clear()
        self.dirty_objects.clear()
        self.removed_objects.clear()

    def insert_new(self):
        print(self.new_objects)
        for obj in self.new_objects:
            print(f"Вывожу {self.MapperRegistry}")
            self.MapperRegistry.get_mapper(obj).insert(obj)

    def update_dirty(self):
        for obj in self.dirty_objects:
            self.MapperRegistry.get_mapper(obj).update(obj)

    def delete_removed(self):
        for obj in self.removed_objects:
            self.MapperRegistry.get_mapper(obj).delete(obj)

    @classmethod
    def new_current(cls):
        cls.set_current(CRUDMapper())

    @classmethod
    def set_current(cls, crud_mapper):
        cls.current.crud_mapper = crud_mapper

    @classmethod
    def get_current(cls):
        try:
            return cls.current.crud_mapper
        except AttributeError:
            cls.new_current()
            return cls.current.crud_mapper
