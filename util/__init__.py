from django.core.paginator import Paginator, InvalidPage, EmptyPage

def paginate(request, object_list, *args, **kwargs):
    paginator = Paginator(object_list, *args, **kwargs)

    # Make sure page request is an int. If not, deliver first page.
    try:
        page_num = int(request.GET.get('page', '1'))
    except ValueError:
        page_num = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        page = paginator.page(page_num)
    except (EmptyPage, InvalidPage):
        page = paginator.page(paginator.num_pages)

    setattr(page.object_list,'paginator_page',page)

    return page.object_list


