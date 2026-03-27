from datetime import datetime, timedelta
from pytz import timezone
from dateutil.relativedelta import relativedelta

data = datetime.now(timezone('Asia/Tokyo'))

print(data)
print()

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
diferenca = data_fim - data_inicio
print(diferenca.days, diferenca.seconds)
print()
delta = timedelta(seconds=60)
ultima_data = data_fim + delta
print(ultima_data)

# EXERCÍCIO
# MARIA PEGOU UM EMPRÉSTIMO DE 1 MILHÃO PARA PAGAR EM 5 ANOS
# A DATA QUE ELA PEGOU O EMPRÉSTIMO FOI 20/12/2020 E O VENCIMENTO
# DE CADA PARCELA É NO DIA 20 DE CADA MÊS.
# CRIE A DATA INICIAL E FINAL DO EMPRÉSTIMO
# MOSTRE TODAS AS DATAS DE VENCIMENTO E O VALOR DE CADA PARCELA

formato = '%d/%m/%Y'
data_inicial = datetime.strptime('20/12/2020', formato)
data_final = data_inicial + relativedelta(years=5)
MESES_PAGANDO = 5 * 12
VALOR_MENSAL = 1_000_000 / MESES_PAGANDO
total_pago = 0
parcelas = 0

while data_inicial < data_final:
    data_inicial += relativedelta(months=1)
    total_pago += VALOR_MENSAL
    parcelas += 1
    print( f'Parcela: {parcelas}\n'
          f'Data: {datetime.strftime(data_inicial, formato)}\n'
          f'Pagamento de R${VALOR_MENSAL:,.2f}\n'
          f'Total pago: R${total_pago:,.2f}')
    print()