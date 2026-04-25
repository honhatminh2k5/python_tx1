def nhap_dict():
    d={}
    n=int(input("nhap so luong sp: "))
    for i in range(n):
        key=input(f"nhap ma sp {i+1}:")
        value=int(input(f"nhap so luong {i+1}:"))
        d[key]=value
    return d

def in_dict(d):
    print("Tu dien hien tai: ")
    for k, v in d.items():
        print(f"{{{k} : {v}}}")

def xuly_dict(d):
    if "sp01" in d:
        d["sp01"]=50
    else:
        sl=int(input("nhap so luong cho ma sp01: "))
        d["sp01"]=sl

def xoa_sp(d):
    key_to_remove=[]
    for k, v in d.items():
        if v <= 0:
            key_to_remove.append(k)
    for k in key_to_remove:
        del d[k]

def chuyen_dl(d):
    list_msp=list(d.keys())
    list_sl= list(d.values())
    return list_msp, list_sl

def in_kq(list_msp, list_sl):
    print("2 phan tu dau tien cua ds msp: ", list_msp[:2])
    print("2 phan tu cuoi cung cua ds sl: ", list_sl[-2:])

d=nhap_dict()
in_dict(d)
xuly_dict(d)
xoa_sp(d)
print("\n Tu dien sau xu ly: ")
in_dict(d)
list_msp,list_sl=chuyen_dl(d)
in_kq(list_msp, list_sl)