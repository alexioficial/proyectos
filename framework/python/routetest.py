from coffee import Import

sc = Import(__name__, url_prefix = '/test')

@sc.route('/hola', methods = ['POST'])
def hola(request):
    return request.json_data
