import asyncio
from aiocryptopay import AioCryptoPay, Networks

crypto = AioCryptoPay(token='239902:AA5391uAyBLB9qvi8WnuOo8qBmzHPOH1v6Z', network=Networks.MAIN_NET)

async def info():
    # Получение информации о профиле
    # profile = await crypto.get_me()
    # print(f"Profile: {profile}")
    
    # # Получение списка поддерживаемых криптовалют
    # currencies = await crypto.get_currencies()
    # print(f"Currencies: {currencies}")
    
    # # Получение баланса
    balance = await crypto.get_balance()
    print(f"Balance: {balance}")
    
    # # Получение курсов обмена
    # rates = await crypto.get_exchange_rates()
    # print(f"Exchange rates: {rates}")
    
    # # Получение статистики
    # stats = await crypto.get_stats()
    # print(f"Stats: {stats}")

    # Создание счета-фактуры
    # invoice = await crypto.create_invoice(asset='USDT', amount=0.52)
    # print(f"Invoice URL: {invoice.bot_invoice_url}")
    # deleted_invoice = await crypto.delete_invoice(invoice_id="IVRYCcF3JTaf")
    # old_invoice = await crypto.get_invoices(invoice_ids="IVRYCcF3JTaf")
    # print(old_invoice)
    #check = await crypto.create_check(asset='USDT', amount=4)
    #print(check)

    # deleted_check = await crypto.delete_check(check_id="9362191")
    # print(deleted_check)
    # all_check = await crypto.get_checks("USDT")
    # print(f"all_check{all_check}")


# Запуск асинхронной функции с помощью asyncio.run
asyncio.run(info())