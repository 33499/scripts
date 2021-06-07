import random
import string

def randstr(str_len=32) -> str:
     return ''.join(random.choices(string.ascii_letters + string.digits, k=str_len))

template = """Sailor(chinese_name='{cn}', english_name='{EN}', position='水手', phone_number='10086', 
photos=[SailorPhoto(photo_name='{hash}.png', v512d_name='{hash}.pth')])"""

print(type(template))
cns = ['dh','ysx','lk']
ens = ['丁豪', '叶少雄', '罗坤']
re = '\n'.join([template.format(cn=cn, EN=en,hash=randstr()) for cn, en in zip(cns, ens)])
print(re)