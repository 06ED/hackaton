from config import strings
from db import Database
from db.models.contact_model import ContactModel
from db.models.location_model import LocationModel
from db.models.rent_model import RentModel
from db.models.service_model import ServiceModel


def generate(db: Database):
    db.session.add(LocationModel(
        name="г. Ижевск, ул. 9 января, 213, магазин «Погода в доме»",
        lat=56.877598,
        lon=53.255480
    ))
    db.session.add(LocationModel(
        name="улица 9 Января, 259",
        lat=56.883991,
        lon=53.257520
    ))
    db.session.add(LocationModel(
        name="Автозаводская улица, 50",
        lat=56.877287,
        lon=53.289716
    ))
    db.session.add(LocationModel(
        name="улица Дзержинского, 48А",
        lat=56.882929,
        lon=53.249651
    ))
    db.session.add(LocationModel(
        name="г Ижевск, ул. Молодежная, д. 96",
        lat=56.846981,
        lon=53.295977
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Молодежная, д.79В",
        lat=56.851402,
        lon=53.298285
    ))
    db.session.add(LocationModel(
        name="Молодёжная улица, 101",
        lat=56.849556,
        lon=53.297648
    ))
    db.session.add(LocationModel(
        name="улица А.Н. Сабурова, 27А",
        lat=56.874739,
        lon=53.298780
    ))
    db.session.add(LocationModel(
        name="улица Ленина, 120А",
        lat=56.848685,
        lon=53.266647
    ))
    db.session.add(LocationModel(
        name="г Ижевск, ул. 40 лет Победы, д. 72",
        lat=56.853306,
        lon=53.280957
    ))
    db.session.add(LocationModel(
        name="г Ижевск, ул. 40 лет Победы, д. 52",
        lat=56.848941,
        lon=53.283948
    ))
    db.session.add(LocationModel(
        name="г Ижевск, ул. Ворошилова, д. 53",
        lat=56.877243,
        lon=53.269342
    ))
    db.session.add(LocationModel(
        name="д. Хохряки, ул. Трактовая,д. 1",
        lat=56.914537,
        lon=53.317977
    ))
    db.session.add(LocationModel(
        name="г.Ижевск, ул.Ракетная, 24, м-н «Карамель»",
        lat=56.832269,
        lon=53.284231
    ))
    db.session.add(LocationModel(
        name="г Ижевск, ул. Максима Горького, 149",
        lat=56.854291,
        lon=53.197512
    ))
    db.session.add(LocationModel(
        name="улица Карла Маркса, 393",
        lat=56.862248,
        lon=53.201124
    ))
    db.session.add(LocationModel(
        name="улица Холмогорова, 24А",
        lat=56.875502,
        lon=53.216377
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Гагарина, д. 49Б, ТЦ «Московский»",
        lat=56.794347,
        lon=53.182983
    ))
    db.session.add(LocationModel(
        name="г Ижевск, ул. Героя России Ильфата Закирова, д.21",
        lat=56.839484,
        lon=53.288925
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Клубная, д.27",
        lat=56.830418,
        lon=53.147773
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Выставочная, д. 3Б",
        lat=56.916099,
        lon=53.267285
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Школьная, д.44А",
        lat=56.876722,
        lon=53.184855
    ))
    db.session.add(LocationModel(
        name="Майская улица, 9А",
        lat=56.869692,
        lon=53.212416
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Карла Либкнехта, 51",
        lat=56.838760,
        lon=53.230301
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Клубная, 50",
        lat=56.831462,
        lon=53.137056
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. 8ая Подлесная, 48",
        lat=56.872329,
        lon=53.185466
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Карла Либнихта, 10",
        lat=56.837362,
        lon=53.213673
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Ордженикидзе, 36А",
        lat=56.841916,
        lon=53.239087
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Ордженикидзе, 40",
        lat=56.842753,
        lon=53.237856
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Удмуртская, 304",
        lat=56.858735,
        lon=53.223114
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Барышникова, 9",
        lat=56.871394,
        lon=53.295626
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Пугачева, 43",
        lat=56.820695,
        lon=53.211014
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Молодежная, 74",
        lat=56.847976,
        lon=53.290255
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Дзержинского, 30",
        lat=56.881266,
        lon=53.243093
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Ленина, 166А",
        lat=56.843555,
        lon=53.297845
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Азина, 152",
        lat=56.815966,
        lon=53.175935
    ))
    db.session.add(LocationModel(
        name="г. Ижевск, ул. Репина, 215",
        lat=56.864728,
        lon=53.232466
    ))

    rent1 = ServiceModel(type="Гостевой домик 1")
    rent2 = ServiceModel(type="Гостевой домик 2")
    rent3 = ServiceModel(type="Гостевой домик 3 (ЭКО)")
    rent4 = ServiceModel(type="Беседка на воде")
    rent5 = ServiceModel(type="Беседка у пруда")
    db.session.add(rent1)
    db.session.add(rent2)
    db.session.add(rent3)
    db.session.add(rent4)
    db.session.add(rent5)

    for rent in strings.RENTS:
        db.session.add(RentModel(name=rent.name, description=rent.description, cost=rent.cost, img_url=rent.img_url))

    db.session.commit()
