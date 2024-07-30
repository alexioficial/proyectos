from coffee import Coffee

coffee = Coffee(__name__)

@coffee.route('/')
def index(request):
    return coffee.render('index.html')

from routetest import sc as routetest

coffee.import_coffee(routetest)

if __name__ == '__main__':
    coffee.drink()