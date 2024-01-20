from datetime import datetime


def retornar_data() -> str:
    data = datetime.now()
    formt_data = '%d/%m/%Y'
    data_formatada = data.strftime(formt_data)

    return data_formatada

