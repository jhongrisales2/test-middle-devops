import datetime
"""
• Este código importa el módulo datetime, que proporciona clases para trabajar con fechas y horas.
• La función get_age toma tres argumentos enteros: yyyy para el año, mm para el mes y dd para el día.
• Dentro de la función, se utiliza la función datetime.date para crear un objeto dob que representa la fecha de nacimiento.
• La función datetime.date.today() se utiliza para crear un objeto today que representa la fecha actual.
• La variable age se calcula restando el objeto dob del objeto today, lo que da como resultado un objeto datetime.timedelta que representa la diferencia entre las dos fechas.
• El atributo .days del objeto timedelta se divide por 365,25 (para tener en cuenta los años bisiestos) y se redondea al número entero más próximo mediante la función round.
• Por último, la variable age se devuelve como un número entero.
"""
def get_age(yyyy:int, mm:int, dd:int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age