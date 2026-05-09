from creational.factory import run as factory_run
from creational.singleton import run as singleton_run
from structural.adapter import run as adapter_run
from structural.decorator import run as decorator_run
from behavioral.strategy import run as strategy_run
from behavioral.observer import run as observer_run

print("=== ВІТІ | гр.3201 | Кузнєцова Т.Ю. ===\n")

factory_run()
singleton_run()
adapter_run()
decorator_run()
strategy_run()
observer_run()

input("\nНатисни Enter щоб закрити...")