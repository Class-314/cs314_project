from Records import Address
from Records import UserRecord
from Records import MemberRecord
from Records import ServiceRecord
from Records import ProviderRecord

def sample_load_member(id):
    filename = ("Members/M_")
    filename += str(id) + ".txt"
    with open(filename, 'r') as file:
        lines = file.readlines()
        mID = lines[0].strip()
        name = lines[1].strip()
        street = lines[2].strip()
        city = lines[3].strip()
        state = lines[4].strip()
        zip = lines[5].strip()
    
    curr_member = MemberRecord(name, mID, street, city, state, zip)
    print(curr_member)

def exercise_records():


    # a = Address("10 Main St.", "Portland", "OR", "97035")
    # p = ProviderRecord("Richard Simmons", 123456123, a)
    # print(p)
    
    sr = ServiceRecord(555555, 888888888, 444444444, "09-09-1991", "\n\n\n\ndietitian and test", "99.99")
    print(sr)
    # a1 = Address("10 Hollywood blvd", "Los Angeles", "CA", "97305")
    # a2 = Address(a1)
    # a3 = Address()

    # print("a1: " + str(a1))
    # print("a2: " + str(a2))


    # u1 = UserRecord()
    # u3 = UserRecord("Richard Simmons", 123123123, a1)
    # print(u3)
    # u4 = UserRecord("Richard Simmons", 123123123, "1 Main st.", "Portland", "or", 97202)
    # print(u4)
    # u2 = UserRecord(u4)
    # print("U2: \n")
    # print(u2)

    # m1 = MemberRecord()
    # m2 = MemberRecord("Richard Simmons", 123123123, a1)
    # print(m2)
    # m3 = MemberRecord(m2)
    # print(m3)
    # m4 = MemberRecord("Richard Simmons", 123123123, "1 main st.", "portland", "or", "97000")
    # print(m4)


    # s1 = ServiceRecord(999999, 999888777, 444555666, "09-09-1881")
    # s2 = ServiceRecord(123123, 123456789, 987654321, "12-20-2024")
    # print(s2)
    # s3 = ServiceRecord(123222, 123456789, 987654321, "1-1-1", "These are some comments")
    # print(s3)
    # s4 = ServiceRecord(s3)
    # s4._comments += " Additional comments"
    # print(s4)

    # print(m4._ID)

    # m4.add_service(s4)
    # m4.add_service(s3)
    # m4.add_service(s2)

    # print("=====================")
    # m4.display_services()

    # m5 = MemberRecord(m4)
    # #m5 = m4

    # #curr_member = MemberRecord(DBmgr.getMember(MemberID))

    # m5._name = "NEW NAME"
    # m5._ID = 909090901

    # m5.add_service(s1)

    # print ("====== MEMBER 5 =========")
    # print(m5)
    # m5.display_services()


    # print ("========== MEMBER 4 =======")
    # print(m4)
    # m4.display_services()


