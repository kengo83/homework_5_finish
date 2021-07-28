import eel
import desktop
from pos_system import PosSystem
from pos_system import Order

app_name="html"
end_point="index.html"
size=(700,600)

CSV_FILE_PATH = "./super.csv"

@eel.expose
def payment_money(payment_money):
    global system
    if payment_money == '':
        eel.display_alert('金額を入力して下さい')
    else:
        system.order.pay_money(payment_money)

@eel.expose
def clear_list():
    system.order.clear_list()
    

@eel.expose
def log_order_item(code,number):
    global system
    result = system.order.check_code_in_item_master(code)
    if code == '' or number == '':
        eel.display_alert('入力できていない箇所が有ります')
    elif code == '' and number == '':
        eel.display_alert('入力できていない箇所が有ります')
    else:
        if result == True:
            system.order.add_item_order(code,number)
            system.order.view_order()
            system.order.display_item()
        else:
            eel.display_alert('この商品は登録されていません、商品コードを打ち直して下さい')

def init_pos_system(csv_file_path):
    global system #グローバル変数を宣言
    system = PosSystem(csv_file_path)
    system.add_item_master_by_csv()
    system.create_order_class() #system.order = Order(self.item_master)、引数がself.item_masterのOrder()インスタンスを作る

if __name__ == "__main__": #csvからself.item_masterに商品登録。Orderインスタンスを作成(system.order)。htmlを起動する
    init_pos_system(CSV_FILE_PATH)
    desktop.start(app_name,end_point,size)
