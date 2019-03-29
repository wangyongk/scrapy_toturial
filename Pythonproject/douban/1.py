import requests
from urllib.parse import urlencode
import json
import time, datetime
import logging
from lxml import etree
import pymysql
from pymysql.err import IntegrityError

proxies_ = {
    'http': '@http-dyn.abuyun.com:9020',
    'https': '@http-dyn.abuyun.com:9020',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52'
}
session = requests.Session()


def session_get(url, header=headers, tab=12):
    if tab == 0:
        return False
    try:
        response = session.get(url, headers=header, proxies=proxies_)
        time.sleep(2)
        return response if response.status_code == 200 else session_get(url, header, tab - 1)
    except Exception as e:
        if tab == 1:
            logging.exception(e)
        return session_get(url, header, tab - 1)


def session_post(url, header=headers, data=None, tab=12):
    if tab == 0:
        return False
    try:
        response = session.post(url, headers=header, data=data, proxies=proxies_)
        time.sleep(2)
        return response if response.status_code == 200 else session_post(url, header, data, tab - 1)
    except Exception as e:
        if tab == 1:
            logging.exception(e)
        return session_post(url, header, data, tab - 1)


def get_node_text(node, xpath):
    """
    通过节点和xpath来获取节点需要的内容
    :param node:
    :param xpath:
    :return:
    """
    try:
        if xpath == "string(.)": return node.xpath('string(.)').strip()
        if len(node.xpath(xpath)) > 0:
            return node.xpath(xpath)[0].strip() if isinstance(node.xpath(xpath)[0], str) else node.xpath(xpath)[0]
        return ""
    except:
        logging.exception('获取xpath %s 出错' % (xpath))
        return None


def get_youjia_tpp_conn():
    """
    获取井队数据库连接
    :return:
    """
    return pymysql.connect(host='host', user='user', passwd='passwd', db='db', port=3306,
                           charset='utf8')


def storage_database_text(data_json, t_name, l_name="youjia_tpp"):
    """
    非json类型数据存储数据库
    :param data_json:
    :param t_name:
    :param l_name:
    :return:
    """
    now_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    data_list = []
    insert_sql = "INSERT INTO " + l_name + "." + t_name + " ("
    update_sql = "UPDATE " + l_name + "." + t_name + " SET "
    for key in data_json:
        update_sql += str(key) + "=%s , "
        if str(key) == "id":
            id_key = data_json[key]
        insert_sql += str(key) + ","
    update_sql += "modify_time = '" + str(now_time) + "' where id = '" + str(id_key) + "'"
    insert_sql = insert_sql[:-1]
    insert_sql += ")VALUES("
    for key in data_json:
        insert_sql += "%s,"
        data_list.append(str(data_json[key]))
    insert_sql = insert_sql[:-1]
    insert_sql += ");"
    # print(update_sql)
    # print(insert_sql)
    with get_youjia_tpp_conn() as conn:
        try:
            print("storage_database_text  insert_sql : ", t_name)
            conn.execute(insert_sql, tuple(data_list))
        except IntegrityError:
            print("storage_database_text  update_sql : ", t_name)
            conn.execute(update_sql, tuple(data_list))
        except Exception as msg:
            logging.exception(msg)


def storage_database_json(id_, data_json, j_name, t_name, l_name="youjia_tpp"):
    """
    存储json形式至数据库
    :param id_: id
    :param data_json: json
    :param j_name: json的名字
    :param t_name: 表名
    :param l_name: 库名
    :return:
    """
    now_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    insert_sql = "INSERT INTO " + l_name + "." + t_name + " (`id`,`" + j_name + "`)VALUES(%s,%s);"
    updatesql = "update " + l_name + "." + t_name + " set `" + j_name + "`=%s , modify_time=%s where id = %s;"
    # print(updatesql % (data_json, now_time, id_))
    with get_youjia_tpp_conn() as conn:
        try:
            print("storage_database_json  insert_sql : ", t_name)
            conn.execute(insert_sql, (id_, data_json))
        except IntegrityError:
            print("storage_database_json  update_sql : ", t_name)
            conn.execute(updatesql, (data_json, now_time, id_))
        except Exception as msg:
            logging.exception(msg)


def pre_login():
    try:
        param = {
            # 'uuid': 'e8514dbe200b4fde9393.1532912269.1.0.0',
            'service': 'phoenix',
            'continue': 'https://www.zhenguo.com/auth/authenticated/?continue=/help/trust/',
        }
        url = 'https://passport.meituan.com/account/unitivelogin?' + urlencode(param)
        response = session_get(url=url, header=headers, tab=5)
        if response.status_code == 200:
            print("pre_login 成功")
            return response.text
        else:
            return None
    except ConnectionError as e:
        print(e.args)
        print('预登陆出错')


