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

# วิธีที่ 1 (แนะนำมากที่สุด): แสดงผลแบบตารางบน Jupyter / Colab
display(membership_df.head())

print("\nจำนวนข้อมูล:",len(membership_df))

# PART 7 : BUSINESS QUESTIONS - PANDAS
from google.colab import auth
from google.cloud import bigquery

auth.authenticate_user()
project_id = 'deadlinesurvivorr'
client = bigquery.Client(project=project_id)
query = """
    SELECT *
    FROM `deadlinesurvivorr.gym_membership_data2.gym_membership_data2`
"""
membership_df = client.query(query).to_dataframe()
# คำถามที่ 1 : บริการประเภทใดสร้างรายได้รวมมากที่สุด?
q1_pandas = (
    membership_df
    .groupby("service_type")
    .agg(total_revenue=("price", "sum"))
    .sort_values("total_revenue", ascending=False)
    .reset_index()
    .head(1)
)
print("QUESTION 1")
display(q1_pandas)

# คำถามที่ 2 : แต่ละบริการมีจำนวนการจองและรายได้รวมเท่าไร?
q2_pandas = (
    membership_df
    .groupby("service_type")
    .agg(
        total_bookings=("booking_id", "count"),
        total_revenue=("price", "sum")
    )
    .sort_values("total_revenue", ascending=False)
    .reset_index()
)
print("\nQUESTION 2")
display(q2_pandas)

# คำถามที่ 3 : น้ำหนักเฉลี่ยของสมาชิกแต่ละบริการเท่าไร?
q3_pandas = (
    membership_df
    .groupby("service_type")
    .agg(avg_weight=("weight_kg", lambda x: round(x.mean(), 2)))
    .sort_values("avg_weight", ascending=False)
    .reset_index()
)
print("QUESTION 3")
display(q3_pandas)

# คำถามที่ 4 : บริการประเภทใดมีค่าเฉลี่ยรายได้ต่อการจองสูงสุด?
q4_pandas = (
    membership_df
    .groupby("service_type")
    .agg(avg_revenue_per_booking=("price", lambda x: round(x.mean(), 2)))
    .sort_values("avg_revenue_per_booking", ascending=False)
    .reset_index()
    .head(1)
)
print("QUESTION 4")
display(q4_pandas)

# คำถามที่ 5 : บริการประเภทใดมีสัดส่วนรายได้ (Revenue Share %)คิดเป็นกี่เปอร์เซ็นต์ของรายได้รวมทั้งหมด?
total_sum = membership_df['price'].sum()
q6_pandas = (
    membership_df
    .groupby("service_type")
    .agg(
        total_revenue=("price", "sum"),
        revenue_share_pct=("price", lambda x: round((x.sum() / total_sum) * 100, 2))
    )
    .sort_values("revenue_share_pct", ascending=False)
    .reset_index()
)
print("\nQUESTION 5")
display(q6_pandas)

# คำถามที่ 6 : หากจัดกลุ่มตามบริการ ราคาตั๋วที่ถูกที่สุดและแพงที่สุดของแต่ละบริการคือเท่าไร?
q7_pandas = (
    membership_df
    .groupby("service_type")
    .agg(
        min_price=("price", "min"),
        max_price=("price", "max")
    )
    .reset_index()
)
print("\nQUESTION 6")
display(q7_pandas)

# คำถามที่ 7 : ลูกค้าที่มีน้ำหนักเกิน 70 kg นิยมจองบริการประเภทใดมากที่สุด?
q10_pandas = (
    membership_df[membership_df['weight_kg'] > 70]
    .groupby("service_type")
    .agg(booking_count=("booking_id", "count"))
    .sort_values("booking_count", ascending=False)
    .reset_index()
    .head(1)
)
print("\nQUESTION 7")
display(q10_pandas)

# คำถามที่ 8 : เปรียบเทียบค่ามัธยฐาน (Median) ของราคาระหว่างบริการต่างๆ เพื่อดูระดับราคาของบริการส่วนใหญ่
q12_pandas = (
    membership_df
    .groupby("service_type")
    .agg(median_price=("price", "median"))
    .reset_index()
)
print("\nQUESTION 8")
display(q12_pandas)

# PART 8 : SQLITE DATABASE
conn = sqlite3.connect("fitness_gym.db")
membership_df.to_sql("gym_memberships",conn,if_exists="replace",index=False)
print("บันทึกข้อมูลลง SQLite สำเร็จ")
     