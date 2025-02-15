class Production:
    def __init__(self, id_prod, name_prod, date_start, date_end):
        self.id_prod = id_prod
        self.name_prod = name_prod
        self.date_start = date_start
        self.date_end = date_end

    def add_stage(self, stage):
        pass

    def get_status(self):
        pass


class Stage:
    def __init__(self, id_stage, name_stage, description_stage):
        self.id_stage = id_stage
        self.name_stage = name_stage
        self.description_stage = description_stage


class Catalisator:
    def __init__(self, id_catalisator, private_catalisator, provider):
        self.id_catalisator = id_catalisator
        self.private_catalisator = private_catalisator
        self.provider = provider


class GetAmmiak:
    def __init__(self, catalisator, temperature, percent_mixtures):
        self.catalisator = catalisator
        self.temperature = temperature
        self.percent_mixtures = percent_mixtures

    def get_batch(self):
        pass


class OxidationAmmiak:
    def __init__(self, catalisator, percent_oxygen):
        self.catalisator = catalisator
        self.percent_oxygen = percent_oxygen

    def add_parameter(self, parameter):
        pass


class ConcentrationAcid:
    def __init__(self, concentration_acid):
        self.concentration_acid = concentration_acid


class BatchAmmiak:
    def __init__(self, id_batchammiak, catalisator, date_prodammiak):
        self.id_batchammiak = id_batchammiak
        self.catalisator = catalisator
        self.date_prodammiak = date_prodammiak

    def get_batch(self):
        pass


class AbsortionDioxideAzot:
    def __init__(self, filtr, level_filth):
        self.filtr = filtr
        self.level_film = level_filth

    def check_filtr(self):
        pass


class BatchDioxideAzot:
    def __init__(self, id_batchdioxide, catalisator, date_proddioxide):
        self.id_batchdioxide = id_batchdioxide
        self.catalisator = catalisator
        self.date_proddioxide = date_proddioxide


class Filtr:
    def __init__(self, id_filtr, brand_filtr, model_filtr, level_filth):
        self.id_filtr = id_filtr
        self.brand_filter = brand_filtr
        self.model_filter = model_filtr
        self.level_filth = level_filth

    def replace_filtr(self):
        pass


class AzotnayaAcid:
    def __init__(self, id_add, concentration_acid, date_prodacid):
        self.id_add = id_add
        self.concentration_acid = concentration_acid
        self.date_prodacid = date_prodacid