def parse_param(html):
    try:
        html = etree.HTML(html)
        csrf = html.xpath('//input[@name="csrf"]/@value')[0]
        origin = html.xpath('//input[@name="origin"]/@value')[0]
        fingerprint = html.xpath('//input[@name="fingerprint"]/@value')[0]
        uuid = html.xpath('//i[@class="form-uuid"]/text()')[0]
        need_captcha = html.xpath('//div[@class="form-field J-form-field-captcha form-field--captcha"]/@style')[
            0].replace("display:", "")
        return (csrf, uuid, need_captcha, origin, fingerprint)
    except:
        print('解析csrf,uuid,need_captcha出错')


def formal_login(username, password, param):
    csrf = param[0]
    uuid = param[1]
    origin, fingerprint = param[3], param[4]
    if 1 == 1:
        captcha_param = {
            'uuid': uuid,
        }
        url = 'https://passport.meituan.com/account/captcha?' + urlencode(captcha_param)
        print(url)
        image_resp = session_get(url)
        with open('C:/Users/admin/Desktop/image/zg.jpg', 'wb') as file:
            file.write(image_resp.content)
        captcha = input('需要验证码:')
    # else:
    #     captcha = ''
    url_param = {
        'uuid': uuid,
        'service': 'phoenix',
        'continue': 'https://www.zhenguo.com/auth/authenticated/?continue=/help/trust/',
    }
    postdata = {
        'email': username,
        'password': password,
        'captcha': captcha,
        'origin': origin,
        'fingerprint': fingerprint,
        'csrf': csrf
    }
    url = 'https://passport.meituan.com/account/unitivelogin?' + urlencode(url_param)
    try:
        response = session_post(url, data=postdata, header=headers)
        if response.status_code == 200:
            print("登陆成功！")
            return response.text
        else:
            return None
    except ConnectionError as e:
        print(e.args)
        print('登录出错')


def parse_token(html):
    try:
        html = etree.HTML(html)
        action_url = html.xpath('//form[@class="J-form mainbox__content"]/@action')[0]
        token = html.xpath('//input[@name="token"]/@value')[0]
        expire = html.xpath('//input[@name="expire"]/@value')[0]
        isdialog = html.xpath('//input[@name="isdialog"]/@value')[0]
        autologin = html.xpath('//input[@name="autologin"]/@value')[0]
        csrf = html.xpath('//*[@id="csrf"]/text()')[0]

        # headers['x-csrf-token'] = csrf
        # trust_response = session.post(action_url, data=postdata, headers=headers)
        # print(trust_response.text)
        return {"action_url": action_url, "token": token, "expire": expire, "isdialog": isdialog,
                "autologin": autologin, "csrf": csrf}
    except:
        logging.exception('解析token出错')


def redirect_login(token_json):
    """
    {"action_url": action_url, "token": token, "expire": expire, "isdialog": isdialog,
                "autologin": autologin, "csrf": csrf}
    :param token:
    :return:
    """
    postdata = {
        'token': token_json['token'],
        'expire': token_json['expire'],
        'isdialog': token_json['isdialog'],
        'autologin': token_json['autologin'],
        'logintype': 'normal'
    }
    headers['x-csrf-token'] = token_json['csrf']
    try:
        trust_response = session_post(token_json['action_url'], data=postdata, header=headers)
        print("重定向成功！！")
        # tt = session.get("https://www.zhenguo.com/house/list/", headers=t_h)
    except ConnectionError as e:
        print(e.args)
        print('重定向出错')


def test():
    try:
        time.sleep(5)
        url = 'http://maoyan.com/profile'
        response = session_get(url, header=headers)
        print(response.status_code)
        print(response.text)
    except ConnectionError as e:
        print(e.args)
        print('测试出错')


def crawl_order(account_id, token, page_no=1, page_size=20):
    orders_url = "https://www.zhenguo.com/host/orders/"
    response = session_get(orders_url, header=headers)
    print(response.status_code)
    html = etree.HTML(response.text)
    csrf = html.xpath('//meta[@name="csrf-token"]/@content')[0]
    headers['x-csrf-token'] = csrf
    print(csrf)
    queryOrderByTypeUrl = "https://www.zhenguo.com/gw/order/api/v1/orderSearch/queryOrderByType"
    OrderByType = {'pageNow': page_no, 'pageSize': page_size, 'orderStatusType': 9}
    headers['Accept'] = "application/json"
    headers['Content-Type'] = "application/json"
    query_response = session_post(queryOrderByTypeUrl, data=json.dumps(OrderByType), header=headers)
    query_json = query_response.json()
    query_list = query_json['data']['list']
    print(len(query_list))
    for order_json in query_list:
        order_id = order_json['orderId']
        storage_database_json(order_id, json.dumps(order_json), 'order', 'zhenguo_order')
        storage_database_text({"id": order_id, 'account_id': account_id}, 'zhenguo_order')

    if len(query_list) == page_size:
        crawl_order(account_id, page_no + 1)


