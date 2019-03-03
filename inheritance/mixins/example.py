class Field:
    pass


class SoftDeleteMixin:
    deleted_at = Field()

    def delete(self):
        # soft delete
        pass

    def get(self):
        # get all records not soft deleted
        pass


class BaseModel:
    def delete(self):
        # delete
        pass

    def get(self):
        # get
        pass


class Model(SoftDeleteMixin, BaseModel):
    pass
