# PART 1 : IMPORT LIBRARIES
import random
import sqlite3
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

# PART 2 : CLASS MEMBER
class Member:
    def __init__(self,member_id,name,age,weight_kg,is_vip=False):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
        self.is_vip = is_vip
    def get_member_type(self):
        if self.is_vip:
            return "VIP"
        return "General"
    def __str__(self):
        return (
            f"Member ID: {self.member_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Weight: {self.weight_kg} kg | "
            f"Type: {self.get_member_type()}"
        )

        # PART 3 : CLASS PACKAGE
class Package:
    def __init__(self,package_id,package_name,price,max_hours,duration_days):
        self.package_id = package_id
        self.package_name = package_name
        self.price = price
        self.max_hours = max_hours
        self.duration_days = duration_days
    def get_package_info(self):
        return {
            "package_id": self.package_id,
            "package_name": self.package_name,
            "price": self.price,
            "max_hours": self.max_hours,
            "duration_days": self.duration_days
        }
    def __str__(self):
        return (
            f"Package ID: {self.package_id} | "
            f"Package: {self.package_name} | "
            f"Price: {self.price} บาท | "
            f"Max Hours: {self.max_hours}"
        )

        # PART 4 : CLASS MEMBERSHIPPACKAGE
class MembershipPackage:
    def __init__(self,booking_id,member,package,hours,service_type,booking_date):
        self.booking_id = booking_id
        self.member = member
        self.package = package
        self.hours = hours
        self.service_type = service_type
        self.booking_date = booking_date
        self.status = "Pending"
    def calculate_price(self):
        # คำนวณส่วนลด 10% หากสมาชิกเป็น VIP
        base_price = self.package.price
        if self.member.is_vip:
            return round(base_price * 0.90, 2)
        return round(base_price, 2)
    def mark_done(self):
        self.status = "Completed"
    def __str__(self):
        return (
            f"Booking ID: {self.booking_id} | "
            f"Member: {self.member.name} | "
            f"Package: {self.package.package_name} | "
            f"Service: {self.service_type} | "
            f"Price: {self.calculate_price()} | "
            f"Status: {self.status}"
        )
    # PART 5 : GENERATE 300 DATA
first_names = [
    "ธนกฤต", "ณัฐวุฒิ", "พชร", "ภูริณัฐ", "กิตติพงศ์", "วรากร", "ธนภัทร", "ภัทรพล", "ณัฐพล", "ศุภกร",
    "ก้องภพ", "ชยพล", "รัชชานนท์", "ธีรภัทร", "ปวริศ", "กรวิชญ์", "นนทกร", "ภาคภูมิ", "อัครพล", "สิรวิชญ์",
    "พิมพ์ชนก", "ชนากานต์", "ณิชาภัทร", "ศิริพร", "กัญญารัตน์", "ชลธิชา", "ปุณณภา", "ธัญชนก", "ณัฐธิดา", "พิชชาภา",
    "วริศรา", "สุภัสสรา", "กมลชนก", "ปภาวรินทร์", "อริสรา", "พัชราภา", "นภัสสร", "ชญานิศ", "กุลธิดา", "รินรดา"
]
last_names = [
    "ศรีสุวรรณ", "วัฒนกุล", "เจริญชัย", "พัฒนานนท์", "วงศ์วัฒนะ", "สุวรรณดี", "บุญญฤทธิ์", "ชัยวัฒน์", "รัตนกุล", "ศุภกิจ",
    "ธนากุล", "วัฒนชัย", "เจริญสุข", "พงศ์ไพบูลย์", "สิริวัฒน์", "กิตติธร", "อนันต์ชัย", "รุ่งเรือง", "พัฒนกุล", "ศรีวัฒนานนท์"
]

def generate_name():
    return random.choice(first_names) + " " + random.choice(last_names)
def generate_booking_date():
    start_date = datetime(2026, 1, 1)
    random_days = random.randint(0, 364)
    return start_date + timedelta(days=random_days)
packages = [
    Package(1, "Basic", 1200, 10, 30),
    Package(2, "Premium", 2500, 20, 30),
    Package(3, "VIP", 5000, 50, 60)
]
services = ["Gym", "Personal Training", "Group Class"]
members_300 = []
member_data = {}
for i in range(1, 301):
    member = Member(
        member_id=i,
        name=generate_name(),
        age=random.randint(18, 40),
        weight_kg=round(random.uniform(45, 100), 1),
        is_vip=random.choice([True, False])
    )
    members_300.append(member)
    member_data[i] = member

memberships_300 = []
for i in range(1, 301):
    selected_member = random.choice(members_300)
    selected_package = random.choice(packages)
    selected_service = random.choice(services)
    selected_hours = random.choice([1, 1.5, 2, 2.5, 3])
    membership = MembershipPackage(
        booking_id=i,
        member=selected_member,
        package=selected_package,
        hours=selected_hours,
        service_type=selected_service,
        booking_date=generate_booking_date()
    )
    membership.mark_done()
    memberships_300.append(membership)