def house_detail(list_json):
    """
    解析房屋详情的
    :param list_json:
    :return:
    """
    room_id = list_json["id"]
    room_url = "https://www.zhenguo.com/housing/%s" % room_id
    room_response = session_get(room_url)
    if room_response:
        html = etree.HTML(room_response.text)
        room_type = get_node_text(html,
                                  '//*[@id="J-layout"]/div[2]/div/div[2]/div/div[2]/section[1]/div[2]/span[1]/text()')
        list_json["room_type"] = room_type
        house_wear = get_node_text(html,
                                   '//*[@id="J-layout"]/div[2]/div/div[2]/div/div[2]/section[1]/div[2]/span[2]/text()')
        list_json["house_wear"] = house_wear
        room_area = get_node_text(html,
                                  '//*[@id="J-layout"]/div[2]/div/div[2]/div/div[2]/section[1]/div[2]/span[3]/text()')
        list_json["room_area"] = room_area
        for node in html.xpath('//*[@id="J-layout"]/div[2]/div/div[2]/div/div[2]/section[2]/ul/li'):
            text = get_node_text(node, './div[1]/text()')
            node_detail = get_node_text(node, './div[2]/text()')
            if text == "房源":
                room_count = node_detail
                list_json["room_count"] = room_count
            if text == "评价":
                comment_count = node_detail
                list_json["comment_count"] = comment_count
            if text == "咨询回复率":
                rep_rate = node_detail
                list_json["rep_rate"] = rep_rate
            if text == "咨询回复时长":
                rep_length = node_detail
                list_json["rep_length"] = rep_length
        str(1).strip()
        reserve = get_node_text(html, '//*[@id="J-layout"]/div[2]/div/'
                                      'div[2]/div/div[2]/section[8]/ul[1]/li[2]/text()').split("，")
        # list_json["reserve"] = reserve
        if len(reserve) > 1:
            less_day = reserve[0].replace("最少预订", "").replace("天", "").strip()
            more_day = reserve[1].replace("最多预订", "").replace("天", "").strip()
            list_json["less_day"] = less_day
            list_json["more_day"] = more_day
        unsubscribe = get_node_text(html, '//*[@id="J-layout"]/div[2]/div/div[2]/div/div[2]/section[8]/ul[2]/li/text()')
        list_json["unsubscribe"] = unsubscribe
    return list_json


def crawl_room(account_id, token):
    comment_url = "https://www.zhenguo.com/gw/ugc/api/v1/product/comments?productId=%s&pageNow=1&pageSize=100"
    room_list_url = "https://www.zhenguo.com/house/list/"
    room_response = session_get(url=room_list_url, header=headers)
    if room_response:
        html = etree.HTML(room_response.text)
    for node in html.xpath('//div[@class="houseCard__block"]'):
        title = get_node_text(node, './div[@class="houseCard__titleLine"]/text()')  # 标题
        price = get_node_text(node, './div[@class="houseCard__addLine clearfix"]'
                                    '/span[1]/span[@class="houseCard__price"]/text()').replace("¥", "")  # 价格
        state = get_node_text(node, './div[@class="houseCard__bottomLine clearfix"]/'
                                    'div[1]/span[@class="houseCard__verifyStatus-5"]/text()')  # 状态
        room_id = get_node_text(node, './div[@class="houseCard__bottomLine clearfix"]'
                                      '/div[1]/@data-product-id')  # 房源id
        print(account_id, title, price, state, room_id)
        list_json = {"account_id": account_id, "title": title,
                     "price": price, "state": state, "id": room_id, "room_id": room_id}
        comment_ = comment_url % room_id

        house_json = house_detail(list_json)
        response = session_get(url=comment_)
        if response:
            print(response.text)
            storage_database_json(room_id, json.dumps(response.json()), "comment", "zhenguo_room_info",
                                  l_name="youjia_tpp")
        storage_database_text(house_json, 'zhenguo_room_info')


def crawl_room_list(account_id, token):
    app_header = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; vivo X7 Build/LMY47V) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 TitansX/11.6.12 "
                                "KNB/1.2.0 android/5.1.1 phoenix/com.meituan.phoenix/2.6.0 com.meituan.phoenix/2.6.0",
                  "Cookie": "token=" + token}
    list_url = "https://iphx.meituan.com/ds/product/online/list"
    list_resp = session_get(url=list_url, header=app_header)
    if list_resp:
        list_json = list_resp.json()
        for room_json in list_json['data']['list']:
            room_id = room_json['productId']
            product_quota_url = "https://iphx.meituan.com/api/product/api/v1/product/getProductQuota/"+str(room_id)
            product_quota_resp = session_get(url=product_quota_url, header=app_header)
            print(room_json)
            print(product_quota_resp.json()['data'])



def crawl(account_id, token):
    """
    登录的session搞定之后 开始爬取详细信息
    :return:
    """
    crawl_room_list(account_id, token)  # 爬取手机端信息

    # crawl_room(account_id, token)  # 房屋爬取
    # crawl_order(account_id, token)  # 订单爬虫


def login(username, password):
    html_pre_login = pre_login()
    param = parse_param(html_pre_login)
    print("param: ", param)
    html_login = formal_login(username, password, param)
    # print(html_login)
    token_json = parse_token(html_login)
    print("token_json: ", token_json)
    redirect_login(token_json)
    return token_json['token']


if __name__ == '__main__':
    username = 'username'
    password = 'username'
    token = login(username, password)
    crawl(1, token)