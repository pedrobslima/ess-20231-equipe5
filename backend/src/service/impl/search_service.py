from schemas.response import HTTPResponses, HttpResponseModel, Optional
from service.meta.item_service_meta import ItemServiceMeta
from db.server import server_ as db

class SearchService():

    @staticmethod
    def search_for_tags(tags) -> HttpResponseModel:
        """Get posts that match the multiple tags"""
        
        if (len(tags) == 0) or (len(tags) == 1 and (tags[0] == '' or tags[0] == None)):
            return HttpResponseModel(
                message="Empty Query values",
                status_code=400,
            )


        item = db.search_for_tags(tags)
        if len(item['matches']) == 0:
            return HttpResponseModel(
                message='No Content',
                status_code=204,
                #data=item,
            )
        return HttpResponseModel(
                message=HTTPResponses.ITEM_FOUND().message,
                status_code=HTTPResponses.ITEM_FOUND().status_code,
                data=item,
            )
    