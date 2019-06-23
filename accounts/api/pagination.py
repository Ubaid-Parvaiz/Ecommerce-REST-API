from rest_framework import pagination

class CustomLimitPagination(pagination.LimitOffsetPagination):
	max_limit = 30
	default_limit = 10
	limit_query_param = "q"