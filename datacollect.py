import streamlit as st
import pandas as pd
import re
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def init_driver():
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--disable-gpu")  

    return webdriver.Chrome(options=options)

def get_text_safe(driver, xpath, multiple=False):
    try:
        if multiple:
            return [elem.text.strip() for elem in driver.find_elements(By.XPATH, xpath)]
        return driver.find_element(By.XPATH, xpath).text.strip()
    except:
        return [] if multiple else "Not Available"

def get_attr_safe(driver, xpath, attr="href", multiple=False):
    try:
        if multiple:
            return [elem.get_attribute(attr) for elem in driver.find_elements(By.XPATH, xpath)]
        return driver.find_element(By.XPATH, xpath).get_attribute(attr)
    except:
        return [] if multiple else "Not Available"

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except:
        return None

def list_jobs():
    st.subheader("📌 Sarkari Job Listings")

    # Scrape jobs
    driver = init_driver()
    driver.get("https://www.sarkariresult.com/latestjob/")
    job_elements = driver.find_elements(By.XPATH, '//div[@id="post"]/ul/li')

    jobs = []
    for job in job_elements[:30]:
        try:
            link_elem = job.find_element(By.TAG_NAME, "a")
            name = link_elem.text
            link = link_elem.get_attribute("href")
            date_text = job.text
            match = re.search(r"Last Date\s*:\s*(\d{2}/\d{2}/\d{4})", date_text)
            last_date = match.group(1) if match else "31/12/2099"

            jobs.append({
                "Job Title": name,
                "Deadline": last_date,
                "Link": link,
            })
        except:
            continue

    driver.quit()

    if not jobs:
        st.warning("🚫 No jobs found.")
        return

    # 🔍 Filter UI
    with st.expander("🔍 Filter Jobs", expanded=True):
        keyword = st.text_input("Search by keyword", "")
        deadline_only = st.checkbox("Only show active jobs (deadline in future)", True)

    today = datetime.now()
    filtered = []
    for job in jobs:
        job_deadline_date = parse_date(job["Deadline"])
        matches_keyword = keyword.lower() in job["Job Title"].lower()
        is_active = job_deadline_date is None or job_deadline_date >= today

        if matches_keyword and (not deadline_only or is_active):
            filtered.append(job)

    if not filtered:
        st.info("🙁 No jobs match your filter.")
        return

   
    for i, job in enumerate(filtered):
        with st.container():
            st.markdown(f"### {job['Job Title']}")
            st.markdown(f"**🗓 Deadline:** {job['Deadline']}")
            if st.button("🔍 View Details", key=f"view_{i}"):
                st.session_state["selected_job"] = job["Link"]
                st.rerun()

def get_link_by_text(driver, *keywords):
    for keyword in keywords:
        keyword_lower = keyword.lower()
        try:
            elem = driver.find_element(
                By.XPATH,
                f"//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{keyword_lower}') or "
                f"contains(translate(@title, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{keyword_lower}')]"
            )
            return elem.get_attribute("href")
        except:
            continue
    return "Not Available"



