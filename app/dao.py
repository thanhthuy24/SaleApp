def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },
        {
            'id': 2,
            'name': 'Laptop'
        },
        {
            'id': 3,
            'name': 'PC'
        }
    ]


def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'iPhone 13',
        'price': 20000000,
        'image': 'https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain'
    },
        {
            'id': 2,
            'name': 'Laptop Asus Vivobook',
            'price': 19980000,
            'image': 'https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain'

        },
        {
            'id': 3,
            'name': 'SamSung S20 FE',
            'price': 16000000,
            'image': 'https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain'

        },
        {
            'id': 4,
            'name': 'iPhone 15',
            'price': 30000000,
            'image': 'https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain'

        },
        {
            'id': 5,
            'name': 'iPhone 14',
            'price': 20000000,
            'image': 'https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain'
        },
        {
            'id': 6,
            'name': 'Laptop MSI',
            'price': 19980000,
            'image': 'https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain'

        },
        {
            'id': 7,
            'name': 'SamSung Note 20',
            'price': 16000000,
            'image': 'https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain'

        },
        {
            'id': 8,
            'name': 'iPhone 15 Pro Max',
            'price': 30000000,
            'image': 'https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain'

        }
    ]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