# PART 6 : CREATE DATAFRAME
data = []
for booking in memberships_300:
    data.append({
        "booking_id": booking.booking_id,
        "member_id": booking.member.member_id,
        "name": booking.member.name,
        "age": booking.member.age,
        "weight_kg": booking.member.weight_kg,
        "is_vip": booking.member.is_vip,
        "package_id": booking.package.package_id,
        "package_name": booking.package.package_name,
        "price": booking.calculate_price(),
        "hours": booking.hours,
        "service_type": booking.service_type,
        "booking_date": booking.booking_date.strftime("%Y-%m-%d"),
        "status": booking.status
    })
membership_df = pd.DataFrame(data)
display(membership_df.head())

print("\nจำนวนข้อมูล:",len(membership_df))

# PART 7 : BUSINESS QUESTIONS - PANDAS
from google.colab import auth
from google.cloud import bigquery

auth.authenticate_user()
project_id = 'deadlinesurvivorr'
client = bigquery.Client(project=project_id)
#ดึงข้อมูลจาก BigQuery
query = """SELECT *
           FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`"""
membership_df = client.query(query).to_dataframe()
# คำถามที่ 1 :บริการประเภทใดสร้างรายได้รวมมากที่สุด?
q1_pandas = (membership_df.groupby("service_type").agg(total_revenue=("price", "sum"))
.sort_values("total_revenue", ascending=False).reset_index().head(1))

print("QUESTION 1")
display(q1_pandas)

# คำถามที่ 2 : แต่ละบริการมีจำนวนการจองและรายได้รวมเท่าไร?
q2_pandas = (membership_df.groupby("service_type")
.agg(total_bookings=("booking_id", "count"),total_revenue=("price", "sum"))
.sort_values("total_revenue", ascending=False).reset_index())

print("\nQUESTION 2")
display(q2_pandas)

# คำถามที่ 3 : น้ำหนักเฉลี่ยของสมาชิกแต่ละบริการเท่าไร?
q3_pandas = (membership_df.groupby("service_type")
.agg(avg_weight=("weight_kg", lambda x: round(x.mean(), 2)))
.sort_values("avg_weight", ascending=False).reset_index())

print("QUESTION 3")
display(q3_pandas)

# คำถามที่ 4 : บริการประเภทใดมีค่าเฉลี่ยรายได้ต่อการจองสูงสุด?
q4_pandas = (membership_df.groupby("service_type")
.agg(avg_revenue_per_booking=("price", lambda x: round(x.mean(), 2)))
.sort_values("avg_revenue_per_booking", ascending=False).reset_index().head(1))

print("QUESTION 4")
display(q4_pandas)

# คำถามที่ 5 : บริการประเภทใดมีสัดส่วนรายได้ (Revenue Share %)คิดเป็นกี่เปอร์เซ็นต์ของรายได้รวมทั้งหมด?
total_sum = membership_df['price'].sum()
q6_pandas = (membership_df.groupby("service_type")
.agg(total_revenue=("price", "sum"),revenue_share_pct=("price", lambda x: round((x.sum() / total_sum) * 100, 2)))
.sort_values("revenue_share_pct", ascending=False).reset_index())

print("\nQUESTION 5")
display(q6_pandas)

# คำถามที่ 6 : หากจัดกลุ่มตามบริการ ราคาตั๋วที่ถูกที่สุดและแพงที่สุดของแต่ละบริการคือเท่าไร?
q6_pandas = (membership_df.groupby("service_type")
.agg(min_price=("price", "min"),max_price=("price", "max")).reset_index())

print("\nQUESTION 6")
display(q6_pandas)

# คำถามที่ 7 : ลูกค้าที่มีน้ำหนักเกิน 70 kg นิยมจองบริการประเภทใดมากที่สุด?
q7_pandas = (membership_df[membership_df['weight_kg'] > 70].groupby("service_type")
.agg(booking_count=("booking_id", "count")).sort_values("booking_count", ascending=False).reset_index().head(1))

print("\nQUESTION 7")
display(q7_pandas)

# คำถามที่ 8 : เปรียบเทียบค่ามัธยฐาน (Median) ของราคาระหว่างบริการต่างๆ เพื่อดูระดับราคาของบริการส่วนใหญ่
q8_pandas = (membership_df.groupby("service_type")
.agg(median_price=("price", "median")).reset_index())
print("\nQUESTION 8")
display(q8_pandas)

# PART 8 : SQLITE DATABASE
conn = sqlite3.connect("fitness_gym.db")
membership_df.to_sql("gym_memberships",conn,if_exists="replace",index=False)
print("บันทึกข้อมูลลง SQLite สำเร็จ")

# PART 9 : SQL ANALYSIS
# QUESTION 1
q1_sql = client.query("""
    SELECT service_type, SUM(SAFE_CAST(price AS INT64)) AS total_revenue
    FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`
    GROUP BY service_type
    ORDER BY total_revenue DESC
    LIMIT 1""").to_dataframe()

print("QUESTION 1 - SQL")
display(q1_sql)

# QUESTION 2
q2_sql = client.query("""
    SELECT service_type, COUNT(booking_id) AS total_bookings, SUM(SAFE_CAST(price AS INT64)) AS total_revenue
    FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`
    GROUP BY service_type
    ORDER BY total_revenue DESC
""").to_dataframe()

