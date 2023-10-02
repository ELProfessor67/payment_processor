def generatehtml(transactions,total,cards):

    cards_code = ""
    for card in cards:
        
        cards_code += f"<div style='display: flex; justify-content: flex-start; align-items: center; margin: .5rem 0;'><h1 style='margin: 0;'>{card} : </h1><h1 style='margin: 0;'> {cards[card]}$</h1></div>"
    

    tables_code = ""
    for i,transaction in enumerate(transactions):
        tables_code += f"<tr><th>{i}</th><th>{transaction.amount}$</th><th>{transaction.codes.get('transaction_type')}</th><th>{transaction.codes.get('code')}</th><th>{transaction.card_number}</th><th>{transaction.created_at}</th></tr>"



    code = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible"content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1"></head><body><h2 style="color: red; font-size: 2.5rem; text-align: center;">Transaction Reports</h2><div style="display: flex; justify-content: flex-start; align-items: center; margin: .5rem 0; margin-bottom: 2rem;"><h1 style="margin: 0;">Total Transactions : </h1><h1 style="margin: 0;">'+str(total)+'$ </h1></div>'+cards_code+'<table border="1" style="border-collapse: collapse; font-size: .9rem; margin-top: 2rem;"><thead><tr><th scope="col">#</th><th scope="col">Aviable Amount</th><th scope="col">Transaction Type</th><th scope="col">Status Code</th><th scope="col">Card Number</th><th scope="col">Date</th></tr></thead><tbody>'+tables_code+'</tbody></table></body></html>'

    return code;