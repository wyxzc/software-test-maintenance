# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# class TestOnlineBoutique:
#     def setup_method(self, method):
#         # self.driver = webdriver.Chrome()
#         self.driver = webdriver.Edge()  # 使用 Edge 浏览器
#         # self.driver = webdriver.Edge(executable_path="C:/Users/15706/Downloads/edgedriver_win64/msedgedriver.exe")

#         self.vars = {}

#     def teardown_method(self, method):
#         self.driver.quit()

#     def test_shopping_flow(self):
#         # 记录页面加载时间
#         start_time = time.time()
#         self.driver.get("http://127.0.0.1:44065/")
#         self.driver.set_window_size(1722, 1034)
#         load_time = time.time() - start_time
#         print(f"页面加载时间: {load_time:.2f} 秒")

#         # 模拟用户浏览和购买商品的操作，并记录每个操作的响应时间
#         actions = [
#             {"description": "点击第一个商品", "locator": (By.CSS_SELECTOR, ".col-md-4:nth-child(2) .hot-product-card-img-overlay")},
#             {"description": "点击添加到购物车", "locator": (By.CSS_SELECTOR, ".cymbal-button-primary")},
#             {"description": "点击继续购物", "locator": (By.LINK_TEXT, "Continue Shopping")},
#             {"description": "点击第二个商品", "locator": (By.CSS_SELECTOR, ".col-md-4:nth-child(3) .hot-product-card-img-overlay")},
#             {"description": "点击添加到购物车", "locator": (By.CSS_SELECTOR, ".cymbal-button-primary")},
#             {"description": "点击继续购物", "locator": (By.LINK_TEXT, "Continue Shopping")},
#             {"description": "点击第三个商品", "locator": (By.CSS_SELECTOR, ".col-md-4:nth-child(4) .hot-product-card-img-overlay")},
#             {"description": "点击添加到购物车", "locator": (By.CSS_SELECTOR, ".cymbal-button-primary")},
#             {"description": "点击查看购物车", "locator": (By.CSS_SELECTOR, ".cymbal-button-secondary")},
#             {"description": "点击第四个商品", "locator": (By.CSS_SELECTOR, ".col-md-4:nth-child(7) .hot-product-card-img-overlay")},
#             {"description": "点击添加到购物车", "locator": (By.CSS_SELECTOR, ".cymbal-button-primary")},
#             {"description": "点击继续购物", "locator": (By.LINK_TEXT, "Continue Shopping")},
#         ]

#         for action in actions:
#             start = time.time()
#             self.driver.find_element(*action["locator"]).click()
#             end = time.time()
#             print(f"{action['description']} 响应时间: {end - start:.2f} 秒")

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestOnlineBoutique:
    def setup_method(self, method):
        # self.driver = webdriver.Edge()  # 使用 Edge 浏览器
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_shopping_flow(self):
        # 记录页面加载时间
        start_time = time.time()
        self.driver.get("http://127.0.0.1:32965")
        self.driver.set_window_size(1722, 1034)
        load_time = time.time() - start_time
        print(f"页面加载时间: {load_time:.2f} 秒")

        # 每一步操作带有响应时间记录
        def click_and_measure(description, by, locator):
            start = time.time()
            self.driver.find_element(by, locator).click()
            end = time.time()
            print(f"{description} 响应时间: {end - start:.2f} 秒")

        click_and_measure("点击第一个商品", By.CSS_SELECTOR, ".col-md-4:nth-child(2) .hot-product-card-img-overlay")
        click_and_measure("点击添加到购物车", By.CSS_SELECTOR, ".cymbal-button-primary")
        click_and_measure("点击继续购物", By.LINK_TEXT, "Continue Shopping")
        
        click_and_measure("点击第二个商品", By.CSS_SELECTOR, ".col-md-4:nth-child(3) .hot-product-card-img-overlay")
        click_and_measure("点击添加到购物车", By.CSS_SELECTOR, ".cymbal-button-primary")
        click_and_measure("点击提交购物订单", By.CSS_SELECTOR, ".cymbal-button-primary:nth-child(1)")
        click_and_measure("点击继续购物", By.LINK_TEXT, "Continue Shopping")
        
        click_and_measure("点击第三个商品", By.CSS_SELECTOR, ".col-md-4:nth-child(4) .hot-product-card-img-overlay")
        click_and_measure("点击添加到购物车", By.CSS_SELECTOR, ".cymbal-button-primary")
        click_and_measure("点击移除出购物车", By.CSS_SELECTOR, ".cymbal-button-secondary")
        
        click_and_measure("点击第四个商品", By.CSS_SELECTOR, ".col-md-4:nth-child(7) .hot-product-card-img-overlay")
        click_and_measure("点击添加到购物车", By.CSS_SELECTOR, ".cymbal-button-primary")
        click_and_measure("点击提交购物订单", By.CSS_SELECTOR, ".cymbal-button-primary:nth-child(1)")
        click_and_measure("点击继续购物", By.LINK_TEXT, "Continue Shopping")
