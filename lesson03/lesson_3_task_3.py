from address import Address
from mailing import Mailing

from_addr = Address("125009", "Москва", "Тверская улица", "15", "34")

to_addr = Address("620000", "Екатеринбург", "Ленина проспект", "20", "78")

my_mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track="123456789RU"
)

print(f"Отправление {my_mailing.track} из {my_mailing.from_address.index}, "
      f"{my_mailing.from_address.city}, {my_mailing.from_address.street}, "
      f"{my_mailing.from_address.house} - {my_mailing.from_address.apartment} "
      f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, "
      f"{my_mailing.to_address.street}, {my_mailing.to_address.house} -"
      f"{my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} рублей.")