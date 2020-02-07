from rest_framework.views import APIView
from rest_framework.response import Response
    

class CharCount(APIView):
    """
    View to get the length of a given text.
    """

    def get(self, request, *args, **kwargs):
        """
        Return the number of characters
        """
        text = request.GET.get("text", "")
        return Response({"count": len(text)})