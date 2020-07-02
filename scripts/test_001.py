import pytest,allure

@allure.feature("allure测试")
@allure.story("测试用例集")
class Test_allure():
    @allure.title("用例1")
    # 测试步骤
    @allure.step(title="这是第一个测试用例")
    # 测试缺陷
    @allure.issue("http://www.163.com")
    # 测试用例
    @allure.testcase("http://www.baidu.com")
    # 用例级别
    @allure.severity("TRIVIAL")
    def test_num1(self):
        # 测试描述信息
        allure.attach('这是一个用例描述','试一下')
        assert 0

    @allure.title("用例2")
    @allure.testcase("http://www.baidu.com")
    @allure.severity("critical")
    def test_num2(self):
        allure.attach("这是一个用例描述","嗯嗯哈哈")
        assert 1

    @allure.title("用例3")
    @allure.testcase("http://www.baidu.com/test")
    @allure.severity("blocker")
    def test_num3(self):
        allure.attach("这是一个用例描述", "啊啊啊大风刮")
        assert 1

    @allure.title("用例4")
    @allure.testcase("http://www.baidu.com")
    @allure.severity("normal")
    def test_num4(self):
        allure.attach("这是一个用例描述", "呵呵呵钱钱钱")
        assert 0

#
# if __name__ == '__main__':
#     pytest.main(["-s","--alluredir=../report4","test_001.py"])
#     # pytest.main(["--alluredir=../report2", "test_001.py"])