import vk
import time
import datetime

print('VKBot')
# или с помощью id приложения и данных авторизации пользователя
session = vk.AuthSession('5730806', '+79885372442', 'korova,90')
api = vk.API(session)
while(True):
    messages = api.messages.get()
    commands = ['help', 'завтрак', 'обед', 'ужин', 'легкий перекус', 'десерт']
    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]
    for m in messages:
                    user_id = m[0]
                    message_id = m[1]
                    command = m[2]
                    date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
                    if command == 'help':
                                api.messages.send(user_id=user_id,
                                                    message=date_time_string + '\n>VKBot v0.1 by Ann\nЧто вас интересует?\n-Завтрак\n-Обед\n-Ужин\n-Легкий перекус\n-Десерт')
                    if command == 'завтрак':
                                api.messages.send(user_id=user_id,
                                                     message='http://eda.ru/recepty/zavtraki/zavtrak-dlja-lenivih-21975?from=search\nhttp://eda.ru/recepty/zavtraki/polnij-anglijskij-zavtrak-20740?from=search\nhttp://eda.ru/recepty/zavtraki/poleznij-zavtrak-22515?from=search')
                    if command == 'обед':
                                api.messages.send(user_id=user_id,
                                                    message='http://eda.ru/recepty/osnovnye-blyuda/obed-iz-kartofelja-s-gribami-ovoschnimi-ruletami-29587?from=search\nhttp://eda.ru/recepty/supy/tikvennij-sup-s-imbirem-29617?from=search\nhttp://eda.ru/recepty/supy/gorohovij-sup-33827?from=search')
                    if command == 'ужин':
                                api.messages.send(user_id=user_id,
                                                    message='http://eda.ru/recepty/salaty/salat-romanticheskij-uzhin-21374?from=search\nhttp://eda.ru/recepty/osnovnye-blyuda/zapechennaja-kurica-s-ovoshhami-17672?from=search\nhttp://eda.ru/recepty/pasta-picca/lazanja-klassicheskaja-s-mjasom-31799?from=search')
                    if command == 'легкий перекус':
                                api.messages.send(user_id=user_id,
                                                    message='http://eda.ru/recepty/salaty/legkij-salat-s-krevetkami-15161?from=search\nhttp://eda.ru/recepty/sendvichi/sjendvich-s-tuncom-31829?from=search\nhttp://eda.ru/recepty/salaty/teplij-salat-iz-kurici-vinograda-22187?from=search')
                    if command == 'десерт':
                                api.messages.send(user_id=user_id,
                                                    message='http://eda.ru/recepty/vypechka-deserty/tvorozhnij-desert-bez-vipechki-33617?from=search\nhttp://eda.ru/recepty/vypechka-deserty/bananovij-desert-46070?from=search\nhttp://eda.ru/recepty/vypechka-deserty/amerikanskiy-desert-smor-s-more-58074?from=search')
    ids = ', '.join([str(m[1]) for m in messages])
    if ids:
        api.messages.markAsRead(message_ids=ids)

    time.sleep(3)
