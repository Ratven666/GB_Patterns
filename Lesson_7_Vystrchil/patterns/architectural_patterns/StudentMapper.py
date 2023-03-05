from patterns.architectural_patterns.DB_Exceptions import RecordNotFoundException, DbCommitException, DbUpdateException, \
    DbDeleteException
from patterns.creational_patterns.Users import Student


class StudentMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.table_name = "students"

    def all(self):
        statement = f"SELECT * from {self.table_name}"
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id_, name = item
            student = Student(name)
            student.id_ = id_
            result.append(student)
        return result

    def find_by_id(self, id_):
        statement = f"SELECT id, name FROM {self.table_name} WHERE id=?"
        self.cursor.execute(statement, (id_,))
        result = self.cursor.fetchone()
        if result:
            return Student(*result)
        else:
            raise RecordNotFoundException(f"record with id={id_} not found")

    def insert(self, obj):
        statement = f"INSERT INTO {self.table_name} (name) VALUES (?)"
        self.cursor.execute(statement, (obj.name,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, obj):
        statement = f"UPDATE {self.table_name} SET name=? WHERE id=?"

        self.cursor.execute(statement, (obj.name, obj.id))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, obj):
        statement = f"DELETE FROM {self.table_name} WHERE id=?"
        self.cursor.execute(statement, (obj.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)
