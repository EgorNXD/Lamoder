from requests_html import HTMLSession

BASE_URL = 'https://www.lamoda.ru'


def get_page(url):
    print(url)
    page = HTMLSession().get(url)
    print(page)
    return page


def get_catalogsearch_page(query):
    url = f'{BASE_URL}/catalogsearch/result/?q={query}&submit=y&page=1'
    return HTMLSession().get(url)


def get_product_urls(page):
    cards = page.html.find('.x-product-card__link')
    return list(map(lambda card: card.attrs['href'], cards))


def get_product_info(product):
    price = product.html.find('.x-product-card-description__price-single')
    articul = product.attrs['id']
    brand = product.html.find('.x-product-card-description__brand-name')

    return {
        'цена': price.text,
        'артикул': articul.text,
        'брэнд': brand.text
    }


def get_products(page):
    return page.html.find('.x-product-card__card')


query = 'Куртка'

page = get_catalogsearch_page(query)

info = list(map(lambda product: get_product_info(product), get_products(page)))
print(info)


# products = list(map(lambda url: get_page(f'{BASE_URL}{url}'), get_product_urls(page)))
#
# for product in products:
#     print(get_product_info(product))
#
# page = get_page('https://www.lamoda.ru/p/mp002xm1ue5y/clothes-grizman-kurtka-uteplennaya/')
# print(get_products(page))