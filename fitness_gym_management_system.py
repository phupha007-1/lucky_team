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

# --------------------------------------------
# BUSINESS SUMMARY & INSIGHTS (สรุปผลเชิงธุรกิจ)
# --------------------------------------------
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