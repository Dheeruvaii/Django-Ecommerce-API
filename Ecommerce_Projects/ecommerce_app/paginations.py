from  rest_framework.pagination import BasePagination,PageNumberPagination
from rest_framework.response import  Response



default_page=1
default_page_size=10

class CustomPagination(PageNumberPagination):
    page = default_page
    page_size = default_page_size
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', default_page)),
            'page_size': int(self.request.GET.get('page_size', default_page_size)),
            'results': data
        })