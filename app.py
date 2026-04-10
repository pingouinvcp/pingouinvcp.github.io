import json
import os
import re
import sqlite3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(ROOT_DIR, 'perfumes.db')
PORT = 8000

ARABES_PREFIXES = ('afnan', 'lattafa', 'armaf', 'rasasi', 'french avenue')


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def get_category(perfume: str) -> str:
    normalized = perfume.strip().lower()
    for prefix in ARABES_PREFIXES:
        if normalized.startswith(prefix):
            return 'arabe'
    return 'disenador'


def load_products() -> list[dict]:
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f'Base de datos no encontrada: {DB_PATH}')

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT perfume, precio, imagen1, imagen2 FROM perfumes')
        rows = cursor.fetchall()

    productos = []
    for row in rows:
        perfume = row['perfume']
        producto = {
            'slug': slugify(perfume),
            'perfume': perfume,
            'precio': row['precio'],
            'imagen1': row['imagen1'],
            'imagen2': row['imagen2'],
            'category': get_category(perfume),
        }
        productos.append(producto)
    return productos


class APIRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/api/products':
            self.handle_products()
            return
        if parsed.path == '/api/product':
            self.handle_product(parsed)
            return
        super().do_GET()

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def handle_products(self):
        try:
            productos = load_products()
            self.send_json(productos)
        except Exception as exc:
            self.send_json({'error': str(exc)}, status=500)

    def handle_product(self, parsed):
        query = parse_qs(parsed.query)
        slug = query.get('slug', [''])[0]
        if not slug:
            self.send_json({'error': 'Falta el parámetro slug'}, status=400)
            return

        try:
            productos = load_products()
            producto = next((item for item in productos if item['slug'] == slug), None)
            if producto is None:
                self.send_json({'error': 'Producto no encontrado'}, status=404)
                return
            self.send_json(producto)
        except Exception as exc:
            self.send_json({'error': str(exc)}, status=500)

    def log_message(self, format, *args):
        # Evitar demasiado logging en consola
        return


if __name__ == '__main__':
    os.chdir(ROOT_DIR)
    server = ThreadingHTTPServer(('0.0.0.0', PORT), APIRequestHandler)
    print(f'Serving on http://localhost:{PORT}')
    print('Presiona Ctrl+C para detener')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print('\nServidor detenido')
import os
import re
import sqlite3
from flask import Flask, jsonify, request, send_from_directory, abort

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'perfumes.db')

app = Flask(__name__, static_folder=None)
app.config['JSON_AS_ASCII'] = False

DESIGNER_BRANDS = [
    'dior', 'ga ', 'giorgio armani', 'versace', 'xerjoff', 'chanel', 'paco rabanne',
    'yves saint laurent', 'carolina herrera', 'jean paul gaultier', 'montblanc',
    'ralph lauren', 'calvin klein', 'valentino'
]
ARAB_BRANDS = [
    'afnan', 'lattafa', 'armaf', 'rasasi', 'french avenue'
]


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def slugify(value):
    slug = re.sub(r'[^a-z0-9]+', '-', value.lower())
    return slug.strip('-')


def determine_category(name):
    lower = name.lower()
    for brand in DESIGNER_BRANDS:
        if brand in lower:
            return 'disenador'
    for brand in ARAB_BRANDS:
        if brand in lower:
            return 'arabe'
    return 'disenador'


def load_products():
    with get_db_connection() as conn:
        rows = conn.execute('SELECT perfume, precio, imagen1, imagen2 FROM perfumes').fetchall()
        products = []
        for row in rows:
            name = row['perfume']
            products.append({
                'slug': slugify(name),
                'perfume': name,
                'precio': row['precio'],
                'imagen1': row['imagen1'],
                'imagen2': row['imagen2'],
                'category': determine_category(name)
            })
        return products


@app.route('/api/products')
def api_products():
    products = load_products()
    return jsonify(products)


@app.route('/api/product')
def api_product():
    product_id = request.args.get('id') or request.args.get('slug') or request.args.get('perfume')
    if not product_id:
        abort(400, 'Missing product id')
    product_id = product_id.strip().lower()
    products = load_products()
    product = next((p for p in products if p['slug'] == product_id or p['perfume'].lower() == product_id), None)
    if not product:
        abort(404)
    return jsonify(product)


@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/<path:filename>')
def serve_file(filename):
    if os.path.exists(os.path.join(BASE_DIR, filename)):
        return send_from_directory(BASE_DIR, filename)
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
