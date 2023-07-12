import time
import pytest
from selenium.webdriver.common.by import By
from TestData.home_login_data import HomeLoginData
from pageObjects.homepage import HomePage
from utilities.basefile import Base


class TestTrip(Base):

    def test_home(self, get_data):

        log = self.get_logger()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        home_obj = HomePage(self.driver)
        home_obj.meth_user().send_keys(get_data["Username"])
        home_obj.meth_pass().send_keys(get_data["Password"])
        time.sleep(5)
        home_obj.meth_hide().click()
        home_obj.meth_butt1().click()

        slot = 20
        for i in range(12):
            time.sleep(1)
            self.driver.execute_script(f"window.scrollBy(0,{slot})", "")
            slot += 20
            time.sleep(1)

        home_obj.meth_scroll9()
        time.sleep(3)
        home_obj.meth_scroll_up()

        # searching the jobs
        home_obj.meth_search1().click()
        home_obj.meth_design().send_keys("Python Software Developer")
        time.sleep(3)
        lists_design = home_obj.meth_list_design()
        for ll in lists_design:
            if ll.text == "Python Software Developer":
                ll.click()
                break

        home_obj.meth_exp().click()
        lists_exp = home_obj.meth_list_exp()
        for ex in lists_exp:
            txt = ex.text
            if txt == "2 years":
                ex.click()
                break

        home_obj.meth_location().send_keys("bangalore")
        list_places = home_obj.meth_list_locations()
        for place in list_places:
            tt = place.text
            if tt == "Bangalore":
                place.click()
                break

        # second page
        second_obj = home_obj.meth_search2()
        time.sleep(2)
        second_obj.meth_work_f_home().click()
        time.sleep(2)
        second_obj.meth_remote().click()
        time.sleep(2)

        # Department
        second_obj.meth_view().click()
        time.sleep(2)
        second_obj.meth_depart_input().send_keys("engineering")
        time.sleep(2)
        second_obj.meth_depart_name().click()
        time.sleep(2)
        second_obj.meth_depart_button().click()
        time.sleep(2)

        # salary
        second_obj.meth_salary_view().click()
        time.sleep(2)
        second_obj.meth_salary_option().click()
        time.sleep(2)
        second_obj.meth_salary_button().click()
        time.sleep(2)

        # company type
        second_obj.meth_company_choice().click()
        time.sleep(2)

        # role category
        second_obj.meth_role_cate().click()
        time.sleep(2)

        # education
        second_obj.meth_educ_view().click()
        time.sleep(2)
        second_obj.meth_educ_option().click()
        time.sleep(2)
        second_obj.meth_educ_button().click()

        slot2 = 10
        # scrolling after all
        for j in range(30):
            self.driver.execute_script(f"window.scrollBy(0,{slot})", "")
            time.sleep(1)
            slot2 += 10

        self.driver.execute_script("window.scrollBy(300,document.body.scrollHeight)", "")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 0)", "")

        # logout section
        second_obj.meth_logout_option().click()
        second_obj.meth_logout_button().click()

    @pytest.fixture(params=HomeLoginData().get_data_xlsx())
    def get_data(self, request):
        return request.param