print("\nQUESTION 2 - SQL")
display(q2_sql)

# QUESTION 3
q3_sql = client.query("""
    SELECT
        service_type,
        ROUND(AVG(SAFE_CAST(weight_kg AS FLOAT64)), 2) AS avg_weight
    FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`
    GROUP BY service_type
    ORDER BY avg_weight DESC""").to_dataframe()

print("\nQUESTION 3 - SQL")
display(q3_sql)

# QUESTION 4
q4_sql = client.query("""
    SELECT service_type,
        ROUND(AVG(SAFE_CAST(price AS INT64)), 2) AS avg_revenue_per_booking
    FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`
    GROUP BY service_type
    ORDER BY avg_revenue_per_booking DESC
    LIMIT 1""").to_dataframe()

print("\nQUESTION 4 - SQL")
display(q4_sql)

# QUESTION 5
q5_sql = client.query("""
    SELECT service_type,
        SUM(SAFE_CAST(price AS INT64)) AS total_revenue,
        ROUND((SUM(SAFE_CAST(price AS INT64)) / (SELECT SUM(SAFE_CAST(price AS INT64)) FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`)) * 100, 2) AS revenue_share_pct
    FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`
    GROUP BY service_type
    ORDER BY revenue_share_pct DESC
""").to_dataframe()

print("\nQUESTION 5 - SQL")
display(q5_sql)

# QUESTION 6
q6_sql = client.query("""
    SELECT service_type,
        MIN(SAFE_CAST(price AS INT64)) AS min_price,
        MAX(SAFE_CAST(price AS INT64)) AS max_price
    FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`
    GROUP BY service_type""").to_dataframe()

print("\nQUESTION 6 - SQL")
display(q6_sql)

# QUESTION 7
q7_sql = client.query("""
    SELECT service_type,
        COUNT(*) AS booking_count
    FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`
    WHERE SAFE_CAST(weight_kg AS FLOAT64) > 70
    GROUP BY service_type
    ORDER BY booking_count DESC
    LIMIT 1""").to_dataframe()

print("\nQUESTION 7 - SQL")
display(q7_sql)

# QUESTION 8
q8_sql = client.query("""
    SELECT DISTINCT
        service_type,
        PERCENTILE_CONT(SAFE_CAST(price AS INT64), 0.5) OVER(PARTITION BY service_type) AS median_price
    FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`
    """).to_dataframe()

print("\nQUESTION 8 - SQL")
display(q8_sql)

# PART 10 : DATABASE TABLES + JOIN

# MEMBERS
members_df = pd.DataFrame([
    {
        "member_id": member.member_id,
        "name": member.name,
        "age": member.age,
        "weight_kg": member.weight_kg,
        "is_vip": int(member.is_vip)
    }
    for member in members_300
])
members_df.to_sql("members",conn,if_exists="replace",index=False)

# PACKAGES
packages_df = pd.DataFrame([
    package.get_package_info()
    for package in packages
])
packages_df.to_sql("packages",conn,if_exists="replace",index=False)

# SERVICES
services_df = pd.DataFrame({"service_id": range(1,len(services) + 1),"service_name": services})
services_df.to_sql("services",conn,if_exists="replace",index=False)

# CREATE MEMBERSHIP TABLE
service_map = {service: i + 1
               for i, service in enumerate(services)}
bookings_df = membership_df.copy()
bookings_df["service_id"] = (bookings_df["service_type"].map(service_map))
bookings_df = bookings_df[
    [
        "booking_id",
        "member_id",
        "package_id",
        "service_id",
        "price",
        "hours",
        "booking_date",
        "status"
    ]
]
bookings_df.to_sql("membership_bookings",conn,if_exists="replace",index=False)

# JOIN 4 TABLES
join_result = pd.read_sql_query("""
    SELECT
        b.booking_id,
        m.name
        AS member_name,
        CASE
            WHEN m.is_vip = 1
            THEN 'VIP'
            ELSE 'General'
        END
        AS member_type,
        p.package_name,
        s.service_name,
        b.price,
        b.hours,
        b.booking_date,
        b.status
    FROM membership_bookings b
    JOIN members m
        ON b.member_id = m.member_id
    JOIN packages p
        ON b.package_id = p.package_id
    JOIN services s
        ON b.service_id = s.service_id
    ORDER BY b.booking_id
""",conn)

print("JOIN 4 TABLES สำเร็จ")
display(join_result.head(10))

vip_discount_sql = pd.read_sql_query(
    """SELECT
        b.booking_id,
        m.name
        AS member_name,
        CASE
            WHEN m.is_vip = 1
            THEN 'VIP'
            ELSE 'General'
        END
        AS member_type,
        b.price
        AS original_price,
        CASE
            WHEN m.is_vip = 1
            THEN b.price * 0.10
            ELSE 0
        END
        AS discount,
        CASE
            WHEN m.is_vip = 1
            THEN b.price * 0.90
            ELSE b.price
        END
        AS final_price
    FROM membership_bookings b
    JOIN members m
        ON b.member_id = m.member_id
    ORDER BY b.booking_id
""", conn)


