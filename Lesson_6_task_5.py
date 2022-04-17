class Stationery:
    title: str
    _m = "Запуск отрисовки."
    def draw(self):
        print(self._m)
class Pen(Stationery):
    title = 'Ручка'
    _m = f"{title} - рисует в тетрадке."
class Pencil(Stationery):
    title = 'Карандаш'
    _m = f"{title} - рисует на листке."
class Handle(Stationery):
    title = 'Маркер'
    _m = f"{title} - рисует на доске."
its = [Pen(), Pencil(), Handle()]
for i in its:
    i.draw()