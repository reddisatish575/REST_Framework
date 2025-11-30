
from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'  # Allow client to set page size
    page_query_param = 'page-num'  # Page query parameter 
    max_page_size = 1  # Maximum limit for page size   

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'count': self.page.paginator.count,
                'page_size': self.get_page_size(self.request),
                'results': data
            },
        })