# PART 1 : IMPORT LIBRARIES
import random
import sqlite3
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

# PART 2 : CLASS MEMBER
class Member:
    def __init__(
        self,
        member_id,
        name,
        age,
        weight_kg,
        is_vip=False
        ):
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
    def __init__(
        self,
        package_id,
        package_name,
        price,
        max_hours,
        duration_days
    ):
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
    def __init__(
        self,
        booking_id,
        member,
        package,
        hours,
        service_type,
        booking_date
    ):
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
    "ธนกฤต",
    "ณัฐวุฒิ",
    "พชร",
    "ภูริณัฐ",
    "กิตติพงศ์",
    "วรากร",
    "ธนภัทร",
    "ภัทรพล",
    "ณัฐพล",
    "ศุภกร",
    "ก้องภพ",
    "ชยพล",
    "รัชชานนท์",
    "ธีรภัทร",
    "ปวริศ",
    "กรวิชญ์",
    "นนทกร",
    "ภาคภูมิ",
    "อัครพล",
    "สิรวิชญ์",
    "พิมพ์ชนก",
    "ชนากานต์",
    "ณิชาภัทร",
    "ศิริพร",
    "กัญญารัตน์",
    "ชลธิชา",
    "ปุณณภา",
    "ธัญชนก",
    "ณัฐธิดา",
    "พิชชาภา",
    "วริศรา",
    "สุภัสสรา",
    "กมลชนก",
    "ปภาวรินทร์",
    "อริสรา",
    "พัชราภา",
    "นภัสสร",
    "ชญานิศ",
    "กุลธิดา",
    "รินรดา"
]
last_names = [
    "ศรีสุวรรณ",
    "วัฒนกุล",
    "เจริญชัย",
    "พัฒนานนท์",
    "วงศ์วัฒนะ",
    "สุวรรณดี",
    "บุญญฤทธิ์",
    "ชัยวัฒน์",
    "รัตนกุล",
    "ศุภกิจ",
    "ธนากุล",
    "วัฒนชัย",
    "เจริญสุข",
    "พงศ์ไพบูลย์",
    "สิริวัฒน์",
    "กิตติธร",
    "อนันต์ชัย",
    "รุ่งเรือง",
    "พัฒนกุล",
    "ศรีวัฒนานนท์"
]
def generate_name():
    return (
        random.choice(first_names)
        + " "
        + random.choice(last_names)
    )
def generate_booking_date():
    start_date = datetime(2026, 1, 1)
    random_days = random.randint(
        0,
        364
    )
    return start_date + timedelta(
        days=random_days
    )
packages = [
    Package(
        1,
        "Basic",
        1200,
        10,
        30
    ),
    Package(
        2,
        "Premium",
        2500,
        20,
        30
    ),
    Package(
        3,
        "VIP",
        5000,
        50,
        60
    )
]
services = [
    "Gym",
    "Personal Training",
    "Group Class"
]
members_300 = []
member_data = {}
for i in range(1, 301):
    member = Member(
        member_id=i,
        name=generate_name(),
        age=random.randint(18, 40),
        weight_kg=round(
            random.uniform(45, 100),
            1
        ),
        is_vip=random.choice(
            [True, False]
        )
    )
    members_300.append(member)
    member_data[i] = member
memberships_300 = []
for i in range(1, 301):
    selected_member = random.choice(
        members_300
    )
    selected_package = random.choice(
        packages
    )
    selected_service = random.choice(
        services
    )
    selected_hours = random.choice(
        [1, 1.5, 2, 2.5, 3]
    )
    membership = MembershipPackage(
        booking_id=i,
        member=selected_member,
        package=selected_package,
        hours=selected_hours,
        service_type=selected_service,
        booking_date=generate_booking_date()
    )
    membership.mark_done()
    memberships_300.append(
        membership
    )
print("สร้างข้อมูลสำเร็จ")
print("Members:", len(members_300))
print("Membership Packages:", len(memberships_300))