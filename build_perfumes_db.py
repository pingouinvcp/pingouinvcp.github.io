import sqlite3

PRODUCTOS = [
    # Árabes
    {
        'perfume': 'Afnan 9PM',
        'precio': 69000,
        'imagen1': 'https://recal.com.ar/uploads/AFNAN%209%20PM%20MEN%20EDP%20X%20100%20ML.-01.jpg',
        'imagen2': 'https://via.placeholder.com/400x400?text=Afnan+9PM',
    },
    {
        'perfume': 'Lattafa Asad Bourbon',
        'precio': 99000,
        'imagen1': 'https://acdn-us.mitiendanube.com/stores/003/226/824/products/1024-x-1024-px-2025-05-04t225835-636-487a509fe4bbb3bd6317464103199324-1024-1024.webp',
        'imagen2': 'https://via.placeholder.com/400x400?text=Lattafa+Asad+Bourbon',
    },
    {
        'perfume': 'Armaf Mandarin Sky',
        'precio': 69000,
        'imagen1': 'https://cdnx.jumpseller.com/matis1/image/67764697/resize/1000/1000?1758559039',
        'imagen2': 'https://via.placeholder.com/400x400?text=Armaf+Mandarin+Sky',
    },
    {
        'perfume': 'Rasasi Hawas Ice',
        'precio': 109000,
        'imagen1': 'https://http2.mlstatic.com/D_Q_NP_724947-MLU74163301315_012024-O.webp',
        'imagen2': 'https://via.placeholder.com/400x400?text=Rasasi+Hawas+Ice',
    },
    {
        'perfume': 'French Avenue Vulcan Feu',
        'precio': 99000,
        'imagen1': 'https://fragrances.com.ng/media/catalog/product/cache/0daeb07bb1d294c1f281fab47369d56a/f/r/french_avenue_vulcan_feu-1.jpg',
        'imagen2': 'https://via.placeholder.com/400x400?text=French+Avenue+Vulcan+Feu',
    },
    {
        'perfume': 'Lattafa Khamrah',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Khamrah',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Khamrah+2',
    },
    {
        'perfume': 'Lattafa Khamrah Qahwa',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Khamrah+Qahwa',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Khamrah+Qahwa+2',
    },
    {
        'perfume': 'Lattafa Asad',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Asad',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Asad+2',
    },
    {
        'perfume': 'Lattafa Bade\'e Al Oud For Glory',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Badee+Al+Oud',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Badee+Al+Oud+2',
    },
    {
        'perfume': 'Lattafa Fakhar Black',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Fakhar+Black',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Fakhar+Black+2',
    },
    {
        'perfume': 'Lattafa Yara Rosa',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Yara+Rosa',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Yara+Rosa+2',
    },
    {
        'perfume': 'Lattafa Yara Moi',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Yara+Moi',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Yara+Moi+2',
    },
    {
        'perfume': 'Lattafa Yara Tous',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Yara+Tous',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Yara+Tous+2',
    },
    {
        'perfume': 'Lattafa Nebras',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Nebras',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Nebras+2',
    },
    {
        'perfume': 'Lattafa Qaed Al Fursan',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Qaed+Al+Fursan',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Qaed+Al+Fursan+2',
    },
    {
        'perfume': 'Lattafa Maahir Legacy',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Lattafa+Maahir+Legacy',
        'imagen2': 'https://via.placeholder.com/300x300?text=Lattafa+Maahir+Legacy+2',
    },
    {
        'perfume': 'Armaf Club De Nuit Intense EDT',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Intense+EDT',
        'imagen2': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Intense+EDT+2',
    },
    {
        'perfume': 'Armaf Club De Nuit Intense Parfum',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Intense+Parfum',
        'imagen2': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Intense+Parfum+2',
    },
    {
        'perfume': 'Armaf Club De Nuit Sillage',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Sillage',
        'imagen2': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Sillage+2',
    },
    {
        'perfume': 'Armaf Club De Nuit Milestone',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Milestone',
        'imagen2': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Milestone+2',
    },
    {
        'perfume': 'Armaf Club De Nuit Iconic',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Iconic',
        'imagen2': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Iconic+2',
    },
    {
        'perfume': 'Armaf Club De Nuit Untold',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Untold',
        'imagen2': 'https://via.placeholder.com/300x300?text=Armaf+Club+De+Nuit+Untold+2',
    },
    {
        'perfume': 'Rasasi Hawas For Him',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Rasasi+Hawas+For+Him',
        'imagen2': 'https://via.placeholder.com/300x300?text=Rasasi+Hawas+For+Him+2',
    },
    {
        'perfume': 'Rasasi Hawas Fire',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Rasasi+Hawas+Fire',
        'imagen2': 'https://via.placeholder.com/300x300?text=Rasasi+Hawas+Fire+2',
    },
    {
        'perfume': 'Rasasi Hawas Black',
        'precio': 85000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Rasasi+Hawas+Black',
        'imagen2': 'https://via.placeholder.com/300x300?text=Rasasi+Hawas+Black+2',
    },
    # Diseñador
    {
        'perfume': 'Dior Sauvage EDP',
        'precio': 390000,
        'imagen1': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSC6GMkwrWD0vMzMCOMdC3lH1K-PtsbUwzjSg&s',
        'imagen2': 'https://via.placeholder.com/400x400?text=Dior+Sauvage+EDP',
    },
    {
        'perfume': 'GA Stronger With You EDP',
        'precio': 299000,
        'imagen1': 'https://yauras.cl/cdn/shop/files/Disenosintitulo_4_55dc84be-2355-431f-b845-2eba1b643a03_700x700.jpg?v=1764006452',
        'imagen2': 'https://via.placeholder.com/400x400?text=GA+Stronger+With+You+EDP',
    },
    {
        'perfume': 'JP Gaultier Le Male Elixir',
        'precio': 279000,
        'imagen1': 'https://felix.com.pa/cdn/shop/files/1086-65189083_2_600x.jpg?v=1729275283',
        'imagen2': 'https://via.placeholder.com/400x400?text=JP+Gaultier+Le+Male+Elixir',
    },
    {
        'perfume': 'Versace Eros EDT',
        'precio': 169000,
        'imagen1': 'https://nextcell.com.ar/wp-content/uploads/2024/12/D_Q_NP_851229-MLA46088840723_052021-O.webp',
        'imagen2': 'https://via.placeholder.com/400x400?text=Versace+Eros+EDT',
    },
    {
        'perfume': 'Xerjoff Erba Pura',
        'precio': 569000,
        'imagen1': 'https://http2.mlstatic.com/D_970456-MLA98385992798_112025-C.jpg',
        'imagen2': 'https://via.placeholder.com/400x400?text=Xerjoff+Erba+Pura',
    },
    {
        'perfume': 'Chanel Bleu De Chanel EDT',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Chanel+Bleu+De+Chanel+EDT',
        'imagen2': 'https://via.placeholder.com/300x300?text=Chanel+Bleu+De+Chanel+EDT+2',
    },
    {
        'perfume': 'Chanel Bleu De Chanel Parfum',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Chanel+Bleu+De+Chanel+Parfum',
        'imagen2': 'https://via.placeholder.com/300x300?text=Chanel+Bleu+De+Chanel+Parfum+2',
    },
    {
        'perfume': 'Chanel Coco Mademoiselle',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Chanel+Coco+Mademoiselle',
        'imagen2': 'https://via.placeholder.com/300x300?text=Chanel+Coco+Mademoiselle+2',
    },
    {
        'perfume': 'Chanel N°5',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Chanel+N5',
        'imagen2': 'https://via.placeholder.com/300x300?text=Chanel+N5+2',
    },
    {
        'perfume': 'Dior Sauvage EDT',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Dior+Sauvage+EDT',
        'imagen2': 'https://via.placeholder.com/300x300?text=Dior+Sauvage+EDT+2',
    },
    {
        'perfume': 'Dior Sauvage Elixir',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Dior+Sauvage+Elixir',
        'imagen2': 'https://via.placeholder.com/300x300?text=Dior+Sauvage+Elixir+2',
    },
    {
        'perfume': 'Dior Miss Dior',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Dior+Miss+Dior',
        'imagen2': 'https://via.placeholder.com/300x300?text=Dior+Miss+Dior+2',
    },
    {
        'perfume': 'Dior J\'adore',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Dior+Jadore',
        'imagen2': 'https://via.placeholder.com/300x300?text=Dior+Jadore+2',
    },
    {
        'perfume': 'Dior Fahrenheit',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Dior+Fahrenheit',
        'imagen2': 'https://via.placeholder.com/300x300?text=Dior+Fahrenheit+2',
    },
    {
        'perfume': 'Giorgio Armani Acqua Di Gio EDP',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Giorgio+Armani+Acqua+Di+Gio+EDP',
        'imagen2': 'https://via.placeholder.com/300x300?text=Giorgio+Armani+Acqua+Di+Gio+EDP+2',
    },
    {
        'perfume': 'Giorgio Armani Acqua Di Gio Profondo',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Giorgio+Armani+Acqua+Di+Gio+Profondo',
        'imagen2': 'https://via.placeholder.com/300x300?text=Giorgio+Armani+Acqua+Di+Gio+Profondo+2',
    },
    {
        'perfume': 'Giorgio Armani Stronger With You',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Giorgio+Armani+Stronger+With+You',
        'imagen2': 'https://via.placeholder.com/300x300?text=Giorgio+Armani+Stronger+With+You+2',
    },
    {
        'perfume': 'Giorgio Armani Stronger With You Intensely',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Giorgio+Armani+Stronger+With+You+Intensely',
        'imagen2': 'https://via.placeholder.com/300x300?text=Giorgio+Armani+Stronger+With+You+Intensely+2',
    },
    {
        'perfume': 'Paco Rabanne 1 Million',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+1+Million',
        'imagen2': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+1+Million+2',
    },
    {
        'perfume': 'Paco Rabanne 1 Million Elixir',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+1+Million+Elixir',
        'imagen2': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+1+Million+Elixir+2',
    },
    {
        'perfume': 'Paco Rabanne Invictus',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+Invictus',
        'imagen2': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+Invictus+2',
    },
    {
        'perfume': 'Paco Rabanne Invictus Parfum',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+Invictus+Parfum',
        'imagen2': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+Invictus+Parfum+2',
    },
    {
        'perfume': 'Paco Rabanne Olympea',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+Olympea',
        'imagen2': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+Olympea+2',
    },
    {
        'perfume': 'Paco Rabanne Phantom',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+Phantom',
        'imagen2': 'https://via.placeholder.com/300x300?text=Paco+Rabanne+Phantom+2',
    },
    {
        'perfume': 'Versace Eros Parfum',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Versace+Eros+Parfum',
        'imagen2': 'https://via.placeholder.com/300x300?text=Versace+Eros+Parfum+2',
    },
    {
        'perfume': 'Versace Dylan Blue',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Versace+Dylan+Blue',
        'imagen2': 'https://via.placeholder.com/300x300?text=Versace+Dylan+Blue+2',
    },
    {
        'perfume': 'Versace Pour Homme',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Versace+Pour+Homme',
        'imagen2': 'https://via.placeholder.com/300x300?text=Versace+Pour+Homme+2',
    },
    {
        'perfume': 'Yves Saint Laurent Y Intense',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Yves+Saint+Laurent+Y+Intense',
        'imagen2': 'https://via.placeholder.com/300x300?text=Yves+Saint+Laurent+Y+Intense+2',
    },
    {
        'perfume': 'Yves Saint Laurent Y Elixir',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Yves+Saint+Laurent+Y+Elixir',
        'imagen2': 'https://via.placeholder.com/300x300?text=Yves+Saint+Laurent+Y+Elixir+2',
    },
    {
        'perfume': 'Yves Saint Laurent MYSLF',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Yves+Saint+Laurent+MYSLF',
        'imagen2': 'https://via.placeholder.com/300x300?text=Yves+Saint+Laurent+MYSLF+2',
    },
    {
        'perfume': 'Carolina Herrera 212 Men',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Carolina+Herrera+212+Men',
        'imagen2': 'https://via.placeholder.com/300x300?text=Carolina+Herrera+212+Men+2',
    },
    {
        'perfume': 'Carolina Herrera 212 VIP Men',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Carolina+Herrera+212+VIP+Men',
        'imagen2': 'https://via.placeholder.com/300x300?text=Carolina+Herrera+212+VIP+Men+2',
    },
    {
        'perfume': 'Carolina Herrera Good Girl',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Carolina+Herrera+Good+Girl',
        'imagen2': 'https://via.placeholder.com/300x300?text=Carolina+Herrera+Good+Girl+2',
    },
    {
        'perfume': 'Carolina Herrera Bad Boy',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Carolina+Herrera+Bad+Boy',
        'imagen2': 'https://via.placeholder.com/300x300?text=Carolina+Herrera+Bad+Boy+2',
    },
    {
        'perfume': 'Jean Paul Gaultier Le Male',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Jean+Paul+Gaultier+Le+Male',
        'imagen2': 'https://via.placeholder.com/300x300?text=Jean+Paul+Gaultier+Le+Male+2',
    },
    {
        'perfume': 'Jean Paul Gaultier Le Beau',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Jean+Paul+Gaultier+Le+Beau',
        'imagen2': 'https://via.placeholder.com/300x300?text=Jean+Paul+Gaultier+Le+Beau+2',
    },
    {
        'perfume': 'Montblanc Explorer',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Montblanc+Explorer',
        'imagen2': 'https://via.placeholder.com/300x300?text=Montblanc+Explorer+2',
    },
    {
        'perfume': 'Montblanc Legend Spirit',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Montblanc+Legend+Spirit',
        'imagen2': 'https://via.placeholder.com/300x300?text=Montblanc+Legend+Spirit+2',
    },
    {
        'perfume': 'Ralph Lauren Polo Blue',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Ralph+Lauren+Polo+Blue',
        'imagen2': 'https://via.placeholder.com/300x300?text=Ralph+Lauren+Polo+Blue+2',
    },
    {
        'perfume': 'Calvin Klein CK One',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Calvin+Klein+CK+One',
        'imagen2': 'https://via.placeholder.com/300x300?text=Calvin+Klein+CK+One+2',
    },
    {
        'perfume': 'Calvin Klein CK IN2U',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Calvin+Klein+CK+IN2U',
        'imagen2': 'https://via.placeholder.com/300x300?text=Calvin+Klein+CK+IN2U+2',
    },
    {
        'perfume': 'Valentino Uomo Born In Roma',
        'precio': 280000,
        'imagen1': 'https://via.placeholder.com/300x300?text=Valentino+Uomo+Born+In+Roma',
        'imagen2': 'https://via.placeholder.com/300x300?text=Valentino+Uomo+Born+In+Roma+2',
    },
]

DB_PATH = 'perfumes.db'

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS perfumes')
    cursor.execute(
        '''
        CREATE TABLE perfumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            perfume TEXT NOT NULL,
            precio INTEGER NOT NULL,
            imagen1 TEXT NOT NULL,
            imagen2 TEXT NOT NULL
        )
        '''
    )

    cursor.executemany(
        'INSERT INTO perfumes (perfume, precio, imagen1, imagen2) VALUES (?, ?, ?, ?)',
        [(p['perfume'], p['precio'], p['imagen1'], p['imagen2']) for p in PRODUCTOS]
    )

    conn.commit()

print(f'Created {DB_PATH} with {len(PRODUCTOS)} perfumes')
