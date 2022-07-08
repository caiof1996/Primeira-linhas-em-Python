from twilio.rest import Client
import pandas as pd
import twilio as tw

# Your Account SID from twilio.com/console
account_sid = "ACe4f7af790dddfb4d9c39bffc81584f41"
# Your Auth Token from twilio.com/console
auth_token = "df5eb67fb5a5580adf22df941cac889a"

client = Client(account_sid, auth_token)
'''
1 - Abrir arquivos em excel
2 - para cada arquivo, verificar se algum valor na coluna de vendas é maior que 55000
3 - Se for maior que 55000 => enviar sms com o nome, o mês e as vendas do vendedor
'''

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        print(
            f'Encontramos um ganhador no mês de {mes}. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511945041999",
            from_="+19804475079",
            body=f'Encontramos um ganhador no mês de {mes}. Vendedor: {vendedor}, Vendas: {vendas}')

        print(message.sid)