def detail_job():
    job_link = st.session_state.get("selected_job", None)
    if not job_link:
        st.warning("⚠️ No job selected.")
        return

    driver = init_driver()
    driver.get(job_link)
    st.subheader("📄 Job Details")

    try:
        job_name = get_text_safe(driver, ".//table[2]//td[@valign='top'][1]/h2/span/b") or "No Title"
        job_desc = get_text_safe(driver, ".//tr[@valign='top']//tr[3]/td[2]") or "No Description Provided"

        # Important Dates
        application_dates = get_text_safe(driver, ".//table[2]/tbody/tr[2]/td/ul/li/b", multiple=True)
        last_date = get_text_safe(driver, ".//table[2]/tbody/tr[2]/td/ul/li[2]/span/b")
        last_datec = get_text_safe(driver, ".//table[2]/tbody/tr[2]/td/ul/li[3]/b")
        exam_date = get_text_safe(driver, ".//table[2]/tbody/tr[2]/td/ul/li[4]/b")
        admit_card_date = get_text_safe(driver, ".//table[2]/tbody/tr[2]/td/ul/li[5]/b")

        # Application Fee
        fee_categories = get_text_safe(driver, ".//table[2]/tbody/tr[2]/td[2]/ul/li", multiple=True)
        fee_amounts = get_text_safe(driver, ".//table[2]/tbody/tr[2]/td[2]/ul/li/b", multiple=True)

        # Age Limit
        minimum_age = get_text_safe(driver, ".//table[2]/tbody/tr[3]/td/ul/li/b")
        maximum_age = get_text_safe(driver, ".//table[2]/tbody/tr[3]/td/ul/li[2]/b")

        # Positions
        position_rows = driver.find_elements(By.XPATH, ".//table[2]/tbody/tr[td[@valign='top'] and count(td)=3]")
        positions = []
        for row in position_rows:
            try:
                cols = row.find_elements(By.XPATH, ".//td")
                if len(cols) == 3:
                    name = cols[0].text.strip()
                    vacancy = cols[1].text.strip()
                    eligibility = cols[2].text.strip()
                    if name and vacancy and eligibility:
                        positions.append((name, vacancy, eligibility))
            except:
                continue

        # Links
        apply_link = get_link_by_text(driver, "apply online", "apply", "registration")
        notif_link = get_link_by_text(driver, "notification", "download notification", "advt")
        official_link = get_link_by_text(driver, "official", "visit official")

        driver.quit()

        # 🧾 Job Title & Description
        st.write(f"### 📌 {job_name}")
        st.text_area("📝 Job Description", job_desc, height=150)

        # ✅ KEEPING YOUR ORIGINAL UI FOR DATES
        st.write("### 📆 Important Dates")
        st.write(f"- Application Start: **{application_dates[0] if application_dates else 'N/A'}**")
        st.write(f"- Last Date to Apply: **{last_date}**")
        st.write(f"- Form Completion Last Date: **{last_datec}**")
        st.write(f"- Exam Date: **{exam_date}**")
        st.write(f"- Admit Card Release: **{admit_card_date}**")

        # 💸 Application Fee
        st.write("### 💰 Application Fee")
        if fee_categories and fee_amounts:
            for category, fee in zip(fee_categories, fee_amounts):
                st.write(f"- 💸 **{category}:** {fee}")
        else:
            st.write("No fee info found.")

        # 👶 Age
        st.write(f"🧑‍🎓 **Age Limit:** Minimum {minimum_age}, Maximum {maximum_age}")

        st.markdown("### 📋 Available Positions")
        if positions:
            for idx, (name, vacancy, eligibility) in enumerate(positions, 1):
                with st.expander(f"🔹 Position {idx}: {name}"):
                    st.markdown(f"- 🧾 **Vacancies:** {vacancy}")
                    st.markdown(f"- 📚 **Eligibility:** {eligibility}")
        else:
            st.info("ℹ️ No positions listed.")
        st.markdown("---")

        # 🔗 Important Links
        st.markdown("### 🔗 Useful Links")
        col1, col2, col3 = st.columns(3)
        with col1:
            if apply_link and apply_link != "Not Available":
                st.link_button("✅ Apply Now", apply_link)
            else:
                st.write("❌ No Apply Link")

        with col2:
            if notif_link and notif_link != "Not Available":
                st.link_button("📜 Notification", notif_link)
            else:
                st.write("❌ No Notification")

        with col3:
            if official_link and official_link != "Not Available":
                st.link_button("🌐 Official Site", official_link)
            else:
                st.write("❌ No Official Site")

        # ⬅️ Back Button
        st.markdown("---")
        if st.button("🔙 Back to Listings"):
            del st.session_state["selected_job"]
            st.rerun()

    except Exception as e:
        st.error(f"❌ Error: {e}")
        driver.quit()

def list_admit_cards():
    st.subheader("🎟 Direct Admit Card Download")

    driver = init_driver()
    driver.get("https://www.sarkariresult.com/admitcard/")
    card_elements = driver.find_elements(By.XPATH, '//div[@id="post"]/ul/li')

    cards = []
    for card in card_elements[:20]:
        try:
            link_elem = card.find_element(By.TAG_NAME, "a")
            title = link_elem.text.strip()
            detail_link = link_elem.get_attribute("href")

            # Open the detail link in a new tab
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(detail_link)

            # Try to find the final download link
            try:
                download_elem = driver.find_element(
                    By.XPATH,
                    '//a[contains(translate(text(), "CLICK HERE", "click here"), "click here") and contains(@href, "http")]'
                )
                final_download_link = download_elem.get_attribute("href")
            except:
                final_download_link = "Not Available"

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            cards.append({
                "Title": title,
                "Download": final_download_link
            })

        except Exception as e:
            print(f"Error: {e}")
            continue

    driver.quit()

    # UI display
    for item in cards:
        st.markdown(f"### 📄 {item['Title']}")
        if item["Download"] != "Not Available":
            st.link_button("📥 Download Admit Card", item["Download"])
        else:
            st.warning("❌ Download link not found.")



def list_results():
    st.subheader("📢 Direct Results Download")

    driver = init_driver()
    driver.get("https://www.sarkariresult.com/result/")
    result_elements = driver.find_elements(By.XPATH, '//div[@id="post"]/ul/li')

    results = []
    for result in result_elements[:20]:
        try:
            link_elem = result.find_element(By.TAG_NAME, "a")
            title = link_elem.text.strip()
            detail_link = link_elem.get_attribute("href")

            # Open detail link in a new tab
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(detail_link)

            # Try to extract the final download link
            try:
                download_elem = driver.find_element(
                    By.XPATH,
                    '//a[contains(translate(text(), "CLICK HERE", "click here"), "click here") and contains(@href, "http")]'
                )
                final_download_link = download_elem.get_attribute("href")
            except:
                final_download_link = "Not Available"

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            results.append({
                "Title": title,
                "Download": final_download_link
            })

        except Exception as e:
            print(f"Error: {e}")
            continue

    driver.quit()

    # Display result list
    for item in results:
        st.markdown(f"### 🧾 {item['Title']}")
        if item["Download"] != "Not Available":
            st.link_button("📥 Download Result", item["Download"])
        else:
            st.warning("❌ Download link not found.")









