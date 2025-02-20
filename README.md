# PWAphoneCheck
用于完美世界电竞APP的手机号验证工具

# Step 1 
使用Http抓包工具对完美世界电竞APP进行抓包，以下操作使用Reqable
# Step 2
开启抓包后，返回APP进行一次提交。请将中间四位填写0000以便能在0000-9999遍历
![image](https://github.com/user-attachments/assets/13147697-98c2-4073-aada-2d1384c38a75)
返回Reqable，找到如图所示。
![image](https://github.com/user-attachments/assets/2056fb02-9672-4584-9568-cd336b71fc2a)
# Step 3
复制params参数和headers请求头，与python内替换。
![image](https://github.com/user-attachments/assets/f497cc6f-46a8-4e9d-b215-5fa28c529515)
# Step 4
python wanmei.py

请注意：本方法更新于2025/02/20 python 3.13
