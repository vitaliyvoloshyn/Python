class Warehouse:
    warehouse_dict = {}

    def income(self, obj):
        """Отвечает за прием оргтехники на склад.
        Обязательный параметр - обьект оргтехники"""
        if isinstance(obj, Printer):
            if 'printer' in Warehouse.warehouse_dict:
                Warehouse.warehouse_dict['printer'].append(obj)
            else:
                Warehouse.warehouse_dict.setdefault('printer', [obj])
        if isinstance(obj, Scaner):
            if 'scaner' in Warehouse.warehouse_dict:
                Warehouse.warehouse_dict['scaner'].append(obj)
            else:
                Warehouse.warehouse_dict.setdefault('scaner', [obj])
        if isinstance(obj, Xerox):
            if 'xerox' in Warehouse.warehouse_dict:
                Warehouse.warehouse_dict['xerox'].append(obj)
            else:
                Warehouse.warehouse_dict.setdefault('xerox', [obj])

    def total_count(self, **kwargs):
        """Возвращает общее кол-во оргтехники на складе"""

        if 'type' in kwargs:
            if 'model' in kwargs:
                return len([y for i in Warehouse.warehouse_dict.values() for y in i if y.eg_type == kwargs['type'] and y.model == kwargs['model']])
            else:
                return len([y for i in Warehouse.warehouse_dict.values() for y in i if
                            y.eg_type == kwargs['type']])
        else:
            return len([y for i in Warehouse.warehouse_dict.values() for y in i])






class OfficeEquipment:
    def __init__(self, brand, model, year, eg_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.eg_type = eg_type


class Printer(OfficeEquipment):
    def __init__(self, brand, model, year, eg_type, print_res, print_type, cartridge_life, sheets_per_min):
        super().__init__(brand, model, year, eg_type)
        self.print_res = print_res
        self.print_type = print_type
        self.cartridge_life = cartridge_life
        self.sheets_per_min = sheets_per_min

    def __repr__(self):
        return 'Printer'


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, year, eg_type, print_res, print_type, cartridge_life, sheets_per_min):
        super().__init__(brand, model, year, eg_type)
        self.print_res = print_res
        self.print_type = print_type
        self.cartridge_life = cartridge_life
        self.sheets_per_min = sheets_per_min

    def __repr__(self):
        return 'Xerox'


class Scaner(OfficeEquipment):
    def __init__(self, brand, model, year, eg_type, scan_res):
        super().__init__(brand, model, year, eg_type)
        self.scan_res = scan_res

    def __repr__(self):
        return 'Scaner'


obj1 = Printer('Cannon', 'Pixel 1255n', 2015, 'printer', '1200*900', 'laser', 1000, 24)
obj5 = Printer('Cannon', 'Pixel 1250n', 2015, 'printer', '1200*900', 'laser', 1000, 24)
obj2 = Scaner('HP', 'Desk 455af', 2018, 'scaner', '1200*1200')
ware = Warehouse()
ware.income(obj1)
print(ware.warehouse_dict)
ware.income(obj2)
print(ware.warehouse_dict)
obj3 = Printer('HP', 'Pixel 1250n', 2016, 'printer', '1200*900', 'laser', 1200, 27)
ware.income(obj3)
obj4 = Xerox('Cannon', 'Pixel 1250n', 2015, 'xerox', '1200*900', 'laser', 1000, 24)
ware.income(obj4)
ware.income(obj5)
print(ware.warehouse_dict)
print(ware.warehouse_dict['printer'][1].model)
print(ware.total_count(type='printer', model='Pixel 1250n'))
print(ware.total_count(type='printer', model='Pixel 1250n'))
print(ware.total_count(type='printer'))
print(ware.total_count())

