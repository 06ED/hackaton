from typing import Union
from dataclasses import dataclass


@dataclass
class Rent:
    name: str
    description: Union[str, None]
    cost: str
    img_url: str


RENTS = [
    Rent(
        "Прокат батута",
        None,
        "10 минут 150 руб",
        "https://sun9-50.userapi.com/vAyegDoSMqF9eoA33e9byZfaQx1G6d1h_Ww6WQ/UL3yvZPcYwE.jpg"
    ),
    Rent(
        "Категория А электромобиль Лексус",
        "Возраст от 1 до 8 лет, до 45 кг",
        "Цена 150 руб- 5 минут, 200 руб- 10 минут",
        "https://sun9-14.userapi.com/M5Nb6JTXL0n09Pugn5JXPdX1ygv9UCac9zPAKg/OXY4kl1TG-8.jpg"
    ),
    Rent(
        "Категория Б электроквадроцикл",
        "Возраст от 2х до 8 лет, до 50 кг",
        "Цена 200 руб- 5 минут, 250 руб- 10 минут",
        "https://sun9-30.userapi.com/w487e6R34vt71P7uPH1HKQeJpMORA4xXLaXVZw/mMgWdWcExvM.jpg"
    ),
    Rent(
        "Трактор электромобиль",
        "Возраст от 1 до 6 лет, до 35 кг",
        "Цена 150 руб- 5 минут, 200 руб- 10 минут",
        "https://sun9-11.userapi.com/Y01Yr9IhKRoG576q1qZ9PyWUn74paPjwcaOlAg/K8koBzJvwCU.jpg"
    ),
    Rent(
        "Прокат велосипедов",
        None,
        "Цена 150 руб- 30 минут, 250 руб- 1 час, 1000 руб- суточный тариф",
        "https://sun9-34.userapi.com/BGQ7lHgdgxMPJdjM3Uzwq9V8UdlPgksQZYBahA/3hesd11dzvY.jpg"
    ),
    Rent(
        "Фотосессия с лошадью",
        "Предоставляем лошадь с инструктором для фотосессии",
        "30 минут 500 руб",
        "https://sun9-64.userapi.com/-GFnN8CH6E4d4rq4SAgA8F_CEueR71kE5q0c0g/BjLQo40t14A.jpg"
    ),
    Rent(
        "Троллей",
        "Троллей или zipline – это специальный канатный спуск,"
        " по которому посетитель спускается на блок-ролике под тяжестью собственного веса. Возраст 5+.",
        "100 руб. с человека (не более часа)",
        "https://sun9-60.userapi.com/yf6SLNNZNmPMI0yrkr_ihPgWTP7lBb3rzdJrww/yAHegkxbdWE.jpg"
    ),
    Rent(
        "Прокат сап-борда",
        "SUP серфинг - это скольжение по воде при помощи доски и весла. Научиться этому процессу сможет абсолютно "
        "каждый, независимо от возраста и спортивной подготовки. Все что вам потребуется это сап-борд и весло.",
        "30 мин. - 400 руб./чел.\n30 мин. - 800 руб./2 чел.\nДети до 4 лет. катаются бесплатно",
        "https://sun9-73.userapi.com/0vani0UeASwTDRb1pW-vMOPjR9xjlkzuZPFqSg/mik_ohO0H7o.jpg"
    ),
    Rent(
        "Баня на дровах",
        "Баня рассчитана на 8-10 чел.",
        "Аренда 1500 руб. 2 часа, каждый последующий час 500 руб.",
        "https://sun9-71.userapi.com/impg/dRG9hhKH8ghjlNZaTARveDM3dSg_DwQHhjaeLA/gUvXDEcY9KE.jpg"
        "?size=807x605&quality=96&sign=a503df80410e2467249af5875a76eee2"
        "&c_uniq_tag=YY777vqp4L9cAna9eqVyYbcWpVvfsDLmAFhGUgI1OYQ&type=none"
    ),
    Rent(
        "Рыбалка",
        "Какую рыбу можно поймать: щука, карась, сорожка, линь",
        "Рыбалка со своей удочкой"
        "\n- Взрослые 300 руб./чел. 2 часа"
        "\n- Дети 5-16 лет 150 руб./чел. 2 часа"
        "\n- Дети до 4 лет бесплатно"
        "\nБилет рыбака на день 600 руб. взрослый+1 ребёнок"
        "\nАренда удочки в чехле 200 руб."
        "\nНаживка 50 руб.",
        "https://sun9-46.userapi.com/RAz8cKI90MOy4xU2M9ecBFQ55HSqF84GRoDPDQ/fLnehLCR9ak.jpg"
    ),
    Rent(
        "Прокат лодок",
        "Вместимость одной лодки 3 взрослых 1 ребёнок",
        "Прокат лодки 400 руб./30 мин.",
        "https://sun9-29.userapi.com/K8XHWKRwSlRepXmqQKGopUODgPnASyHnz5_2hw/qfapSAGvlBw.jpg"
    ),
    Rent(
        "Инвентарь",
        "Различный инвентарь, необходимый на отдыхе",
        "Предоставление мангала, казана, котла - 450 руб.\n"
        "Предоставление сковороды - 50 руб.\n"
        "Предоставление шампуров, решетки для гриля - 50 руб.\n"
        "Использование дров - 250 руб./10 шт.\n"
        "Аренда русской печи - 500 руб. час",
        "https://sun9-70.userapi.com/ErpDltSw0_BNk2idfzjJKaHfYc66yByFvUqz9Q/OPm7_i4Hrlg.jpg"
    )
]
