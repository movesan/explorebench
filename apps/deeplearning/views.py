from rest_framework.views import APIView
from rest_framework.response import Response


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        good_list = []
        i = 0
        while i < 10:
            json_dict = {
                'name': "商品" + str(i),
                'market_price': i * 10,
                '销量排名': i * 5
            }
            i += 1
            good_list.append(json_dict)

        return Response(good_list)
