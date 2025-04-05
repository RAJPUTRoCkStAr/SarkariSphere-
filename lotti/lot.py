import json
import requests
from streamlit_lottie import st_lottie
def load_lottiefile(filepath:str):
    with open (filepath, 'r',encoding='utf-8') as f:
        return json.load(f)
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
Admit_card = load_lottiefile("./lotti/Admit_card.json")
Front_page = load_lottiefile("./lotti/Front_page.json")
job_detail = load_lottiefile("./lotti/job_detail.json")
Result = load_lottiefile("./lotti/Result.json")