#!/usr/local/bin/python3
from selenium import webdriver

# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import datetime
import jaconv
import re
from Mysql import Mysql
from dateutil.relativedelta import relativedelta

import mysql.connector


def bunkyo_scraper(browser: webdriver, mysql):
    for i in range(5):
        bunkyo_court_scraper(i + 1, browser, mysql)
        break


def date_modifier(date):
    next_year_date = date + relativedelta(years=1)
    today = datetime.date.today()
    if next_year_date - today > today - date:
        return date
    else:
        return next_year_date


def term(date, court_number, availability):
    Mysql.get(date, court_number)
    return True


def schedule_parser(text, court_number, mysql):
    tdate = None
    for line in text.split("\n"):
        if tdate:
            terms = line.split()
            for i in len(terms):
                if terms[i] == "○":
                    term(tdate, court_number, True)
                if terms[i] == "×":
                    term(tdate, court_number, False)

        if re.match("日\(\w\)", line):
            flag = "saturday"
            day = line.replace("月", "-")
            day = re.sub("日\(\w\)", "", day)
            day = datetime.datetime.now().strftime("%Y") + "-" + day
            tdatetime = datetime.datetime.strptime(day, "%Y-%m-%d")
            tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
            tdate = date_modifier(tdate)
        else:
            tdate = None
    return True


def bunkyo_court_scraper(court_number, browser: webdriver, mysql):
    # スクリーンショットのファイル名用に日付を取得
    dt = datetime.datetime.today()
    dtstr = dt.strftime("%Y%m%d%H%M%S")

    browser.get("https://www.yoyaku.city.bunkyo.lg.jp/reselve/m_index.do")
    sleep(2)

    browser.find_element_by_link_text("施設空き状況").click()
    sleep(2)

    browser.find_element_by_link_text("利用目的から選ぶ").click()
    sleep(2)

    browser.find_element_by_link_text("利用目的名から選択").click()
    sleep(2)

    browser.find_element_by_css_selector("input[type='submit']").click()
    sleep(2)

    browser.find_element_by_css_selector("input[type='submit']").click()
    sleep(2)

    browser.find_element_by_link_text("竹早テニスコート（土日祝）").click()
    sleep(2)

    court_number_full = jaconv.h2z(str(court_number), digit=True)
    browser.find_element_by_link_text(f"第{court_number_full}コート土日祝").click()
    sleep(2)

    # element = driver.find_element_by_partial_link_text(u"(日)")
    element = browser.find_element_by_css_selector("form")
    # print(element.text)
    schedule_parser(element.text, court_number, mysql)

    browser.find_element_by_css_selector("input[value='  次の週  ']").click()
    sleep(2)

    browser.save_screenshot("images/" + dtstr + ".png")


if __name__ == "__main__":
    try:

        # 接続する
        conn = mysql.connector.connect(
            host="db", port=3306, user="root", password="root"
        )
        mysql = Mysql()

        # browser = webdriver.Firefox()  # 普通のFilefoxを制御する場合
        # browser = webdriver.Chrome()   # 普通のChromeを制御する場合

        # HEADLESSブラウザに接続
        browser = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME,
        )

        # Googleで検索実行
        bunkyo_scraper(browser, mysql)

    finally:
        # 終了
        browser.close()
        browser.quit()
        # 接続を閉じる
        mysql.close()
