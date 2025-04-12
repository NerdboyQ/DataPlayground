import requests, time
from datetime import datetime
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Chrome, ChromeOptions, Keys

# Collect stats from NIH:
# National Institue of Minority Health and Health Disparities
url = "https://hdpulse.nimhd.nih.gov/data-portal/social"

class NIH_Scraper:
    def __init__(self, state:str ="North Carolina", delay: int =5):
        self.Topics = []
        self._delay = delay
        self._state = state
        opts = ChromeOptions()
        opts.add_argument("--start-maximized")
        self.driver = Chrome(options=opts)
        self.driver.get(url)
        time.sleep(self._delay/2)
        self.select_area()

        topic_sel_fld = self.driver.find_element(By.ID, "socialtopic")
        self.Topics = [n.text for n in topic_sel_fld.find_elements(By.TAG_NAME, "option")]
        self.Topics = self.Topics[1:]
        print(self.Topics)
        for i in range(len(self.Topics)): self.get_topic_data(idx = i)
        time.sleep(self._delay)

    def select_area(self) -> bool:
        sel_fld = self.driver.find_element(By.ID, "statefips")
        sel_fld.click()
        for state_fld in sel_fld.find_elements(By.TAG_NAME, "option")[3:]:
            if state_fld.text.find(self._state) > -1:
                Select(sel_fld).select_by_visible_text(state_fld.text)
                time.sleep(self._delay/2)
                return True
        
        return False        

    def get_topic_data(self, idx: int):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Table").click()
        opic_sel_fld = self.driver.find_element(By.ID, "socialtopic")
        if idx: Select(opic_sel_fld).select_by_index(index=idx)
        if self.select_area():
            print("="*60)
            print("Topic:", self.Topics[idx])
            time.sleep(self._delay/2)
            Var_fld = self.driver.find_element(By.ID, "demo")
            RaE_fld = self.driver.find_element(By.ID, "race")
            Sex_fld = self.driver.find_element(By.ID, "sex")
            Age_fld = self.driver.find_element(By.ID, "age")
            Var_opts = [x.text for x in Var_fld.find_elements(By.TAG_NAME, "option")][1:]
            RaE_opts = [x.text for x in RaE_fld.find_elements(By.TAG_NAME, "option")][1:]
            Sex_opts = [x.text for x in Sex_fld.find_elements(By.TAG_NAME, "option")][1:]
            Age_opts = [x.text for x in Age_fld.find_elements(By.TAG_NAME, "option")][1:]
            
            # print(" - Variables:\n\t", Var_opts)
            # print(" - Race/Ethnicity:\n\t", RaE_opts)
            # print(" - Sex:\n\t", Sex_opts)
            # print(" - Age:\n\t", Age_opts)
            self.collect_tbl_data()

    def collect_tbl_data(self):
        table = self.driver.find_element(By.TAG_NAME, "table")
        tbl_title = table \
            .find_element(By.TAG_NAME, "caption") \
            .find_element(By.TAG_NAME, "span")
        print(tbl_title.text)
        headers = table \
            .find_elements(By.TAG_NAME, "th")
        headers = [h.find_element(By.TAG_NAME, "span").text for h in headers]
        print(headers)
        data = {h:[] for h in headers}
        trows = table\
            .find_element(By.TAG_NAME, "tbody") \
            .find_elements(By.TAG_NAME, "tr")
        
        for trow in trows:
            cols = [c.find_element(By.TAG_NAME, "span").text for c in trow.find_elements(By.TAG_NAME, "td")]
            if cols[0].find("County") < 0: continue
            for i in range(len(headers)): 
                data[headers[i]].append(cols[i])

        pprint(data,indent=2)
    
    def __del__(self):
        self.driver.close()

NIH_Scraper()