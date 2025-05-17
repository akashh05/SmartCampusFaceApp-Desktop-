import pymongo
import bcrypt

# MongoDB Connection
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["FaceRecognitionDB"]
    students_collection = db["students"]
    admins_collection = db["admins"]
except Exception as e:
    print(f"❌ MongoDB Connection Error: {e}")
    students_collection = None
    admins_collection = None

# ---------------- Student Operations ----------------

def add_student(name, contact, roll_number, face_image):
    if students_collection is None:
        print("❌ MongoDB not connected.")
        return False

    student_data = {
        "name": name,
        "contact": contact,
        "roll_number": roll_number,
        "face_image": face_image
    }
    students_collection.insert_one(student_data)
    return True

def get_students():
    if students_collection is None:
        return []
    return list(students_collection.find({}, {"_id": 0}))

def get_student_by_roll(roll_number):
    if students_collection is None:
        return None
    return students_collection.find_one({"roll_number": roll_number}, {"_id": 0})

def delete_student(roll_number):
    if students_collection is None:
        return False
    result = students_collection.delete_one({"roll_number": roll_number})
    return result.deleted_count > 0

def update_student(roll_number, name=None, contact=None):
    if students_collection is None:
        return False
    update_fields = {}
    if name:
        update_fields["name"] = name
    if contact:
        update_fields["contact"] = contact
    if update_fields:
        result = students_collection.update_one(
            {"roll_number": roll_number}, {"$set": update_fields}
        )
        return result.modified_count > 0
    return False

def update_student_details(roll_number, name, contact):
    if students_collection is None:
        return False
    result = students_collection.update_one(
        {"roll_number": roll_number},
        {"$set": {"name": name, "contact": contact}}
    )
    return result.modified_count > 0

# ---------------- Admin Operations ----------------

def add_admin(username, password):
    if admins_collection is None:
        print("❌ Admins DB not available.")
        return False
    if admins_collection.find_one({"username": username}):
        print("⚠️ Admin already exists.")
        return False

    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Ensure password is stored as binary, not string
    admins_collection.insert_one({
        "username": username,
        "password": hashed_password  # This stays as bytes
    })
    return True


def authenticate_admin(username, password):
    user = admins_collection.find_one({"username": username})
    if user:
        stored_hash = user["password"]
        if isinstance(stored_hash, str):
            print("❌ Invalid hash format: stored as string")
            return False
        print("✅ Hash looks correct. Trying login...")
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash)
    print("❌ User not found.")
    return False
