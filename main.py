
from Records import Address
from Records import UserRecord
from Records import MemberRecord
from Records import ServiceRecord
 
if __name__ == "__main__":
    a1 = Address("10 Hollywood blvd", "Los Angeles", "CA", "97305")
    # a2 = Address(a1)
    # a3 = Address()

    # print("a1: " + str(a1))
    # print("a2: " + str(a2))

    # a1.zip = "test"
    # print(a1)

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

    # print("PULL REQUEST TESTING")

    s1 = ServiceRecord()
    s2 = ServiceRecord(123123, 123456789, 987654321, "12-20-2024")
    print(s2)
    s3 = ServiceRecord(123123, 123456789, 987654321, "12-20-2024", "These are some comments")
    print(s3)
    s4 = ServiceRecord(s3)
    s4._comments += " Additional comments"
    print(s4)