from jinja2 import Environment, FileSystemLoader
import urllib.parse
import http.server
import json
import os

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request('GET')

    def do_POST(self):
        self.handle_request('POST')

    def handle_request(self, http_method):
        parsed_path = urllib.parse.urlparse(self.path)

        if parsed_path.path.startswith('/static/'):
            self.serve_static_file(parsed_path.path)
            return

        if parsed_path.path in Coffee.routes:
            if http_method in Coffee.routes[parsed_path.path]:
                handler = Coffee.routes[parsed_path.path][http_method]
                request_instance = Request(self)
                response = handler(request_instance)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                if isinstance(response, dict):  # Verificar si la respuesta es un diccionario
                    response = json.dumps(response)  # Convertir a JSON

                self.wfile.write(response.encode())
            else:
                self.send_response(405)  # Method Not Allowed
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Method not allowed</h1></body></html>')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>Page not found</h1></body></html>')
    
    def serve_static_file(self, file_path):
        file_path = file_path.lstrip('/static/')
        full_file_path = os.path.join('static', file_path)

        if os.path.exists(full_file_path) and os.path.isfile(full_file_path):
            with open(full_file_path, 'rb') as file:
                content = file.read()

            self.send_response(200)
            self.send_header('Content-type', 'application/javascript')
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>File not found</h1></body></html>')

class Request:
    def __init__(self, http_handler):
        self.method = http_handler.command
        self.headers = http_handler.headers
        self.path = http_handler.path
        self.body = None

        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            self.body = http_handler.rfile.read(content_length)
            try:
                self.json_data = json.loads(self.body.decode('utf-8'))
            except json.JSONDecodeError:
                self.json_data = {}

class Import:
    def __init__(self, name, template_folder = 'templates', url_prefix = ''):
        self.name = name
        self.template_folder = template_folder
        self.url_prefix = url_prefix
        self.routes = {}

    def route(self, path, methods = ['GET']):
        def decorator(handler_func):
            for method in methods:
                self.routes[method] = (self.url_prefix + path, handler_func)
            return handler_func
        return decorator

    def render(self, file_name, context=None):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(current_dir, str(self.template_folder))
        file_loader = FileSystemLoader(template_dir)
        env = Environment(loader=file_loader)

        template = env.get_template(file_name)
        rendered_template = template.render(context or {})

        return rendered_template

class Coffee:
    routes = {}
    def __init__(self, name, template_folder = 'templates'):
        self.name = name
        self.template_folder = template_folder

    def drink(self, host = 'localhost', port = 5000):
        server = http.server.HTTPServer((host, port), RequestHandler)
        print(f'Server running on http://{host}:{port}')
        server.serve_forever()

    def render(self, file_name, context=None):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(current_dir, str(self.template_folder))
        file_loader = FileSystemLoader(template_dir)
        env = Environment(loader=file_loader)

        template = env.get_template(file_name)
        rendered_template = template.render(context or {})

        return rendered_template

    @classmethod
    def route(cls, path, methods = ['GET']):
        def decorator(handler_func):
            if path not in cls.routes:
                cls.routes[path] = {}
            for method in methods:
                cls.routes[path][method] = handler_func
            return handler_func
        return decorator
    
    def import_coffee(self, import_coffee_instance):
        for method, (path, handler_func) in import_coffee_instance.routes.items():
            if path not in self.routes:
                self.routes[path] = {}
            self.routes[path][method] = handler_func

