from rest_framework.generics import ListAPIView

from .models import Page, Block
from .serializers import AllPageSerializer, BlockSerializer


class AllPagesViewSet(ListAPIView):
    """Список страниц"""
    queryset = Page.objects.all()
    serializer_class = AllPageSerializer


class DetailPageView(ListAPIView):
    """Детальная страница"""
    serializer_class = BlockSerializer

    def get_queryset(self):
        page_object = Block.objects.filter(pageblock__page__slug=self.kwargs.get("slug"))
        for block in page_object:
            block.shows_number += 1
            block.save()
        return page_object
