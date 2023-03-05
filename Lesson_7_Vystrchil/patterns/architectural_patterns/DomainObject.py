from patterns.architectural_patterns.CRUDMapper import CRUDMapper


class DomainObject:

    def mark_new(self):
        CRUDMapper.get_current().register_new(self)

    def mark_dirty(self):
        CRUDMapper.get_current().register_dirty(self)

    def mark_removed(self):
        CRUDMapper.get_current().register_removed(self)
