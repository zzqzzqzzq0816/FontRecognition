import os
import time


from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

def tran_name(image):
    curr_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    suffix = image.name.split('.')[-1].replace('"', '')
    image.name = curr_time + '.' + suffix

def save_image(image):
    image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')
    full_path = image_path + '/' + image.name
    with open(full_path, 'wb') as f:
        for c in image.chunks():
            f.write(c)
    return full_path

@csrf_exempt
@api_view(['POST'])
def get_recognition_result(request):
    response = {}
    try:
        image = request.data['image']
        tran_name(image)
        full_path = save_image(image)

        response['msg'] = '成功！'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return Response(response)