from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.item_service_meta import ItemServiceMeta
from src.db.__init__ import database as db

class ItemService(ItemServiceMeta):

    @staticmethod
    def get_item(item_id: str, ctg: str) -> HttpResponseModel:
        """Get item by id and category method implementation"""
        item = db.get_item(item_id, ctg)
        if not item:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=item,
            )
    
    @staticmethod
    def get_comments(post_id: str) -> HttpResponseModel:
        """Get comments method implementation"""
        items = db.get_all_items('items')
        if not items:
            return HttpResponseModel(
                message=HTTPResponses.ITEM_NOT_FOUND().message,
                status_code=HTTPResponses.ITEM_NOT_FOUND().status_code,
            )
        
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=items,
            )
    
    # TODO: implement other methods (create, update, delete)