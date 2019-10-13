import re
from django.shortcuts import render, get_object_or_404, redirect

from .models import Item

def item_list(request):
    items = Item.objects.all()
    # 키값이 'q'로 지정된 값이 없으면 None이 반환됨
    q = request.GET.get('q', '')  # 'q'로 지정된 값이 없으면 '' 반환
    if q:  # q가 널 아니면 qs에 filter 조건 추가
        items = items.filter(name__icontains=q)
    return render(request, 'forSale/item_list.html', {
        'item_list': items,
        'q': q, })


# 상가 매물 목록 수정 삭제
def item_new(request, item=None):
    error_list = []
    initial = {}

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        name = data.get('name')
        location = data.get('location')
        area = data.get('area')
        sector = data.get('sector')
        option = data.get('option')
        tel = data.get('tel')
        floor = data.get('floor')
        desc = data.get('desc')
        price = data.get('price')
        photo = files.get('photo')


        # 유효성 검사
        if len(name) == 0:
            error_list.append('title을 1글자 이상 입력해주세요.')

        if re.match(r'^[\da-zA-Z\s]+$', desc):
            error_list.append('한글을 입력해주세요.')

        if not error_list:
            # 저장 시도
            if item is None:
                item = Item()

            item.name = name
            item.location = location
            item.area = area
            item.sector = sector
            item.option = option
            item.tel = tel
            item.floor = floor
            item.desc = desc
            item.price = price

            if photo:
                item.photo.save(photo.name, photo, save=False)

            try:
                item.save()
            except Exception as e:
                error_list.append(e)
            else:
                # return redirect(item)  # item.get_absolute_url 호출됨
                return redirect('forSale:item_list')

        initial = {
            'name': name,
            'location': location,
            'area': area,
            'sector': sector,
            'option': option,
            'tel': tel,
            'floor': floor,
            'desc': desc,
            'price': price,
            'photo': photo,
        }
    else:
        if item is not None:
            initial = {
                'name': item.name,
                'location': item.location,
                'area': item.area,
                'sector': item.sector,
                'option': item.option,
                'tel': item.tel,
                'floor': item.floor,
                'desc': item.desc,
                'price': item.price,
                'photo': item.photo,
            }
    return render(request, 'forSale/item_form.html', {
        'error_list': error_list,
        'initial': initial,
    })

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return item_new(request, item)


def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('forSale:item_list')





def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'forSale/item_detail.html',
                  {'item': item})

