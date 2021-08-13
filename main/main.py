class Car:
    def __init__(self, name='Banana', amount=10_000_000):
        self.car_name = name
        self.car_amount = amount

    def car_display_price(self):
        return f'{self.car_amount:,}円'

    def get_table(year_lastmonth_information):
        options = {
            'FilterExpression': Attr('used_at_date').contains(year_lastmonth_information),
            'ProjectionExpression' : 'mail_address,used_at_date,used_in,reservation_num'
        }
        response = table.scan(**options)
        #確認用
        #pprint.pprint(response)
        return response