display(vip_discount_sql.head(10))

# PART 11 : DATA VISUALIZATION & BUSINESS INSIGHTS

# GRAPH 1: Total Revenue by Service
plt.figure(figsize=(8, 5))
q2_pandas.plot(
    kind="bar",
    x="service_type",
    y="total_revenue",
    legend=False,
    color="skyblue"
)
plt.title("Total Revenue by Service")
plt.xlabel("Service Type")
plt.ylabel("Total Revenue (Baht)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# GRAPH 2: Total Bookings by Service
plt.figure(figsize=(8, 5))
q2_pandas.plot(
    kind="bar",
    x="service_type",
    y="total_bookings",
    legend=False,
    color="orange"
)
plt.title("Total Bookings by Service")
plt.xlabel("Service Type")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# GRAPH 3: Monthly Revenue Trend
membership_df["booking_date"] = pd.to_datetime(
    membership_df["booking_date"],
    dayfirst=True,
    errors="coerce"
)
monthly_revenue = (
    membership_df
    .groupby(membership_df["booking_date"].dt.to_period("M"))
    ["price"]
    .sum()
)
plt.figure(figsize=(8, 5))
monthly_revenue.plot(
    kind="line",
    marker="o",
    color="green"
)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (Baht)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# BUSINESS SUMMARY & INSIGHTS (สรุปผลเชิงธุรกิจ)

print("\n" + "="*50)
print("          BUSINESS SUMMARY & INSIGHTS")
print("="*50)

print("""
1. สรุปภาพรวมรายได้และการใช้บริการ (Revenue & Service Trends):
   - บริการ Personal Training สร้างรายได้รวมและมีค่าเฉลี่ยรายได้ต่อการจองสูงที่สุด
     เนื่องจากเป็นบริการแบบตัวต่อตัวที่มีราคาแพ็กเกจต่อหน่วยสูง
   - บริการ Gym ทั่วไป และ Group Class มีจำนวนผู้เข้าใช้งาน (Bookings) ถี่ที่สุด
     ซึ่งเป็นฐานลูกค้าหลักในการสร้าง Traffic ให้กับฟิตเนส

2. พฤติกรรมและกลุ่มเป้าหมายลูกค้า (Customer Segmentation):
   - ลูกค้าที่มีน้ำหนักมากกว่า 70 kg มีแนวโน้มจองบริการ Personal Training มากที่สุด
     สะท้อนความต้องการเทรนเนอร์ดูแลการออกกำลังกายและควบคุมน้ำหนักแบบเข้มข้น
   - การมอบส่วนลด VIP 10% ช่วยกระตุ้นการตัดสินใจซื้อแพ็กเกจราคาสูง (เช่น VIP 5,000 บาท) ได้ดี

3. ข้อเสนอแนะเชิงบริหาร (Business Recommendations):
   - Upselling Strategy: ควรจัดโปรโมชันดึงลูกค้าจาก Gym ปกติ ให้มาทดลอง Personal Training
     โดยเจาะกลุ่มลูกค้าที่ต้องการลดน้ำหนักหรือเล่นเวทจริงจัง
   - Capacity Management: ควรบริหารจัดการตารางเวลา Group Class และพื้นที่เล่น Gym
     ในช่วงเวลา Peak Hours เพื่อลดความแออัดขณะเช็คอินใช้งาน
""")
print("="*50)

# PART 12 : ERROR HANDLING
def find_member(member_id):
    try:
        member_id = int(member_id)
    except ValueError:
        print("Member ID ต้องเป็นตัวเลข")
        return None
    if member_id not in member_data:
        print(f"ไม่พบ Member ID: {member_id}")
        return None
    return member_data[member_id]
def find_package(package_id):
    try:
        package_id = int(package_id)
    except ValueError:
        print("Package ID ต้องเป็นตัวเลข")
        return None
    for package in packages:
        if (package.package_id== package_id):
            return package
    print(f"ไม่พบ Package ID: {package_id}")
    return None
def validate_hours(hours):
    try:
        hours = float(hours)
    except ValueError:
        print("จำนวนชั่วโมงต้องเป็นตัวเลข")
        return False
    if hours <= 0:
        print("จำนวนชั่วโมงต้องมากกว่า 0")
        return False
    if hours > 12:
        print("ไม่สามารถจองเกิน 12 ชั่วโมง")
        return False
        return True
print("===== ERROR HANDLING TEST =====")
find_member(999999)
find_package(999999)
validate_hours(-5)
print(validate_hours(2))

# PART 13 : FITNESS DASHBOARD & CHECK-IN SYSTEM
def dashboard_report(report_type):
    data = membership_df.copy()
    data["booking_date"] = pd.to_datetime(data["booking_date"])
    # DAILY
    if report_type == "1":
        date_input = input("กรอกวันที่ (YYYY-MM-DD): ").strip()
        try:
            selected_date = pd.to_datetime(date_input, format="%Y-%m-%d")
        except ValueError:
            print("รูปแบบวันที่ไม่ถูกต้อง")
            return
        report = data[data["booking_date"].dt.date == selected_date.date()]
        title = f"วันที่ {selected_date.date()}"
    # WEEKLY
    elif report_type == "2":
        date_input = input("กรอกวันที่ในสัปดาห์ (YYYY-MM-DD): ").strip()
        try:
            selected_date = pd.to_datetime(date_input, format="%Y-%m-%d")
        except ValueError:
            print("รูปแบบวันที่ไม่ถูกต้อง")
            return
        start_date = selected_date - pd.Timedelta(days=selected_date.weekday())
        end_date = start_date + pd.Timedelta(days=6)
        report = data[(data["booking_date"] >= start_date) & (data["booking_date"] < end_date + pd.Timedelta(days=1))]
        title = f"สัปดาห์ {start_date.date()} ถึง {end_date.date()}"
    # MONTHLY
    elif report_type == "3":
        try:
            year = int(input("กรอกปี: "))
            month = int(input("กรอกเดือน (1-12): "))
        except ValueError:
            print("กรุณากรอกตัวเลข")
            return
        if month < 1 or month > 12:
            print("เดือนไม่ถูกต้อง")
            return
        report = data[(data["booking_date"].dt.year == year) & (data["booking_date"].dt.month == month)]
        title = f"เดือน {month}/{year}"
    else:
        print("กรุณาเลือก 1, 2 หรือ 3")
        return

    # SUMMARY
    total_bookings = len(report)
    total_revenue = report["price"].sum()
    average_revenue = report["price"].mean() if total_bookings > 0 else 0
    vip_count = report["is_vip"].sum() if total_bookings > 0 else 0
    general_count = total_bookings - vip_count

    print("\n====================================")
    print("    FITNESS MEMBERSHIP DASHBOARD")
    print("====================================")
    print(f"ช่วงเวลา: {title}")
    print(f"จำนวนการจอง: {total_bookings}")
    print(f"รายได้รวม: {total_revenue:,.2f} บาท")
    print(f"รายได้เฉลี่ย: {average_revenue:,.2f} บาท")
    print(f"VIP: {vip_count}")
    print(f"General: {general_count}")
    print("====================================")

    if total_bookings > 0:
        service_summary = (
            report.groupby("service_type")
            .agg(bookings=("booking_id", "count"), revenue=("price", "sum"))
            .sort_values("revenue", ascending=False)
        )
        print("\nSERVICE SUMMARY")
        display(service_summary)
    else:
        print("\nไม่มีข้อมูลในช่วงเวลาที่เลือก")

def dashboard_menu():
    while True:
        print("\n==============================")
        print("      FITNESS DASHBOARD")
        print("==============================")
        print("1. รายวัน")
        print("2. รายสัปดาห์")
        print("3. รายเดือน")
        print("0. ออกจาก Dashboard")
        choice = input("เลือกช่วงเวลา: ").strip()
        if choice == "0":
            print("ออกจาก Dashboard")
            break
        dashboard_report(choice)

def view_all_packages():
    print("\n====================================")
    print("          PACKAGE INFORMATION")
    print("====================================")
    print(f"{'ID':<5}{'Package':<15}{'Price':<12}{'Max Hours':<12}{'Duration':<12}")
    print("-" * 56)
    for package in packages:
        print(f"{package.package_id:<5}{package.package_name:<15}{package.price:,.2f} บาท{'':<3}{package.max_hours:<12}{package.duration_days} days")
    print("====================================")

def search_booking():
    global membership_df
    try:
        booking_id = int(input("\nกรอก Booking ID: "))
        result = membership_df[membership_df["booking_id"] == booking_id]
        if result.empty:
            print("❌ ไม่พบข้อมูลการจอง")
        else:
            booking = result.iloc[0]
            for p in packages:
                if p.package_id == booking['package_id']:
                    original_price = float(p.price)
                    break
            is_vip_bool = bool(booking['is_vip'])
            discount = original_price * 0.10 if is_vip_bool else 0.0
            final_price = original_price - discount
            print("\n====================================")
            print("          BOOKING INFORMATION")
            print("====================================")
            print(f"Booking ID   : {booking['booking_id']}")
            print(f"Member ID    : {booking['member_id']}")
            print(f"ชื่อสมาชิก   : {booking['name']}")
            print(f"อายุ         : {booking['age']} ปี")
            print(f"น้ำหนัก      : {booking['weight_kg']} kg")
            print(f"VIP          : {'ใช่' if is_vip_bool else 'ไม่ใช่'}")
            print("------------------------------------")
            print(f"Package ID   : {booking['package_id']}")
            print(f"Package      : {booking['package_name']}")
            print(f"Service      : {booking['service_type']}")
            print(f"จำนวนชั่วโมง : {booking['hours']} ชั่วโมง")
            print("------------------------------------")
            print(f"ราคาเต็ม     : {original_price:,.2f} บาท")
            print(f"ส่วนลด VIP   : {discount:,.2f} บาท")
            print(f"ราคาสุทธิ    : {final_price:,.2f} บาท")
            print(f"วันที่จอง    : {booking['booking_date']}")
            print(f"สถานะ        : {booking['status']}")
            print("====================================")
    except ValueError:
        print("❌ Booking ID ต้องเป็นตัวเลข")

def save_data():
    global membership_df
    membership_df.to_csv("gym_membership_data.csv", index=False, encoding="utf-8-sig")
    membership_df.to_sql("gym_memberships", conn, if_exists="replace", index=False)

# PART 14 : ADD NEW BOOKING
def add_new_booking():
    global membership_df
    try:
        # 1. เลือก Member
        member_id = int(input("\nกรอก Member ID: "))
        if member_id not in member_data:
            print("❌ ไม่พบ Member ID")
            return
        selected_member = member_data[member_id]
        # 2. ตรวจสอบ VIP
        is_vip_member = bool(selected_member.is_vip)
        # 3. แสดง Package
        print("\n====================================")
        print("             PACKAGE")
        print("====================================")
        for package in packages:
            print(f"{package.package_id} - {package.package_name} - {package.price:,.2f} บาท")
        print("====================================")
        # 4. เลือก Package
        package_id = int(input("กรอก Package ID: "))
        selected_package = find_package(package_id)
        if selected_package is None:
            print("❌ ไม่พบ Package ID")
            return
        # 5. เลือก Service
        print("\n====================================")
        print("           SERVICE TYPE")
        print("====================================")
        print("1. Gym")
        print("2. Personal Training")
        print("3. Group Class")
        service_choice = input("เลือกประเภทบริการ: ").strip()
        if service_choice == "1":
            service_type = "Gym"
        elif service_choice == "2":
            service_type = "Personal Training"
        elif service_choice == "3":
            service_type = "Group Class"
        else:
            print("❌ ประเภทบริการไม่ถูกต้อง")
            return
        # 6. จำนวนชั่วโมง
        hours = float(input("จำนวนชั่วโมง: "))
        if hours <= 0:
            print("❌ จำนวนชั่วโมงต้องมากกว่า 0")
            return
        # 7. วันที่จอง
        booking_date = input("วันที่จอง (YYYY-MM-DD): ").strip()
        # 8. สร้าง Booking ID
        if len(memberships_300) > 0:
            new_booking_id = max(booking.booking_id for booking in memberships_300) + 1
        else:
            new_booking_id = 1
        # 9. สร้าง Booking Object
        new_booking = MembershipPackage(
            booking_id=new_booking_id,
            member=selected_member,
            package=selected_package,
            hours=hours,
            service_type=service_type,
            booking_date=booking_date
        )
        # 10-13. คำนวณส่วนลด
        original_price = float(selected_package.price)
        discount = round(original_price * 0.10, 2) if is_vip_member else 0.0
        final_price = round(original_price - discount, 2)
        # 14. อัปเดตราคาใน Booking
        new_booking.price = final_price
        # 15. แสดงสรุปราคา
        print("\n====================================")
        print("          PRICE SUMMARY")
        print("====================================")
        print(f"ราคาเต็ม       : {original_price:,.2f} บาท")
        print(f"ส่วนลด VIP     : {discount:,.2f} บาท")
        print(f"ราคาสุทธิ      : {final_price:,.2f} บาท")
        print("====================================")
        # 16. เพิ่ม Booking เข้า List
        memberships_300.append(new_booking)
        # 17. สร้าง DataFrame
        new_data = pd.DataFrame([{
            "booking_id": new_booking.booking_id,
            "member_id": selected_member.member_id,
            "name": selected_member.name,
            "age": selected_member.age,
            "weight_kg": selected_member.weight_kg,
            "is_vip": is_vip_member,
            "package_id": selected_package.package_id,
            "package_name": selected_package.package_name,
            "original_price": original_price,
            "discount": discount,
            "price": final_price,
            "hours": new_booking.hours,
            "service_type": new_booking.service_type,
            "booking_date": str(booking_date),
            "status": new_booking.status
        }])
        # 18. เพิ่มลง membership_df
        membership_df = pd.concat([membership_df, new_data], ignore_index=True)
        # 19. บันทึก CSV
        membership_df.to_csv("gym_membership_data.csv", index=False, encoding="utf-8-sig")
        # 20. บันทึก SQLite
        try:
            # แปลงคอลัมน์ booking_date เป็น string ก่อนลง SQL ป้องกัน Error Timestamp
            temp_df = membership_df.copy()
            temp_df["booking_date"] = temp_df["booking_date"].astype(str)
            temp_df.to_sql(
                "gym_memberships",
                conn,
                if_exists="replace",
                index=False
            )
        except Exception as e:
            print(f"⚠️ SQLite ไม่สำเร็จ: {e}")
        # 21. แสดงผล Booking
        print("\n====================================")
        print("        BOOKING SUCCESS")
        print("====================================")
        print(f"Booking ID : {new_booking.booking_id}")
        print(f"Member ID  : {selected_member.member_id}")
        print(f"ชื่อสมาชิก : {selected_member.name}")
        print(f"VIP        : {'ใช่' if is_vip_member else 'ไม่ใช่'}")
        print(f"Package    : {selected_package.package_name}")
        print(f"Service    : {service_type}")
        print(f"ราคาเต็ม   : {original_price:,.2f} บาท")
        print(f"ส่วนลด VIP : {discount:,.2f} บาท")
        print(f"ราคาสุทธิ  : {final_price:,.2f} บาท")
        print(f"วันที่จอง   : {booking_date}")
        print("====================================")
    except ValueError:
        print("❌ กรุณากรอกข้อมูลให้ถูกต้อง")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")

# PART 15 : CHECK-IN / CHECK-OUT SYSTEM
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

checkin_df = pd.DataFrame(columns=[
    "member_id", "name", "package_name", "service_type",
    "checkin_time", "checkout_time", "hours_used", "status"
])

def check_package_expiry(member_id):
    member_bookings = membership_df[membership_df["member_id"] == member_id]
    if member_bookings.empty:
        return False, None, "ไม่พบข้อมูล Package ของสมาชิก"
    latest_booking = member_bookings.iloc[-1]
    package_id = latest_booking["package_id"]
    selected_package = None
    for package in packages:
        if package.package_id == package_id:
            selected_package = package
            break
    if selected_package is None:
        return False, None, "ไม่พบข้อมูล Package"
    booking_date = pd.to_datetime(latest_booking["booking_date"])
    expiry_date = booking_date + timedelta(days=selected_package.duration_days)
    current_date = datetime.now()
    if current_date > expiry_date:
        return False, latest_booking, f"Package หมดอายุแล้ว ({expiry_date.strftime('%Y-%m-%d')})"
    return True, latest_booking, f"Package ใช้งานได้ถึง {expiry_date.strftime('%Y-%m-%d')}"

def check_in():
    global checkin_df
    try:
        member_id = int(input("\nกรอก Member ID: "))
        if member_id not in member_data:
            print("❌ ไม่พบสมาชิก")
            return
        active_checkin = checkin_df[(checkin_df["member_id"] == member_id) & (checkin_df["status"] == "Checked In")]
        if not active_checkin.empty:
            print("⚠️ สมาชิกคนนี้ Check-in อยู่แล้ว")
            return
        is_valid, booking, message = check_package_expiry(member_id)
        if not is_valid:
            print(f"❌ {message}")
            return
        print(f"✅ {message}")
        member = member_data[member_id]
        checkin_time = datetime.now()
        new_row = pd.DataFrame([{
            "member_id": member_id,
            "name": member.name,
            "package_name": booking["package_name"],
            "service_type": booking["service_type"],
            "checkin_time": checkin_time,
            "checkout_time": None,
            "hours_used": 0,
            "status": "Checked In"
        }])
        checkin_df = pd.concat([checkin_df, new_row], ignore_index=True)
        print("\n====================================")
        print("          CHECK-IN SUCCESS")
        print("====================================")
        print(f"Member ID    : {member_id}")
        print(f"ชื่อสมาชิก   : {member.name}")
        print(f"Package      : {booking['package_name']}")
        print(f"Service      : {booking['service_type']}")
        print(f"เวลาเข้า     : {checkin_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("สถานะ        : Checked In")
        print("====================================")
    except ValueError:
        print("❌ Member ID ต้องเป็นตัวเลข")

def check_out():
    global checkin_df
    try:
        member_id = int(input("\nกรอก Member ID: "))
        active_checkin = checkin_df[(checkin_df["member_id"] == member_id) & (checkin_df["status"] == "Checked In")]
        if active_checkin.empty:
            print("❌ ไม่พบข้อมูล Check-in ของสมาชิก")
            return
        index = active_checkin.index[-1]
        checkin_time = pd.to_datetime(checkin_df.loc[index, "checkin_time"])
        checkout_time = datetime.now()
        time_used = checkout_time - checkin_time
        hours_used = round(time_used.total_seconds() / 3600, 2)
        checkin_df.loc[index, "checkout_time"] = checkout_time
        checkin_df.loc[index, "hours_used"] = hours_used
        checkin_df.loc[index, "status"] = "Completed"
        print("\n====================================")
        print("          CHECK-OUT SUCCESS")
        print("====================================")
        print(f"Member ID    : {member_id}")
        print(f"เวลาเข้า     : {checkin_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"เวลาออก      : {checkout_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"เวลาที่ใช้จริง : {hours_used:.2f} ชั่วโมง")
        print("สถานะ        : Completed")
        print("====================================")
    except ValueError:
        print("❌ Member ID ต้องเป็นตัวเลข")

def view_checkin_history():
    if checkin_df.empty:
        print("\n❌ ยังไม่มีประวัติการเข้า-ออก")
        return
    print("\n====================================")
    print("     CHECK-IN / CHECK-OUT HISTORY")
    print("====================================")
    for _, row in checkin_df.iterrows():
        print(f"\nMember ID    : {row['member_id']}")
        print(f"ชื่อสมาชิก   : {row['name']}")
        print(f"Package      : {row['package_name']}")
        print(f"Service      : {row['service_type']}")
        print(f"เวลาเข้า     : {row['checkin_time']}")
        if pd.notna(row["checkout_time"]):
            print(f"เวลาออก      : {row['checkout_time']}")
        else:
            print("เวลาออก      : ยังไม่ได้ Check-out")
        print(f"เวลาที่ใช้    : {float(row['hours_used']):.2f} ชั่วโมง")
        print(f"สถานะ        : {row['status']}")
        print("------------------------------------")
    print("====================================")

def walk_in_checkin():
    global checkin_df
    print("\n====================================")
    print("          WALK-IN CHECK-IN")
    print("====================================")
    name = input("กรอกชื่อลูกค้า: ").strip()
    if not name:
        print("❌ กรุณากรอกชื่อลูกค้า")
        return
    print("เลือกบริการ: 1. Gym (150฿) | 2. Personal Training (500฿) | 3. Group Class (300฿)")
    service_choice = input("เลือกบริการ (1-3): ").strip()

    service_info = {
        "1": ("Gym", 150),
        "2": ("Personal Training", 500),
        "3": ("Group Class", 300)
    }
    service_type, price = service_info.get(service_choice, ("Gym", 150))

    new_id = 9900 + len(checkin_df) + 1
    checkin_time = datetime.now()

    new_row = pd.DataFrame([{
        "member_id": new_id,
        "name": f"[Walk-in] {name}",
        "package_name": "Day Pass",
        "service_type": service_type,
        "checkin_time": checkin_time,
        "checkout_time": None,
        "hours_used": 0,
        "status": "Checked In"
    }])

    checkin_df = pd.concat([checkin_df, new_row], ignore_index=True)

    print("\n====================================")
    print("      WALK-IN CHECK-IN SUCCESS")
    print("====================================")
    print(f"Member ID (Temp) : {new_id}")
    print(f"ชื่อลูกค้า       : [Walk-in] {name}")
    print(f"Package          : Day Pass")
    print(f"Service          : {service_type}")
    print(f"ราคาชำระ         : {price:,} บาท")
    print(f"เวลาเข้า         : {checkin_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("====================================")

# PART 16 : SUMMARY REPORT
total_bookings = len(membership_df)
total_revenue = membership_df["price"].sum()
average_price = membership_df["price"].mean()
vip_bookings = membership_df["is_vip"].sum()
print("================================")
print("      GYM MEMBERSHIP REPORT")
print("================================")
print(f"Total Bookings: {total_bookings}")
print(f"Total Revenue: {total_revenue:,.2f} Baht")
print(f"Average Price: {average_price:,.2f} Baht")
print(f"VIP Bookings: {vip_bookings}")
print("================================")

# PART 100 : EXPORT CSV
membership_df.to_csv(
    "gym_membership_data.csv",
    index=False,
    encoding="utf-8-sig")
print("Export CSV สำเร็จ")

# MAIN MENU
def main_menu():
    while True:
        print("\n====================================")
        print("          FITNESS GYM SYSTEM")
        print("====================================")
        print("1. สมัครสมาชิก")
        print("2. ใช้บริการ / จอง Package")
        print("3. ดู Package ทั้งหมด")
        print("4. ค้นหาข้อมูลการจอง")
        print("5. Service & Revenue Dashboard")
        print("6. Check-in")
        print("7. Check-out")
        print("8. ดูประวัติการเข้า-ออก")
        print("9. Walk-in (เข้าใช้งานชั่วคราว)")
        print("0. ออกจากระบบ")
        print("====================================")
        choice = input(
            "เลือกเมนู: "
        ).strip()

        # 1. ADD MEMBER
        if choice == "1":
            try:
                name = input("ชื่อสมาชิก: ").strip()
                age = int(input("อายุ: "))
                weight = float(input("น้ำหนัก (kg): "))
                vip_input = input("สมัครเป็นสมาชิก VIP หรือไม่? (สมัคร/ไม่สมัคร): ").strip().lower()
                is_vip = (vip_input == "สมัคร")
                new_member_id = (max(member_data.keys()) + 1)
                new_member = Member(new_member_id,name,age,weight,is_vip)
                members_300.append(new_member)
                member_data[new_member_id] = new_member

                print("\n================================")
                print("       สมัครสมาชิกสำเร็จ!")
                print("================================")
                print(new_member)
            except ValueError:
                print(
                    "❌ กรุณากรอกข้อมูลให้ถูกต้อง"
                )
        # 2. BOOK PACKAGE
        elif choice == "2":
            add_new_booking()
        # 3. VIEW PACKAGES
        elif choice == "3":
            view_all_packages()
        # 4. SEARCH BOOKING
        elif choice == "4":
            search_booking()
        # 5. REPORT DASHBOARD
        elif choice == "5":
            dashboard_menu()
        # 6. CHECK-IN
        elif choice == "6":
            check_in()
        # 7. CHECK-OUT
        elif choice == "7":
            check_out()
        # 8. ดูประวัติการเข้า-ออก
        elif choice == "8":
            view_checkin_history()
        #9.Walk-in
        elif choice == "9":
            walk_in_checkin()
        # 0. ออกจากระบบ
        elif choice == "0":
            print("\n====================================")
            print("ขอบคุณที่ใช้ FITNESS GYM SYSTEM")
            print("ออกจากระบบเรียบร้อย 👋")
            print("====================================")
            break
       # เลือกเมนูผิด
        else:
          print("❌ กรุณาเลือกเมนู 1-9")
main_menu()