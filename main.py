from program import Calculation
from program import States


if __name__ == '__main__':
    Policy_Global = input("全球政策:", )
    Policy_Online = input("政策在线buff:", )
    Policy_Offline = input("政策离线buff:", )
    Policy_Residence = input("政策住宅buff:", )
    Policy_Commercial = input("政策商业buff:", )
    Policy_Industry = input("政策工业buff:", )
    Policy_JiaGuoZhiGuang = input("家国之光buff:", )
    Photos_Global = input("画册全球buff:", )
    Photos_Online = input("画册在线buff:", )
    Photos_Offline = input("画册离线buff:", )
    Photos_Residence = input("画册住宅buff:", )
    Photos_Commercial = input("画册商业buff:", )
    Photos_Industry = input("画册工业buff:", )

    states = States.Buff(Policy_Global, Policy_Online, Policy_Offline, Policy_Residence,Policy_Commercial,Policy_Industry,
                Policy_JiaGuoZhiGuang, Photos_Global, Photos_Online, Photos_Offline, Photos_Residence, Photos_Commercial,
                Photos_Industry)

    Calculation()


