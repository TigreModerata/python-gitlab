from typing import Any, cast, Union

from gitlab.base import RequiredOptional, RESTManager, RESTObject
from gitlab.mixins import CRUDMixin, ObjectDeleteMixin, SaveMixin

__all__ = [
    "GroupBoardList",
    "GroupBoardListManager",
    "GroupBoard",
    "GroupBoardManager",
    "ProjectBoardList",
    "ProjectBoardListManager",
    "ProjectBoard",
    "ProjectBoardManager",
]


class GroupBoardList(SaveMixin, ObjectDeleteMixin, RESTObject):
    pass


class GroupBoardListManager(CRUDMixin, RESTManager):
    _path = "/groups/%(group_id)s/boards/%(board_id)s/lists"
    _obj_cls = GroupBoardList
    _from_parent_attrs = {"group_id": "group_id", "board_id": "id"}
    _create_attrs = RequiredOptional(required=("label_id",))
    _update_attrs = RequiredOptional(required=("position",))

    def get(
        self, id: Union[str, int], lazy: bool = False, **kwargs: Any
    ) -> GroupBoardList:
        return cast(GroupBoardList, super().get(id=id, lazy=lazy, **kwargs))


class GroupBoard(SaveMixin, ObjectDeleteMixin, RESTObject):
    lists: GroupBoardListManager


class GroupBoardManager(CRUDMixin, RESTManager):
    _path = "/groups/%(group_id)s/boards"
    _obj_cls = GroupBoard
    _from_parent_attrs = {"group_id": "id"}
    _create_attrs = RequiredOptional(required=("name",))

    def get(self, id: Union[str, int], lazy: bool = False, **kwargs: Any) -> GroupBoard:
        return cast(GroupBoard, super().get(id=id, lazy=lazy, **kwargs))


class ProjectBoardList(SaveMixin, ObjectDeleteMixin, RESTObject):
    pass


class ProjectBoardListManager(CRUDMixin, RESTManager):
    _path = "/projects/%(project_id)s/boards/%(board_id)s/lists"
    _obj_cls = ProjectBoardList
    _from_parent_attrs = {"project_id": "project_id", "board_id": "id"}
    _create_attrs = RequiredOptional(required=("label_id",))
    _update_attrs = RequiredOptional(required=("position",))

    def get(
        self, id: Union[str, int], lazy: bool = False, **kwargs: Any
    ) -> ProjectBoardList:
        return cast(ProjectBoardList, super().get(id=id, lazy=lazy, **kwargs))


class ProjectBoard(SaveMixin, ObjectDeleteMixin, RESTObject):
    lists: ProjectBoardListManager


class ProjectBoardManager(CRUDMixin, RESTManager):
    _path = "/projects/%(project_id)s/boards"
    _obj_cls = ProjectBoard
    _from_parent_attrs = {"project_id": "id"}
    _create_attrs = RequiredOptional(required=("name",))

    def get(
        self, id: Union[str, int], lazy: bool = False, **kwargs: Any
    ) -> ProjectBoard:
        return cast(ProjectBoard, super().get(id=id, lazy=lazy, **kwargs))
