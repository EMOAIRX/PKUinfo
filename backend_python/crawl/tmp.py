text = '''
['北京大学智能学院', '北大国发院', '北京大学公共卫生学院生物统计系', '北京大学光华管理学院', '北京大学对外汉语教育学院', '北京大学物理学院人才培养', '北京大学教育学院', 'SMS_Stu_Union', '北大数院人', 'PKU言之有物', '北大物理人', '北京大学学生会', 'PKU医预之家', '大信科', '北京大学历史学系学生会', '北大数院青年志愿者协会', '数院研究生会', '物院学生会', '北大心理人', 'PKU信科职业发展中心', '光华CDC', '走进光华', '北大史学人', '北京大学教育学院团研', '北大脑科学', '北京大学人文社会科学研究院', '北京国际数学研究中心BICMR', '北京大学语言学实验室', '北京大学文学讲习所', '北京大学前沿计算研究中心', '大数据分析与应用国家工程实验室', '北京大学统计科学中心', '北京大学文化产业研究院', '北大古典语文学', '思想与社会', '北京大学严复班', '北京大学', '北大团委', '北大体育', '北京大学学生发展支持', '北大新青年', 'PKU体委', '北京大学教务部', '北大餐饮中心官方资讯', '燕园学子微助手', '平安燕园', '燕园微后勤', '北京大学招生办', '北京大学百周年纪念讲堂', '北大就业', '北大未名BBS', '北大政治法律与社会项目', 'Paideia_et_Cultura', '北京大学国发院经济双学位', '湘思PKU', '北大辩协', '北大红会', '爱心驿站', 'PKU思潜十周年', '未名超算队', '燕语配音社', 'PKUSAA', '北大猫协', '风雷街舞社FLCrew', '北大粤协', '北大耕读社', '元火动漫社', 'pku心协', 'PKU_CACA', 'PKU烹协', 'PKU创新学社', '北大汉推办', '北京通用人工智能研究院', '北京大学学生服务总队', '北京大学社会学系', '北京大学计算机学院', '北京大学历史学系', '北京大学经济学院', '北京大学数学科学学院', 'pku数学系', 'P大CoE教务', '北京大学中文系', '北大社会学'] ['Mzk0NDE3ODg5Nw==', 'MjM5MDIwNDg0MA==', 'MzU5MDg1ODYyMA==', 'MjM5MDk3NDgwMQ==', 'MzA3ODU2MTk4NA==', 'MzUxODk4MDA4NA==', 'MzA4OTA5MjA4MA==', 'MzA5NDAxMDYzMQ==', 'MzU3NzA0OTA5Mg==', 'MzAwMDEwMzI0MQ==', 'MzA5NzUwODgxMw==', 'MzA3MDAxMTIxMQ==', 'MzAxOTAyMjk0MA==', 'MzA4MTAzMzQ5NA==', 'MzA3NDYwMzkxMg==', 'MjM5MDAwNzExMA==', 'MzAwNTA1MjA1OA==', 'MzIwNDEzMDI5OA==', 'MjM5NjQ4ODc1MA==', 'MzI3NTQ2MjM5NA==', 'MzA4MDM0NDcwMg==', 'MzkwMDIzNTgxMg==', 'MzkyODMwMzEwMw==', 'Mzg3MzE5MzQzNA==', 'MzAwNTEzNzcwNg==', 'MzIzNDQ0MDUwNg==', 'MzI1ODQ2MTkwOQ==', 'Mzg3OTg2NTkxMw==', 'Mzg3ODU1OTE2MQ==', 'MzU0MjU5NjQ3NA==', 'MzkyMDE5NTM0NA==', 'Mzg3MTcyNzA1OQ==', 'Mzg4NTE0MDUwNg==', 'MzAwNzc0NzMwMw==', 'Mzg4ODEzNTExNw==', 'MzUyOTkwNTQwNQ==', 'MzA3OTE0MjQzMw==', 'MzIxNjMzMDE1NQ==', 'MzA5MjI1NjIyOA==', 'MzU5OTk0MTE3Mg==', 'MzU3ODg5ODQ3MA==', 'MzAwNDg0MDA4Mw==', 'MzIzNzc4ODkxOA==', 'Mzg4MTIzNzU4OQ==', 'MzA3NzE0MjcyMQ==', 'MzI2OTQ2NDg5Ng==', 'MzUxMzEyNTczNw==', 'MzA4NjEzNDYxMQ==', 'MzU2ODY1ODE1MQ==', 'MzA4NjAzMTIxNw==', 'MzA3OTMwMjc5Mg==', 'Mzg3NjcxNTMzNA==', 'MzkwMzI0MjEyNw==', 'MzA3MzQ5ODIyNA==', 'MzU4NjMyNzM3Nw==', 'MjM5MTg0MDE4NQ==', 'MzA3NzAwNjI5NA==', 'MzA5ODA4ODExMg==', 'Mzg4OTY4NDgxMA==', 'MzUzOTk3NzkxMg==', 'MzAxMzMwNTAxNQ==', 'Mzg4NjExNDUzMg==', 'MjM5NDc5MzgzNg==', 'MzI0NjA0MTUwNA==', 'MzA5MTk4NTgxNg==', 'MzAwNjA3NDQxMQ==', 'MjM5NjY2ODY0OQ==', 'MzA4ODg5NzU4NA==', 'MzA3OTQwMTAwOQ==', 'MzI4MjU0Njc1Ng==', 'MzA3MjMzNTQ1OQ==', 'MzI2ODA5NTg4Nw==', 'Mzg2Njc1NjM2OA==', 'MzU5NjYzNjg0Mw==', 'MzU5MjczNjU0NQ==', 'MzU2MTEwNjk4Mg==', 'MzI0ODE4MjM5Mw==', 'MzIzMzM2NDA5Nw==', 'MzUzMzg4MzgxMQ==', 'MzkxNTM1MjU5Mw==', 'MzI4OTYxMzkyOA==', 'MzI0ODcwNjkwNw==', 'MzkxMzMxMzQ2NQ==']
北京大学智能学院 Mzk0NDE3ODg5Nw==
sleep 130
<Response [200]>
SIST迎新 | 蒋济懋：北京大学智能学院2023年开学典礼学生代表发言 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488959&idx=1&sn=4b0eafbbac589bad5639ea325f0b3e07&chksm=c329c601f45e4f173de9f63617bc6fdba218b76a09110371fcfda3f558c4c96b347ee7f6b28a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SIST迎新 | 钟伊凡：北京大学智能学院2023年开学典礼学生代表发言 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488958&idx=1&sn=ed06ca234f4637e13a278f8e3813613f&chksm=c329c600f45e4f16b2fcd1a3d0f00584b6981e19f6aaa74fd4cfcbdb3bb196904374605e04e6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SIST迎新 | 教师代表张牧涵在北京大学智能学院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488957&idx=1&sn=8f1bf4cbaba62de7528a6cc73e3d1df6&chksm=c329c603f45e4f15cfd38487656c3e4429947284af12be393676a9fba8599bb9bc26fdcb07ed#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SIST迎新 | 吴玺宏书记在北京大学智能学院2023年开学典礼上的讲话 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488956&idx=1&sn=538515efa95f9ec51315722ddaac6440&chksm=c329c602f45e4f14833875254452e0c15ba66b28c6e23fb14c75ab83fca9e3c7646e0112526d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SIST迎新 | 北京大学智能学院举行2023年开学典礼暨开学第一课 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488948&idx=1&sn=b86794f16f791f11080b9e5b35e60755&chksm=c329c60af45e4f1c9632c2b731555ada58557b3209101e7a3c777afb1ca5ff3f9a7ecf918a8f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大国发院 MjM5MDIwNDg0MA==
sleep 404
<Response [200]>
周子焜、雷晓燕、沈艳：教育减负、家庭教育支出与教育公平 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902797&idx=1&sn=edf9e7df84a18c520699ca7dad89a107&chksm=be4eb80a8939311cab2a0236f4243715a5250f9b3006316741989e5577bde5b42cc81ced6ebc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
视频全集 | 宫玉振+杨壮+侯宏：变局时代的战略定力与领导力 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902769&idx=1&sn=628b661b949bdd21fe93c8f29bdca85b&chksm=be4eb87689393160654e4310640ce8981df6fdd0907ed46018da4f600b68c10d369852c9642b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
9.15论坛直播 | 剧变时代的品类创新与战略定位 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902769&idx=2&sn=f648469be1415b2c1de0ae72698871d8&chksm=be4eb87689393160e7ec8d71628c8dff994a852a04f11a859274d26554cd1dcbe5e7ec664271#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
9.15论坛报名 | 剧变时代的品类创新与战略定位 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902750&idx=1&sn=e4a06a4bbecd0d50ca0d33a48aadee1e&chksm=be4eb8598939314f5c7e4312af0d67f9295730d535d6ade0ff0bd3e09faf0ea425c91b0de8e4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
9.12讲座预告 | 林毅夫：百年未有大变局加速演进下党的二十大“两大任务”的实现路径 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902741&idx=1&sn=04ed7e176604fcecbaea9cfc04c04f85&chksm=be4eb852893931443f695a14791b764edf1bf3ba180110245e50d41229065ec0e26de0e7fc12#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
黄益平：清晰区别调控、监管与市场的功能 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902728&idx=1&sn=0d0d78f023ee07431559061b7315178b&chksm=be4eb84f893931593f691638078fc8bb0ecadda1065995a34cf0120f11933427f02d480ed548#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学公共卫生学院生物统计系 MzU5MDg1ODYyMA==
sleep 141
<Response [200]>
讲座预告|(9月19日) ——Theis Lange（University of Copenhagen） http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491794&idx=1&sn=6383976bee995fbd4ec435e720466dc6&chksm=fe3570c1c942f9d71ff3d66f0d5705fc7f9a9ffca4c13f37404e0083202420a92087801f8d95#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告|(9月18日) ——Kun Zhang（Carnegie Mellon University & MBZUAI） http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491786&idx=1&sn=632d0392c514767f85eccdf8d513b6e4&chksm=fe3570d9c942f9cf3196dc78f73280d99dafad1da886f4b9f17e2a82724e799d307db9a7c9b4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告|(9月15日) ——Mingming Gong（The University of Melbourne） http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491781&idx=1&sn=379952060e9e1498dbd6a31d71e4db2b&chksm=fe3570d6c942f9c0c2f551370aec1ebb7822b2be22002bec958ac536bf529a4276442f162651#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告|(9月14日) ——申舒廷（杜克大学） http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491775&idx=1&sn=7f8ae66da288c72c667ecade4287735a&chksm=fe3570acc942f9ba6d15efb61f2a77089eecac872eedafe5ee68cae2045c4e3e6fb91f052083#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023PCIC泛太平洋因果推断大会日程发布 http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491765&idx=1&sn=716247be5631d2e4fb10e8c13bb1ea88&chksm=fe3570a6c942f9b0383b843533454b81e4a0ca946df16d2483dee74f50932689ace066e2a990#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学光华管理学院 MjM5MDk3NDgwMQ==
sleep 199
<Response [200]>
郭翔：携笔从戎男儿志，百战归来再读书@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400020&idx=1&sn=f51e023d44155bb50e4f155b82221055&chksm=bde98bea8a9e02fc400a02103b00e473a6575a282d28891bfa065d532587df3a54a66d76c694#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
张新朝：百战归来再读书，寻找发展的力量@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400020&idx=2&sn=f895e9789fc429a7cc651e7c8e7d9299&chksm=bde98bea8a9e02fcea0969971556ef67205b8234b13a1f2dd570fc923d78f735ec9b75293fec#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
刘春河：赤子笃行，扬帆向光华@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400020&idx=3&sn=d0185f5dab98b2994c7e44b0e8a946e0&chksm=bde98bea8a9e02fc40adfb3f48402ccda9c595cbc35f848784f31a6628dfe4156c0acd9bbe27#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
杨毅：拥抱变化，破局成长@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400015&idx=1&sn=c58d3ad74b514eb46419ac33660d9e39&chksm=bde98bf18a9e02e74d6c27f4d7ec828f221dd2cf70d98e5dd3e54252f397a18cc7f9ff11d86a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
钱婧涵：拥抱变化，破局成长@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400015&idx=2&sn=24272a5b708ca35ac3cd1ce79642d454&chksm=bde98bf18a9e02e73e93eaad526b2928d61e3d7c0846891379038beb8bddecb6acfe35e6a64e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
佀骅羽：拥抱变化，破局成长@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400015&idx=3&sn=0aca5bf9fa221f1d2afc99ac342e5f4c&chksm=bde98bf18a9e02e7064d0b2bf1adf91e81799f74308cff3a6e51c110aeb7937b94924289abfd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
韩靖熙：梦落生花，梦始光华@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=1&sn=075e63369d747a9f7965e94c45bcb2b3&chksm=bde98bf68a9e02e0866614b7563b7df22a918d897686cdfafb14b531628c94629e83bca9ae9b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
CURE Matheo: Chase the light, follow the dream@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=2&sn=227999afb9874d4c8c5dc5950d5f3197&chksm=bde98bf68a9e02e01b03968748f6b0095f40dd55b04a31c66909d706250932575464cc7a05f4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
杨子夏：履方致远，逐梦追光@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=3&sn=11119ae3720d48ab6f5ec49995db5673&chksm=bde98bf68a9e02e0f6b9ce9c288c966adfb6daa17952e60e8a55e8be76962831709673e5ec8e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
欢迎你们！第四届“未来领导者”新生 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=4&sn=36d986fba37694fefe3dfaefaf644438&chksm=bde98bf68a9e02e0ad98f5652c0d8f9a52dcf16f6a2d17780b355320b44ffa59e03eae5c82f4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
一场最美好的双向奔赴丨北大光华2023年开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661399936&idx=1&sn=2faeec1d2fd9be46d142ce9d4fd68c6e&chksm=bde98bbe8a9e02a896216380424d7d7b02dcbc3f69f7079dc1bac09d36e6e88cc89e440c9358#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大光华喊你来上课！3门经管好课9月齐上新 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661399936&idx=2&sn=2ba95e3b3c18ed14cd6c8f4d10eeb56a&chksm=bde98bbe8a9e02a85c114d09e53c2d99021995ff8129cec232abd09ba855aaa5748b99980323#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
苍茫万景，而无苍劲如人者丨北大光华院长刘俏2023年开学典礼致辞 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661399826&idx=1&sn=50ca9843b458676579d29f1b4bcd8b8f&chksm=bde98b2c8a9e023af2fec3647595a1f4cfe8156ec5b2f5d1959190831ab202ca873bebe4c610#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
光华新力量：晖光日新，岁月可期 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661399826&idx=2&sn=3f8093bd1e08da047a82896b18ad6db3&chksm=bde98b2c8a9e023a111919970a3c505b8b40d7347a092e611d65b7f7a2276c07b3231362f4b4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学对外汉语教育学院 MzA3ODU2MTk4NA==
sleep 400
<Response [200]>
舞梦敦煌，国风古韵：对外汉语教育学院举办敦煌舞体验活动 http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728914&idx=1&sn=12a98c20446cc1b5f51dd138a8b8779e&chksm=874a9e7db03d176b8c90840439f02c3b72dba858ce99971095497153654a3e63edd03ea72591#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【北京大学国际中文教育讲坛】代云海《经济学视角下的国际中文教育》讲座纪要 http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728899&idx=1&sn=e970230a65a3e3b2debf4f4cd7c04a17&chksm=874a9e6cb03d177accc8ec7b37013703d243d82ea57bde3a35a26202f8d7daf348ecf064bd2a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
对外汉语教育学院举办第七届汉语作为第二语言研究国际研讨会（CASLAR-7） http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728887&idx=1&sn=d582400f437c42c2769f44f5385e4a24&chksm=874a9e18b03d170ec2342c080e35fd43f32677b74dd503858fcf6c0be6747dda705b408dc070#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
第七届汉语作为第二语言研究国际研讨会 http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728865&idx=1&sn=380089548e4ac82b85d5aacb2bff28bd&chksm=874a9e0eb03d1718fec700569eb4a19f665dbed0d36ce2cb12862680af7b9ba54a2ea14c98da#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【北大国际中文教育讲坛预告】代云海：经济学视角下的国际中文教育 http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728852&idx=1&sn=11528e02ae602206ac6a6ac3090d063d&chksm=874a9e3bb03d172d9d478871670af1de72cb6330af519e3223ce99fffb143241731dea337cfd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学物理学院人才培养 MzUxODk4MDA4NA==
sleep 427
<Response [200]>
新闻 | 物理学院刘川老师获2023年度北京市高等学校教学名师奖 http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486933&idx=1&sn=6f3dff5ba632a98fa2d42a8f7751f0b0&chksm=f981e54ecef66c5855d61722c94a9192eea2e8949cf591b51ebe5110fc7f2c00d9e1e900fcd9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻 | 北京大学代表队在第九届全国大学生物理实验竞赛（教学赛）中获一项一等奖和两项二等奖 http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486776&idx=1&sn=58176c59738aa1c4e66dbc65db06f7f2&chksm=f981e5a3cef66cb505d992d21904195321d323d60eb6924a4307fc544d37d3ecde9427ddd785#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知｜2023秋季物理学院免修考试 http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486771&idx=1&sn=6d5f5a5cdad4682444ab541e7e257664&chksm=f981e5a8cef66cbe813e4c759e1b1cf57deeead882fa2bca179a53b9d4d4d612861deff09c02#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
专访 | 北大物理学院量子材料科学中心研究团队发表论文回应“全球首个室温超导材料” http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486758&idx=1&sn=9c177973ae0721a952514a1f8b8218ab&chksm=f981e5bdcef66cab327a5e7080cdbedd8aaa77b3b92303d7ff77021dd3df1795d4bbad1c1de2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回顾 ｜ 北京大学2023年全国物理学与大气科学优秀大学生暑期学校成功举办 http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486744&idx=1&sn=e5bdc0bb15f5a563b856963dd70f756b&chksm=f981e583cef66c954532d14d26b4844c9ed1d212e1ef6acb60a690467be24b9df35f7c6a5c31#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学教育学院 MzA4OTA5MjA4MA==
sleep 372
<Response [200]>
我院Ed.D.于晶荣获2023年全国新时代“百姓学习之星”称号 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738434&idx=1&sn=1bcd35b09683bcb300d64a5d19d8eb04&chksm=8bc9091dbcbe800b0e958bc38468afeadc7f9c0aa5742be167520ffda166e32b459159dad3ef#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 北京大学教育学院招聘博士后研究人员 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738416&idx=1&sn=2a2c23d6addbeeaf1256ab652c8c5154&chksm=8bc909efbcbe80f9b65cd5e5226f52d345a023ad9a1e332e3455ffed43d7b44c5569a3a550b4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学教育学院2024年接收推荐免试研究生的说明 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738416&idx=2&sn=a04091a499e6bc82b2bd5505ec05bf33&chksm=8bc909efbcbe80f96c15443779566a7dd34a2ee05f716db4e2ea5511504898ed8ceec9391757#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学教育学院2024年接收推荐免试研究生的说明 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738408&idx=1&sn=7a73a1cd80b8c76e8b5608025a4b3423&chksm=8bc909f7bcbe80e1a29bacff271d7b0a9ef5b02b6cdfdfdb13dff1135336bfb4bfca43338eba#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学学生参加2023科大讯飞星火营并荣获佳绩 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738395&idx=1&sn=96ddc1c9922f2e382d75633bb7de22b1&chksm=8bc909c4bcbe80d28efcaf51e93687aed387b79c2b300e382c676315ae27447444a9d72e640e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教育学院举办承办中国高等教育学会学习科学研究分会首届杰出青年学者训练营 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738382&idx=1&sn=6a764e0c5f457a6bfd5390ab8799c087&chksm=8bc909d1bcbe80c7e5c416e3eac8071bfdb7650ca24c3e2ce803f7ca113d1d7c20452e4f22fb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SMS_Stu_Union MzA5NDAxMDYzMQ==
sleep 401
<Response [200]>
【颁奖盛典】数学游园会预热 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886159&idx=1&sn=78f09ae2cef978d956995994ce7f5c30&chksm=8ba0dc67bcd755713a04208b57c68cec14a18da3847e7dc047e453be4ca2a0be34b9f80a4c2f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【推广】Optiver北京大学专场活动报名 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886159&idx=2&sn=a7b8632d10dfe082f1215bdc6f9f2892&chksm=8ba0dc67bcd75571bfa237bae27cf71e986513ed5c3c4cdf1872d188588709c8da9f341af380#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【暑期实践】探求生态文明建设，赓续西南联大精神——北京大学数学科学学院2023年云南实践团 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886141&idx=1&sn=12884fb667af1e03c9c8825064b60f36&chksm=8ba0c395bcd74a83ff9e8d652c5f73bbe03bfa2090b3b34ec71dc5dab396ca2c77bcb99de662#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【新生破冰】回顾·参与丰富活动，融化社交初冰 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886141&idx=2&sn=95828b448839b751d647812f0d7de53b&chksm=8ba0c395bcd74a833a4e1c592ae17d967b787276e4028ec1f31234bd40d4423c635c9615023e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【颁奖盛典】主题辩论：AI能否取代数学工作者 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886127&idx=1&sn=4aa1f016d13079383b2fb3474f40f06f&chksm=8ba0c387bcd74a9177218d914188deb309727ee8221e694f97ab48ec785576379cc4e3b39387#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【颁奖盛典】阿赛数学讲坛震撼来袭 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886110&idx=1&sn=8329bfa136b3dafb0f766e5a854903a3&chksm=8ba0c3b6bcd74aa0691700f2abf050f5ef668d4fd728ac583ff62506bf468a33dca9337fcb9b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【推广】“不踩坑”“有效率”—【大三申请规划】优秀模板到！ http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886110&idx=2&sn=1140c2703818a86ebde38a1931825072&chksm=8ba0c3b6bcd74aa0508347a5f82513eb2491100a3f33ab373a1387de690fa73d4cf867c4281f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【新生定向】数院&外院&化院联合新生定向越野活动预告 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886055&idx=1&sn=de41e53766f13bbf30199020f78891b5&chksm=8ba0c3cfbcd74ad90568c7262c5aaaef9499f0257487b837628f835a3346da91c3bf6fd34b5c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【新生定向】新生定向越野活动志愿者招募！ http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886055&idx=2&sn=928ac7905e87bb42450dfbb7ddfb0bf7&chksm=8ba0c3cfbcd74ad9454ab65e28a35735df24787c0df2fbdafe8e28fc58f8bce5a9013d887b2b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大数院人 MzU3NzA0OTA5Mg==
sleep 362
<Response [200]>
数学科学学院召开带班辅导员新学期见面会 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499185&idx=1&sn=5e22f7df15f21ce4aedee9996180c993&chksm=fd083adaca7fb3cc70cb9df10b46e66e26766bbb9a745eff4adbd4062ba6759cb5b3592224df#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动回顾 | “薪火相传”旧书回收活动顺利举办！ http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499142&idx=1&sn=872ec858010675a812aec3cf6060519f&chksm=fd083aedca7fb3fba40bad4a65c7c344c66cef1b436d4d7273d1c6d666629eb1c3c1347b9194#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
颁奖盛典 | 阿赛数学讲坛震撼来袭 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499142&idx=2&sn=e0e220b65c024d9610b6820254c9c0c0&chksm=fd083aedca7fb3fbd20f7e243b39830b93a1de3e770580b47a081172fa23d56eb59cb9f0dab6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
颁奖盛典 | 主题辩论：AI能否取代数学工作者 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499142&idx=3&sn=104dcb7544130385902a294d4806a270&chksm=fd083aedca7fb3fb7f40a998a5591a4277c8d9328bc53fc9958438b923418e2687d9e66945ba#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本科生新生代表胡殊闻在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=1&sn=e887c8e8bdb0f6374809dc87860495cc&chksm=fd083a16ca7fb300d52737f7606093c1922e40408c87fc3b6a1a6daf03f0efbbac724ba97675#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
硕士研究生新生代表王楚凡在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=2&sn=a5da0b7ebc8a59fec8ba0bc3bc55cdfe&chksm=fd083a16ca7fb300902172736b99b2a5d6138b1638a2f93771c18ee4c622af0898919e7bb456#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
博士研究生新生代表史庭潇在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=3&sn=ab0c81747d066b108533187a400c7257&chksm=fd083a16ca7fb3007a5b03c4a047d619e9df2f6e5ac9906aa08b9835f5c77b6d28e784359b7c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
老生代表杨晨曦在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=4&sn=ff251ad0d7416956475235abfc52ee2e&chksm=fd083a16ca7fb300280a6b8f14c2040d4a6fe41186b241d5192671c5a0c35193c32a019bd391#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
培养更多数学拔尖人才 | 院长陈大岳在北大数院2023年开学典礼上的致辞 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499126&idx=1&sn=3eeaeb009d5b36ae12cc844ca7ce5c7e&chksm=fd083a1dca7fb30b2e8ebacaf57d50a158da4baf9e061b778b3f7007f692752e7b6994ab8bf8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教师代表卢朓在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499126&idx=2&sn=8fd2a4843952ecae12775d0dfa21e1b2&chksm=fd083a1dca7fb30b12878e36482e53a1226dadc4cf227e2f439c2367aadbb04b13cb900912f3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
院友代表于品在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499126&idx=3&sn=d283a8a67ba3289b8676573d2262fc18&chksm=fd083a1dca7fb30b7d2166470532335fa7e61c3dae685ee52925c7d7c3e044c858042d8f5c91#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学数学科学学院2023年开学典礼在智华楼隆重举行 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499121&idx=1&sn=384b04a60f55fbbc1373ab745229c780&chksm=fd083a1aca7fb30c0e92f190af50555108c6b2bb858d2bb5c80db21ca2abdc562d0112bafb4b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
110周年庆·数学学人 | 王诗宬：从书房出发，到全世界去 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499121&idx=2&sn=24aca25a403976b9700227d0b1c6c710&chksm=fd083a1aca7fb30cb93a5aa7ea7eeac47fe9dd2fcd669f5c7e71a2fae653cbc3f7a77ddd2164#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU言之有物 MzAwMDEwMzI0MQ==
sleep 526
<Response [200]>
物理·班团丨青春不息，奔赴不止——物理学院2023级本科10班开展班级建设暨团建总结交流会 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832575&idx=1&sn=412a44fba3cc574dc641ca90722fc79d&chksm=bfd70e5988a0874fa2eef895c5275393c54d149c98ab0b7e8809a8769e4b314051cbed57b387#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新丨“团”学聚星火，“组”织汇英才——物院团组等你加入 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832554&idx=1&sn=515bd2295976d746e157a0d2a8cf57fa&chksm=bfd70e4c88a0875ad2e1c0e2181d3ad8d1a77ebe38c2315e59dfdd8eab9b9a87d0a5449c6317#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物院·就业丨联影医疗宣讲会成功举办 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832554&idx=2&sn=46a8989ad559e031ec29c67585d251ec&chksm=bfd70e4c88a0875a67bac82f8767796a48692361ffeda4fc4470d5ea5472cb51ba44cdad2fbe#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
迎新丨探理博雅梦，格物迎新篇——2023级北京大学物理学院研究生迎新与入学教育综合报道 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=1&sn=3697089919596e58ce19e3b9bfe0e97c&chksm=bfd70e1088a08706c1266ffbc9768e3c6a229d3c1981c2da086ed17230caaa1af53fcd540b2a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物理人如何拥抱新能源时代？第二期“物理+”校友沙龙等你参与！ http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=2&sn=990d9ace5cc7077edb4409531ab9b26f&chksm=bfd70e1088a08706a4523c33df4345ace8d3ba3262484ca5cf7ca125c1c5bdf28b4014697feb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物院·就业 | 2024届毕业生就业指导会报名通知 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=3&sn=94123a90b986798165ac173c6ee70c74&chksm=bfd70e1088a08706ecce58d0afe72aaea0e0b5aa3603204aea3d16dec30c057895b403b46a65#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
研会·放映丨《教父3》 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=4&sn=e1afb39dfde5557dbbe5b9a28f565115&chksm=bfd70e1088a08706c71f4ddcb9f8099801838b084d05b34913c7d87fd2263e3d9959009b7e15#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物院·就业丨燕园快讯直通车 (第一期) http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832482&idx=1&sn=8f9548f78678ef19c4a0942517dcb031&chksm=bfd70e0488a08712e9e1820196b514f3610d2620c2ebfd5dcd7a2ba9114acd9d4c0cfbc1943a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教师节丨感恩老师，感谢有您 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832437&idx=1&sn=234675a92fd4c02fa00e4eafa8655852&chksm=bfd701d388a088c544c56ca20a0bc0a67b28196b650df5c54d8c7edd9d52dd2d9e302cae3990#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼丨院长高原宁致辞 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832437&idx=2&sn=4eac8f9a71005690c4ccd02a1dec721d&chksm=bfd701d388a088c54ff4ef6734b6531fb89b7b30f0f6ec3636ff67194e4e717d5cf89717b138#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼丨校友代表贾金锋发言 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832437&idx=3&sn=09fac2ce9a56fa9db0b1d33029e4693b&chksm=bfd701d388a088c58f53e902f9435cb88cb54097bcfedfdf588f0cc10921ea924d8877a092ed#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼丨教师代表俞妍发言 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832437&idx=4&sn=b00d876ca3cf7fff64de962be2f3e30f&chksm=bfd701d388a088c585b482c3e5f8dac641c4632dea1477c64cdad6dda2e0ca7c675c480763b6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼丨本科生在校生代表柳天昊发言 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832437&idx=5&sn=40749d36ec58369cf6eaaf5d65308c4a&chksm=bfd701d388a088c5373a3fd57867ffc095847646ddbac5e4484d643d4307cd594c009be5f4d0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼丨研究生在校生代表戴天祥发言 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832437&idx=6&sn=de2566b7c3be18142452b7a0856b61be&chksm=bfd701d388a088c5f8d79ac8cc796cb3c0aedb2956a4f8183e5a2c787a99206ae75479bc41e2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼丨本科生新生代表李开阳发言 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832437&idx=7&sn=86a28b853cdd50d55ef3827091444a5d&chksm=bfd701d388a088c5b6dd47e6c89ea23c6d3e45d67faa998c6b3a59a7f2b2edbbf85b3677a320#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼丨研究生新生代表顾昱晨发言 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832437&idx=8&sn=12f4183062f2c1c32993a52089d975a0&chksm=bfd701d388a088c5f30679f66f7fc4643b8a45eb3a2ee02da7fb85505c65f35f05c1026b875e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大物理人 MzA5NzUwODgxMw==
sleep 241
<Response [200]>
成果 | 极端光学创新研究团队刘运全、龚旗煌等在二维过渡金属硫化物各向异性间接层间激子态的超快电子动力学研究中取得重要进展 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058320&idx=1&sn=6325a5e6f5faac81b1c5f81892b33956&chksm=8b3b5772bc4cde64e7ee7656da63cd75293ef96dc4ef09efe89d5f169a3e12056d7ebf74cb77#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告 | 北京大学物理学院学术论坛（第二十六讲） http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058312&idx=1&sn=9b48235343a49045e6c2f18aa0bfaa42&chksm=8b3b576abc4cde7c74dc5c2ddd5f289dc27529388f72e2c27e753e404ba1e577609a88b33b92#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告 | 格致论坛（第十七讲）：超冷原子气体中的精密测量、精密调控及其若干应用 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058312&idx=2&sn=7e069fb3e525f4e481f1342a9f5aa095&chksm=8b3b576abc4cde7ca4ceed5a1c66fc275c901f83c73c2c92fde16e3357c650cbce3828bd8ecb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告 | 北京大学物理学科卓越人才培养计划讲堂：名师面对面（一） http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058295&idx=1&sn=a722546cef89c21cb28efc8ae77043f5&chksm=8b3b5715bc4cde03f0caa0423b73d83bd98cc02f9b289044f53d6e07f9c76c8781f352d99496#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告 | 北京大学物理学科卓越人才培养计划讲堂：名师面对面（第十三期） http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058295&idx=2&sn=720a8b57e6216002b7cb9845109d80ca&chksm=8b3b5715bc4cde0331f1eda8cf82845bc7b1b7ec72473917237ae4407a44e7f1e3136dbc3a32#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
节日 | 恭祝物理学院全体教师节日快乐！ http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=1&sn=1e59d085db07b4e4448cece35b7a05f7&chksm=8b3b570dbc4cde1b4facff5a6b766ee17fb3fb55970be506fe6012a85e8f722792bcf27e402f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 院长高原宁致辞 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=2&sn=68313d8894c367ff73b8a6d8697d3858&chksm=8b3b570dbc4cde1ba3daba229807f1395bffbc8f3abe427be2a7e4463916b62b13fd8189ab89#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 校友代表贾金锋发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=3&sn=062f556e65117a2b80ffae3d1b965bfa&chksm=8b3b570dbc4cde1bbd7f12fea6ae3aff1f1500e3440f3cf9b20b7f71788b9cb5eef431d716ef#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 教师代表俞妍发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=4&sn=f44cbc67ab648b08c1f14778bc28bae3&chksm=8b3b570dbc4cde1b54faee5b16bef833ca321b7e35ed17c2fa30c031e7529663d8efa3ae49ec#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 本科生在校生代表柳天昊发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=5&sn=17fcb687696f5409cc89f5095dad62a9&chksm=8b3b570dbc4cde1ba2be4c174556e935d2736de48d0efd5739fcf0793c3fdb9b2ff65d319413#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 研究生在校生代表戴天祥发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=6&sn=9f4887c642a99ff0309290571aaba9f1&chksm=8b3b570dbc4cde1bbf8f67b7239f2d79a179d7bed6201320e0aa82b11c007d431d847b24b149#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 本科生新生代表李开阳发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=7&sn=85ab6b51fc80b93a78ddc14a9d5f9bec&chksm=8b3b570dbc4cde1be54a2bdf5f4691db076934334cd1598dcb2101e225d20bffc44425ec384d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 研究生新生代表顾昱晨发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=8&sn=94a3958866adc4551d0c7c469a03978f&chksm=8b3b570dbc4cde1bb31ff390c4f2c437cd77afeddbf98ae6809c06c8215635fc76ffcbe266ad#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻 | 北京大学物理学院2023年开学典礼隆重举行 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058282&idx=1&sn=12693ebcdc295f82c800877e7f9c3296&chksm=8b3b5708bc4cde1e18f42159b4a3e00c6ea867192889b1a316612879162ccb1b50585119a5ef#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 2023级新生合影（组图） http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058282&idx=2&sn=92f560fcc42c542ad0cbf29deca6570d&chksm=8b3b5708bc4cde1e7ae2afb708dd9bcdab7713170a05af992ca06361eb6ecb8eb1562754e7a3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学学生会 MzA3MDAxMTIxMQ==
sleep 129
<Response [200]>
星野·回顾 | “星野”社会实践团赴北大红楼开展实践活动 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120168&idx=1&sn=4c88ab79aa6904669b5bc22bbdfaeb39&chksm=8533120cb2449b1ab92a1e3242d60f93ccaa830d92ba87dc04cac468f1e0fc57396b011804db#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新｜综办在等你 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120116&idx=1&sn=2de9fe587417622adaad7d04f6c928bd&chksm=853311d0b24498c6b069ef8b70640ce482b7e429609ab8d3ab7c49c41b077929523a112f453b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 快来加入监察部吧~ http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120116&idx=2&sn=60fbe5d1932226b0948a012b12c43ea5&chksm=853311d0b24498c67aa0a120e383584ea52be89d0e3bbd242838911b412e388a0f7f635f77e8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 常代会权益提案部期待你的加入！ http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120116&idx=3&sn=5d2d0236ce7b2ac65c32f4e00676817f&chksm=853311d0b24498c64d96401f07d9adca18e30fe30e34d388ba7a7abe7b83259b6bc8294d3301#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大之锋 | 决赛预告 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120115&idx=1&sn=b40087af58627bea3c0cac471fd8f8b2&chksm=853311d7b24498c12cb5544c2c84efbb54bbb04886261c0a995cc6618960f0b8fecb733bf673#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 北大学生会，期待每一朵星火 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=1&sn=213830056e89c1abe5c474db95a1ba52&chksm=853311ffb24498e91dd996fc264100b723a9249dbdc2d9bd2ceedc7ff73edfc3741c7b6c2dfc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 综合管理部：综以有序，扎实建树 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=2&sn=f9b72ac5fbf0c6fdaabe388b22ea57c8&chksm=853311ffb24498e94104cc798a2b68ac6278949de780dbbe3a4144d3933fd5d40f281d257f3d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 宣传交流部拍了拍你，邀请你一起前行 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=3&sn=c62346986a935b0f19e70315a6b05f6d&chksm=853311ffb24498e9080001e32f95cc62eb9e257213714d54bd4655ea46d564dbeed194db245f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 风采实践部：承风采神韵，开实践新风 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=4&sn=9ba8f10175426d3f90204cd5ee6d2d31&chksm=853311ffb24498e9dc8befe37cca349f44aa9d3f5de51a97896d789e777bfbff2f65612e8c1b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 学术科创部：亦知亦行，求实创新 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=5&sn=5e22367eb1193ff2ddbb6d1c160976ed&chksm=853311ffb24498e96c961f043963c85f777522a8a659ff950dee54a7fe3c5a337e02bd5cbbcd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 赋生活以精彩，许服务以未来——我们在生活服务部等你哦~ http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=6&sn=8c04413274bc30e099fd483791160891&chksm=853311ffb24498e9b7b0ed00c408db3d3b6e30ca3607502bb94d63e852e767c1c08e80518dcf#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 文化体育部：发光的少年，请留步！你五行缺文体！ http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=7&sn=56a08fc35e1d5ddb2bd62e6bcab610dd&chksm=853311ffb24498e9aa4f53c9f5d04c09d81735504eed5fe2dd38c322ea1fc28057a619a39c2c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 心心念念，从新出发 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651119983&idx=1&sn=503464da24f9fd7914f6d9d604a2e3cf&chksm=8533114bb244985da7e765db5c2aec42b71109049f9f5543040b3e0a34d3df363d329c048745#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU医预之家 MzAxOTAyMjk0MA==
sleep 488
<Response [200]>
【志实部.055&&助理团.021】朋辈π：PS和Canva保姆级教学来喽~ http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048752&idx=1&sn=438a09d75812618db8ff59677585181b&chksm=8069e343b71e6a5504ece02a4d5b4483d05c81deaf554eafc73c60815c28a8696c9aa773901b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
医路奋进，踏浪高歌｜医预主席团&部长团复试通知与志愿者招募 http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048739&idx=1&sn=1c323b416254599ad33be7dddf2c7ef1&chksm=8069e350b71e6a46a0fa3d8d401434c898c43eaf894051b5e62483b3e321e136f30e3e09b6af#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
医学特色橄榄绿在盛夏绽放 ——三营八连军训连队活动简报 http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048726&idx=1&sn=8cc50a1a4a73d0c92e9930c1e29edb8f&chksm=8069e365b71e6a739aabc2cfbe92ae0dac24d72c0353d12b3a591d4b46a2bc18280df90986da#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
医路扬帆新梦想，奋进征程同启航——医学预科学业辅导与生涯发展规划工作室开张啦！ http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048695&idx=1&sn=71137534a6d895c3302922e13dbd7174&chksm=8069e304b71e6a12a154a848037707f87d5231bb9369c0f46aeab3610dc492291eccd78576a9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【学习部.040】医歌不辍，薪火相传｜快来捧走学长学姐“沉甸甸”的爱～ http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048688&idx=1&sn=8d52aa5a2676139b6b8b5191b7be9810&chksm=8069e303b71e6a153bfe24599eed6235bd0bbf9342ad9fa8a7deb6f111743fff1ba81bcd8b27#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
大信科 MzA4MTAzMzQ5NA==
sleep 588
<Response [200]>
预告 | 北京大学显示技术系列讲座第3期——OLED材料的发展和趋势分析 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886182&idx=1&sn=6673c569b3e4ca9211f3fdca2a87774e&chksm=846ed05fb31959499957318767d493e0549befabd9bc116e43f802fff3bf3dab270e87cad73f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回顾 | 信息科学技术学院2023年“新生杯”  乒乓球赛 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886182&idx=2&sn=8a0952186ec984d98adc52ead5f71225&chksm=846ed05fb31959491602352865c849ab41a6ea596c115c70b6015935a4b059bb625fff465a9c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信息科学技术学院2023级本科生陈浩伟在北京大学2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886182&idx=3&sn=1bf410ff6c03b687438cdb328b95ed7c&chksm=846ed05fb3195949c25976836eb5628e58890d44e98ebda1ddc0998e9f9badde72f371efe9da#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动 | 新生定向越野报名启动 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886172&idx=1&sn=0a45715bcedb7719e416a1edffa01c16&chksm=846ed065b319597340be07578807fc19b5a4d17c515f740cc822b99fe47a6f79c170d59b82e6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信有所行 | 披荆斩棘鸿蒙启，中华有为天下先——2023信息科学技术学院赴华为北京研究所思政实践纪实（上） http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886172&idx=2&sn=44b242859f175871cb964b2bad4c2285&chksm=846ed065b3195973c89f99d30c8e90a0b3f9fd45fccef206ad6e67c23939d26b6762903136cd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信有所行 | 厚积薄发创芯业，以行践言开新篇——2023信息科学技术学院赴华为北京研究所思政实践纪实（下） http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886172&idx=3&sn=1d39ea9113a5d5144ac1cbada91d64a2&chksm=846ed065b31959737054419fd5aa758a84327f58a6ee3e20c3885bc62353201c530ea91fa8e8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
学术丨虚拟机配置教程 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886132&idx=1&sn=0c59c88a2697d9ac98a5805f95bb1383&chksm=846ecf8db319469bed08bed545b1b0ad166dc83724c82296f6d854d920598e25ce585429237d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信有所行 | 高举旗帜跟党走，躬耕实践促新知——2023信息科学技术学院赴重庆璧山思政实践纪实（上） http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886132&idx=2&sn=8601151f24005d7d324d297630cf3916&chksm=846ecf8db319469b775895dcea79f355c6e5affe1d6096dde222c88fe61441792cd674b77f73#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信有所行 | 红岩精神传薪火，勇立潮头谱新篇——2023信息科学技术学院赴重庆璧山思政实践纪实（下） http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886132&idx=3&sn=eae39a63db580f5225a31716c303d5e2&chksm=846ecf8db319469b151a63fdb8f018ddbc46c29f8a1633dc20303b2cf419fc5787a8eed99b5a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知 | 北京大学信息科学技术学院2023-2024年度团委部长团招募通知 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886121&idx=1&sn=43aacf62444db4243c6a1e0cb4a549d1&chksm=846ecf90b3194686e88f6a2370489e88522985f18632f3550fe2bbba22198a2079ec0be89e07#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻 | 2023-2024学年信息科学技术学院团学各部门交流会顺利召开 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886121&idx=2&sn=f921c41f1a54c35012cb1aba860d0caf&chksm=846ecf90b3194686ebfa74f45638eb41de5f39abacb1cb7403a2543003cb72554f932b736a94#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
学术丨vscode配置 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886121&idx=3&sn=a7832f79c4fec88e1b35cc5ff0c90800&chksm=846ecf90b3194686697fd30493243f5b61af6801ea711e269b2ae10e4e9b608ce31f0f1ef1a6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“信”理论，“心”思想 ——北京大学信息科学技术学院本科生第五党支部与北京师范大学心理学部本科生第二党支部主题教育党课 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886064&idx=1&sn=ca4099aa4e684dee7025e39b79bc9597&chksm=846ecfc9b31946df6b8e2556be17644cb39568d8452b428da790656a78e1ca016590a55fd7da#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学历史学系学生会 MzA3NDYwMzkxMg==
sleep 512
<Response [200]>
招新啦 | 历史学系球队介绍(补充) http://mp.weixin.qq.com/s?__biz=MzA3NDYwMzkxMg==&mid=2650386840&idx=1&sn=b954e0771c58977656c6116fa0c26095&chksm=87705d7fb007d46955364b140010bf5ab8bc3e274066d5eb14473f39c31e00229732fa0fac31#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新啦 | 历史学系球队介绍 http://mp.weixin.qq.com/s?__biz=MzA3NDYwMzkxMg==&mid=2650386818&idx=1&sn=70a874a40f97fd6bbacd3574b7702366&chksm=87705d65b007d473362940a4cd9feba19751aa1ee4f34349ae34fb7a826b98de9a6a8113a820#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新啦 | 历史学系团委介绍 http://mp.weixin.qq.com/s?__biz=MzA3NDYwMzkxMg==&mid=2650386748&idx=1&sn=a6bf3a33aff2f2830ffe336390debb7b&chksm=87705ddbb007d4cd20f6c2183e834fa3b73af229060f2bf06fbb944c8b5f5214f7d3c02ac8a8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新啦 | 历史学系学生会介绍 http://mp.weixin.qq.com/s?__biz=MzA3NDYwMzkxMg==&mid=2650386748&idx=2&sn=275f430671f00634bd5e6cf8b8857125&chksm=87705ddbb007d4cd4c5056a2be00166e434bbfa429e92591f1be151ff86899d555bace6f0e9f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新啦 | 历史学系青协介绍 http://mp.weixin.qq.com/s?__biz=MzA3NDYwMzkxMg==&mid=2650386748&idx=3&sn=ab9a28c7af4e8dd1ebdcbc340e3f9b6c&chksm=87705ddbb007d4cd7bc3e12ed2d46951626d5b1a7fa76ad703e84af9ec65005ae2975b92d2e3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
军歌嘹亮，新燕启航 | 北京大学历史学系2023级本科生军训总结 http://mp.weixin.qq.com/s?__biz=MzA3NDYwMzkxMg==&mid=2650386705&idx=1&sn=65922533475eb79bc998e37b43a6e8f9&chksm=87705df6b007d4e08ef41bc9bb1f7ecb52e80f553456f86da6468cd96f217678d6281b8564d6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
公告牌 | 学校近一周重要通知汇总 http://mp.weixin.qq.com/s?__biz=MzA3NDYwMzkxMg==&mid=2650386705&idx=2&sn=1dae4f4a3b4ea26cc134bdbedf891b38&chksm=87705df6b007d4e0635bb0771895411137b952ce55b7aef55130340a6b1d0d6d8135e70875d6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
军歌嘹亮，新燕起航 | 北京大学历史学系2023级本科生军训纪实（二） http://mp.weixin.qq.com/s?__biz=MzA3NDYwMzkxMg==&mid=2650386686&idx=1&sn=46d31711891c9e55c337a3adba7ce5c2&chksm=87705c19b007d50ff9cfee7cd4748e4d0ddbdd53d4805e95ade3b9aa7b2e0ad0ab09bebd3ee2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大数院青年志愿者协会 MjM5MDAwNzExMA==
sleep 459
<Response [200]>
活动回顾 | “薪火相传”旧书回收活动顺利举办！ http://mp.weixin.qq.com/s?__biz=MjM5MDAwNzExMA==&mid=2650767460&idx=1&sn=d498c5cee79f95cc5120ae63dfa7ac67&chksm=be404a4d8937c35bd813c6b691205a8cc826d0c3b3e515f46d721d4f3a9a497483c66e1343c9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“青”囊相助，“协”手同行｜数院青协招新啦 http://mp.weixin.qq.com/s?__biz=MjM5MDAwNzExMA==&mid=2650767453&idx=1&sn=0734cb2ac153fc70c037f44a4fddbe6e&chksm=be404a748937c362aa1357cae1033efdfe6941959ebf12f6f66f651a7b049f49e30fa1626aa9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
一号院系服务队 | 学业辅导、高数线代串讲 http://mp.weixin.qq.com/s?__biz=MjM5MDAwNzExMA==&mid=2650767450&idx=1&sn=40cdba85d6561e3113f332362f74a1b5&chksm=be404a738937c365a262730e96a988a4320c74c193d0688be2e437010341768b35d7d8cfb650#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
学业辅导第二弹 | 五一专场 http://mp.weixin.qq.com/s?__biz=MjM5MDAwNzExMA==&mid=2650767446&idx=1&sn=18fedf1f38b98a98ae98a0a06af2e877&chksm=be404a7f8937c369108886ba66fd380317d616ddfec8f9048c4956dbad5f38cd902e35952678#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
一号院系服务队 | 滴~您收到一份高数串讲邀请函 http://mp.weixin.qq.com/s?__biz=MjM5MDAwNzExMA==&mid=2650767443&idx=1&sn=6ec95d544bebe096090ef615fca3ef48&chksm=be404a7a8937c36cb21a6086922cb245ce5f0c37effefaba101d6cfbc119a80f7ee655665814#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
数院研究生会 MzAwNTA1MjA1OA==
sleep 444
<Response [200]>
【颁奖盛典】数学游园会预热 http://mp.weixin.qq.com/s?__biz=MzAwNTA1MjA1OA==&mid=2651020791&idx=1&sn=05b4d8323d9513c688093daa17c29a92&chksm=80d57e02b7a2f714847d2bf44b4738880ce42c4d305990e27dc372e3935e033cc7778d6e8d8b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【颁奖盛典】主题辩论：AI能否取代数学工作者 http://mp.weixin.qq.com/s?__biz=MzAwNTA1MjA1OA==&mid=2651020789&idx=1&sn=aa873f58a3f28c5ee5efd286dd9ec528&chksm=80d57e00b7a2f7161aaa54c22320b81b6b25c5125ef4cf746e4d5507de9b78caa241bb8a5937#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【颁奖盛典】阿赛数学讲坛震撼来袭 http://mp.weixin.qq.com/s?__biz=MzAwNTA1MjA1OA==&mid=2651020787&idx=1&sn=2dc4d9383d6397b7e3157330ebd310a2&chksm=80d57e06b7a2f710303d9cc0c8a9a1a50690a3e48eb615cd100a2759408d2fec4ab3b73b3792#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
第五十七期学术午餐会 http://mp.weixin.qq.com/s?__biz=MzAwNTA1MjA1OA==&mid=2651020784&idx=1&sn=8caf7aefda6adb2f58f994024241f764&chksm=80d57e05b7a2f71364dbe4711aab02d469de87e521bcfcd4370a8c119668d4e7960f7981cba2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学数学科学学院全体研究生祝老师们节日快乐！ http://mp.weixin.qq.com/s?__biz=MzAwNTA1MjA1OA==&mid=2651020784&idx=2&sn=945d9e7147e0e34d9ada409f2cae6038&chksm=80d57e05b7a2f713c23c7bd8df38026b8feef43cfbf779e46627e9543fc97efdd5c43941036c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
第一届数学前沿博士生学术交流会议报名通知 http://mp.weixin.qq.com/s?__biz=MzAwNTA1MjA1OA==&mid=2651020746&idx=1&sn=d5e94e9249ae5b705b4fa8699f9e0ef8&chksm=80d57e3fb7a2f7290e0477a1313a7fd41e6c7adcec2e115a6c0a318f73d0524173f15bdc0df0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物院学生会 MzIwNDEzMDI5OA==
sleep 529
<Response [200]>
【物理·学术】新老生交流会成功举行 http://mp.weixin.qq.com/s?__biz=MzIwNDEzMDI5OA==&mid=2247503746&idx=1&sn=6fbcf7903487ac84dfcd38ce5d1db094&chksm=96c65d17a1b1d40152a34eeaea8426ade0320fa5c6184214ef04e16344dfa42efd000af61a2e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【物理·生活】费米子失踪案——2023新生定向越野开始报名啦！ http://mp.weixin.qq.com/s?__biz=MzIwNDEzMDI5OA==&mid=2247503741&idx=1&sn=39d0068d2f91103a8e37b40b590bba38&chksm=96c65de8a1b1d4fe11292b394d72463f2994f4a81cae1f064019379d17c38f7390dee1f0b06c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【物理·迎新】新老生交流会预告 http://mp.weixin.qq.com/s?__biz=MzIwNDEzMDI5OA==&mid=2247503730&idx=1&sn=12d5f74f4a4af56424bd498a64af96c3&chksm=96c65de7a1b1d4f18fa9b2db69caa4d6d4bc9658733d9f1794858f6c5ba5fe957f7d935c4797#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【物理·活动】物理学院辩论队招新啦！ http://mp.weixin.qq.com/s?__biz=MzIwNDEzMDI5OA==&mid=2247503730&idx=2&sn=4d51a516ef981273ef425baad4c74a77&chksm=96c65de7a1b1d4f12869ca9fb7e5f331f4567417f453d14f96c904530e7f2d5081d2e3c0dc8e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【物理·活动】2023年迎新晚会节目征集&主持人招募 http://mp.weixin.qq.com/s?__biz=MzIwNDEzMDI5OA==&mid=2247503707&idx=1&sn=fe7f00e95d94540a0a8ce3509e116d16&chksm=96c65dcea1b1d4d844f7357a99c847a99736cc1e908d461f1dc47d3643c36d7338469254e285#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【物理·文艺】艺境·佳音|夏日专属歌单 http://mp.weixin.qq.com/s?__biz=MzIwNDEzMDI5OA==&mid=2247503706&idx=1&sn=451ca77b6b92875356ce0405fe277777&chksm=96c65dcfa1b1d4d94d0cf358564d0f3db030305b67b6619c438a91e1d0f93e9edae677d75bf9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大心理人 MjM5NjQ4ODc1MA==
sleep 520
<Response [200]>
从心启航丨心理与认知科学学院2023级研究生新生教育系列活动成功举办 http://mp.weixin.qq.com/s?__biz=MjM5NjQ4ODc1MA==&mid=2650520711&idx=1&sn=2d082787c176e1b2f3aef0ac04e695e3&chksm=bee76fc68990e6d0d211aa8e9b3281b04a20211d5c11aa438622b325d8afc3e7665d7e2a15b0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
温心驿站丨国家网络安全宣传周来了！这些知识你学会了吗？ http://mp.weixin.qq.com/s?__biz=MjM5NjQ4ODc1MA==&mid=2650520691&idx=1&sn=1b0d3fd257dc142a6fa0f0b258321bfe&chksm=bee76f328990e62484c0d8762e0c3811aacf4d0f97204af8f8886983353b1db911c8d8627828#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
心理为你丨实验报告指导讲座预告 http://mp.weixin.qq.com/s?__biz=MjM5NjQ4ODc1MA==&mid=2650520691&idx=2&sn=0e867ca05c61eed884f1b732b3d77d0d&chksm=bee76f328990e624e8f484c175583b24016346e0dc4413f1aa6a0097eeeb0626ff11accd9a1e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
从心启航｜2023级本科新生赴北大红楼、北大二院旧址参观学习 http://mp.weixin.qq.com/s?__biz=MjM5NjQ4ODc1MA==&mid=2650520679&idx=1&sn=384fbc1b832805ace040f7d8a2fbff7e&chksm=bee76f268990e6304edaeda356e86a5c3193c40d904dd9c1e1aaf212acfce79af16fcc5b03c5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
温心驿站 | 心院专属表情包第二弹上线啦！ http://mp.weixin.qq.com/s?__biz=MjM5NjQ4ODc1MA==&mid=2650520678&idx=1&sn=a23d904465e40c77d643f0821a1abefe&chksm=bee76f278990e6317f33d0150267c3430e5cecd0d26070b7637906366490e56471c2f3a46ad8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
温心驿站丨北大心理人祝全体老师教师节快乐！ http://mp.weixin.qq.com/s?__biz=MjM5NjQ4ODc1MA==&mid=2650520643&idx=1&sn=a59fda7a4f4e6e0a7ed5a3853f1e7e2e&chksm=bee76f028990e6141d560bf14b8574cf1692f218836005535761fe4b52d336ab2b22f0c0d15f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU信科职业发展中心 MzI3NTQ2MjM5NA==
sleep 512
<Response [200]>
报名 | 第六期“知行计划”地方党政机关暑期见习实践（第二批）报名开启！ http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485934&idx=1&sn=bd5402bf2ab5aff69697fcbf0b7ab9bd&chksm=eb05287bdc72a16d2201b77a995a7d34a1d430f96e1ca27d496f5f37bb5a88b93a9311ab793f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动 | 第二届Touch•CIB数字兴业科技挑战赛高燃来袭！ http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485934&idx=2&sn=79f0d21c0dc0bf73cb51b2e6952b7bc1&chksm=eb05287bdc72a16d5449b22effabe2f5d6508992b6d61a310d75fe76658a210eeb0b39f5409d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动 | 珠梦未来，海纳英才——珠海2023年全球优秀青年人才暑期实践计划正式启动！ http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485934&idx=3&sn=a47dbf3457eabac442477eed068e22fc&chksm=eb05287bdc72a16dd8946cfe4144b93ffee61afcc9564be3ad026c031d62a807c24b66fbb2a9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中芯国际夏季校园招聘全球启航 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485934&idx=4&sn=034d8820c203cec96e95b05e5dcee265&chksm=eb05287bdc72a16d490ca14051262c83c1e15a4864609ff02ab0333a6f5a45e0eff276626a03#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 南京银行2024届校园招聘提前批正式启动！ http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485934&idx=5&sn=13b50d2d1843b3336afcb58b72d7d409&chksm=eb05287bdc72a16db8a7f0dc8cbdc8eb80eb18c12c63ed7a50690509cba60904b94e6db90aba#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 火羽科技2024届校园招聘 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485934&idx=6&sn=315aa74f7fbff21893833274e248ca7a&chksm=eb05287bdc72a16db8fed0988158820254de6828d0703ad819f7128d631d41a3e4ce1a53ec21#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 来辽回辽创新创业大会 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485934&idx=7&sn=55d3ff3055b943998b5c68f08429544a&chksm=eb05287bdc72a16df46e5d03e8b0ee82fbd17f1db124acc523c5235aa253818f97a2ec31a2d9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 浙江广播电视集团2023年度招聘 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485934&idx=8&sn=d6fae86c6aa933586bd02fbd0307fd86&chksm=eb05287bdc72a16dedba7bc484e4f883e556694d7ef58d122bb99f770ed335b42e75e1e626ee#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动 | 2023可信数据库发展大会（TDBC） http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485827&idx=1&sn=58dd006f8fb9b3fdf5b422db9cd497ac&chksm=eb052816dc72a1008819246cf891407c97bed17505197e473263ea37f9387acd70b8ec73e150#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 小米集团2024届未来星技术沙龙—北京场报名启动 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485827&idx=2&sn=0cf12b8192e2bd546dafd5772f46859b&chksm=eb052816dc72a1002996eefe2e28742499a12372cd391bfd2a245e059c0c16f1129da4b3fd3f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 2023年江苏省扬州市邗江区优秀青年人才选聘工作简章 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485827&idx=3&sn=1828dd6e886231dfdefb3877d288414f&chksm=eb052816dc72a100f6732013e4511dee8a48d21e4fb46126a28ca7a8f01f9d348b9e1d5c5419#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 中国移动2023“梦想+”实习生计划邀你加入！ http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485827&idx=4&sn=bbd179c893ac20154e2ed3929181b6e8&chksm=eb052816dc72a1008b004151f7f816fa604f3298444a56b7cd8f4b6515eb06e8a02f1e3b94c1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 中国建设银行北京市分行2023年度暑期实习生招聘 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485827&idx=5&sn=47a9cd6f768bf7abb05bd95962cdc733&chksm=eb052816dc72a100fec729ad14f1cea065136282d8d3216129f3fe5bce9ec3fed318bec4fdb6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 中国外汇交易中心2023暑期实习生招募 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485827&idx=6&sn=5da319b267f0f26aabb5241187283015&chksm=eb052816dc72a100c10502a3b11f66a4e5196269431e7505105a1e4e16b82c4923c52146dc84#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习｜上汽通用2024届暑期实习生招募开启 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485827&idx=7&sn=97429514949f5fbde8758042dfaa01ce&chksm=eb052816dc72a10078674c97bacdc94f46356ecd38048ae786cee414719064bc6f2b776c2a34#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 星耀盛夏——工银科技2023年星令营暑期实习招募 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485827&idx=8&sn=eeb1a02920117b83fef373d98aa2b2cf&chksm=eb052816dc72a100279b5b92f68433fe4d98aa1a1e866502f03ec00c1823225ccbe0ed73bd2b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
公告 | 2024年青岛选调引才宣讲会报名公告 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485776&idx=1&sn=1b784e91bbed614a777cc7721fd092a0&chksm=eb0528c5dc72a1d37839cdbcaf63f8430452229bb77c97c1f5750ff3880bd363bbc52895eac2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 国家邮政局发展研究中心下属北京国邮科讯科技发展有限公司2023年度第二批公开招聘应届毕业生公告 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485776&idx=2&sn=1212ad2daef72c993f6c741d5708afdb&chksm=eb0528c5dc72a1d30f7342be7dcd94e7d2b119a31a7e7c96706109ab0d230a500b0ac500913a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 悦有你 期不凡——东证期货2023暑期校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485776&idx=3&sn=f52ce0cee534c2fa8fd0bce5fff4f03c&chksm=eb0528c5dc72a1d3405fc3dd8d1ad7d8e09bd1e8fa2c522d3b5e0d4205f0159577e93e90edb4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 中国移动信息技术中心2023年实习生招聘重磅来袭！ http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485776&idx=4&sn=4eed322a3d02b54adf4b5f46a05bac8d&chksm=eb0528c5dc72a1d37eedcb77dcca85c03a5db701b40e0b494d52742e21ef208371d19604390a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 中汽智库实习招聘 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485776&idx=5&sn=bc79cbac8c1b1faff6e079fdbbe864ed&chksm=eb0528c5dc72a1d3a4ae92707e4cb129c4a02230355fff586762d2a8982498999fd8295516a7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 中邮理财2024届暑期实习生招聘 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485776&idx=6&sn=63539cda20ce7d22ea3070f25906ef61&chksm=eb0528c5dc72a1d3c59e9a2b6be3174fe54854c81d43fc8b509faec19a0838e1057ad8c1b577#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 中国移动四川公司2023梦想+实习生计划正式启动啦！ http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485776&idx=7&sn=529743b28c1deb95e4bd1d602e09d3b8&chksm=eb0528c5dc72a1d32acfe4e7f28a09fc9f36e699bb7e79caea9b833f1c3fc50aa3cbfe177c5c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 五矿期货2023暑期实习生招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485776&idx=8&sn=3cdbcf74bd202aa045d0fe59971e153c&chksm=eb0528c5dc72a1d3d90a4f9ef3c3d24cc48fdea60e92330297016a5b37e19773e812c495ee0e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
科研与技术服务行业实习信息汇总 | 格灵深瞳、雅诗兰黛集团等 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485664&idx=1&sn=59c6c5f21f3a5f7e10051b213a164a85&chksm=eb052975dc72a0638fb4b7ce493b40b21ee75b0b7fd4cdaa8fc81b52f9df98ffbfbcb17a8419#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 小米集团2024届实习生招聘 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485664&idx=2&sn=eafc31c21327dfcc24937cd93fe4e2b0&chksm=eb052975dc72a063ae74fdbdf612339c12936b9fc9417a1e6394a44fa1e0a5c50c085975a698#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动｜看见未来 2023京东方（BOE）校园创新挑战赛正式启动！ http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485664&idx=3&sn=7ea517409e169ad002ee0f78e8987ec8&chksm=eb052975dc72a06334d0aa983eb8ae0ba1c8d4f848f92400664076e7d99a0fe160529504af14#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 华为面向全球招募天才少年 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485664&idx=4&sn=7ec6be987a34d542a1b5b17dd75944d1&chksm=eb052975dc72a06346c19297ffcd579f66191fe9ee3cdf267fd4d7c6702c958194e70d79198d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘｜海尔智家2024未来合伙人校园招聘提前批正式启动 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485664&idx=5&sn=4395ea9df1b54b50c0b3f8b993607b3e&chksm=eb052975dc72a063b8d980eda372b8efd69bfdd4e5eab8e08ec172f35e7b12d20c08ad6b09f6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 三一集团2024届校招提前批正式启动 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485664&idx=6&sn=7c090db69c78a187e3c2499239d5b37b&chksm=eb052975dc72a06308b8448ab3f662595550000d4e10a217b543e61f00940d36b9f048995cc3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 恒越基金2023年校园招聘 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485664&idx=7&sn=5aecdf7fc133436bd33c1886c734f09d&chksm=eb052975dc72a0630fd1dff27a244b40b337ef85ba16e8344fb8c857bd61da22aba30c5440dc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 量化“蒙”新 随时随“递” 蒙玺投资2023年全年实习生计划 http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485664&idx=8&sn=b4f0aca79143f6aa8c60ccdaac4a3eb0&chksm=eb052975dc72a0638e56d1c6f44b0b4294f79dd105a631ac049a1686a1446b6c7b35507fffcc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
E往职前 | 信科就业招聘实习资讯汇（0523） http://mp.weixin.qq.com/s?__biz=MzI3NTQ2MjM5NA==&mid=2247485516&idx=1&sn=7dfd465067a954c34e8eec37e5fac3d7&chksm=eb0529d9dc72a0cf6bc6d1c7f4ab8f7ca36973d8eadee04ca91493e369d0e932f05a44644155#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
光华CDC MzA4MDM0NDcwMg==
sleep 598
<Response [200]>
看这里！北大光华学生的职业发展信息库 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625445&idx=1&sn=84b17d82632590eaaafb6d2df262ce2a&chksm=87ac56b4b0dbdfa229f55fc79da8af11a3b4a225a2d065b5aa5e5d1f435500aab8436a0d1231#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
Last update on the English official website. http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625445&idx=2&sn=a8543ae449af91b5280fd1c00d23b35e&chksm=87ac56b4b0dbdfa2573979577e9855bde11d8fa393ead02a38b0bc83659656edbe5c2af70664#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 工银瑞信2024年度校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625445&idx=3&sn=505f2e86bdb4c001f6f386183254f1b6&chksm=87ac56b4b0dbdfa2c0fb5ec404c6cc0f537a5097ea5b461c4fea83dbde1df77b448f23b0e92c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中银证券2024年校园招聘火热进行中 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625445&idx=4&sn=e597787a1fac33000b026f567aae72c9&chksm=87ac56b4b0dbdfa2e32b50fa13b0bb9ca650a950a956a2584f4030387a93c4ab68bdb11807a2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 强生2024校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625445&idx=5&sn=ade66745653b395d9706181b0aec3ad1&chksm=87ac56b4b0dbdfa2fdc47869913e203d682986bbd0b153bcd0d10d919d2b20ea246c4e3a2e54#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 2024年秋季校园招聘正式开启 | 高鹄招聘 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625445&idx=6&sn=cda010bd93ac2dcc4947ee6630cbf4b4&chksm=87ac56b4b0dbdfa2e4ffac5c9acea0ce4adc95775cef83e5de267fb57f0b8a5f8097e3c213d3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 雅砻江水电2024届校园招聘启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625445&idx=7&sn=7e1dd0f7049891b0d37ef434d3c17041&chksm=87ac56b4b0dbdfa21bd97d40fa240acad34c56938c024e4b28ddb2a650232d2951ca35d9de99#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘｜阳光资产管理股份有限公司招聘境外投资部/策略研究岗 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625445&idx=8&sn=cc1aa2910113cee27cf035e51cf6afd9&chksm=87ac56b4b0dbdfa2989d8c4eb20fbdcc15341068c73a72d0575975ba97df94b265b160532916#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 桥水（中国）2024年校园实习生招募启事 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625438&idx=1&sn=1cc3a65ca3584544cd0b13a22e41002d&chksm=87ac568fb0dbdf99ef37494d9a5113005c6eaf43320679f18a2ce09ae363070e96f09e53fb7f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动 | Barclays Insights into Investment Banking! http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625438&idx=2&sn=364304c3e3e159a23f6371c424a81d18&chksm=87ac568fb0dbdf990daa5931d2e475111be67dab2626bdd8ffa7c83f7e0c7f7db031c92929ff#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动 | MINGHONG Talks|和明汯团队分享你有趣的研究和实践！ http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625438&idx=3&sn=0e52b5629adfe95ca0c9ba40cf863834&chksm=87ac568fb0dbdf99a61cdef1f9b5f8f01d8d7272bad2c1f502293f11db2b13239dc5b0af2ae1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘及宣讲 | 易方达基金2024校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625438&idx=4&sn=98b4ea01e33b38e09bb5d3cc0d2a640a&chksm=87ac568fb0dbdf9915742a5f2af8f10588c468e00924c289e576472b00b0c1e7bb6c380472b0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 国金证券研究所2024届秋季校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625438&idx=5&sn=2b9d3b109f2daeb25088853b07cb9bdd&chksm=87ac568fb0dbdf99944ff54191d4e4a2a1db1ae8130322ae0623bb0b6e6ab2e80a92e4419c9c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 农墨重彩 青春奋发 ｜ 中国农业发展银行2024年度校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625438&idx=6&sn=6d5aef7006c635c32197f139e9db59b9&chksm=87ac568fb0dbdf9962d19edbfa505e2175f14b5bea8a88a1581e564c2f977674a95cbcc5f841#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 财通资管2024届秋季校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625438&idx=7&sn=b2539888cc5f2ff5cf335bd7c4b047fa&chksm=87ac568fb0dbdf995ec6c90c51310ecd21be19a60fc941e581d8c0bda4a1dc55f047da4fddaa#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中国工商银行博士后科研工作站2024年度招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625438&idx=8&sn=df185b3ad31ec912e810aaac76dd6b3b&chksm=87ac568fb0dbdf99bfe4a8d4a16d9e701ff3924283eb045d2fb59203697524d4ad7101fe56f5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
关于职业发展，来听师兄师姐说！ http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625422&idx=1&sn=98c55d1ee7ee5b1c7a870bf957131939&chksm=87ac569fb0dbdf891072ea72fe983f92d4a818d5e68945d0f8ef26308fc7aa440c7f2d826d94#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 麦肯锡中国2024校园招聘火热进行中 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625422&idx=2&sn=5924781f82b5c149d0a5304c57f1c2b8&chksm=87ac569fb0dbdf8954d8e5ffb9f14620d597e645cc7609e76f4638921b549104b4c0146824e1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 网易游戏（互娱）2024校园招聘启动！ http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625422&idx=3&sn=a3bc22bc6783787cf7b8e5be60e5e92a&chksm=87ac569fb0dbdf891197ff62b58d2dc96f9604be39905460dc2baf2163bb66dcd1ceaaca8377#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 腾讯2024校园招聘城市双选会&交流会安排 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625422&idx=4&sn=e4e8837cc77d78b8edf85df8d5627e17&chksm=87ac569fb0dbdf894b200553faa399af42a6a9bcdb8805960b632bf2fe2646158d6ed49a5314#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中国建设银行2024年度校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625422&idx=5&sn=f777f47271d85afe0956f802371a4a71&chksm=87ac569fb0dbdf89b7d0b2bb15bc33ae1dd02bb2e9e9a5d9e823a6bdad538b0f54b2edfd1017#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 中国银行2024年全球校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625422&idx=6&sn=9c2f59e40000f2201354e92370c5b881&chksm=87ac569fb0dbdf89be6e02cccd5f75ddaddd1d34afc3b3e8269acf3a90bcd74736b4a271bb2e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 梅赛德斯-奔驰实习生项目X-SEED计划首次实地测评大揭秘！ http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625422&idx=7&sn=4d6b8fddc7102ea5f1dab13ccca1d1b7&chksm=87ac569fb0dbdf8917eedb411bb8016e80be9eb7926e908069815d07b16843af08ef9df633c7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
苍茫万景，而无苍劲如人者丨北大光华院长刘俏2023年开学典礼致辞 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625134&idx=1&sn=7e787ec097f371805a3538ad74665167&chksm=87ac577fb0dbde695cd545db1a03348808e5c32b1a458e0a6fedcb25186bc8e6852809ad7839#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘｜锐思锐拓2024年秋季校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625134&idx=2&sn=3f3074079cf1f5dacd3ed25f5a62eb3d&chksm=87ac577fb0dbde69d99434169532737e1390ea5adb06958e250d5f87b54c4f98417affbe9744#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘｜德意志银行最新全职及实习机会速递 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625134&idx=3&sn=8faad6918b542f727193aa08128d74a3&chksm=87ac577fb0dbde69905b04b5355783895639a191cc8ddd9061ba0ff3508b32baf2effc5b86be#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘｜华为财经2024届应届生全球招聘全面启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625134&idx=4&sn=fa63949eb64de6aa06117e94aaf1e97d&chksm=87ac577fb0dbde695e42782c77719706e554e802441b6f7f9dddc3871bac45fad87095f02ce8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘｜北京 | 江苏银行北京分行2024届校园招聘报名进行中 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625134&idx=5&sn=4a78812a3d3399918f33342155c4e172&chksm=87ac577fb0dbde697a631a01fbd75121f2e95a2571a83b26c974d23d893a0d971fea836ef965#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘｜聚宽投资2024校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625134&idx=6&sn=9ab782c32a30771da67555f1f9d7b4ba&chksm=87ac577fb0dbde69ac3b061cb9bcef06df6a6b579b3740496946925f2bc485233eb739c0dd14#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘｜腾讯战略发展部2024校园招聘全面启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625134&idx=7&sn=d9a1528a27f8ceda3ebad9b331a4fe05&chksm=87ac577fb0dbde691428e39d29aaf0013d6871295e16c4d49356d63c9baee7b426890d8c121d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘｜浓情不负青衿志 | 中国农业银行2024年度校园招聘盛大开启 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625134&idx=8&sn=aa07d29910f83e51e9c407166775c4ca&chksm=87ac577fb0dbde6973ca6d71162674a851f5ca414a5c6c9dbeccbb09fc63f208f98c78f896b1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 花旗银行2024暑期实习招聘启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625123&idx=1&sn=2d5378cca2a8030c10b4cd66ac2ca54f&chksm=87ac5772b0dbde64841947324a3f4b491317057a6a3d55a71fdbc561d34e531c101db2a5dbad#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 航天科技集团2024届校园招聘开启｜发展航天事业 建设航天强国 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625123&idx=2&sn=02a5622580502f4ca94c38cc3aacab44&chksm=87ac5772b0dbde640d6077294c363e5750e47c79815e97fc9c6d0766a659c0079faa81a8e442#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中电熊猫2024届校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625123&idx=3&sn=88f9020ed36a5eb401152f562bc2b3ee&chksm=87ac5772b0dbde649e426ecd82dc81d1c2c81a9bb5ee828ae198d0cba5ab4f1c659f8db5c8fc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 航空工业制动2024届秋季校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625123&idx=4&sn=0b89c502fdae1b66af66dd0dbe305389&chksm=87ac5772b0dbde647c0328f2109e84fe71338ce08de432f79eddf3f330312d8607f0796c2d0b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中国航空无线电电子研究所2024届校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625123&idx=5&sn=bf958f19aa5ebd958111df8a156f6f8b&chksm=87ac5772b0dbde64e1f15413870c70f7e6aa4c3250fc4cb8daab167cd09ce8a12d1ce7252f60#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 航空工业特种所2024届秋季招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625123&idx=6&sn=ad625d5b265718f0a4d66a7627623dc5&chksm=87ac5772b0dbde64d03fb380abdfc59f545fbd762de7398ca3e7d9a18e02c9cfde53570a75a8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 航空工业自控所2024校园招聘公告 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625123&idx=7&sn=4d387f61573912847ce33ff218c27e5f&chksm=87ac5772b0dbde643e280a2f71aadd6dc777257a3aa3d77a1b4a14d7ca94a74e19ad73578ac1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 航空工业哈飞2024届招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4MDM0NDcwMg==&mid=2650625123&idx=8&sn=458bd794e5008c7974e1b9b0ac5f1e97&chksm=87ac5772b0dbde64eb820514db896592bef6e8e4a0039c6e1f170a06b12973ee7af556c57c1f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
走进光华 MzkwMDIzNTgxMg==
sleep 80
<Response [200]>
光华人物志｜内蒙古-吴超：在光华，重构自我，找到自我 http://mp.weixin.qq.com/s?__biz=MzkwMDIzNTgxMg==&mid=2247487019&idx=1&sn=a3397b459c79d128596ed52ec8aed0f2&chksm=c0465960f731d076d4c18e15f733c4d9d88344de419d563f9d408202fb418c2c2fadb0c5f890#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
苍茫万景，而无苍劲如人者丨北大光华院长刘俏2023年开学典礼致辞 http://mp.weixin.qq.com/s?__biz=MzkwMDIzNTgxMg==&mid=2247487000&idx=1&sn=0a480d8830c68a7a9eed720b2308e31b&chksm=c0465953f731d0458ee2d0ddecfabff11969476969bfad223227f1c13898d035a88756cb4658#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
亲爱的同学们，2023年秋季开学快乐！ http://mp.weixin.qq.com/s?__biz=MzkwMDIzNTgxMg==&mid=2247487000&idx=2&sn=a3036cc3ee0bc60067b70b3cc1466442&chksm=c0465953f731d0451a9b3e3a3466fc9d01dcc1bd8c808abd429eb28aeb0ef1aa403e96e0f3c0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
光华人物志｜黄静远：潜心求索真知，踏实充盈自我 http://mp.weixin.qq.com/s?__biz=MzkwMDIzNTgxMg==&mid=2247486991&idx=1&sn=f5bc9df189f0a60cdc95ba077ccfb0c9&chksm=c0465944f731d0525490dcb6592ede99969af302d1aada830e3807aba6237ee2fcf6d27e22f3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023暑期课堂 | 跨越山海，我们相逢在光华 http://mp.weixin.qq.com/s?__biz=MzkwMDIzNTgxMg==&mid=2247486972&idx=1&sn=07679e9054f2acff0c0243e9dbfd261d&chksm=c0465ab7f731d3a15b8290a75aa8acfd03ffa3072b706eb83118926cb4d2c0b410358046a00b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
钥匙就在阳光里丨北大光华院长刘俏2023年毕业致辞 http://mp.weixin.qq.com/s?__biz=MzkwMDIzNTgxMg==&mid=2247486967&idx=1&sn=2a19c91876aec86ccda313d2d6a42090&chksm=c0465abcf731d3aaa9aa50ae8d862265de0cbfc02ecef7addfe1b3058e73e20f7d63cc2f4b84#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大史学人 MzkyODMwMzEwMw==
sleep 580
<Response [200]>
系研会招新｜历久弥“新”，“研”途似锦 http://mp.weixin.qq.com/s?__biz=MzkyODMwMzEwMw==&mid=2247486887&idx=1&sn=78e84bce2df97f6591bbd31dbcfe7ca3&chksm=c21b9f37f56c16213def8264d192e1e2531d5e3fa842afb1e2f8ed45ed90de107dc57aca86b5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学历史学系举办2023年毕业典礼 http://mp.weixin.qq.com/s?__biz=MzkyODMwMzEwMw==&mid=2247486867&idx=1&sn=e22c92da0dc54e59925aaa76b6175859&chksm=c21b9f03f56c161556c581ba5a328ce6a2cb98c7476b74f3de8cf2cb6839302122145804f468#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
帮推｜复旦大学历史学系第二届“博思”史学论坛 http://mp.weixin.qq.com/s?__biz=MzkyODMwMzEwMw==&mid=2247486864&idx=1&sn=14c0c49eff2eba33146cc165e2a2fd51&chksm=c21b9f00f56c16168da1e06c99857dcd64ccf8a27393b54f1911543f897ea94160921e6beb05#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
帮推｜新史料与新史学——武汉大学第十届珞珈史学博士论坛会议通知 http://mp.weixin.qq.com/s?__biz=MzkyODMwMzEwMw==&mid=2247486864&idx=2&sn=aa774a2f2f82b566b3a06198e398d8fe&chksm=c21b9f00f56c1616c42c1f87ab59e956bbcf35e7ff184dc598afc7bc288a79ab46311c6f1285#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
燕啾声｜历史学系师生近期学术成果汇总（2023年3-5月） http://mp.weixin.qq.com/s?__biz=MzkyODMwMzEwMw==&mid=2247486851&idx=1&sn=08a8f377c04e03857159967eca8c06dd&chksm=c21b9f13f56c160542d3ef4d1912f20259a3c4e4a28c323b4bc5a86d8dea504b1b7ce0bbe93b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
使劲打！｜第二届“人使劲杯”羽毛球赛精彩回顾 http://mp.weixin.qq.com/s?__biz=MzkyODMwMzEwMw==&mid=2247486848&idx=1&sn=a48c4cd9bf7640fe3c049bca00202f6d&chksm=c21b9f10f56c16069c932c731b153acc59df40d6234cb8dd42a7d2a2ca47b5217f866dcdb432#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学教育学院团研 Mzg3MzE5MzQzNA==
sleep 190
<Response [200]>
一见倾“新”，情系中秋｜2023教育学院迎新暨中秋晚会静候君来 http://mp.weixin.qq.com/s?__biz=Mzg3MzE5MzQzNA==&mid=2247490376&idx=1&sn=1745466b980002583df794cae8503e8e&chksm=cee291fdf99518eb6fe94a8f781818f01f8d6d9d2dff7e952c8046d9237d1b8319da501bf654#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教师节颂丨致敬天底下最光辉的职业 http://mp.weixin.qq.com/s?__biz=Mzg3MzE5MzQzNA==&mid=2247490331&idx=1&sn=0557c26a709f55d7c267e126c0e9bad8&chksm=cee291aef99518b8b785977fe095d8e587ab73e22567a0a292115c2e84fd15075c9eee5506e5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
岁月留声 | 2023年教育学院毕业歌会圆满落幕 http://mp.weixin.qq.com/s?__biz=Mzg3MzE5MzQzNA==&mid=2247490322&idx=1&sn=ab3afc0ff64b88a2c2c68af63ddf44a3&chksm=cee291a7f99518b1c90cf147ae0891ac0546055cf4d73034a26cd855fd1e887c80ac04e1a693#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
端午 | “情浓万柳，粽叶飘香”端午活动回顾 http://mp.weixin.qq.com/s?__biz=Mzg3MzE5MzQzNA==&mid=2247490292&idx=1&sn=5297e5666e900aa5bd4e59ea62bc24cd&chksm=cee29041f9951957b3aac286f0181b025b4d12d16b22c5942a9f8f7987394db785d21f05e3cb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
参访回顾 | AI未来已来，教育的变与不变——教育学院师生前往科大讯飞北京总部进行参观交流活动 http://mp.weixin.qq.com/s?__biz=Mzg3MzE5MzQzNA==&mid=2247490236&idx=1&sn=880d93c2e3aa654fa20d36008389f00f&chksm=cee29009f995191f9f97c92da2b9f1bba9d5b4c2f59f7aa6837579becb1bc0180ef72421e99f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大脑科学 MzAwNTEzNzcwNg==
sleep 449
<Response [200]>
学术笔记 | Lixing Sun: The Liars of Nature and the Nature of Liars http://mp.weixin.qq.com/s?__biz=MzAwNTEzNzcwNg==&mid=2651115588&idx=1&sn=68ff7f327f3eb568713ba769a7d06094&chksm=80d14401b7a6cd177b3de5cf8779d240a3f47febcde13b6b7ba165c6d768c309637b430350cb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻快报 | 陆林、李毓龙、方方教授获评“北京大学优秀研究生指导教师” http://mp.weixin.qq.com/s?__biz=MzAwNTEzNzcwNg==&mid=2651115566&idx=1&sn=29c7e4abb9057feae3c68440bec5ee81&chksm=80d1446bb7a6cd7df2c7f29845e349bfba58c531e67e908daaed91547a05f4ca11e0dea76da8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告 | Lixing Sun: The Liars of Nature and the Nature of Liars http://mp.weixin.qq.com/s?__biz=MzAwNTEzNzcwNg==&mid=2651115501&idx=1&sn=a794b0c8e02f759f73ebebe60f1b65b5&chksm=80d15ba8b7a6d2befd0312a2e6c6a7becf684e2421e0b48b4baf0ed1b5a4249b9fad5474222b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻快报 | 陆林院士荣获“中国侨界杰出人物” http://mp.weixin.qq.com/s?__biz=MzAwNTEzNzcwNg==&mid=2651115492&idx=1&sn=a95e57c3d48ae2a3c5d15a74cc982b1d&chksm=80d15ba1b7a6d2b79a5af53f389afb2fea95f3a762b2f4167b2408d4c0d421d8ee792a2583fb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻快报 | 北大IDG麦戈文脑科学研究所获批多项国家自然科学基金项目 http://mp.weixin.qq.com/s?__biz=MzAwNTEzNzcwNg==&mid=2651115483&idx=1&sn=03967fdee49a58148dc731c50506198f&chksm=80d15b9eb7a6d288e14601689d72b75dc9bc5bbd603e88f34792e7f68432dbcf5b57a02f6f2a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学人文社会科学研究院 MzIzNDQ0MDUwNg==
sleep 585
<Response [200]>
预告｜文研七周年系列学术活动 http://mp.weixin.qq.com/s?__biz=MzIzNDQ0MDUwNg==&mid=2247537425&idx=1&sn=ec025bca1e34ecb57983f875318f93e9&chksm=e8f44144df83c852bdbc7ea967920cc53fe50a30f21f28ecd541ae4730a0ef9caede3bc45c39#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
书事｜罗丰：曲折的经典之路 http://mp.weixin.qq.com/s?__biz=MzIzNDQ0MDUwNg==&mid=2247537363&idx=1&sn=2ec710fa866704a77d14c49367ce200a&chksm=e8f44086df83c990ac484b6d248f857f1b9fc11d1f19c2889886b1f31bf45248e803b739d84e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻｜郝平书记会见文研院新老班子 http://mp.weixin.qq.com/s?__biz=MzIzNDQ0MDUwNg==&mid=2247537363&idx=2&sn=fc0f58927eda7a162c1838db58b1086a&chksm=e8f44086df83c99063d86e7cf6d9ae0fd5f589bda12610b32a495cc1de4ea17822362a48c33c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
文研院院长杨立华教授在北京大学2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzIzNDQ0MDUwNg==&mid=2247537355&idx=1&sn=23d45c0675e8cdfa73b897710860f209&chksm=e8f4409edf83c98855fdb2a105c3d435fe6157758bbd462708018d1f25548b1c356c01d03cb1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告｜【文研讲座302】Vincent Tournier：古印度案达罗地区的佛教施设与供养：从公元前二世纪到公元七世纪 http://mp.weixin.qq.com/s?__biz=MzIzNDQ0MDUwNg==&mid=2247537317&idx=1&sn=7a5e6cd707d2ffe6c159f5be9824fcd1&chksm=e8f440f0df83c9e6d747737aaa654b20b46cc64464b37dcead4edcb3b51099bd66b8c89c1e84#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
纪要｜【文研讲座300】余辉：图像何以证史——古画鉴定与史学考据 http://mp.weixin.qq.com/s?__biz=MzIzNDQ0MDUwNg==&mid=2247537303&idx=1&sn=e10742c934f84563b26b3d7abeb7a0e2&chksm=e8f440c2df83c9d4ad2c3e1d27d40306ebd97f05db23b8d198c47b25f460646e1917e4dde906#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京国际数学研究中心BICMR MzI1ODQ2MTkwOQ==
sleep 571
<Response [200]>
千万里归来，学长们带了哪些话 | 北大数学校友学生交流会纪实（下篇） http://mp.weixin.qq.com/s?__biz=MzI1ODQ2MTkwOQ==&mid=2247503243&idx=1&sn=841657cf3052faf794c61959391720ab&chksm=ea055431dd72dd277eda7fb31f38367dd8994261f38856005e05ff755fec1206bd1aa80db53a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
学术活动 | 量子计算秋季学校 http://mp.weixin.qq.com/s?__biz=MzI1ODQ2MTkwOQ==&mid=2247503242&idx=1&sn=8d089006d6e68bc71884ed255b6f6b1f&chksm=ea055430dd72dd263e45c5836fb96e14ec33f196834ae1825d946b46591719c991b11ca9f29d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
110周年庆 | 概率论与随机分析国际会议 http://mp.weixin.qq.com/s?__biz=MzI1ODQ2MTkwOQ==&mid=2247503241&idx=1&sn=a8b4d26680b646f5a1036d2cf8523859&chksm=ea055433dd72dd25487ddbbe0b1f34420d5e418c46428fc02093fffcda4e0cf21b16e84731a1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
《北京数学杂志（英文）》2023年在线出版文章速递（五） http://mp.weixin.qq.com/s?__biz=MzI1ODQ2MTkwOQ==&mid=2247503205&idx=1&sn=3239849681e84abaa8e9506df1ffbf24&chksm=ea0554dfdd72ddc948ae15c3cea4d86144bd35d304829823ae8377296e0dc5ce335e5235cd82#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
白露 | 概率论为什么也关心二维量子引力？ http://mp.weixin.qq.com/s?__biz=MzI1ODQ2MTkwOQ==&mid=2247503177&idx=1&sn=82c76d0668d431f8cb02c95f51d3afb0&chksm=ea0554f3dd72dde52e93e3779e697b4096f65ec46c02af76bf5aafae9cb3de19e5e899ccc2f5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学语言学实验室 Mzg3OTg2NTkxMw==
sleep 324
<Response [200]>
《光明日报》刊发陆尧、吴西愉老师文章《激发儿童语言的活力》 http://mp.weixin.qq.com/s?__biz=Mzg3OTg2NTkxMw==&mid=2247483784&idx=1&sn=26a1202a42b5bf08035a6e9e4d282823&chksm=cf7cb8def80b31c8ad060159aa3ee26ff8faf49cd3e9b6fb42c1958716bb82994010876c53f1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告 | 马国国与彝族口弦的故事 http://mp.weixin.qq.com/s?__biz=Mzg3OTg2NTkxMw==&mid=2247483777&idx=1&sn=fd3c504b1757f95999e4119b71eab5dc&chksm=cf7cb8d7f80b31c1c986b62cb6134241494341859ce2bb5ac42c31520dd17c2ccd0b1d9332e5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
《文汇报》：北大语言学实验室，在这里“看见”声音 http://mp.weixin.qq.com/s?__biz=Mzg3OTg2NTkxMw==&mid=2247483764&idx=1&sn=fbbcf011c7e51d8059503dfcfeb0a8ce&chksm=cf7cb822f80b3134291816b8e31e28eb9cf63c289f1612c15004270f0ca7529b1813465e53dd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告 | 李云兵：苗瑶语实证研究问题 http://mp.weixin.qq.com/s?__biz=Mzg3OTg2NTkxMw==&mid=2247483750&idx=1&sn=cec31d940ff508f603b1859344cf84c1&chksm=cf7cb830f80b3126709589737094386330e2494383c6841a6b879f95e87ab4b148d13f4eaf20#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回顾 | 横断山脉三江流域中华民族语言大融合田野调查 http://mp.weixin.qq.com/s?__biz=Mzg3OTg2NTkxMw==&mid=2247483734&idx=1&sn=449fc675b60ce9c01edb45ad7ece3ca2&chksm=cf7cb800f80b311617b8876c3c88e98668d0688c77a034e8c3dfd39be8c2dd272c88a5c83b81#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学文学讲习所 Mzg3ODU1OTE2MQ==
sleep 497
<Response [200]>
回 顾｜“AI是什么？网文怎么办？——人工智能时代的语言算法和网文写作”高峰论坛 http://mp.weixin.qq.com/s?__biz=Mzg3ODU1OTE2MQ==&mid=2247486222&idx=1&sn=cd6954711373f31981b3912502e16bc2&chksm=cf10a1d8f86728ce9a730c1318266da4b75e2bec4c72d63c9756b71baad61317dc86544e3a94#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新 闻｜网络作家进校园：狐尾的笔北大分享会 http://mp.weixin.qq.com/s?__biz=Mzg3ODU1OTE2MQ==&mid=2247486109&idx=1&sn=2cfe9f44e8787f445845f4973ebea371&chksm=cf10a04bf867295d3c63bc94f8f9744b2423b9486fbf48992eaab0638fcc57a70ee92c1fe2bc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回 顾｜北京大学全国网络文学高级研修班举行第一日线下研讨活动 http://mp.weixin.qq.com/s?__biz=Mzg3ODU1OTE2MQ==&mid=2247486108&idx=1&sn=71bb5d55b076d7b3388177c57a4d6466&chksm=cf10a04af867295ca84d36bef267f292ecbd6bd4b2c635ffbc477b5636c5c05823eb52bd6dd0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回 顾｜“数码媒介环境的底层逻辑——新媒体文艺评论为什么要关注软件？”专题研讨会 http://mp.weixin.qq.com/s?__biz=Mzg3ODU1OTE2MQ==&mid=2247485945&idx=1&sn=4541d39645c3a7ec6a2094eb80bcc69d&chksm=cf10a32ff8672a397a6f8d286904046ea1b20e47269db37acf965808ca842e1844a29746ab11#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学全国网络文学高级研修班线下研讨活动安排 http://mp.weixin.qq.com/s?__biz=Mzg3ODU1OTE2MQ==&mid=2247485945&idx=2&sn=6746d0835adadfbeabd2fbfffb3df44f&chksm=cf10a32ff8672a3954523b5674115ebdc9cfba9fb159bf5166073f8af8095caa75e7fda9f776#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新 闻｜网络文学青春榜年榜发布暨起点读书“字在青年”高校网文创作大赛启动仪式在北京大学成功举办 http://mp.weixin.qq.com/s?__biz=Mzg3ODU1OTE2MQ==&mid=2247485872&idx=1&sn=51937e31054293e54593e0cd780c57ed&chksm=cf10a366f8672a70ca10f4eb57e2e0ce01db6d4c45b8bbee44dae96c75b03daa4b9eea68616e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
会议预告 | “王默人-周安仪世界华文文学系列研讨”启动仪式暨石一枫文学创作研讨会 http://mp.weixin.qq.com/s?__biz=Mzg3ODU1OTE2MQ==&mid=2247485872&idx=2&sn=ff4d27425de7d74a0451e187f9fd79ab&chksm=cf10a366f8672a706eb70c729fa715295fac21e995437b0a143a45a680c207ccdfbe1f5d797d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学前沿计算研究中心 MzU0MjU5NjQ3NA==
sleep 534
<Response [200]>
静5青年讲座 | Approximate Counting for Spin Systems... http://mp.weixin.qq.com/s?__biz=MzU0MjU5NjQ3NA==&mid=2247500931&idx=1&sn=76509415a33c68eeffca22ed3ac78746&chksm=fb1ac896cc6d4180c4bbc15189c8b738adb8773432205ed4ba86694e9b60f8de9812a22cc6e1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
静5青年讲座 | Foundations of Multimodal Embodied Agents http://mp.weixin.qq.com/s?__biz=MzU0MjU5NjQ3NA==&mid=2247500930&idx=1&sn=5e0a28585799aa5f73932a5c7a7e5df5&chksm=fb1ac897cc6d4181980ebe2fcdf04a6b6430bf1a108207f1086a09b1e2b3151971827ef5d39b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
静5前沿讲座 | Advances in Cryptography & Blockchain Applications系列报告 http://mp.weixin.qq.com/s?__biz=MzU0MjU5NjQ3NA==&mid=2247500895&idx=1&sn=988fbc29bdc57309152dfa06c7ee760f&chksm=fb1ac84acc6d415c8403115761cbbc0380164dacb5b292928f7ab58852641c0148281ce4927f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
静5青年讲座 | 量子计算软件优化方法 http://mp.weixin.qq.com/s?__biz=MzU0MjU5NjQ3NA==&mid=2247500895&idx=2&sn=885a4e9da37f3fa80157beb0383a6381&chksm=fb1ac84acc6d415c8a190109a51f3d3771f284fe8ad00a65fecdef323a1f4fb2dccbff71ba01#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
静5前沿讲座 | Data-driven Auction Design系列讲座三则 http://mp.weixin.qq.com/s?__biz=MzU0MjU5NjQ3NA==&mid=2247500873&idx=1&sn=1fbe34d9f4bc31bb8f2600bb7a6d4c45&chksm=fb1ac85ccc6d414ac3fe3c25b4b48811cd8749aaffbccd48f120edb712810529b5c6e2e5ba22#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
静5青年讲座回顾 | 徐海峰博士谈机器学习中的经济学 http://mp.weixin.qq.com/s?__biz=MzU0MjU5NjQ3NA==&mid=2247500860&idx=1&sn=98019992a8514faa68ab1f9c1e991e05&chksm=fb1ac829cc6d413fdf9d0e53b5c9ccb27c65be455b11940c8c10fe85992ddcda15f49a0fb046#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
大数据分析与应用国家工程实验室 MzkyMDE5NTM0NA==
sleep 480
<Response [200]>
会议预告丨“第二届数学促进经济社会发展论坛（2023）”分论坛——第二届国产通用型科学计算软件研究与发展研讨会诚邀您出席！ http://mp.weixin.qq.com/s?__biz=MzkyMDE5NTM0NA==&mid=2247491620&idx=1&sn=524c469eef28fbcc0b8fc7439834713a&chksm=c194385bf6e3b14dc3ed93f1e389e1912f0aa75bc934ec4f6d4447d3d9cdf03c75e9d3b6ef68#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
鎏金九月 盛会来袭丨历年数字生态指数发布回顾 http://mp.weixin.qq.com/s?__biz=MzkyMDE5NTM0NA==&mid=2247491616&idx=1&sn=092474d8f7a0e9b3a95348d32b081ca6&chksm=c194385ff6e3b149acbd020341e344d37fe5d1f93582744566cff0bf1bb9a1a070e581e539f1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
国家工程实验室科研团队在Nature子刊发表“新能源多时空尺度不确定性数据解析方法” http://mp.weixin.qq.com/s?__biz=MzkyMDE5NTM0NA==&mid=2247491607&idx=1&sn=ecc46ef18f86f2c6677826b3caed129e&chksm=c1943868f6e3b17ed4fa8c56c30c1d3beb21b3daaea53ae173b6bebffaf968ca3e5bfd800de8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
国家工程实验室Newsletter 2023年 8月 http://mp.weixin.qq.com/s?__biz=MzkyMDE5NTM0NA==&mid=2247491574&idx=1&sn=96370245c4d0b50565a769d560c7da06&chksm=c197c789f6e04e9f44cc35a8edec62cb61e74fe70e4e03da4934d3c4f1d86f2acf044c8fdcc1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
正式发布！北京大学重庆大数据研究院携5项科技创新成果亮相2023智博会 http://mp.weixin.qq.com/s?__biz=MzkyMDE5NTM0NA==&mid=2247491573&idx=1&sn=4cc89446898768ce1a75f7c874ae43c8&chksm=c197c78af6e04e9c77dc4c953d39b7429ccdfee53ca0118a6ed83e8797eea33ae082168d6bd3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学统计科学中心 Mzg3MTcyNzA1OQ==
sleep 305
<Response [200]>
北京大学统计科学中心9月14日报告 | 统计与数据科学系列 http://mp.weixin.qq.com/s?__biz=Mzg3MTcyNzA1OQ==&mid=2247487788&idx=1&sn=da0452045d841c3d3ddcb597fe23f10f&chksm=cefb7b90f98cf2864003b5229a363b432090c7aa084a45fc60a102a6682fad826d7cb50bbbdc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学统计科学中心科研秘书岗位招聘 http://mp.weixin.qq.com/s?__biz=Mzg3MTcyNzA1OQ==&mid=2247487781&idx=1&sn=af872d98e5e3c6ad7c4247f85e6853ff&chksm=cefb7b99f98cf28f25550ac482a1986b331675f0c0277649921ad55ef3c760eb24dcea8664db#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“Survey Data Integration”短课报名通知 http://mp.weixin.qq.com/s?__biz=Mzg3MTcyNzA1OQ==&mid=2247487779&idx=1&sn=51bff2df3f4011271e164b5b42f3e3e6&chksm=cefb7b9ff98cf289594f65d4555cadcae69408a92140ad617acaa8d45de97f02f5c2aaf55f76#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
时移世易 踵事增华——第四届光华时间序列论坛成功举办 http://mp.weixin.qq.com/s?__biz=Mzg3MTcyNzA1OQ==&mid=2247487772&idx=1&sn=9d5d6282537a1031707b4bb896c193bf&chksm=cefb7ba0f98cf2b678896ec3304828acf860d69591801a2afed036f22205d212692eb6572f17#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学统计科学中心8月16日报告 | 统计与数据科学系列 http://mp.weixin.qq.com/s?__biz=Mzg3MTcyNzA1OQ==&mid=2247487770&idx=1&sn=97058ea98321f0887b3f749434584159&chksm=cefb7ba6f98cf2b008db1cecfaf7e76ab53f632086b1d59aac72c057b1e8f2646a4a26c5eddb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学文化产业研究院 Mzg4NTE0MDUwNg==
sleep 83
<Response [200]>
【活动闭幕】毕城村的种花家：2023第五届花田STEAM课堂圆满结束 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492611&idx=1&sn=4db426b4769728121c1a6bb47bb90047&chksm=cfafd976f8d8506028621d913d50d99f5c0e993d9b64f0ab229a0cdc29d1b6b011690bc39760#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【燕南智库】王一川：建设永远为人民绽放的影视百花园 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492611&idx=2&sn=d5d4edee3da7e1e25383026ed1f80e69&chksm=cfafd976f8d85060eba9b14813454e1677b3b6bd2e70d604f5530a3d168358c2ebcd77c1dcb8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
民居文化 || 王曙光：探寻中国漆器文化的发展与传承之路 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492611&idx=3&sn=95110cac42409e6112d7b2b3ec0b4ca4&chksm=cfafd976f8d8506033146d532189bac32876828b035d0290a03badc435e7840d7ef551d490a8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
闭幕｜2023北京大学艺术学国际博士生学术论坛文化产业分论坛全回顾 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492599&idx=1&sn=32a05c60e7d21d5d74c2dfd38a8e1df9&chksm=cfafde82f8d85794d773be04be7ccc1bc4d8c185d2eba6e15dc5403ddee77e3386be8f692622#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023北京大学艺术学国际博士生学术论坛设计学分论坛全回顾 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492599&idx=2&sn=ce82c9730c4a2c1ca0bbb3392def19a1&chksm=cfafde82f8d857949d40733d373346682380f0b56f6e3aa29854e4d5c47418e0e24bde34dca5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大文产院工作简报2023年第8期 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492599&idx=3&sn=4864e913385c0468815ba5830fe556f5&chksm=cfafde82f8d8579456302f6a9f1684fa338de8095c4f31b8380d7222543b430b1fb63e1d5ec4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“‘京’彩文化”园区行：北大文产院师生赴751园区及隆福寺园区开展调研 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492599&idx=4&sn=0ae800bc64dfdaab003103b13b8831b5&chksm=cfafde82f8d85794f666de727bab75eea2353a273d2b02cf348913098e3997985aed044743fa#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【燕南智库】向勇：乡村振兴，乡创何为？ http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492599&idx=5&sn=f632c1a9dc91f732fb1991d4dcd2055a&chksm=cfafde82f8d8579401a6eac42e37b1e2d770e15d326974ccbf50178016284ec3f422d033cf91#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【燕南智库】陈旭光、孙茜蕊：“高概念”与电影工业美学的遇合——对电影创意生产体系的思考 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492599&idx=6&sn=be17d9f42583535736ef0d4cc1564d4d&chksm=cfafde82f8d8579401291c160081d87a204a81b5ee10c2ef149110ce4c54dadcb615857d0802#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
祝   帅｜中国艺术学“三大体系”的历史传统与当代建构 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492470&idx=2&sn=24d5cbb214f066e68a11ae80d8dd7673&chksm=cfafde03f8d857157b76d2e1714700dd0a08738a96e036066b73006796991ddf0c2a570e2058#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【燕园智库】陈刚、唐金楠：北京大学新闻学研究会：马克思主义在中国早期传播的重要力量 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492470&idx=3&sn=da222fde584f08d63064ce81e0708533&chksm=cfafde03f8d8571558ce5e3165aeb332bdab8264cb5809d1007fed73bdc06c6eafd2264720d6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023年北京大学艺术管理与文化产业暑期学校顺利举办 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492434&idx=1&sn=f386915910c06e632303dad64c531d21&chksm=cfafde27f8d8573173074cb14b893fee0c57b1afc29bd9891459134e0049051fc812eaf962be#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【燕南智库】张颐武：诗歌的新发展与文明的新形态 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492434&idx=2&sn=ad3645bfa2c1cee69d649685eac11837&chksm=cfafde27f8d8573104f51239c61197be696a5199658ecc72b971857a2b1cc98c46c04b02c1ae#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【燕南智库】彭锋：不同的知识生产 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492434&idx=3&sn=d151198f2248a84d6657b80f9159afed&chksm=cfafde27f8d85731238dea683a93645e8feadd57a9fff9b359ca02edcf4c7b5b40336d77f94b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【燕南智库】陈旭光：论电影工业美学的学科体系建构与方法论意识 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492347&idx=1&sn=8e35e07dcf38ae8bd8d40a4229fd3fcf&chksm=cfafdf8ef8d85698a0f5a21e0a493ddd268e006aac053ec971cc6e27301df0f0c2f069fb8ae8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【燕南智库】王一川：中国现实主义文艺中的心性论传统 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492347&idx=2&sn=69c0f34a9aa0b26c4a8559f930f5019d&chksm=cfafdf8ef8d85698b5f0799f76c3983f888c67cedfedebbfe49139f90f84a1c43bf07ef88d2f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【燕南智库】杭侃：守护文化遗产，推动文明互鉴，日渐成为国际社会的共识 http://mp.weixin.qq.com/s?__biz=Mzg4NTE0MDUwNg==&mid=2247492347&idx=3&sn=1276377b73615850aada8ff37d01d4de&chksm=cfafdf8ef8d8569872afeb24f86fbe30569eab0d204f2112334edb4dc2d2c3801b63793b7e25#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大古典语文学 MzAwNzc0NzMwMw==
sleep 337
<Response [200]>
纪要 ǀ 北京大学古典语文学项目2023届毕业典礼 http://mp.weixin.qq.com/s?__biz=MzAwNzc0NzMwMw==&mid=2651307598&idx=1&sn=d177879b07f743bffec55f6b826e11b2&chksm=808a7dc6b7fdf4d085afdff048c61d739e6884f5502bea82fa8b9a34c9836f53e9ca9c598d2f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知 | 2023年“古典语文学”项目（第十四届）录取名单 http://mp.weixin.qq.com/s?__biz=MzAwNzc0NzMwMw==&mid=2651307581&idx=1&sn=51058f8d2b9fb1cff068a4fd012f345f&chksm=808a7db5b7fdf4a3b432601da6ba7918b22d4daa3ebe0a8a15a92ff3ee44f8fdcfb54d3c1090#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 西方古典学方向宣讲 http://mp.weixin.qq.com/s?__biz=MzAwNzc0NzMwMw==&mid=2651307571&idx=1&sn=f1ff512618d0579827ab00d3a6285e59&chksm=808a7dbbb7fdf4ad9ff54424692c45691adac2bb077fa68b59dd9c5cd0bba6ada46855a9f664#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知 | 2023年“古典语文学”项目（第十四届）招生简章 http://mp.weixin.qq.com/s?__biz=MzAwNzc0NzMwMw==&mid=2651307560&idx=1&sn=b0ee4133bd0c31228e75f1c450ae5790&chksm=808a7da0b7fdf4b6641d262c082389fbad1248abb22dfe86f3757331568fb8943fd0fe508439#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告 | 2022北大古典班学年论文讲评会本周五举行 http://mp.weixin.qq.com/s?__biz=MzAwNzc0NzMwMw==&mid=2651307542&idx=1&sn=4d5714452630b2073724b58becfcfbf1&chksm=808a7d9eb7fdf488950ed53c0250ff8b2d1523575df2d6453a273219f68f894a5124b24f431b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
思想与社会 Mzg4ODEzNTExNw==
sleep 516
<Response [200]>
活动 | ”思文在兹“暑期支教队支教活动收官 http://mp.weixin.qq.com/s?__biz=Mzg4ODEzNTExNw==&mid=2247484586&idx=1&sn=dff15e31b3d7b6421421875f125976b6&chksm=cffe8808f889011e4e04df0a55b74c82a0a2fe035695b55e54ba5172da8bf9c6abe87d39039e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023年“思想与社会”项目毕业典礼 http://mp.weixin.qq.com/s?__biz=Mzg4ODEzNTExNw==&mid=2247484533&idx=1&sn=06f43f3b6e834fe8b0ed666429b53799&chksm=cffe88d7f88901c167fd71deadac1b05c79598054df0b7f42662d4a70010611aad893607b963#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
纪要 | 教育与文明发展、思想与社会项目师生参访清华大学 http://mp.weixin.qq.com/s?__biz=Mzg4ODEzNTExNw==&mid=2247484500&idx=1&sn=c7ea478e00bedad6bb7a5a2ca6cfeb0f&chksm=cffe88f6f88901e028ab5151ce769ede8a66554f444c75499c5baa6641377bafeec48ff67b72#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
未名圆桌·报名 | 圆桌×思社：努力奋斗走到头了吗？和李猛、周飞舟、林叶老师聊聊优绩主义 http://mp.weixin.qq.com/s?__biz=Mzg4ODEzNTExNw==&mid=2247484491&idx=1&sn=458f955d1a8ad475137a6e442aa32f72&chksm=cffe88e9f88901ffbeaed8cce2131b772bd18b172a5ef7d0d21af233eecdfd5f735303244f40#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
各位有意报名“思想与社会”项目的同学们好，在报名期内，请各位登录教务部统一招生平台，完成个人信息的填报，并在附件中上传本人成绩单+本人习作一篇。为防止文件上传错误，请各位同时将本人成绩单和习作发至公共邮箱logosandpolis@163.com。祝各位报名过程顺利，期待不久的未来与你们相见！ http://mp.weixin.qq.com/s?__biz=Mzg4ODEzNTExNw==&mid=2247484467&idx=1&sn=e7ee4978a8d0f065a96abba8cf0b6c2e&chksm=cffe8891f889018790a8f786480da51d27e7fab317b64da85761f9a7d999d1b667c17d3693ba#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学严复班 MzUyOTkwNTQwNQ==
sleep 220
<Response [200]>
讲座预告｜书法，书同文的社会机制 http://mp.weixin.qq.com/s?__biz=MzUyOTkwNTQwNQ==&mid=2247485168&idx=1&sn=13a8f0c70b48cb95824c17b13fe251c4&chksm=fa58a562cd2f2c7419401e06a65deb1a6c783798a8a4c2a9078d3ceafe7e627b4fcb2cf200c7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
刊物｜2023年春季号目录 http://mp.weixin.qq.com/s?__biz=MzUyOTkwNTQwNQ==&mid=2247485161&idx=1&sn=37f940ca74b190f7c050d9100deb395d&chksm=fa58a57bcd2f2c6d0e3baad4031012834ce44f390b88173ad1a24cb8af55006bca3b9ae69417#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
谈天｜甘鹏祺：书写立体的生命——家庭史参展人专访 http://mp.weixin.qq.com/s?__biz=MzUyOTkwNTQwNQ==&mid=2247485156&idx=1&sn=4bc80f88c5b1100650819ad685eb0da1&chksm=fa58a576cd2f2c6017ac2dce4af9384593174a84e1aa9e9c5500ae31482693baf20db525a238#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
严复班的团建日常 http://mp.weixin.qq.com/s?__biz=MzUyOTkwNTQwNQ==&mid=2247485145&idx=1&sn=57694818ee4862bc8d30963e58f4fa8c&chksm=fa58a54bcd2f2c5daeb1301935c09374b3cff2a30e509b9dcaa54ff02656ce2291f4ba4bb42a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
学生风采 | 严复班成员毕业去向和学术经历一览 http://mp.weixin.qq.com/s?__biz=MzUyOTkwNTQwNQ==&mid=2247485129&idx=1&sn=291745e380e75c3db0f487790bbb2c75&chksm=fa58a55bcd2f2c4da5d495ea65468220cb898fcc2f1138a65dc1e52a2d7df97e4fbd236baf89#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学 MzA3OTE0MjQzMw==
sleep 450
<Response [200]>
刷到20年前的北大课，“想掉泪” http://mp.weixin.qq.com/s?__biz=MzA3OTE0MjQzMw==&mid=2651965828&idx=1&sn=3277ed67821f10d59dc4c376673633e6&chksm=845d62cab32aebdc05ec924a9892ce340bc3e43a7f6dd2b7a4ea7515b3e7eb82ba14d42789e7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大学生暑假去哪了？ http://mp.weixin.qq.com/s?__biz=MzA3OTE0MjQzMw==&mid=2651965815&idx=1&sn=e945e625fea421a794e158d37b6d12af&chksm=845d6239b32aeb2f33934f798adc2c0607566f8c3653606862a1ccbe7139daea1fe401940902#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
两亿字，282册！北大人事不避难、义不逃责 http://mp.weixin.qq.com/s?__biz=MzA3OTE0MjQzMw==&mid=2651965807&idx=1&sn=8a56cb5253cb171c792bd15fe1019148&chksm=845d6221b32aeb37ae797130a4b7054aca1849d79cccd6e9ee08408fde3c66bfa82ae880aa18#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大图灵班孪生兄弟，合作发顶会顶刊？ http://mp.weixin.qq.com/s?__biz=MzA3OTE0MjQzMw==&mid=2651965719&idx=1&sn=0bee55f3f21aed947da46281be08a543&chksm=845d6259b32aeb4fbd87c66ca61b9dac75cc791311a1c44c28e49650b09cd050f968428b8c49#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新学期，北大开课！ http://mp.weixin.qq.com/s?__biz=MzA3OTE0MjQzMw==&mid=2651965693&idx=1&sn=3090b152f94a0c5687e2e7031482c372&chksm=845d63b3b32aeaa53d5d1020e4e9f0f417e204ae566cef62b57ddac0b64096410768cf6efcca#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大团委 MzIxNjMzMDE1NQ==
sleep 351
<Response [200]>
《学爸》走进北大！与主创团队一起品读成长故事 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247586137&idx=1&sn=13af1b3a6d91c936ef8fb4aef6b266b7&chksm=97896b9da0fee28b042b95de6e197683a9c3513de3a271b8dca8ad3e3c5e87ca8611b65d2793#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
冠军讲堂预告 | 刘伟：乒乓国球与体育精神 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247586136&idx=1&sn=c16680683e9cee3006e4cfdefa71f6c8&chksm=97896b9ca0fee28a65d9d64ca7d16dec4fdfdefbb26c469403271dc3599dd3ada22c6f6e0fbd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
百载回眸风云在，青春如歌响红楼 | 校团委、学生会组织开展北大红楼实践活动 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247586136&idx=2&sn=9443d893a09a198892ff8cfc1f2e3601&chksm=97896b9ca0fee28ad2bc73d84c6b1ff5f7ef43cf82e12976573de8020b4a67b64d9b94434394#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学暑期“三下乡”社会实践团赴贵州省调研“村超”和“村BA” http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247586136&idx=3&sn=44ce6123dd69676000be5e379dde0cde&chksm=97896b9ca0fee28a4cfeb34c14371ee3aecf2532dac9cb588a08e56f08d9e0551e474b01a2c6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023年“力行计划”纪实丨用青年话语讲好党的创新理论 在新征程上谱写实践壮丽篇章 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247586136&idx=4&sn=5ca74b6a165bff8dcc1d50429e0818dd&chksm=97896b9ca0fee28adcc9106e0af861be95bf19445e37f6f1d3fe11cd21ca9e5fa5624018e274#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新生音乐思政课 | 北京大学深圳研究生院与北京大学歌剧研究院党史教育、党团共建活动成功举办 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247586136&idx=5&sn=501a81184c1070856ddd5a377b3dc4f9&chksm=97896b9ca0fee28a08d1c32483363fd2ceb6ef523051ba76566deee846665160df5987363e23#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
喜报！北大研支团项目办在全国大学生志愿服务西部计划考核中获评优秀！ http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585990&idx=1&sn=56c6ac6f3c723272ba1761849c9a8d28&chksm=97896a02a0fee3143dcd458766e7423df80ea2c3e1c35b85205c0a0ddef008dba7820e8fff4b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023开学典礼暖场｜斜风细雨新燕至，幕后台前总关情 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585990&idx=2&sn=a750d577865243be609971230d154a56&chksm=97896a02a0fee3145ca5bee89213716587615b6c1fa8c1160d5543677a01e440c18d6b9b4723#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“1000+”迎新｜2023级研究生“1000+”领航培养计划开展爱校荣校教育 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585990&idx=3&sn=79f7833ddd19d1b6747fce8fe5290bb2&chksm=97896a02a0fee31496064a6ee1553d7f751907f0db3b75674d7c03249b97644980e734f7cf06#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“1000+”迎新｜2023园区行活动——北京大学研究生骨干走进中关村软件园 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585990&idx=4&sn=4d88995729ee7d9a2a86ef7b2cf28433&chksm=97896a02a0fee3142be8a97018c2201bf814c40528a542bfe0c61993acba5fdd048357e755a3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“1000+”迎新｜“勤学深思新思想 力行建功新时代”研究生新生骨干新思想宣讲会暨“力行计划”社会实践分享会顺利举行 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585990&idx=5&sn=8efa0978c0ff79d16a751e484bdf194c&chksm=97896a02a0fee3142d51881f913404f82bb6bb2fa8c98f61f747fff3ef716e625ef6ae949c9d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学2023年中秋国庆晚会暨校团委文艺人才库纳新启动！ http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585893&idx=1&sn=f65dddc6ccc30e3036d465c96f93aeaf&chksm=97896aa1a0fee3b7f137eecb172917d673b332f3c921a2b64195db5e3f4cd85bc9a2c1cb5817#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“1000+”迎新｜2023级研究生“1000+”领航培养计划班委培训会顺利举行 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585893&idx=2&sn=3a68fe2c80e77e7bd6ef90fc258b7d9e&chksm=97896aa1a0fee3b77dd88a776b7724bb4fa146b9397b51432ca141bf0ff9119095f50060a5ff#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学第25届研究生支教团开展教师节主题党团日活动 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585888&idx=1&sn=3ae9b786794d4dbb2caefb23078d1d0e&chksm=97896aa4a0fee3b2819ac7d11510d48d12af0afeb45243756704d2017672a6c8ae3e5f31c3ee#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 在权益部，书写你的全心全意 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585888&idx=2&sn=21213289d108de8bc5a038f3ba3cb2b0&chksm=97896aa4a0fee3b2e233ba454eaf986393b0403f545901efa194680d3fd293b77824aa752ff9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023嘉里调研江西遂川团 | 三色交辉促发展，龙泉古卷谱新篇 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585888&idx=3&sn=6e8cd294733da42972e7797de75bf491&chksm=97896aa4a0fee3b2d5eccb0e89fb5599a2d6e03c62d189a5312a7411d1ef03feaac7baa530a6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023嘉里调研贵州兴仁团 | 文旅融合发展兴 古韵新城万家仁 http://mp.weixin.qq.com/s?__biz=MzIxNjMzMDE1NQ==&mid=2247585888&idx=4&sn=be64660ebca800455c05aae896df140b&chksm=97896aa4a0fee3b2e66ca836fc845740c21acfebf4c146ea6b196fd7b4ec729cecc26f707ee1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大体育 MzA5MjI1NjIyOA==
sleep 83
<Response [200]>
妇联童运，京澳同运 | 澳门爱国教育总会与北京大学体育教研部召开合作交流会议 http://mp.weixin.qq.com/s?__biz=MzA5MjI1NjIyOA==&mid=2649444976&idx=1&sn=6bdc66e336d3b09193c5f21254914513&chksm=887010fbbf0799edef8688be400ef051e1073d6ea782231c51feb151d29189251feabd044a8e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大女篮二队｜2023秋季招新！ http://mp.weixin.qq.com/s?__biz=MzA5MjI1NjIyOA==&mid=2649444976&idx=2&sn=b218ef45065cec3b22b2f43a81c5c45b&chksm=887010fbbf0799ed4045cfbeb22d177db33975c3511888efe8ff25b5f06ddbffef34e9ec6da9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学网球队招新啦！ http://mp.weixin.qq.com/s?__biz=MzA5MjI1NjIyOA==&mid=2649444976&idx=3&sn=eca6d15137fbef1cf86381c085b5f309&chksm=887010fbbf0799ed3564c5bbae5955fcbdea0cca9ab248539727c853f98412c56ea3b7498807#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
莫道桑榆晚，为霞尚满天：张锐教授荣休仪式举办 http://mp.weixin.qq.com/s?__biz=MzA5MjI1NjIyOA==&mid=2649444974&idx=1&sn=2835a8b3b87fbd081b34f9ad001842bd&chksm=887010e5bf0799f31278332a3f25eefe0eb59c22a299fbfb128bdfe7c4f4b9bf1a3a4c894daa#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
从这里开始认识北大——体育教研部开展2023级新生教育活动 http://mp.weixin.qq.com/s?__biz=MzA5MjI1NjIyOA==&mid=2649444917&idx=1&sn=bf63b9ea4179d0436866675332d43bd0&chksm=887010bebf0799a8edbd50484009473d9f3f2ad47474d3b14751dcc0dd1b15d29ff1da8d294e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2022-2023学年第二学期学生体质健康测试补测通知 http://mp.weixin.qq.com/s?__biz=MzA5MjI1NjIyOA==&mid=2649444886&idx=1&sn=91d48d7b4eaa61b8bf0a4f7783923b39&chksm=8870109dbf07998b7b1247b15ac6b76e1f941799f5f4b2e1ebb8936588d1af2aabb740949b07#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大女足正在召唤闪闪发光的你！ http://mp.weixin.qq.com/s?__biz=MzA5MjI1NjIyOA==&mid=2649444886&idx=2&sn=f7c6e3438abd5cdb7baee49642ca5638&chksm=8870109dbf07998b531042e7fcf5f49a3c2fc6f20148faabe9d6fe1a4021604b1eefdf5b94d5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
体育教研部2023级迎新系列活动顺利举行 http://mp.weixin.qq.com/s?__biz=MzA5MjI1NjIyOA==&mid=2649444881&idx=1&sn=ef134113af46a73b81aac99f5d1d7742&chksm=8870109abf07998c21fdd9a3879426ddac59dae8b20ee3cbc958ac071eac5155e49b8fd82047#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学学生发展支持 MzU5OTk0MTE3Mg==
sleep 317
<Response [200]>
问吧 | “问吧”答疑约起来！ http://mp.weixin.qq.com/s?__biz=MzU5OTk0MTE3Mg==&mid=2247491985&idx=1&sn=7d77ab0ff930d2824cb9e129d1881002&chksm=feafe8cac9d861dc0a81335a4c12227464b3ff5028f73914aee9aa5000728aa92435cb613c27#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新｜学生发展支持，助力北大人的梦想！ http://mp.weixin.qq.com/s?__biz=MzU5OTk0MTE3Mg==&mid=2247491971&idx=1&sn=299d9a30c91a8affbe82a0e9a5f46927&chksm=feafe8d8c9d861ce5b828438daa0d40e251a6d4092085472bfbbd3ea40958246751e3b4e65d2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
欢迎选修朋辈心理辅导 http://mp.weixin.qq.com/s?__biz=MzU5OTk0MTE3Mg==&mid=2247491935&idx=1&sn=a39272f1ed8cc28334af2874e1ef8751&chksm=feafe804c9d86112635a55500bf41566e863965f05b4a066d72775d5715a76a6e7cfbf0d8034#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
心科普 | 积极改变生活的两条路径 http://mp.weixin.qq.com/s?__biz=MzU5OTk0MTE3Mg==&mid=2247491933&idx=1&sn=12aa74f07738a809b879fbb76ef501a4&chksm=feafe806c9d8611070f747dfe4bfb81f6a326c1d157645657978cf53c68dc4c52e8e16b61a38#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
心科普 | 帮助睡眠的小贴士 http://mp.weixin.qq.com/s?__biz=MzU5OTk0MTE3Mg==&mid=2247491933&idx=2&sn=5f7d1207d65a51cc36830c3d2fa02463&chksm=feafe806c9d86110e659f239e154ec372639df49db711b4e1c29f4e366fad59f83e9f707ee5a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
心科普 | 更喜欢自己的 7 个秘诀 http://mp.weixin.qq.com/s?__biz=MzU5OTk0MTE3Mg==&mid=2247491923&idx=1&sn=d8d19ffb2847881dfa1631263144ba36&chksm=feafe808c9d8611ea013b7efb5d88b4a6df8065e2e0f73e48bccd1ac2d3cd431d2122b565f60#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
心科普 | 为什么母亲是我们的头号英雄 http://mp.weixin.qq.com/s?__biz=MzU5OTk0MTE3Mg==&mid=2247491923&idx=2&sn=32a422fdc024a81106618f1dab6f0d34&chksm=feafe808c9d8611ed839d6361dd29ab9ecf8501b74681cdf3e73dc690e84048ce4ecd529a40a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大新青年 MzU3ODg5ODQ3MA==
sleep 475
<Response [200]>
招新｜Ai盲盒+北大新青年=？ http://mp.weixin.qq.com/s?__biz=MzU3ODg5ODQ3MA==&mid=2247492621&idx=1&sn=380b44ad6784569cec6b5b24fc93b259&chksm=fd6cfb44ca1b7252b838cddd8d7b3755fbd145cb3a210f5f5e64582b50172c43154d10b546a8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
迎新特辑 | 来北大的第一天，可以做些什么？ http://mp.weixin.qq.com/s?__biz=MzU3ODg5ODQ3MA==&mid=2247492514&idx=1&sn=ac38d4abd5532139cbf802eab1453a66&chksm=fd6cfcebca1b75fda4c0b2c8016091ef76ebe89d86ffc66888dabf7a15961945ecab79cc5119#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
毕业特辑 | 分享你的故事，有机会领取免费毕业照拍摄！ http://mp.weixin.qq.com/s?__biz=MzU3ODg5ODQ3MA==&mid=2247492410&idx=1&sn=14d98ca6251e622dc751e2a9be6b524c&chksm=fd6cfc73ca1b7565860119744a8f3187b750c34365aa503878efa2a09596c979fdd512c9e6cf#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
在场 | 燕南开业倒计时 http://mp.weixin.qq.com/s?__biz=MzU3ODg5ODQ3MA==&mid=2247492351&idx=1&sn=a987def041d86b7c27d153d483d02f69&chksm=fd6cfdb6ca1b74a0eec7bd9e47a04b889a26a6509dda822b089087fd24a37eaf77f56852f9be#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
趣谈 | 燕园省钱小技巧（“五一”归来特供版） http://mp.weixin.qq.com/s?__biz=MzU3ODg5ODQ3MA==&mid=2247492298&idx=1&sn=c569adb27de10d584511eb4f09f3176c&chksm=fd6cfd83ca1b74952d37bdddd3e64b5b8ba11c2a0648868cec281f913d4161c8a43617685f43#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU体委 MzAwNDg0MDA4Mw==
sleep 216
<Response [200]>
周四歌单 | 六一儿童节欢乐跑 http://mp.weixin.qq.com/s?__biz=MzAwNDg0MDA4Mw==&mid=2652687597&idx=1&sn=b12ac733f2911ae8e4f7f6f8dbd3f578&chksm=80cda311b7ba2a0736400dc07b97a7e4d67d81572636e495ddf52db1d1b3288b683deb531f42#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
六一儿童节欢乐跑 http://mp.weixin.qq.com/s?__biz=MzAwNDg0MDA4Mw==&mid=2652687564&idx=1&sn=6e4db0f4b228bf90fd80bba151329557&chksm=80cda330b7ba2a26d1a79f54e18c94284e96a03a978c305120e258de971ca311911c7e24169f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023年首都高校乒乓球锦标赛志愿者招募 http://mp.weixin.qq.com/s?__biz=MzAwNDg0MDA4Mw==&mid=2652687469&idx=1&sn=9056069ea9ac420af4c3a13502b2f136&chksm=80cda391b7ba2a87c4de409f5a683e43fdeed857768c59b2c06db6987df933e9de07a3467f5e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知 | 85公里完成奖励领取 http://mp.weixin.qq.com/s?__biz=MzAwNDg0MDA4Mw==&mid=2652687463&idx=1&sn=d5712989bd445bf5982a244f65c426dd&chksm=80cda39bb7ba2a8df68571a2d7c1cccbd0778f14a27c00136fc1051b01f1ad542ca4486a0847#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知｜课外锻炼奖励申请 http://mp.weixin.qq.com/s?__biz=MzAwNDg0MDA4Mw==&mid=2652687446&idx=1&sn=98bf704c655b207f6dddb68b35ad8424&chksm=80cda3aab7ba2abcf61d424391638ef7d92bd5b2ee6810e3a665696d2bf2f25ebcf9c2b95370#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学教务部 MzIzNzc4ODkxOA==
sleep 564
<Response [200]>
北京大学通识核心课优秀作业奖（2023年春季学期）评选结果 http://mp.weixin.qq.com/s?__biz=MzIzNzc4ODkxOA==&mid=2247506516&idx=1&sn=c6073e6b648c6714c87ed3090afb813f&chksm=e8c1d1cddfb658dbd6663401801b826890cbdda0eff11ec38980ee0e6b6a306ec7245dd2265f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本科教育动态 | 2023.9.11 http://mp.weixin.qq.com/s?__biz=MzIzNzc4ODkxOA==&mid=2247506500&idx=1&sn=db2ec68fc6dfe91b0800481b8960ed4a&chksm=e8c1d1dddfb658cb9bfe6db732f2664b4a5806ddb4394badad9cb898a22f20917c6a7b1ac380#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学关于推荐2024届优秀本科毕业生免试攻读研究生的办法 （校本部） http://mp.weixin.qq.com/s?__biz=MzIzNzc4ODkxOA==&mid=2247506481&idx=1&sn=269f66c1d4c9d0e2fdeb67993177ff3c&chksm=e8c1d1a8dfb658be594147c4d27b323db18b25c747b8c84cf4d9b43dc0b2c7efde055115b6b0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
课程推荐 | 博雅理学讲堂开讲啦！点击查看课程方案 http://mp.weixin.qq.com/s?__biz=MzIzNzc4ODkxOA==&mid=2247506466&idx=1&sn=7fa92ac85b37612c88a6bd824ef80f43&chksm=e8c1d1bbdfb658adaf2021be772cc99d7be060c65653ea9b11bd1eb4a0c76ef20866c671af7d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
课程推荐 | 博雅理学讲堂开讲啦！点击查看课程方案 http://mp.weixin.qq.com/s?__biz=MzIzNzc4ODkxOA==&mid=2247506465&idx=1&sn=ec95e88308bdd6174fd7f90c04ec1745&chksm=e8c1d1b8dfb658aec5a808e7256cce470cfac0500063903b6f31dbab1c8bd43b5bc6582d7a37#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大餐饮中心官方资讯 Mzg4MTIzNzU4OQ==
sleep 487
<Response [200]>
寻味燕园·开学季 | 勺园一层大量新品上线，烹饪与创意的魔法调和 http://mp.weixin.qq.com/s?__biz=Mzg4MTIzNzU4OQ==&mid=2247521249&idx=1&sn=e7d8fe06782a24f59f3f907d67eb8256&chksm=cf6bd8dbf81c51cdad794c73dac3d1545f91d7bd037ef05f7f53836f4931e1df6648d143dcb5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
寻味燕园 | 秋韵十足！万柳食堂的秋季特色鱼菜登场！ http://mp.weixin.qq.com/s?__biz=Mzg4MTIzNzU4OQ==&mid=2247521210&idx=1&sn=659644b34fc08e4b5c7abac73db9f326&chksm=cf6bd880f81c51962f8b041df21eeda51237759b45e01453acec93cecb3d82f19435b513c2c9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
寻味燕园 | 『开学季·教师节特惠』好味来袭，农园三层上新啦！ http://mp.weixin.qq.com/s?__biz=Mzg4MTIzNzU4OQ==&mid=2247521209&idx=1&sn=7109ad9bd9b8e83b005b63304c0b06de&chksm=cf6bd883f81c519592d589042c6d5d83e4537420304187cc4ba1c154b3aad4b6df6c87f9586c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
时食记 | 今日白露！宜食减苦增辛、平养五脏 http://mp.weixin.qq.com/s?__biz=Mzg4MTIzNzU4OQ==&mid=2247521169&idx=1&sn=2c9862a0d46b7ef14c412d7d10b2e271&chksm=cf6bd8abf81c51bd440b1c7c11823d706e3802e4140c1573e56290c773dbee745017b874f28b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
寻味燕园·开学季｜农园二层“炖、烤、烧、炒”火炎焱燚热焕新啦~ http://mp.weixin.qq.com/s?__biz=Mzg4MTIzNzU4OQ==&mid=2247521156&idx=1&sn=98c14881838368f400629d49e773fc3f&chksm=cf6bd8bef81c51a89b0f6d256eb92044478ef663f3a671006f6347e32d813bf3e9eef83293aa#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
燕园学子微助手 MzA3NzE0MjcyMQ==
sleep 203
<Response [200]>
燕园好景又逢秋，安全提示需牢记 http://mp.weixin.qq.com/s?__biz=MzA3NzE0MjcyMQ==&mid=2656073212&idx=1&sn=a5d2aed2e78d1652de43e2fc99bbcbb7&chksm=84f25a52b385d344af3d4284984050c7914ff0ee88097afbbfbdfadffa42a212e4c73026b0aa#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 学生工作部综合办公室期待你的加入！ http://mp.weixin.qq.com/s?__biz=MzA3NzE0MjcyMQ==&mid=2656073188&idx=1&sn=944d8d09886c9927513b43e8eaa6283a&chksm=84f25a4ab385d35cf0d980f0eff17b396ffb980fffe13382284d8ecafa8ecf1139344cf57ef1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
破笼而出！王宝强、陈永胜、史彭元、张祎曈北大讲述 http://mp.weixin.qq.com/s?__biz=MzA3NzE0MjcyMQ==&mid=2656073157&idx=1&sn=616b0137b3a8190c0efe727420edefd4&chksm=84f25a6bb385d37d88b772dca8b4a9c9699739f2c12bd93c975b706feb517da9d07e6a1e5e3a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
弘扬英模精神 勇担时代使命——2023级本科生军训功勋人物先进事迹报告会举行 http://mp.weixin.qq.com/s?__biz=MzA3NzE0MjcyMQ==&mid=2656073132&idx=1&sn=6571fcef978744598a82b27621245020&chksm=84f25a02b385d314d01d3ab3e28f050cb48b3da35c9f7418c61528d3b39da196ee1762853474#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
从百年复兴看百年变局 ——军训国防教育报告开讲 http://mp.weixin.qq.com/s?__biz=MzA3NzE0MjcyMQ==&mid=2656073128&idx=1&sn=0ac33ddffc48005cd3d6e0f26152e4d5&chksm=84f25a06b385d310f746216136dff49d665918030857a81bd00c51df30fb8e2284007987a0a1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
平安燕园 MzI2OTQ2NDg5Ng==
sleep 233
<Response [200]>
2023国家网络安全宣传周校园活动来啦！ http://mp.weixin.qq.com/s?__biz=MzI2OTQ2NDg5Ng==&mid=2247489622&idx=1&sn=3fd07e901d6d28384140873a4803bd89&chksm=eadebc79dda9356fa201b8eda37f4344829d0833944f0acf794a334dd1de9d7a42402036fedd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023级的萌新们，请查收这份安全指南 http://mp.weixin.qq.com/s?__biz=MzI2OTQ2NDg5Ng==&mid=2247489611&idx=1&sn=553968d20099489a527f4032bd8b1b2d&chksm=eadebc64dda93572d7c13daead579f302a56e7c644274ccc88a4880dcc32867e479c5a6f6b1f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学关于校园参观管理的通知 http://mp.weixin.qq.com/s?__biz=MzI2OTQ2NDg5Ng==&mid=2247489598&idx=1&sn=ea4830e5a3a4df81fbf9206b0c809da8&chksm=eadebc11dda9350798656caf5f98318eb4bae63edb6615cf6816e39aa693f9aca3a1f73369d9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学关于恢复校园预约参观通道的通知 http://mp.weixin.qq.com/s?__biz=MzI2OTQ2NDg5Ng==&mid=2247489590&idx=1&sn=5324a30b04c8048faf9ea0aee12153cd&chksm=eadebc19dda9350f4679a422f5b01d87c7fe4535c20fe4bd2d5fd1431c55544cc63764fc2bb4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
警惕！这些地方竟然能藏75个孩子！ http://mp.weixin.qq.com/s?__biz=MzI2OTQ2NDg5Ng==&mid=2247489567&idx=1&sn=10b90c36eca6be0ed74c4077bebf8b76&chksm=eadebc30dda935261a8a64b0e0341b8185b7bfa0926cffff0f11e939d34e1f74159454d42fdd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
燕园微后勤 MzUxMzEyNTczNw==
sleep 551
<Response [200]>
后勤故事之“暑期守护”系列 | 邵华：坚守保障 温暖护航 http://mp.weixin.qq.com/s?__biz=MzUxMzEyNTczNw==&mid=2247497575&idx=1&sn=03848e585f254cde51ab104f9e6f6482&chksm=f95b4b61ce2cc277157b09471e09886ae3a18b276dbd4b3c982252cde0c7bc0cf05f2568822e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“优化布局地下空间 ，打造多彩第二课堂”—— 北京大学校内宿舍地下空间改造竣工验收 http://mp.weixin.qq.com/s?__biz=MzUxMzEyNTczNw==&mid=2247497569&idx=1&sn=df56b59d8b034a67e491231250371c98&chksm=f95b4b67ce2cc271d5e5dd316c420cf869480fd056fb34916d6bafd24fb2b3ab65747aedac06#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
后勤故事之“暑期守护”系列 | 刘汝昕：坚守调度一线，时时待命 http://mp.weixin.qq.com/s?__biz=MzUxMzEyNTczNw==&mid=2247497545&idx=1&sn=a168955a5c352b25c8402eee13ca1016&chksm=f95b4b4fce2cc2595d287d9a1567afbef50e53d334b2ef021c06c73cf2d1885cf8cfaad58874#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
凝心聚力迎新生——校园服务中心全力做好2023年研究生迎新服务保障工作 http://mp.weixin.qq.com/s?__biz=MzUxMzEyNTczNw==&mid=2247497535&idx=1&sn=c86d911e4d481ba500c0c4800afb64af&chksm=f95b4b39ce2cc22f1e4cb62c67e115badfa74da6849cf6ca4fdefeed23ff291355c29fb4c7e1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
后勤故事之“暑期守护”系列 | 翟博：无形服务，服务师生的最高标准 http://mp.weixin.qq.com/s?__biz=MzUxMzEyNTczNw==&mid=2247497514&idx=1&sn=be76f311a1c668aa309e2b471876a0dd&chksm=f95b4b2cce2cc23a812ba11d1e28446bc65284b1cdf5dc43540f5c5fc5b054a7efc46d8c6625#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学招生办 MzA4NjEzNDYxMQ==
sleep 293
<Response [200]>
北大学生暑假去哪了？ http://mp.weixin.qq.com/s?__biz=MzA4NjEzNDYxMQ==&mid=2650464061&idx=1&sn=4a90d62202974ae3dca0f95053209e06&chksm=87c32501b0b4ac17f14a79781c2873fce537ab9c9d95905567a086cbb0fa233dd17b3adf7241#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
未名新语 | 刘婧玥：十八岁这年，我终于发现 http://mp.weixin.qq.com/s?__biz=MzA4NjEzNDYxMQ==&mid=2650464041&idx=1&sn=3188dc16a7f1714ada241cac3159db5b&chksm=87c32515b0b4ac03bcad8a78233e3fcda897c4474fdbed6e25fbd536f2277000160639baa9f0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
未名新语 | 杨镇溢：追光的我们，终会光芒万丈 http://mp.weixin.qq.com/s?__biz=MzA4NjEzNDYxMQ==&mid=2650463959&idx=1&sn=70de22e3a3c6bd326d46c74f60d50612&chksm=87c324ebb0b4adfde0ad3ed952a1cf8267eddf47879abd6a776868787946f6ae4f1999909b88#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
未名新语 | 王晗普：一腔青年志，点作北大红 http://mp.weixin.qq.com/s?__biz=MzA4NjEzNDYxMQ==&mid=2650463958&idx=1&sn=a02267cf6028451dec29916fec1b4eba&chksm=87c324eab0b4adfcb2956d2ba01016cff11938606172d51ce7951e511cba3a6b1332e2d69340#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教师节特辑 | 在北大，致敬每一位默默付出的老师 http://mp.weixin.qq.com/s?__biz=MzA4NjEzNDYxMQ==&mid=2650463957&idx=1&sn=d3348bbfb2c5fb7b7b476a0d0bc52ee4&chksm=87c324e9b0b4adff473b8137dd12410d47b150adfbe219c38e9cfbbf55b80dad45617b0a6e55#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学百周年纪念讲堂 MzU2ODY1ODE1MQ==
sleep 376
<Response [200]>
开售| 把中国电影资料馆国宝级馆藏搬到北大！《劳工之爱情》《盘丝洞》 http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505096&idx=1&sn=c9e0bc37e1b0ffd6943aa66acb37559b&chksm=fc880540cbff8c56c1353c6870a9725da5dc9b4b4297b6b7a8ba3ca216e3f5e41071cb6d84ec#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开售| 把中国电影资料馆国宝级馆藏搬到北大！《劳工之爱情》《盘丝洞》 http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505095&idx=1&sn=9339868ace2a8763d4c0498ccb5e5c10&chksm=fc88054fcbff8c5936a04c152a4595ee6a7a105addbbdc1ba711e80c0b8ce7a4b8eab11a0bfa#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
独家采访中央芭蕾舞团《红色娘子军》主演武思明、管翀正、张浥洙 http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505095&idx=2&sn=d0482f8efcac2f7e629e5d7f813d4540&chksm=fc88054fcbff8c592ab15dc420a70adc78d5afb42ac3dba71edc54a4028fa01e5e3155c693e2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开售｜遇见 室内合唱音乐会 http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505061&idx=1&sn=309015e64c46fc5ab54103cd3ecba827&chksm=fc88052dcbff8c3b70909495c3ff66120b9424bd423b9ea6a6f54df3bd507386b248b0a1d9d4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回顾｜北大2023级新生开启大学美育第一课 http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505061&idx=2&sn=6dcb3b81c3c6f500ba296e6d6597e44d&chksm=fc88052dcbff8c3bc1ea6bafca2beba33f306f68977dd34c7aa0e2de10df3d941ead8e8782e4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动报名 | “燕园起航 艺路同行”系列课程报名启动！ http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505061&idx=3&sn=ec217e1ff3c2efd33175a813d8ebb24b&chksm=fc88052dcbff8c3b4c5eb66963ae47ef8f249c9349d921fc532e50c15eef92c97a36225c578a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开售 | 戴锦华教授导赏系列之二十四　电影《诗》 http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505029&idx=1&sn=b68bffbea8b4982f74d3b87b04462a68&chksm=fc88050dcbff8c1be0dafb0b74a9c6fac53ca6fc75caaeb1a100cf886cc44729c5f019958a9a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲堂合唱团2023招新｜一起来做合唱Singers http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505029&idx=2&sn=a84d01f861ae09c77da95efb5fd884b5&chksm=fc88050dcbff8c1b11789e0c997803470d41444794b59a2adbeb3651a66303a16f761dd1a841#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
加场 | 大讲堂亲子艺术沙龙 探秘《一团和气图》 http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505029&idx=3&sn=098162f26e9d1f079a286c8cffca4cd6&chksm=fc88050dcbff8c1bdf7ae4383bbf7cc148d9e1c94626eb9dda6d984ea0f7140024ba0f26ed22#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开售｜戏剧的力量——北京人艺进北大  丁西林民国喜剧三则 http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505001&idx=1&sn=259abe89efbd658e085e2efec3bd12d1&chksm=fc8805e1cbff8cf742357b1f29723916c461db46644fa738c4effdb2d26cb75c08d9076281e1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
报名｜国际战略年·国际学生学者美育基地艺术课堂——走进芭蕾 http://mp.weixin.qq.com/s?__biz=MzU2ODY1ODE1MQ==&mid=2247505001&idx=2&sn=fb6d2c25a2689c776bccd295143efe08&chksm=fc8805e1cbff8cf7a592cb4cfae4338cb6ec514135193a58adef998e3dfedebfa6781c338766#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大就业 MzA4NjAzMTIxNw==
sleep 484
<Response [200]>
宣讲 | 中国电子2024届秋季校园招聘北京大学专场宣讲会 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023715&idx=1&sn=6ddf17e56b731371bfc20c26467413fe&chksm=841ba3fdb36c2aeb760cb24fd554fd3f00cf87c79b05c87d6023f668ead80769eccbcae07980#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲会预告 | 9月16日 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023715&idx=2&sn=b857666d51e0a14d34f3b5c299523807&chksm=841ba3fdb36c2aebd12caa1351a511b27c810486f430ce24978ed6a9acaf2fb7001a179178fe#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 中国长城2024届校园招聘公告北京大学专场 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023715&idx=3&sn=f1e67589c14eba1811a2b3e397f4c9b9&chksm=841ba3fdb36c2aeb3c0a9535a209f0ed09031b2577de2943fbe9880f26a182f8938d5eb19a9d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 宽德投资2024全球校招现已启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023715&idx=4&sn=a3ddcf82c2d7fcd0e9ae6c71c1dc0aab&chksm=841ba3fdb36c2aeb07917a06fa85659f1fb59e7632b8c8290aa0432f7ee9772b7358733e0874#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 因诺资产2024届校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023715&idx=5&sn=a1c3e0282bfc38fcf0777ecbba3499f0&chksm=841ba3fdb36c2aebacdcdc66e757a04ffd39a5de13463047cc670f3ef447ec4df5f3298a87fd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 财通资管2024届秋季校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023715&idx=6&sn=9b76c4cc8cec87e0080d27d4a76df604&chksm=841ba3fdb36c2aebcede34e81c2590e1d370c32b0765b985b105c008236da8922dab528522ab#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中国诚通2024届校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023715&idx=7&sn=34e8ca448647be618625af6dea0ce31b&chksm=841ba3fdb36c2aeb1515dfe9cf05bc7103ff8c8e69642ebe7db7e13f277b80852a1931b6eb8b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 清华附中嘉兴学校招募实习教师公告 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023715&idx=8&sn=9eaaf3778e1b5835f59bae539546721a&chksm=841ba3fdb36c2aebb4cb932285f7100f6006ceab2936882b812305e785d3f041c2941b351333#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 九坤投资2024届校内宣讲会北京大学专场 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023664&idx=1&sn=26d6e875ba5824f42f8e40cf9634b994&chksm=841ba3aeb36c2ab8100cb139f721f397c7afb2535262bd675ee2ffc0448c0d7c4fc276393acd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 中国电子2024届秋季校园招聘北京大学专场宣讲会 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023664&idx=2&sn=8124bb9ffc510c9eca387b93215a9d90&chksm=841ba3aeb36c2ab84f8694ed4c810f9727302da9e91f9285dc5a2e470e094820e995bcb9609f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 荣耀2024届全球校园招聘线下专场宣讲会行程 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023664&idx=3&sn=e78e84d3f111d9a2a10b6163b730b4ac&chksm=841ba3aeb36c2ab87d56e9636e33d0b812f12ab217f4768bc35939114c9f78f415f1d93659c3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | “邮你炫，耀出彩”中国邮政储蓄银行2024年度校园招聘重磅开启！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023664&idx=4&sn=0390cb5b9b982257219af5085043da0b&chksm=841ba3aeb36c2ab8efe8a07aea3a9d5cf59a91785a75e66b771457878e6987fe8c95b8110a2a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 工银科技2024年度校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023664&idx=5&sn=42b5a9bc10619d88f261e0a7046a42af&chksm=841ba3aeb36c2ab83a46036efbdd851cfcd01819960dd414761cb4de68b4ae3aa886b2c0f388#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | “海纳百川 • 移往无前”中国移动四川公司2024校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023664&idx=6&sn=351ffff2beb9a3abf1b8747db38656fd&chksm=841ba3aeb36c2ab88f2f58c1492b351d08ad1b2f688430b1fa55f1d38d8f19a509d002022f46#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 联通（广东）产业互联网有限公司2024届校园招聘全面启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023664&idx=7&sn=26047a94778cd53ac24a57b238584b96&chksm=841ba3aeb36c2ab87751010b84312d652ac4d3eafe03ad6015db247060933a8f2a9a8251bdb4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中兴通讯法律合规2024届校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023664&idx=8&sn=e77aa526efd68d5221576cf19e278ee6&chksm=841ba3aeb36c2ab8e2190a5730fc40c3f85f62fc58b1fa73de4179490572fd62cbacd2e113e1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中国农业发展银行2024年度校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023625&idx=1&sn=9f20f99738521b745631eaedf4a61235&chksm=841ba397b36c2a81b25a1363f33f6105d4458525b0bbbd93560e964b6d3bd2f66879ae5c3104#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 易方达基金2024校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023625&idx=2&sn=79e293ea658b0a321e2058b5d07fc1ad&chksm=841ba397b36c2a810391fa0de475a0ee4e4878599eff39c65159b01807c98df584584d4d50fe#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 情系潇湘，与你有约！湖南移动2024秋季校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023625&idx=3&sn=3145fd781d80fc910788cc7f21467895&chksm=841ba397b36c2a81d76ac8f9942ec9620a1267387a776f0952df5100a3f69d1f3a38c0136824#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 贝壳找房2024届ADC校园招聘正式启航！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023625&idx=4&sn=da8b98164f33806a6a452ee4fec4cfe0&chksm=841ba397b36c2a8182fb3409bb5cad2341cfa782afa0992777296064525af74924b8d3a756b2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 凯金新能源2024届秋季校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023625&idx=5&sn=89e218940d3630c7468cdb93a319596f&chksm=841ba397b36c2a8144607938e47d7947c7e1dc89dcad51045cad07a56dbece3d4d0ae51a1f90#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 苏银金融租赁公司2024届校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023625&idx=6&sn=3f11402b868f7a7bfcb3af86dc5a1e9e&chksm=841ba397b36c2a8167c30cf99efe1488cd15d8f59f1f978e26b936c57f1e2b26b31c7d2457f6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中国工商银行博士后科研工作站2024年度招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023625&idx=7&sn=815dfb9e4c028c889b3596111ed6ee61&chksm=841ba397b36c2a81b7aea851162f980cc7fac1494a65d72440fbad3cbb4aa81eec6c8f1358c3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 华润万象生活2024届校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023625&idx=8&sn=5f5bd469f8a473c227ee6e94c1169951&chksm=841ba397b36c2a812e12566587c1d9a0280134394e289e6a4f54e76baeda2f28d5af93db10a7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 中国银行2024年全球校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023537&idx=1&sn=df73c1677127ee991545f96f0bd04747&chksm=841ba32fb36c2a39dfb64184c56ef39dd948dba85a132af313c266ac98e58aaa472be71d52a7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中国移动（成都）产业研究院2024校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023537&idx=2&sn=185ad5e4c119f4924a6136d77c6b07fe&chksm=841ba32fb36c2a3998f31f47d3388032fc28c809d925707064de413ab1767e7954e796a8c946#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 中国建设银行2024年度校园招聘正式启动 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023537&idx=3&sn=b909aadc8c7ad9ba8e9ae4e39bd828a6&chksm=841ba32fb36c2a3929e9640cafe955091ca7b2af5e8e7c253c6343aa81fd3a46d095447e73e5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 平安银行2024届校园招聘全球启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023537&idx=4&sn=97e6ee32a1ebe9203b85471ca4485eb2&chksm=841ba32fb36c2a3995b3ce31875eea771fbeb4cac17744f97166baf075816c220faaf363298f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 帆软2024届秋季校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023537&idx=5&sn=195e0351f58ac9c674a633a2b554e00d&chksm=841ba32fb36c2a390c8e7659296bd910c3f14f7187b68c94a6b09551fe30fecc0ba017c3b973#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 国防科技大学电子对抗学院2023年度秋季校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023537&idx=6&sn=92082c9f527bf7727b9dd96aaea9d224&chksm=841ba32fb36c2a39e85d6789400ed71aaf0bc5e085842da3a4f91ccd877c60c16608e9edffd3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 智洋创新2024届校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023537&idx=7&sn=f8ea234177779dea6896ab2ae5fffcc4&chksm=841ba32fb36c2a39f0e0a17a05730f4ba5f0610e00d571452a05e56a6a23f901cf9b3b45b9a5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
实习 | 梅赛德斯-奔驰实习生项目X-SEED计划首次实地测评大揭秘！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023537&idx=8&sn=01dc013089c603ec37738635c9e4a597&chksm=841ba32fb36c2a39e94dbdeec82835e7609e0aec8989751469e9aa30114c07cb698086c54300#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【即将截止】用人单位邀请函 | 北京大学2024届毕业生就业洽谈会 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023465&idx=1&sn=7f67de9761bbfbe1d51db92cc2d72919&chksm=841ba2f7b36c2be127cca0c761bb71b106cf0db1325010380d83981abe4566d3816202762a00#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 小米集团2024届全球校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023465&idx=2&sn=122999078c33003bfa1748ce4f6e33cf&chksm=841ba2f7b36c2be15629bde660c0e1e9e2c6439ddd153396792a77bff0b2e4fb41ea4fa9f138#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
宣讲 | 宝洁秋招宣讲会9月22日晚上19:00英杰阳光厅等你来！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023465&idx=3&sn=60339bf0bdfdcb1991690ac0b2451983&chksm=841ba2f7b36c2be19bb801c374e3f57579382c802077249c5f82fcca6b335c8a3575b2647d61#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 上海市2024年度选调应届优秀大学毕业生工作已经开始，欢迎各位优秀学子报考长宁！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023465&idx=4&sn=bbae74fd0f230ed5d9c29c26011a6f75&chksm=841ba2f7b36c2be183420d3e11ba00c7da56bb47182afdfca17f59cbef56fa523272cf61b4d2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 新青年，建工人——中建新疆建工（集团）有限公司2024届校园招聘正式开启 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023465&idx=5&sn=54720a1652d02460f5a33a07e4f14880&chksm=841ba2f7b36c2be1b4127a8488915ae5ceb1a99609c454331606047c0d2348b6a80369456096#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 量化蒙新，玺迎未来——蒙玺投资2024届校园招聘正式启动！ http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023465&idx=6&sn=70c260fbfe154f2db09cfb53dec7d0f7&chksm=841ba2f7b36c2be1077fcf1b4f64f3461b91cd8f6496971489cac013810eeebd6b3c34bd6c0e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 创造你的“芯”未来——芯恩2024届校园招聘 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023465&idx=7&sn=6f373a07a3e0edd76d2a5ced58aca197&chksm=841ba2f7b36c2be17ac94899a28e4cdf03f2f9cfb3ab527d8d0bd03cd4eb2cee2cf45f0fab73#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
租赁、商务服务和公共管理行业招聘信息汇总 | 中海油田服务股份有限公司等 http://mp.weixin.qq.com/s?__biz=MzA4NjAzMTIxNw==&mid=2653023465&idx=8&sn=e96d91e77a77900f55bf085ffaaa145d&chksm=841ba2f7b36c2be19edbb4c64580fb75bdd2c0c90dd028fddfa53e57120f2f5bad264c912bc8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大未名BBS MzA3OTMwMjc5Mg==
sleep 348
<Response [200]>
通知 | 学生网上自助关联银行卡指南 http://mp.weixin.qq.com/s?__biz=MzA3OTMwMjc5Mg==&mid=2247489685&idx=1&sn=5cab9f939263f100e307996fd1c6732f&chksm=9fb4c172a8c348644c95aed1a7dbd4fbce1508003b7ef165b9e5ea7e82c2d4d64500c08fb103#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知 | 留学生办公室招聘学生助理 http://mp.weixin.qq.com/s?__biz=MzA3OTMwMjc5Mg==&mid=2247489682&idx=1&sn=2d76a20997226f5de892bc74261da5ab&chksm=9fb4c175a8c348631bbd76d9cd625cdefbbefda732a5091f081230f6ddd1f6dcd07c60180410#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知 | 北京大学国家发展研究院本科招生开放日（4.26） http://mp.weixin.qq.com/s?__biz=MzA3OTMwMjc5Mg==&mid=2247489666&idx=1&sn=56bbdd9f0a56581281b6cc15bf57c7d3&chksm=9fb4c165a8c34873e114ec7ab0a9f623b21f3b12782e1530a5d2a0c362b1acfd1c284e21e538#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知 | 北大国关国际组织与国际公共政策方向招生宣讲会 http://mp.weixin.qq.com/s?__biz=MzA3OTMwMjc5Mg==&mid=2247489657&idx=1&sn=dfeb26955804442b534223314e0c0854&chksm=9fb4c19ea8c34888a6dbdf6c9e6677dda817b6c2c305ebea7fae1c76629cfd9d31dc0099ae9d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知 | 学生自助关联银行卡功能大升级 http://mp.weixin.qq.com/s?__biz=MzA3OTMwMjc5Mg==&mid=2247489647&idx=1&sn=a10cde3fa37971e6456f0fe9fb2e5c82&chksm=9fb4c188a8c3489ef3d86627513327ed5b3fef807a114ba6e883009f3b61a38735dbceb2d380#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大政治法律与社会项目 Mzg3NjcxNTMzNA==
sleep 244
<Response [200]>
回顾 | “政法社”2023年暑期实践圆满举办！ http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484565&idx=1&sn=c390a2bb58cd846ae1dd967bfebd3353&chksm=cf2f48bcf858c1aa28ddb24675f17277910b42576cf0ffff2de926342c3ea624cdaaf5ab12e4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
毕业季回顾 | "政法社"2020级学员毕业啦！ http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484484&idx=1&sn=be6ff6eb34a8a67964877e772e5db99e&chksm=cf2f486df858c17b5b67dd661f2fa46f8db36318b71b65d642a7b8b2555cf77263d57a9f4ea3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
南阳实践第一天现场简报 http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484456&idx=1&sn=dd1e1a32d68a850c5b9a1d3322778fc1&chksm=cf2f4801f858c117c7088750305503d99cd7f6598265a1d9514370a44188ff9cd5f53251440b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
南阳实践第二天A路线现场简报 http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484456&idx=2&sn=eab0c8d42c7f21702088cbe3b981bbc3&chksm=cf2f4801f858c11778cb1126cc3c7b7d880e43d47688c9947ba2e90f2052af59937efdbfe223#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
南阳实践第二天B路线现场简报 http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484456&idx=3&sn=f6e38bf90fe93c0df601cec6d1ec541c&chksm=cf2f4801f858c117bac1f764b33f42437e5c71d9c40e9b822a3645c27bfcc3c1e2245f3a0d29#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
南阳实践第三天A路线现场简报 http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484456&idx=4&sn=5d498d997e94c00c374c533b1ef86cdb&chksm=cf2f4801f858c117889a85177b08ba5fbaae81dd57a77b0bd2ffb9a454049a8ed4e24fa1bcd1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
南阳实践第三天B路线现场简报 http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484456&idx=5&sn=c4459ca3312876fef1a4c83a80964c42&chksm=cf2f4801f858c1170701a18843e0fff04466399a8fd58aea07552f305a0b4ae19bc1b020ea8d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023年北京大学“政治、法律与社会”项目结业汇报会与结业仪式举办 http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484396&idx=1&sn=b467205814ef6a96d966ae7715001b82&chksm=cf2f4fc5f858c6d3fcc3fdd66751d66b7a45a8ad19d2ced26bb96b3fc20c8a27edce8266ceb3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023年北京大学“政治、法律与社会”项目暑期团体实践行前动员会举办 http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484396&idx=2&sn=ed8c678d7bff7bda186d3c2803a10879&chksm=cf2f4fc5f858c6d3f3e5ebda1bf5156ab6641b117643727332236ba8f5b1b43236464d4fea3f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【回顾】绿色经济、文化保护与乡村治理：“政法社”学术实践行第二期 http://mp.weixin.qq.com/s?__biz=Mzg3NjcxNTMzNA==&mid=2247484370&idx=1&sn=f02646328834399942820de746a152f2&chksm=cf2f4ffbf858c6ed7821602774b122021d0613d35b6cbe54fc4d1025d757aa424d2a2913a9e9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
Paideia_et_Cultura MzkwMzI0MjEyNw==
sleep 350
<Response [200]>
支教 | “思文在兹”暑期支教活动收官 http://mp.weixin.qq.com/s?__biz=MzkwMzI0MjEyNw==&mid=2247484492&idx=1&sn=b6e78190b948f65ca1ccec6be18e688e&chksm=c0980cacf7ef85ba861e13e55d1aa76c2a15f2a6e5a1cbca5c371be1745f789b5dc6b0b3e0ca#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
未名圆桌·回顾｜圆桌x教育与文明：大学教育中的“通”，传统与现代之间的通人、通识与通才 http://mp.weixin.qq.com/s?__biz=MzkwMzI0MjEyNw==&mid=2247484468&idx=1&sn=92b2af4a452e8ee3a8ce8ceb0dc360b7&chksm=c0980cd4f7ef85c222181e49ac7ec04493f728a9bc1f02216ae43f4a2d631ecc3bbf5600873a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
纪要 | 教育与文明发展、思想与社会项目师生参访清华大学 http://mp.weixin.qq.com/s?__biz=MzkwMzI0MjEyNw==&mid=2247484459&idx=1&sn=de3075dcc2a38fafb2604b38ec0c98e1&chksm=c0980ccbf7ef85ddcc5cfec00b297c981788c58b37f6c4143ec89fd0f4aef199a082120bfa7f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
未名圆桌·报名 | 圆桌×教育与文明：大学教育中的“通”：传统与现代之间的通人、通识与通才 http://mp.weixin.qq.com/s?__biz=MzkwMzI0MjEyNw==&mid=2247484450&idx=1&sn=bb47df1c14c33b294ecb7e25bad40ae4&chksm=c0980cc2f7ef85d4eb5e162163702bd555aabf49cc3a84cccf53deb1e0e3f17ceb97fb8b2750#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
未名圆桌·报名 | 圆桌×教育与文明：大学教育中的“通”：传统与现代之间的通人、通识与通才 http://mp.weixin.qq.com/s?__biz=MzkwMzI0MjEyNw==&mid=2247484445&idx=1&sn=807d0c1016c51c6a82f440d2c8f43e5e&chksm=c0980cfdf7ef85eb826370f7931064b7cd983f60c2b25e0d74e1b9477c734c1a2bc6cf4a9870#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学国发院经济双学位 MzA3MzQ5ODIyNA==
sleep 166
<Response [200]>
今晚截止！| 2023经双学生会招新信息重磅来袭 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368935&idx=1&sn=fa6de68b1a0b49912df8799b51d6860b&chksm=8703e0b8b07469aeea9265ea049fc7c402a3b5f9c648e2e84617bf61d699a9685863b2c1688e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第一弹：文体部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368935&idx=2&sn=e7be822f371fc88c702f5de0d1231e69&chksm=8703e0b8b07469ae29af3cf12bb0e7bacce5a13707d41304ef06a006f8e603d35d96a09e173b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第二弹：联络部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368935&idx=3&sn=65db942d11c661269fa5eb41c08335e1&chksm=8703e0b8b07469ae218a3df0c4a1f10b36db799afc9cd6806457629deb3743174656ff8e2364#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第三弹：学术部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368935&idx=4&sn=6ce08d7c05ca6482ec208bfaa3a641c8&chksm=8703e0b8b07469ae4013360994dad4bd75814d39e185c88b80a6329cae2d1d33eb019ac8ff3a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第四弹：实践部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368935&idx=5&sn=c1cc4d8b48dc00baeb11e28033cf4e92&chksm=8703e0b8b07469ae4271729d6fe3d194a63ddaa1b8be8cb21124fd726443c7c2fa727cb6ebbc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第五弹：职发部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368935&idx=6&sn=ca9d8ffba59e465a10b90d573baaf33f&chksm=8703e0b8b07469aedc2df06f84bbd19fb7866c2082363a6d3bdffe0d21cf70e0a960baf6d648#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
明晚截止！| 2023经双学生会招新信息重磅来袭 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368931&idx=1&sn=7f7260cdc236d23378f02cca308fcf3d&chksm=8703e0bcb07469aa07fc44141bc337f92f089e4a4fe5d9657b12ded57cc0ff3ed4a169b643c0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第一弹：文体部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368931&idx=2&sn=fd09adddeb3e55a930bf8ef1335d91ef&chksm=8703e0bcb07469aab3d4e4a7da576545b6916ce0b980974c424d0c39713f5e829da23c812f0f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第二弹：联络部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368931&idx=3&sn=18d27bb0c8ddb17a1fe1753c6b770471&chksm=8703e0bcb07469aa5a592da42c83d6c6a9668bcda7b1356236dae44025c895ba975e4f5a321f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第三弹：学术部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368931&idx=4&sn=2b4262fbdf6ff07619e2232964a32321&chksm=8703e0bcb07469aa367f6a64309225e4d0233e1d2fbfa639d4581f634937be8ea219002495b2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第四弹：实践部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368931&idx=5&sn=6c706d562ace61f4d35d6927a3f9a21d&chksm=8703e0bcb07469aab1dd89a4235ed76e3d83fb043b2a674f0a631814e93522630131bb521683#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第五弹：职发部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368931&idx=6&sn=c50319491146b2f50d9c0d71398e2801&chksm=8703e0bcb07469aadc071c7ea8d5af78a48e68754dbbb97f82e567a247f9281552c3f4f175f1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第三弹：学术部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368922&idx=1&sn=1c1249dbae561697e78695c143e62f7e&chksm=8703e085b074699304edddd60c1dc5627b51555110eded2de3d50b9f5b01147750439d795d6a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第四弹：实践部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368922&idx=2&sn=2b1182f6eb04477d577eb752f38bbe77&chksm=8703e085b074699308b801206361a2ac3ec930ca86509988d941b68b805d51374c728e2836f6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第五弹：职发部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368922&idx=3&sn=33ad913f6e50ea4ac81a348e7defd8e9&chksm=8703e085b0746993dc04f36c30a8c270b671647aeeb8655cb0f73fe9ee7066222f5f613e21e2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023年秋季学期办理终止双学位学习手续通知 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368901&idx=1&sn=d812d73c356767bc3f5abcb198a2efef&chksm=8703e09ab074698c9fcd6923548615e91f328e05c78ddbd9355a7cbfb3115ce63a2f0326cff9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第一弹：文体部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368901&idx=2&sn=ef2435fea49b77daf8616a346753ff9c&chksm=8703e09ab074698c82d957bece1ec17df06eca25e28ca3fa13b092415e061b8c5106aa09d81b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
部门招新 | 2023经双学生会部门招新第二弹：联络部 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368901&idx=3&sn=00afdf692e9723d1654671928a07f9ce&chksm=8703e09ab074698c098a8e259f8d6d32ffc997f8c56985177b7b6bb739584716d6be979b5e7c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
国家发展研究院经济学双学位新生开学典礼通知 http://mp.weixin.qq.com/s?__biz=MzA3MzQ5ODIyNA==&mid=2650368864&idx=1&sn=845d6a9192c7c0dfaa6aa0a04d8dee89&chksm=8703e07fb0746969a9ab7a1e9ad62ee49cd29c011c48781fb6e9cb4d38d1cdbd4cd06829fc8c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
湘思PKU MzU4NjMyNzM3Nw==
sleep 80
<Response [200]>
乡情食事·预告 | “真湘”美食探索第八期 http://mp.weixin.qq.com/s?__biz=MzU4NjMyNzM3Nw==&mid=2247485480&idx=1&sn=67f23e14ac7217979ee56dd4c663cece&chksm=fdfdbc16ca8a35003fa96708ace54e06783462c7e47c6a2edaf4539fe6386ce3f18825e89f85#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“走，去永州”北大湘协暑期活动顺利举办 http://mp.weixin.qq.com/s?__biz=MzU4NjMyNzM3Nw==&mid=2247485472&idx=1&sn=18ca4f2c4ce4d801fd0c7ff671283f19&chksm=fdfdbc1eca8a350856c8ce82833f8c78d55b315c24a9b82ae6b64b1a50c86a1e846e4fafd1ba#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
出分在即！北大湖南招生组的联系方式和驻地信息！ http://mp.weixin.qq.com/s?__biz=MzU4NjMyNzM3Nw==&mid=2247485465&idx=1&sn=641a3994b766b74d9ef2c06c0438d70f&chksm=fdfdbc27ca8a3531f7461b93c1494039738db2bcdcecb83f05c34cb3ac7e64850d3061fcf0f0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
集赞有奖|2023年在京湘籍学子毕业欢送晚会 http://mp.weixin.qq.com/s?__biz=MzU4NjMyNzM3Nw==&mid=2247485457&idx=1&sn=fbd48dd220fca3ff1027ecd34216141d&chksm=fdfdbc2fca8a35395c12894789c1cbf90797c4725b249165aa93666480266231a2ee8ccd6601#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
岳阳市“百名博士岳阳行”活动报名 http://mp.weixin.qq.com/s?__biz=MzU4NjMyNzM3Nw==&mid=2247485362&idx=1&sn=91da67659f392d81c8cb17c6024d396e&chksm=fdfdb38cca8a3a9a21466c6fb53305f50e83e0f92f08c35cea93e49bfe8c04b9dc7ad1256e48#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大辩协 MjM5MTg0MDE4NQ==
sleep 422
<Response [200]>
抢票中｜北大、复旦…八所名校云上激辩，致敬“狮城舌战”30周年 http://mp.weixin.qq.com/s?__biz=MjM5MTg0MDE4NQ==&mid=2651231282&idx=1&sn=32bba3c4714bc671b99b489f44ebe756&chksm=bd5d56e48a2adff2c2f0a7b5ad0cdf63985c35bfc3974edaf97a2de949527643b617ae98e734#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
圆满落幕 | 健言青春 · 2023国际华语控烟辩论邀请赛回顾 http://mp.weixin.qq.com/s?__biz=MjM5MTg0MDE4NQ==&mid=2651231272&idx=1&sn=11edc9b76acd4880649f76239e1b5f62&chksm=bd5d56fe8a2adfe8fed21ddf0baaa5adc117288d2a640f73acc8e92c94307de28edc2b84aac8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
决赛亮点抢先看 | 健言青春·国际华语控烟辩论邀请赛决赛来袭！ http://mp.weixin.qq.com/s?__biz=MjM5MTg0MDE4NQ==&mid=2651231262&idx=1&sn=776fb2dd65a9fc1b51effc77e24c1820&chksm=bd5d56c88a2adfded5e8bbfb4a479e45ccd7632ac9625ba7a9e4fbb0ff19478420ccce4ec124#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
倒计时2天 | 健言青春·2023国际华语控烟辩论赛邀请赛决赛来袭！ http://mp.weixin.qq.com/s?__biz=MjM5MTg0MDE4NQ==&mid=2651231260&idx=1&sn=c68186b9669b5838e1d46b6e9f174161&chksm=bd5d56ca8a2adfdc338cc9d7cb3d457a1d5835010253e2c8e0ef3fb4afc5ee91af78633001c1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动预告 | 健言青春·2023国际华语控烟辩论赛邀请赛半决赛邀您共同参与！ http://mp.weixin.qq.com/s?__biz=MjM5MTg0MDE4NQ==&mid=2651231260&idx=2&sn=b1e88e137d12b17bf654b9bb307d7a83&chksm=bd5d56ca8a2adfdc9f6e3fbbf7c12009a2e1700b0e99c863bea737f503bed3606955db0298cd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动预告 | 健言青春·2023国际华语控烟辩论邀请赛半决赛邀您共同参与！ http://mp.weixin.qq.com/s?__biz=MjM5MTg0MDE4NQ==&mid=2651231249&idx=1&sn=fd6d5539f27395f71a656782aea84965&chksm=bd5d56c78a2adfd1647d3d01ed0171d60ca39776735df29e8ac15f874e5d7431edcf02d61420#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大红会 MzA3NzAwNjI5NA==
sleep 131
<Response [200]>
世界急救日 | 数字赋能  救在身边 http://mp.weixin.qq.com/s?__biz=MzA3NzAwNjI5NA==&mid=2656197934&idx=1&sn=0906560881f5ae613309f6326019a230&chksm=84fe6997b389e0813d1133fb898e7946fd1f73f1eb7fea2fb04121e7aa42da71347f78c81603#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
世界献血者日 | 捐献血液，分享生命 http://mp.weixin.qq.com/s?__biz=MzA3NzAwNjI5NA==&mid=2656197932&idx=1&sn=f7a5285297f725663a01416398f079d1&chksm=84fe6995b389e08358ed3c891100a2fbc7458b3e7f52e55344e7ac5ddedff64a9552223f665f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动 | 北大红会和仲英公益促进协会联合举办心肺复苏培训 http://mp.weixin.qq.com/s?__biz=MzA3NzAwNjI5NA==&mid=2656197897&idx=1&sn=7429073bf4015e30f4a6341266c789f2&chksm=84fe69b0b389e0a603e0a2e6ca9e869e44a5593c48b4e6f3dba4b8db00542875c7d928278b17#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
志愿者招募 | 2023春季学期第二次无偿献血 http://mp.weixin.qq.com/s?__biz=MzA3NzAwNjI5NA==&mid=2656197885&idx=1&sn=95a409c70ba6247836cd252333c813ac&chksm=84fe6844b389e1527d5275d29c4b0dc82258d69089f48aaf422633676f97e3c2ede1e250f7ee#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动 | 2023春季学期第二次无偿献血活动 http://mp.weixin.qq.com/s?__biz=MzA3NzAwNjI5NA==&mid=2656197876&idx=1&sn=ad6e0971dab370725ad6737d1cd177a7&chksm=84fe684db389e15bd07d326014ce5f44e55b77080dbe8f0c8335f9115b33296f3271f2ad6b4f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
科普 | 中华骨髓库介绍 http://mp.weixin.qq.com/s?__biz=MzA3NzAwNjI5NA==&mid=2656197876&idx=2&sn=5b70aa6e848d86d760d6b0e0b50bc58d&chksm=84fe684db389e15bdaec1bb6aab4cb9171610ff035e633cfea90e63ff17b1911ea9c9cad1abe#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
爱心驿站 MzA5ODA4ODExMg==
sleep 235
<Response [200]>
爱心社招新 | 希望你比冬天先到来 http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508807&idx=1&sn=867f5c56ab478a887a284d4b594301e4&chksm=8899cbd8bfee42cee40ed7e9b57e90b4ae2790f648d20af9f0a11eea4f6a91d70dd08789074a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
星行 | 启程：跨越3600公里的爱之旅途 http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508756&idx=1&sn=542ae7a94d6d0f13d61a5eab0a079a5f&chksm=8899c80bbfee411dd8aa786020689fb6e8a80673ae007fdc888bd8c51cab13544083f1ffbfaf#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
星晷 | 新疆富蕴路成路一百天啦！（来自阿勒泰的情书·上） http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508756&idx=2&sn=87e850f0d2bbf333b8275f7ee4957e00&chksm=8899c80bbfee411db609da5143a71cd7eb3ee97be8479a39478089daa09b5f3e3257e65f9b58#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
星晷 | 新疆富蕴路成路一百天啦！（来自阿勒泰的情书·下） http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508756&idx=3&sn=689e866ee01d4f6cfaabb3ff3b0e8f4a&chksm=8899c80bbfee411da62bab0452e959630e92335c04429fe7175ab6f654f66ba5ed89b7ec8402#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
银杏叶 | 初见面 http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508572&idx=1&sn=3e184136ed527d2eae8325e48f5ef09c&chksm=8899c8c3bfee41d584c35a0bfab7ff84b6409570d4608e5a05ef5938bf34ca21bec00d35d272#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
银杏叶 | 第一阶段 http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508572&idx=2&sn=186de967d2e1fbb5451a0969a2d42a43&chksm=8899c8c3bfee41d591ebe078d589d467a2b6c0ddea8d0577b4e9e246d9de7ff5670e78d51f2a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
银杏叶 | 第二阶段 http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508572&idx=3&sn=be06ea228179b19801236935f08493bd&chksm=8899c8c3bfee41d52a678b4b16ea6c6219fe4c5f5f3c880255f00f4fd007783887a986093e1c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
银杏叶 | 第三阶段 http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508572&idx=4&sn=ec1c2b7c95af95347215be360ef9c7ba&chksm=8899c8c3bfee41d55194ac71638a44e7a08744585f01a85a249531d643c5dd51537582b91979#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
从海拔43.5m到海拔1200m，  我们经历了..... http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508359&idx=1&sn=f7e6e8013993b307e84d43c56fc647d3&chksm=8899c998bfee408e152dafd994b2d739d3daf2a9015c4e9fbaba3d36b619aaa1762d1eb27c61#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
雷波路——开营啦！ http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508359&idx=2&sn=b0953fd2d40713d496bd976393c1e691&chksm=8899c998bfee408ebeb2b19009fdedb37c75f5d50f7b03e3b079ecb5371ba97f130e2682b4ea#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
雷波路王国通关秘籍（上） http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508359&idx=3&sn=b1c93f55698d511da454439f09a8544c&chksm=8899c998bfee408e746091434866a7a2dc7495ae75f3de79413cf4c623cf99c18960ac33005a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
雷波路王国通关秘籍（下） http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508359&idx=4&sn=65e731f5e1bc23d9aae4eb8d5cf207d3&chksm=8899c998bfee408e6b45f0387e2b134ef563566e34b2cc029bd355c270e0be520a61597a5957#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“银杏叶”的诞生录 http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508209&idx=1&sn=e435f853a48c71a981a228b3c17bd1ee&chksm=8899ce6ebfee4778d85a15b5df1a6378a9216d99b3205e7600166ea8c108d6234fa2d64f7543#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
银杏叶 | 试讲进行中 http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508209&idx=2&sn=0b0638aaf761b329a80f05e129187a70&chksm=8899ce6ebfee4778618008eac355e5a66f64048fdf44e2b32c870c16111e206a54f9b2610187#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
银杏叶 | 出发前夕 http://mp.weixin.qq.com/s?__biz=MzA5ODA4ODExMg==&mid=2650508209&idx=3&sn=e7d8bbbb4073324f6ee063666568370c&chksm=8899ce6ebfee47782e832760c727361a11d015f3a2032d1e68bc522164b244a6e710bd4e1403#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU思潜十周年 Mzg4OTY4NDgxMA==
sleep 168
<Response [200]>
研会·活动丨探索神秘真相，体验别样人生！——剧本杀主题活动 http://mp.weixin.qq.com/s?__biz=Mzg4OTY4NDgxMA==&mid=2247484334&idx=1&sn=0984beda8a6c96ec70e784fe2b4a24a2&chksm=cfe9558bf89edc9db217cdc5549d46816e0d1e1197a36a1323fec4465b0db60686db31c0c06a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
迎校庆，奔巅峰 | “问鼎巅峰杯”《三国杀》2V2比赛开启报名！（更新版） http://mp.weixin.qq.com/s?__biz=Mzg4OTY4NDgxMA==&mid=2247484295&idx=1&sn=35903b86eea8468bc767ea071749c696&chksm=cfe955a2f89edcb407f14bf8fc64eab78842f5b80698b3a1c7c0f60ba227161bd0a37e33f96a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
DM讲堂特别期 | 回顾·对话山梗果·春季招新 http://mp.weixin.qq.com/s?__biz=Mzg4OTY4NDgxMA==&mid=2247484284&idx=1&sn=72e99e5288d722e35ebaa024e482a143&chksm=cfe95559f89edc4f096e134b6b3079a4189c522464d60f8dc11724db2c0af14aabfb2680ba53#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
思维潜能开发协会第二届“迎新杯”开启报名！ http://mp.weixin.qq.com/s?__biz=Mzg4OTY4NDgxMA==&mid=2247484244&idx=1&sn=b5bc284ba14a371c594a1ddce4213bf6&chksm=cfe95571f89edc67ce763aa53d9580bf7a5430ce70f03345f2953e2a0c321e45cfd8ba22d5a4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
剧本杀：相遇在另一个平行时空的江湖 http://mp.weixin.qq.com/s?__biz=Mzg4OTY4NDgxMA==&mid=2247484233&idx=1&sn=5876efc4e0a25f9e07132fe07d8fa3b5&chksm=cfe9556cf89edc7a067c0cbbdb69ac430e0afec43303fed47b696500a076de647881d0a5b6a4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
未名超算队 MzUzOTk3NzkxMg==
sleep 317
<Response [200]>
2023 北大超算队招新 http://mp.weixin.qq.com/s?__biz=MzUzOTk3NzkxMg==&mid=2247483742&idx=1&sn=a509f17fe83664a414a6574a775922ad&chksm=fac17089cdb6f99f6c477d3e0ac3d9387875e36ef8060f9961bc965546f76fa0d58cd5f8b74a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2022北大超算队招新 http://mp.weixin.qq.com/s?__biz=MzUzOTk3NzkxMg==&mid=2247483693&idx=1&sn=b5c5d6027b6dd871d07c6a8fd4379b6a&chksm=fac170facdb6f9ec42cdb12a56df6f18832d2ee5f6c0bd3e4e20c6edd70f3536fa98542cc7dd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2020北大超算队招新 http://mp.weixin.qq.com/s?__biz=MzUzOTk3NzkxMg==&mid=2247483689&idx=1&sn=c3c5aecf600e87bc880b6df42cb6074f&chksm=fac170fecdb6f9e8fb9c8a6c1643f00bdf0e2a76578ba35b88e6d5777f97bc6d8093e7d30fc1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【April Fools】ASC决赛加油 http://mp.weixin.qq.com/s?__biz=MzUzOTk3NzkxMg==&mid=2247483674&idx=1&sn=e9f3728ecf7851fe59cd8081d5c92f20&chksm=fac170cdcdb6f9db0482ded9612c4cf3e0f5438ddc8a127eefdaf886e30726a5a6a4544deb66#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学超算队招新啦 http://mp.weixin.qq.com/s?__biz=MzUzOTk3NzkxMg==&mid=2247483661&idx=1&sn=fca3d395ec91829433f75d2ead095303&chksm=fac170dacdb6f9cc7dcc8b004fa427c51727059fb3feb8fa61ff8577ec9919dac45b20942deb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
燕语配音社 MzAxMzMwNTAxNQ==
sleep 255
<Response [200]>
燕语·线上活动 | 夏日炎炎，一起来快乐pia戏吧！ http://mp.weixin.qq.com/s?__biz=MzAxMzMwNTAxNQ==&mid=2648841192&idx=1&sn=67511b5bee4eaf001f35c4c538b99db8&chksm=83b22e30b4c5a726bfbf7e9a886c96461d4d74aad554be267ae7dc3d2fab1a8a448a3437b58c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
燕语·公示｜2023年秋季学期留任执委名单 http://mp.weixin.qq.com/s?__biz=MzAxMzMwNTAxNQ==&mid=2648841173&idx=1&sn=daddd901d8a72b503650d62821d49af3&chksm=83b22e0db4c5a71b0f6f25d0410d11c99bb0046ac8656b01de6f2f19f24842fe1a437c7438bc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
赛报｜「新声之约」第二届北京大学校园配音大赛决赛顺利举办 http://mp.weixin.qq.com/s?__biz=MzAxMzMwNTAxNQ==&mid=2648841161&idx=1&sn=1c04ca9be0cb3654da30999914a406a6&chksm=83b22e11b4c5a707e127edb216b411bef3d5e7005c9fc2927066ff3bf021ce3eff0c0b6b7d5a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
燕语·线上活动丨“胡燕乱语”评比开始！ http://mp.weixin.qq.com/s?__biz=MzAxMzMwNTAxNQ==&mid=2648841137&idx=1&sn=3f5b38a9efd5244ffd05acef521e2eb7&chksm=83b22e69b4c5a77f1e6834915360077e11aaeee96d70fdbef6bbd756bd5c10b423a3606debbe#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
燕语·演出回顾｜《无人生还》声优剧——记那个「惊心动魄」的夜晚 http://mp.weixin.qq.com/s?__biz=MzAxMzMwNTAxNQ==&mid=2648841100&idx=1&sn=8a6bef3b9093399cddd037eb706dee7c&chksm=83b22e54b4c5a74276b6966afde3cb3d32492a142a5638e970f99ad56349815a0439777d1a06#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKUSAA Mzg4NjExNDUzMg==
sleep 475
<Response [200]>
活动 | 文远知行邀你了解智能自动驾驶！ http://mp.weixin.qq.com/s?__biz=Mzg4NjExNDUzMg==&mid=2247484971&idx=1&sn=3b6356e929f6f594f5654b90ef61be97&chksm=cf9fd7a0f8e85eb63cf0ee6456da4153d2428e216300b0d694dc05dfb3d0390739352000e073#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
赛事相关 | PKUCPC志愿者招募 http://mp.weixin.qq.com/s?__biz=Mzg4NjExNDUzMg==&mid=2247484947&idx=1&sn=41299a50f7bd578300f4a848552caf08&chksm=cf9fd798f8e85e8e6a339e4ef0c5e8d5be30a38a06f4b6ae0c40ae8fa7dad50f2b912984124d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
赛事 | 第二十一届北京大学程序设计竞赛命题大赛 http://mp.weixin.qq.com/s?__biz=Mzg4NjExNDUzMg==&mid=2247484935&idx=1&sn=6646b3ed4e973daccbe96c1e5dd978c4&chksm=cf9fd78cf8e85e9a5935aafe100269cfb3341ee2c6ce2f3c14afcb0a3f75855be953f8d42153#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
赛事 | “思勰杯”计概期末模拟赛 http://mp.weixin.qq.com/s?__biz=Mzg4NjExNDUzMg==&mid=2247484930&idx=1&sn=b559a3c1d5330d9fe86fa6496306a04a&chksm=cf9fd789f8e85e9fafe9edb7da923d8e17971184045abd6a1d44c7b07f3a162eb2b23d7eb048#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
推广 | 思勰投资2023届校园招聘 http://mp.weixin.qq.com/s?__biz=Mzg4NjExNDUzMg==&mid=2247484913&idx=1&sn=e973df38035804cf8a38c35c7c022cf7&chksm=cf9fd47af8e85d6cf4f83471eb8f7cc7d313883e1d60cfb82e5277562222d45cff36cb81ef61#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大猫协 MjM5NDc5MzgzNg==
sleep 412
<Response [200]>
送养｜现在的年轻人都不养猫了？ http://mp.weixin.qq.com/s?__biz=MjM5NDc5MzgzNg==&mid=2649620577&idx=1&sn=32daf9d71168e770733ef71b21457cde&chksm=be98f06289ef7974b739a7bae1b71584c91e39796e54adafd929e1ed0049a78e9a56a68ca75f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
速报｜地下室掉猫梅开二度 http://mp.weixin.qq.com/s?__biz=MjM5NDc5MzgzNg==&mid=2649620454&idx=1&sn=cd5f6fd622327512261d4a517ae2910f&chksm=be9b0fe589ec86f30212618ea826dd4f264696715ca7a0a01457f05895dceb4ae9ddf100fc9b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
失猫招领 http://mp.weixin.qq.com/s?__biz=MjM5NDc5MzgzNg==&mid=2649620414&idx=1&sn=43b66b7eef4602debf1b6820b1aff4da&chksm=be9b0fbd89ec86ab119f62533a73646852003aef3c81606d6175684b39718c936f2e679d9c9f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
失猫招领 http://mp.weixin.qq.com/s?__biz=MjM5NDc5MzgzNg==&mid=2649620409&idx=1&sn=ab7f08b072133128481d692c28917e9a&chksm=be9b0fba89ec86ac665df062f1ff9ece0a2876d7ba48fc94a638a7a448de09e14e36dd7f71bb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
花臂少女的夏天 http://mp.weixin.qq.com/s?__biz=MjM5NDc5MzgzNg==&mid=2649620401&idx=1&sn=9670ff67b72cc393f6c9bf4104063a21&chksm=be9b0fb289ec86a4c6c3faa9aa83e2d37fbc3c01131dcc6e289a2927a23c91c4f92d27fee9c1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
风雷街舞社FLCrew MzI0NjA0MTUwNA==
sleep 436
<Response [200]>
内训｜与乐乐老师重返2021 http://mp.weixin.qq.com/s?__biz=MzI0NjA0MTUwNA==&mid=2650587866&idx=1&sn=fa166a7088b36ed771e079bf855cc0bf&chksm=f14d3c15c63ab5033ac4c25b1bc73fbda7460ad2745b54a77f704509e9b4ba436ee5210e575a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预热丨Back to School Vol.3 http://mp.weixin.qq.com/s?__biz=MzI0NjA0MTUwNA==&mid=2650587380&idx=1&sn=88538ba903c3a0dba1c87408cdc95ef8&chksm=f14d3e3bc63ab72deaa29121aa2706daedbc1bde7f3ba920805c2c6576dda7fcc5c3fe433ed5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预热｜House Party Forever Session.2 http://mp.weixin.qq.com/s?__biz=MzI0NjA0MTUwNA==&mid=2650587363&idx=1&sn=b39a8ddf58873d36b81c0b55f640d33a&chksm=f14d3e2cc63ab73a1033b7b662be1c2c80b506054e992179db70d93582e41e9fbd0cf3ddb6eb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
风雷不再见丨Breaking & Choreography & Hiphop & House http://mp.weixin.qq.com/s?__biz=MzI0NjA0MTUwNA==&mid=2650587155&idx=1&sn=8d024c2e47f113cd48e3c1b0908901ce&chksm=f14d3edcc63ab7ca4e02b5ff52b9a209357445bddb4fc65b402acce4e8a061381376c393522b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
风雷不再见丨Jazz & Locking & Popping & Waacking http://mp.weixin.qq.com/s?__biz=MzI0NjA0MTUwNA==&mid=2650587155&idx=2&sn=ef518c84973e70cbfce82bb667b7e17e&chksm=f14d3edcc63ab7ca14ff4fb97bd8a9d5e4003d08a4c223899ce9cf02fd60ecc072c2faf6d1b6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
随机舞蹈 | 来一场夏日的狂欢 http://mp.weixin.qq.com/s?__biz=MzI0NjA0MTUwNA==&mid=2650586229&idx=1&sn=f77f9d2aca8ac020b5c4b80286ea690f&chksm=f14d42bac63acbac74a67684566b8060ff9649ebe9830a11cfba047e633c169e86be4d79ad77#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大粤协 MzA5MTk4NTgxNg==
sleep 194
<Response [200]>
活动报名 | 中秋联谊&就业指导活动 http://mp.weixin.qq.com/s?__biz=MzA5MTk4NTgxNg==&mid=2650100591&idx=1&sn=630c10363ddd89eedce1488f57c5939a&chksm=8875f198bf02788ee5a21d6d5513535c79122eccec3bd0b7b64861b905488d520eec0ea46a33#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
非遗佛山暑期实践回顾 | 岭南水乡 佛韵悠扬 http://mp.weixin.qq.com/s?__biz=MzA5MTk4NTgxNg==&mid=2650100579&idx=1&sn=b9daacc454840585a1bf8226214a6761&chksm=8875f194bf0278825bde93d1f4a3ba02d7ae1ec783a3f900863b252693188c18af507abc0203#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
早茶回顾|米挂住复习，够钟饮茶啦！ http://mp.weixin.qq.com/s?__biz=MzA5MTk4NTgxNg==&mid=2650100535&idx=1&sn=7993c8eb49c116d4b239b20101d389a2&chksm=8875f1c0bf0278d6632f85b30e455bf3f0a09b22c0d82073b50eeb8f92253b3ca13966b8f719#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
暑期实践招募 | 非遗佛山探索旅程等你来！ http://mp.weixin.qq.com/s?__biz=MzA5MTk4NTgxNg==&mid=2650100510&idx=1&sn=37b61cc09c9b28dcc1aa2b98dc0a7bd5&chksm=8875f1e9bf0278ff6e3125e0925e9a1e2ec39bd74a87b99329d1a35f1a46805980a3ab8f653f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动报名 | “一盅两件”早茶粤定你！ http://mp.weixin.qq.com/s?__biz=MzA5MTk4NTgxNg==&mid=2650100497&idx=1&sn=d7fd6e2fd7f2136930f2f36377f233c1&chksm=8875f1e6bf0278f0cf737cf16202475fc17b408edef7da792320764d324aa88c5a88bed32e2e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大耕读社 MzAwNjA3NDQxMQ==
sleep 516
<Response [200]>
君子之道，人人可为——“心性之学”与“公益实践”讨论会纪实 http://mp.weixin.qq.com/s?__biz=MzAwNjA3NDQxMQ==&mid=2684671980&idx=1&sn=5a2272fcad36e562da7729d06fdcc75a&chksm=bee28ea8899507be329b7742955889d34e8b8b6eb2867c76854f68109dbd541ac0a4955a182b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学学生耕读社成立二十周年纪念大会举行 http://mp.weixin.qq.com/s?__biz=MzAwNjA3NDQxMQ==&mid=2684671975&idx=1&sn=0f83f9b2e2e2fddc6a57f85ad5c2cab1&chksm=bee28ea3899507b557413ba62b0ac40b04d2f9a3c940a3e2b97c5bdc0e44cc58a856b585f28b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告| “心性之学”与“公益实践”讨论沙龙 http://mp.weixin.qq.com/s?__biz=MzAwNjA3NDQxMQ==&mid=2684671937&idx=1&sn=95555694a0f12a6cd525c182f5c101b7&chksm=bee28e8589950793b68e8b9f5e896e50f9072332c02f8b0af876dce704ebff29f1e9d0a721af#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【邀请函】耕读社二十周年社庆 http://mp.weixin.qq.com/s?__biz=MzAwNjA3NDQxMQ==&mid=2684671930&idx=1&sn=b3ef0183bccaa50e0e535724f86e2dbc&chksm=bee28efe899507e88dee8f2b75cf23b69320c008fe3a353c7e9ccc5b7c5fb27c11f3ce0f790e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
耕读再解—生态文明的未来与精神生活的复归 http://mp.weixin.qq.com/s?__biz=MzAwNjA3NDQxMQ==&mid=2684671913&idx=1&sn=ab4f65bdd92ba9b9d86c4305da17c2d5&chksm=bee28eed899507fb517d88309f700f35089a63e0a3c9d8f6c949eaab76c879b86ab190d16f4b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
元火动漫社 MjM5NjY2ODY0OQ==
sleep 584
<Response [200]>
【秋季学期社衫征稿】新学期新痛T！ http://mp.weixin.qq.com/s?__biz=MjM5NjY2ODY0OQ==&mid=2650133383&idx=1&sn=c7f9e96fb1aedf6260ecaae013c0ca82&chksm=bee4c60189934f174c994f6dda18403769f995b1333e8e94e8287825cf3a443235f525a09c1a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
元火动漫社2023秋季迎新晚会节目招募 http://mp.weixin.qq.com/s?__biz=MjM5NjY2ODY0OQ==&mid=2650133374&idx=1&sn=5d45a9d7151ef5c23ebac34bc41abdc7&chksm=bee4c6f889934fee2dd16d9e97a5d9625d53f91e1cfb9efe34ac75d60ed20371e357c1f89088#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
米哈游2024校园招聘限时快闪活动 | 北京大学站 http://mp.weixin.qq.com/s?__biz=MjM5NjY2ODY0OQ==&mid=2650133363&idx=1&sn=26b38e5e708ae79c03040d5d4ad71f20&chksm=bee4c6f589934fe35a1ee032040b154dbb8a6e4081e0d9ec9d1af1256150e3ed5ffe2baa6f1a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【换届公示】元火动漫社第26届执行委员会任命结果 http://mp.weixin.qq.com/s?__biz=MjM5NjY2ODY0OQ==&mid=2650133346&idx=1&sn=be819dc6e3e10d9ae5bcb08866ff9737&chksm=bee4c6e489934ff26e3e4d734dbcb86fbb7ecfc70507c6e7bda1a550ef2d29b1ba574a1c66ab#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【repo】光速出炉的2023年春季晚会 http://mp.weixin.qq.com/s?__biz=MjM5NjY2ODY0OQ==&mid=2650133336&idx=1&sn=2f30cb7788293b06b4133afb2681f1b2&chksm=bee4c6de89934fc8dd636dc22edd672f946c397ce14af959440ade2179ccf9ed0bd2b0ce877a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
pku心协 MzA4ODg5NzU4NA==
sleep 290
<Response [200]>
本周活动预告｜读书会，心理沙龙，茶话会 http://mp.weixin.qq.com/s?__biz=MzA4ODg5NzU4NA==&mid=2655914641&idx=1&sn=3a1c703589b44389eff2300f0b068830&chksm=8b998bcebcee02d8df479ff22c380c9d8d7cfce1c09259ea6418d1051e8487d9ad790b67450a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
读书会招募 | 《不寻常的治疗》 http://mp.weixin.qq.com/s?__biz=MzA4ODg5NzU4NA==&mid=2655914633&idx=1&sn=a0a173117cb2dc376067c540831eb8ca&chksm=8b998bd6bcee02c012d74644e0b6b5c8f08dcd52948136c18233de2a6d50d90aa28843e84e6b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本周活动预告｜读书会 http://mp.weixin.qq.com/s?__biz=MzA4ODg5NzU4NA==&mid=2655914623&idx=1&sn=eab89bb41f25357e39caceeac724b64a&chksm=8b998b20bcee0236f877664a31c83054996f6c1967194530ddf5b94f758f468b8ed9076dd87c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“解忧杂货铺”持续营业中！ 欢迎来信～ http://mp.weixin.qq.com/s?__biz=MzA4ODg5NzU4NA==&mid=2655914617&idx=1&sn=f19bed5b18bf91ffd015f5d34ab632d5&chksm=8b998b26bcee0230cc30c91fb8c2d7362a19402fcfccd24c2554dec54d453510d07b257b416f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本周活动预告｜心理沙龙，解忧培训 http://mp.weixin.qq.com/s?__biz=MzA4ODg5NzU4NA==&mid=2655914615&idx=1&sn=4706eb107eadb1cbe018f31014fa8320&chksm=8b998b28bcee023eb1daef7a30978ce15464ca7ee3f6eee952a663808be5f43e7813fba33c8d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU_CACA MzA3OTQwMTAwOQ==
sleep 341
<Response [200]>
回顾 | 南瓜派活动 http://mp.weixin.qq.com/s?__biz=MzA3OTQwMTAwOQ==&mid=2651338946&idx=1&sn=8b8e7ac7d87dcf415911eb2bbebd0b2d&chksm=8448819cb33f088a0b989e207b56e84e6f8d03a327fa4e8ce139fded84511f7834f1732ab706#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
报名 | 快来做爱心蛋糕卷 http://mp.weixin.qq.com/s?__biz=MzA3OTQwMTAwOQ==&mid=2651338945&idx=1&sn=40c30e222b6a850a8f9e22f83f029e2d&chksm=8448819fb33f088908df8b4414eaec27b128b6e9482f36dcf92fca79d850f65a26fdb77d06e8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回顾 | 玻璃画制作活动 http://mp.weixin.qq.com/s?__biz=MzA3OTQwMTAwOQ==&mid=2651338877&idx=1&sn=8d88020b6e47ad2fcfaf6c222bdd8103&chksm=84488123b33f0835383c183684bd0dbd11ed43a5a7a6f86bf2434dd9d41a852ba6d055405608#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
报名|一起来粘毛球画吧~ http://mp.weixin.qq.com/s?__biz=MzA3OTQwMTAwOQ==&mid=2651338876&idx=1&sn=66feb95389650050c94717b069f9605b&chksm=84488122b33f083455ab095eb2369ed730d903cbb39460d9ef927cfa3079b6b184dafa844063#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
报名｜穿戴甲制作 http://mp.weixin.qq.com/s?__biz=MzA3OTQwMTAwOQ==&mid=2651338818&idx=1&sn=cd1e56abb4efb155be52aa6174d32518&chksm=8448811cb33f080a72b5d22871cf9f352652371d49d4eca1cc427d20257e2db3b56aedb02e19#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU烹协 MzI4MjU0Njc1Ng==
sleep 429
<Response [200]>
MINI厨房| 软fufu的泡芙再次来袭！ http://mp.weixin.qq.com/s?__biz=MzI4MjU0Njc1Ng==&mid=2247487483&idx=1&sn=b18ed1751351ea0142958aac7fb52e3a&chksm=eb9908d0dcee81c65f0f8ae8b2c2225cbe616d158de3a95bc5eab8ff2c0c471338791edb5d7e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
探店预告 | 利桥顺酒楼 http://mp.weixin.qq.com/s?__biz=MzI4MjU0Njc1Ng==&mid=2247487479&idx=1&sn=b90b862576d7b4bb9181accf4a090f81&chksm=eb9908dcdcee81cafc3aa333b1703417a76fce819324a4dba08c7c33f06ca530b6b6dde1a451#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
探店预告 | 泰丰楼 http://mp.weixin.qq.com/s?__biz=MzI4MjU0Njc1Ng==&mid=2247487466&idx=1&sn=0ae03abb46817103f00d6b364ece46f6&chksm=eb9908c1dcee81d7d9ef7b47cc8162fb4aab089438239f69e19e16af75ddcd513f35ee4edc56#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
MINI厨房 | 冰汤圆 http://mp.weixin.qq.com/s?__biz=MzI4MjU0Njc1Ng==&mid=2247487461&idx=1&sn=da32ae2c667119ffb4df9368f223f765&chksm=eb9908cedcee81d86223a39817ed392e476b118c06ac7825bbf8e8e19e00edfb25f822a1937e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
下厨房 | 草莓慕斯杯 http://mp.weixin.qq.com/s?__biz=MzI4MjU0Njc1Ng==&mid=2247487454&idx=1&sn=94421b6e42691673060f19af9cda7f6c&chksm=eb9908f5dcee81e363ff33d555212bda29c23b1ba1ccafc68a968886dddfb54cc28bde7091c1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU创新学社 MzA3MjMzNTQ1OQ==
sleep 590
<Response [200]>
参访报名｜中关村互联网教育创新中心 http://mp.weixin.qq.com/s?__biz=MzA3MjMzNTQ1OQ==&mid=2652719444&idx=1&sn=a17fd9901704aafa10a460f10aa946e9&chksm=84f60058b381894ebffeefd6c9f869d133252ff480fe124173d9a8f95cea7b167c095f252e9c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
大赛推荐 | 听说，你想做大模型时代的应用层创业！ http://mp.weixin.qq.com/s?__biz=MzA3MjMzNTQ1OQ==&mid=2652719424&idx=1&sn=58c0b5b0a2d6ae5a761e37d85a9afdf2&chksm=84f6004cb381895aa1b77163874a0cb753ed9cd78ef88eb00c407ecff4231a0265ef92d2efc7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
大赛推荐 | 第六届人民网内容科技创业大赛 http://mp.weixin.qq.com/s?__biz=MzA3MjMzNTQ1OQ==&mid=2652719412&idx=1&sn=7df0bfbdf1ef33171c2ad356988aa1f9&chksm=84f60038b381892e5e5a6c5bba2914494bd09e79ad3b882bf18170440bd208a876e00034874e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
报名 | 国药创新导论 —— 大咖云集，共话创新 http://mp.weixin.qq.com/s?__biz=MzA3MjMzNTQ1OQ==&mid=2652719412&idx=2&sn=52f3460404e9585a95389290086f6f49&chksm=84f60038b381892e02aeca923059646ea9a7c4cd75f4ae980ef8efdcd5a3c0c3356360384183#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回顾 ｜ 北大创新学社亮相 HICOOL，共襄创新创业盛会 http://mp.weixin.qq.com/s?__biz=MzA3MjMzNTQ1OQ==&mid=2652719380&idx=1&sn=ff564c49697a25c6706faa45574c046c&chksm=84f60018b381890e12c342b435a5142db53ea1a21ad57a909bce3b5a0be92fbd0d7c234fda68#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
报名 | 北京大学创业训练营全国班（十期）报名全面启动 http://mp.weixin.qq.com/s?__biz=MzA3MjMzNTQ1OQ==&mid=2652719369&idx=1&sn=e3737fe65b385c2a4f3c92d32f6da10a&chksm=84f60005b381891305d5156b31c9b00d2f0582d16145d3b8327c7029d57679b8524f95358d2d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
协办活动｜全球化与“合肥模式”：海外创业者落地安徽的机遇与挑战 http://mp.weixin.qq.com/s?__biz=MzA3MjMzNTQ1OQ==&mid=2652719369&idx=2&sn=c7d8ed8e7994512325754db1921ceea4&chksm=84f60005b3818913460f7621ef2df62b4fe249bb5cb81aa8e574259cc4c23a684f69bbf33eb0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大汉推办 MzI2ODA5NTg4Nw==
sleep 150
<Response [200]>
近代中国与日本丨《译书汇编》与晚清政治学的“日本渠道”中日人物论坛第五期顺利召开 http://mp.weixin.qq.com/s?__biz=MzI2ODA5NTg4Nw==&mid=2650154371&idx=1&sn=e294fcdba4988ce8c8d61f41b709b4f0&chksm=f2f65d63c581d475df668626bfa36b34d7f19cf4de0bc65596784e3be0ecb0867680681299d3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
兔年吉祥——来自西班牙的祝福 http://mp.weixin.qq.com/s?__biz=MzI2ODA5NTg4Nw==&mid=2650154351&idx=1&sn=b28706b3631a209e38bc744e5be4835e&chksm=f2f65d8fc581d4994ddfd7622341152b914859d4f344f8ef86239e3488af526f61e5e08e06ea#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学孔子学院中外人文论坛第19期暨中日人文论坛第四期顺利举办 http://mp.weixin.qq.com/s?__biz=MzI2ODA5NTg4Nw==&mid=2650154339&idx=1&sn=c5969140aa81e2a5759f99e5de763e92&chksm=f2f65d83c581d4952a7d0e0a4ea35913bf91b078b548a79e7ee56644f7d34c18e4ba5734a4d1#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“中澳环境治理”——庆祝中澳建交五十周年人文交流论坛顺利召开 http://mp.weixin.qq.com/s?__biz=MzI2ODA5NTg4Nw==&mid=2650154308&idx=1&sn=b05342152f2c6d91c289f3a6126c5120&chksm=f2f65da4c581d4b2c2a732652005f54d2eef392db3ac7fbee323fc421bd1d0900d55430cb50e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学孔子学院中外人文论坛第十七期——莎士比亚与汤显祖顺利举办 http://mp.weixin.qq.com/s?__biz=MzI2ODA5NTg4Nw==&mid=2650154292&idx=1&sn=ff128f084aa1222bf89dca0baa0d5450&chksm=f2f65dd4c581d4c24d0ac4c7708b00d76c0cc2a8bb339c5f7e1b65b4ef5755480371a2300538#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京通用人工智能研究院 Mzg2Njc1NjM2OA==
sleep 384
<Response [200]>
2023年度ACM SIGAI China新星奖和优博奖评选正式启动！| 活动推荐 http://mp.weixin.qq.com/s?__biz=Mzg2Njc1NjM2OA==&mid=2247494940&idx=1&sn=2c3488268b1f3d5ff1f1ce8c700b2d94&chksm=ce475f63f930d675237aa8e28a48d291236f538d83403979a822a0231b2ef96c73c855899994#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通用人工智能讲座系列| 针对物理信息系统的安全性、效率和弹性的学习、控制方法 http://mp.weixin.qq.com/s?__biz=Mzg2Njc1NjM2OA==&mid=2247494924&idx=1&sn=5c4b1fcf65fab88214c5cabe64e6fbfd&chksm=ce475f73f930d665e8052799120ae478b33d802fede90016c929f89231b3abdd29fb786cad3d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“为人文赋理，为机器立心” ，朱松纯教授在图灵大会阐释“通用智能·人机共生” http://mp.weixin.qq.com/s?__biz=Mzg2Njc1NjM2OA==&mid=2247494914&idx=1&sn=686fa95dad99026c586d4eca8352c4d7&chksm=ce475f7df930d66bba5d2f4adf2ac8b01322e3780c01b936d1c8ba2936d237632384f93f0e8e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
焦点评论：大模型与通用人工智能 | 图灵大会SIGAI圆桌论坛在汉举行 http://mp.weixin.qq.com/s?__biz=Mzg2Njc1NjM2OA==&mid=2247494869&idx=1&sn=48385b9adb00a923f09fe0591365104c&chksm=ce475eaaf930d7bcef38b6a383c34963a185dbfed2dc3ee4e469e016446e80660ec055e9c339#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通用人工智能讲座系列|专注于社交影响的交互式AI系统 http://mp.weixin.qq.com/s?__biz=Mzg2Njc1NjM2OA==&mid=2247494801&idx=1&sn=e9344f4ef020d0a886d4836d8d45d324&chksm=ce475eeef930d7f8e88dde02a09891dd3f644ac75224dfab4ed5d59334c104b75f7ec0876573#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学学生服务总队 MzU5NjYzNjg0Mw==
sleep 308
<Response [200]>
Traceback (most recent call last):
  File "/home/info/PKUinfo/crawl/getURL.py", line 147, in <module>
    outdata = page(name,fad,1)
  File "/home/info/PKUinfo/crawl/getURL.py", line 27, in page
    for i in dic['app_msg_list']:     #遍历dic['app_msg_list']中所有内容
KeyError: 'app_msg_list'
['北京大学学生服务总队', '北京大学社会学系', '北京大学计算机学院', '北京大学历史学系', '北京大学经济学院', '北京大学数学科学学院', 'pku数学系', 'P大CoE教务', '北京大学中文系', '北大社会学', '北京大学智能学院', '北大国发院', '北京大学公共卫生学院生物统计系', '北京大学光华管理学院', '北京大学对外汉语教育学院', '北京大学物理学院人才培养', '北京大学教育学院', 'SMS_Stu_Union', '北大数院人', 'PKU言之有物', '北大物理人', '北京大学学生会', 'PKU医预之家', '大信科', '北京大学历史学系学生会', '北大数院青年志愿者协会', '数院研究生会', '物院学生会', '北大心理人', 'PKU信科职业发展中心', '光华CDC', '走进光华', '北大史学人', '北京大学教育学院团研', '北大脑科学', '北京大学人文社会科学研究院', '北京国际数学研究中心BICMR', '北京大学语言学实验室', '北京大学文学讲习所', '北京大学前沿计算研究中心', '大数据分析与应用国家工程实验室', '北京大学统计科学中心', '北京大学文化产业研究院', '北大古典语文学', '思想与社会', '北京大学严复班', '北京大学', '北大团委', '北大体育', '北京大学学生发展支持', '北大新青年', 'PKU体委', '北京大学教务部', '北大餐饮中心官方资讯', '燕园学子微助手', '平安燕园', '燕园微后勤', '北京大学招生办', '北京大学百周年纪念讲堂', '北大就业', '北大未名BBS', '北大政治法律与社会项目', 'Paideia_et_Cultura', '北京大学国发院经济双学位', '湘思PKU', '北大辩协', '北大红会', '爱心驿站', 'PKU思潜十周年', '未名超算队', '燕语配音社', 'PKUSAA', '北大猫协', '风雷街舞社FLCrew', '北大粤协', '北大耕读社', '元火动漫社', 'pku心协', 'PKU_CACA', 'PKU烹协', 'PKU创新学社', '北大汉推办', '北京通用人工智能研究院'] ['MzU5NjYzNjg0Mw==', 'MzU5MjczNjU0NQ==', 'MzU2MTEwNjk4Mg==', 'MzI0ODE4MjM5Mw==', 'MzIzMzM2NDA5Nw==', 'MzUzMzg4MzgxMQ==', 'MzkxNTM1MjU5Mw==', 'MzI4OTYxMzkyOA==', 'MzI0ODcwNjkwNw==', 'MzkxMzMxMzQ2NQ==', 'Mzk0NDE3ODg5Nw==', 'MjM5MDIwNDg0MA==', 'MzU5MDg1ODYyMA==', 'MjM5MDk3NDgwMQ==', 'MzA3ODU2MTk4NA==', 'MzUxODk4MDA4NA==', 'MzA4OTA5MjA4MA==', 'MzA5NDAxMDYzMQ==', 'MzU3NzA0OTA5Mg==', 'MzAwMDEwMzI0MQ==', 'MzA5NzUwODgxMw==', 'MzA3MDAxMTIxMQ==', 'MzAxOTAyMjk0MA==', 'MzA4MTAzMzQ5NA==', 'MzA3NDYwMzkxMg==', 'MjM5MDAwNzExMA==', 'MzAwNTA1MjA1OA==', 'MzIwNDEzMDI5OA==', 'MjM5NjQ4ODc1MA==', 'MzI3NTQ2MjM5NA==', 'MzA4MDM0NDcwMg==', 'MzkwMDIzNTgxMg==', 'MzkyODMwMzEwMw==', 'Mzg3MzE5MzQzNA==', 'MzAwNTEzNzcwNg==', 'MzIzNDQ0MDUwNg==', 'MzI1ODQ2MTkwOQ==', 'Mzg3OTg2NTkxMw==', 'Mzg3ODU1OTE2MQ==', 'MzU0MjU5NjQ3NA==', 'MzkyMDE5NTM0NA==', 'Mzg3MTcyNzA1OQ==', 'Mzg4NTE0MDUwNg==', 'MzAwNzc0NzMwMw==', 'Mzg4ODEzNTExNw==', 'MzUyOTkwNTQwNQ==', 'MzA3OTE0MjQzMw==', 'MzIxNjMzMDE1NQ==', 'MzA5MjI1NjIyOA==', 'MzU5OTk0MTE3Mg==', 'MzU3ODg5ODQ3MA==', 'MzAwNDg0MDA4Mw==', 'MzIzNzc4ODkxOA==', 'Mzg4MTIzNzU4OQ==', 'MzA3NzE0MjcyMQ==', 'MzI2OTQ2NDg5Ng==', 'MzUxMzEyNTczNw==', 'MzA4NjEzNDYxMQ==', 'MzU2ODY1ODE1MQ==', 'MzA4NjAzMTIxNw==', 'MzA3OTMwMjc5Mg==', 'Mzg3NjcxNTMzNA==', 'MzkwMzI0MjEyNw==', 'MzA3MzQ5ODIyNA==', 'MzU4NjMyNzM3Nw==', 'MjM5MTg0MDE4NQ==', 'MzA3NzAwNjI5NA==', 'MzA5ODA4ODExMg==', 'Mzg4OTY4NDgxMA==', 'MzUzOTk3NzkxMg==', 'MzAxMzMwNTAxNQ==', 'Mzg4NjExNDUzMg==', 'MjM5NDc5MzgzNg==', 'MzI0NjA0MTUwNA==', 'MzA5MTk4NTgxNg==', 'MzAwNjA3NDQxMQ==', 'MjM5NjY2ODY0OQ==', 'MzA4ODg5NzU4NA==', 'MzA3OTQwMTAwOQ==', 'MzI4MjU0Njc1Ng==', 'MzA3MjMzNTQ1OQ==', 'MzI2ODA5NTg4Nw==', 'Mzg2Njc1NjM2OA==']
北京大学学生服务总队 MzU5NjYzNjg0Mw==
sleep 575
<Response [200]>
dic: {'app_msg_cnt': 565, 'app_msg_list': [{'aid': '2247493340_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2oHEkYsUWqZohDOuKX23fHjTJIX79OPsb9O4IxPiatbhbXgdmNsvCEUiag/0?wx_fmt=png', 'create_time': 1694503567, 'digest': '点击碎纸，看清信件“自把玉钗敲砌竹，清歌一曲月如霜。”清丽婉转的歌声，表达出歌唱者丰富饱满的心绪。“此曲只应', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=1&sn=5a7ee37b463a42e968ade96a7cb3b0a3&chksm=fe5d0318c92a8a0e97edb354f850e62c278fcdfe14a9a709dc1bf259091a55e39949ba307b7f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “燕园起航 艺路同行”系列课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2oVr7SzNE1XxuYngDcQyGsicsOHEibBJTWt9BmNluSoj9YxomtrHE1q0BA/0?wx_fmt=jpeg', 'create_time': 1694503567, 'digest': '前言： “远看山有色，近听水无声”赞美了中国画的生动传神！“垂露春光满，崩云骨气馀”展现了书法的丰筋多力!', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=2&sn=32f6f0dcb0ae5af82581090f73b924e7&chksm=fe5d0318c92a8a0e07d383d4fd61f7d416df9efff2d7e2e3b33757a1b30478e9dadd07562652#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “燕园起航 笔墨生辉” 书画类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2orR4icE9aRzvWevtS8xNwkUwBM94EBYEdEm1yzeJzuYs4ktOcOqbH18w/0?wx_fmt=png', 'create_time': 1694503567, 'digest': 'NEW TERM活动报名&nbsp;体育类兴趣课程报名启动前言：盼望着，盼望着体育类兴趣课程终于发车啦！快来', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=3&sn=2498c901ec65aa2ea689fb59e0cfb248&chksm=fe5d0318c92a8a0e3f87d4b4b3f456795f945c45cbffde362f354112450999d409a18d6e405e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “韵动燕园 青春起航”体育类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2ohQppeUV1UsXCLYqkGUd7x0jbwn0sRGD1rTXViayvqFxGibKIjib81nx4A/0?wx_fmt=png', 'create_time': 1694503567, 'digest': '前言：以乐会友，以舞传情舞步翩跹，弦音悠悠你是否希望拥有拓展兴趣，展示才华的舞台文艺兴趣小组的大门向你敞开！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=4&sn=04b593d715a80c025fd6b62c186fd245&chksm=fe5d0318c92a8a0e51d824c2a883bf15c037980bde1d5716bba2408b3205e4549fd60aa97f84#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “以乐会友 以舞传情”文艺类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493224_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQYEIOTz4M8yeJmbbxORG13iaDOSA7jw3rSFgGFLLzZfPYJZgn7P0HsXlxV0o2hycf0F9451gInn7Q/0?wx_fmt=jpeg', 'create_time': 1694427957, 'digest': '燕语殷时活动志愿者招募开始啦！快来收获跨越几百公里的友谊吧~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=1&sn=091295a163075b2d4ed9e2a33efcf515&chksm=fe5d03acc92a8aba1259ceb82846f63ed4b2228baa7963367151d975370555fd2cb495e9e741#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名｜燕语殷时活动志愿者招募开始啦', 'update_time': 1694428200}, {'aid': '2247493224_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwSovCNDmxao39yshtB0Ul9qJHdIiaD8C1roQCuwvtQI5o62LhF9oxg1pt9mPusSUd3EdXicBCA2cUhg/0?wx_fmt=png', 'create_time': 1694427957, 'digest': '一起将书籍流转起来吧！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=2&sn=0aa59e5f9568a925ba3b3c1ead0c5914&chksm=fe5d03acc92a8aba2b996fcf883f3da2fa086849145292f2bb26fccccfa2f61b0dc819c1a8c3#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '图书漂流 | 欢迎参加图书漂流——收书活动！', 'update_time': 1694428200}, {'aid': '2247493224_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQYEIOTz4M8yeJmbbxORG13HLDg6mgsZI5ISj5HfPRvXgtUOv0stWtNDVT8AUPRr26LbibicQiamjicXA/0?wx_fmt=jpeg', 'create_time': 1694427957, 'digest': '2023燕园起航第九组见面会成功举办！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=3&sn=907b5c8612583ecb42cc5197a46dfe5a&chksm=fe5d03acc92a8ababee3583b6013683460fa6239de0d4357889d83bab64d812fc28e50c5d8c7#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '起航快讯 | 满“新”欢喜，如约而至：23级燕园起航第9组成功举办破冰活动', 'update_time': 1694428200}, {'aid': '2247493193_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pwmnmfcibjt9vPggrjliaPmJSdHToYDT1by5IiaQh7AogibLYDf0icXB2fIQ/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '中央文明办三局、中国社会工作联合会共同开展2023年“圆梦工程”农村未成年人心理健康教育志愿服务项目大学生', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=1&sn=4d164e76ca0c91a6d146bbc627e7941a&chksm=fe5d038dc92a8a9be165469479dc58a0c52423ef92955808490f75fef7f11675563403c0ae35#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '2023年北京大学“弥渡心理”实践团赴大理自治州实践总结', 'update_time': 1694061000}, {'aid': '2247493193_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pd40UpbdIic0vBKhibibTGPtfg7lZG3FvJjLEWcfuwtZMPtGkMKDyDGZpw/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '2023年北京大学“弥渡心理”实践队赴大理自治州实践纪实①', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=2&sn=a1fe1edff08adb2bc0f4eff373ea70b3&chksm=fe5d038dc92a8a9b03dffb313e737d0eb2f3e00e454e1a965453860de43fe935f0a93c898f75#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '苍山宜洗马 名邦亦峥嵘——2023年圆梦计划“弥渡心理”18日简报', 'update_time': 1694061000}, {'aid': '2247493193_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pLyDWz9TEUYuQGa4ZRMRCWo5dBwIDFt9OibzkyiaR9TvGrrrKicPr1cxzw/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '2023年北京大学“弥渡心理”实践队赴大理自治州实践纪实②', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=3&sn=99cb159ae6d5943d8f4b93b2d03e30f1&chksm=fe5d038dc92a8a9b0fc2f543dc7975fa7bf32ab2d42e91c8d4582718f97aa3c8337f9127400e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '喜洲绽金花 古镇溯红色——2023年圆梦计划“弥渡心理”19日简报', 'update_time': 1694061000}, {'aid': '2247493193_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1px6ZxUxGjSMlmbmOZ0IX61XJLK5vaPKmxickCkibaicsxAYvs72ticiaKz3A/0?wx_fmt=jpeg', 'create_time': 1694060423, 'digest': '唤醒红色记忆，传承革命精神。2023年8月20日，北京大学“弥渡心理”志愿队踏上云南省大理市的土地，赶赴大理博物馆重走红色路线。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=4&sn=04b7931dd41936fb4b5c6b46cf5ef2dd&chksm=fe5d038dc92a8a9b8fc898b64a4e908a09eec97309d9f2b2d44b9daeb17898c232de2f048162#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '南诏存史韵 丹心报家国——2023年圆梦计划“弥渡心理”20日简报', 'update_time': 1694061000}, {'aid': '2247493146_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493146, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwSbbrTIky5xJDsjfLW2ibMTNj4l8LgPuPl01icRR17Ppz0ibz52RG4kh0KN64aQ1LLUrJVJpibgJT9ricA/0?wx_fmt=jpeg', 'create_time': 1693976163, 'digest': '2023研究生迎新活动顺利举行', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493146&idx=1&sn=0ce1429518aaa358af768ef93d59ba26&chksm=fe5d03dec92a8ac80ef681c639bb6ff7ebf1e65956d7388c4edbd874099ff0cc5c4fb4ce1630#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '志愿接力进行时：当我穿上蓝马甲……', 'update_time': 1693976162}, {'aid': '2247493073_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493073, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwSmxnbFeoxbdtAaibnXyART0B8sYIVvsXPZByffQxEXHd3JiaxdTPGvobtpwp2H54vO1jYiaAQlK572A/0?wx_fmt=jpeg', 'create_time': 1693824053, 'digest': '“燕语殷时”活动志愿者招募开始啦！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493073&idx=1&sn=dc78b1b5f3cecc30f6cb50eb2a897d3e&chksm=fe5d0015c92a8903d2bf450f38660c3cf0856985f4ed97b47ed3af6639700a2730224f953e21#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名｜“燕语殷时”活动志愿者招募开始啦', 'update_time': 1693824052}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
活动报名 | “燕园起航 艺路同行”系列课程报名启动！ http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=1&sn=5a7ee37b463a42e968ade96a7cb3b0a3&chksm=fe5d0318c92a8a0e97edb354f850e62c278fcdfe14a9a709dc1bf259091a55e39949ba307b7f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动报名 | “燕园起航 笔墨生辉” 书画类兴趣课程报名启动！ http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=2&sn=32f6f0dcb0ae5af82581090f73b924e7&chksm=fe5d0318c92a8a0e07d383d4fd61f7d416df9efff2d7e2e3b33757a1b30478e9dadd07562652#rd
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 445, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 440, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.10/http/client.py", line 1375, in getresponse
    response.begin()
  File "/usr/lib/python3.10/http/client.py", line 318, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.10/http/client.py", line 287, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
http.client.RemoteDisconnected: Remote end closed connection without response

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 755, in urlopen
    retries = retries.increment(
  File "/usr/lib/python3/dist-packages/urllib3/util/retry.py", line 532, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/usr/lib/python3/dist-packages/six.py", line 718, in reraise
    raise value.with_traceback(tb)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 445, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 440, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.10/http/client.py", line 1375, in getresponse
    response.begin()
  File "/usr/lib/python3.10/http/client.py", line 318, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.10/http/client.py", line 287, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/info/PKUinfo/crawl/getURL.py", line 156, in <module>
    POSTER(link)
  File "/home/info/PKUinfo/crawl/getURL.py", line 140, in POSTER
    r = requests.post(url, data=json.dumps(data), headers=headers)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 119, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 544, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 657, in send
    r = adapter.send(request, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 498, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
['北京大学学生服务总队', '北京大学社会学系', '北京大学计算机学院', '北京大学历史学系', '北京大学经济学院', '北京大学数学科学学院', 'pku数学系', 'P大CoE教务', '北京大学中文系', '北大社会学', '北京大学智能学院', '北大国发院', '北京大学公共卫生学院生物统计系', '北京大学光华管理学院', '北京大学对外汉语教育学院', '北京大学物理学院人才培养', '北京大学教育学院', 'SMS_Stu_Union', '北大数院人', 'PKU言之有物', '北大物理人', '北京大学学生会', 'PKU医预之家', '大信科', '北京大学历史学系学生会', '北大数院青年志愿者协会', '数院研究生会', '物院学生会', '北大心理人', 'PKU信科职业发展中心', '光华CDC', '走进光华', '北大史学人', '北京大学教育学院团研', '北大脑科学', '北京大学人文社会科学研究院', '北京国际数学研究中心BICMR', '北京大学语言学实验室', '北京大学文学讲习所', '北京大学前沿计算研究中心', '大数据分析与应用国家工程实验室', '北京大学统计科学中心', '北京大学文化产业研究院', '北大古典语文学', '思想与社会', '北京大学严复班', '北京大学', '北大团委', '北大体育', '北京大学学生发展支持', '北大新青年', 'PKU体委', '北京大学教务部', '北大餐饮中心官方资讯', '燕园学子微助手', '平安燕园', '燕园微后勤', '北京大学招生办', '北京大学百周年纪念讲堂', '北大就业', '北大未名BBS', '北大政治法律与社会项目', 'Paideia_et_Cultura', '北京大学国发院经济双学位', '湘思PKU', '北大辩协', '北大红会', '爱心驿站', 'PKU思潜十周年', '未名超算队', '燕语配音社', 'PKUSAA', '北大猫协', '风雷街舞社FLCrew', '北大粤协', '北大耕读社', '元火动漫社', 'pku心协', 'PKU_CACA', 'PKU烹协', 'PKU创新学社', '北大汉推办', '北京通用人工智能研究院'] ['MzU5NjYzNjg0Mw==', 'MzU5MjczNjU0NQ==', 'MzU2MTEwNjk4Mg==', 'MzI0ODE4MjM5Mw==', 'MzIzMzM2NDA5Nw==', 'MzUzMzg4MzgxMQ==', 'MzkxNTM1MjU5Mw==', 'MzI4OTYxMzkyOA==', 'MzI0ODcwNjkwNw==', 'MzkxMzMxMzQ2NQ==', 'Mzk0NDE3ODg5Nw==', 'MjM5MDIwNDg0MA==', 'MzU5MDg1ODYyMA==', 'MjM5MDk3NDgwMQ==', 'MzA3ODU2MTk4NA==', 'MzUxODk4MDA4NA==', 'MzA4OTA5MjA4MA==', 'MzA5NDAxMDYzMQ==', 'MzU3NzA0OTA5Mg==', 'MzAwMDEwMzI0MQ==', 'MzA5NzUwODgxMw==', 'MzA3MDAxMTIxMQ==', 'MzAxOTAyMjk0MA==', 'MzA4MTAzMzQ5NA==', 'MzA3NDYwMzkxMg==', 'MjM5MDAwNzExMA==', 'MzAwNTA1MjA1OA==', 'MzIwNDEzMDI5OA==', 'MjM5NjQ4ODc1MA==', 'MzI3NTQ2MjM5NA==', 'MzA4MDM0NDcwMg==', 'MzkwMDIzNTgxMg==', 'MzkyODMwMzEwMw==', 'Mzg3MzE5MzQzNA==', 'MzAwNTEzNzcwNg==', 'MzIzNDQ0MDUwNg==', 'MzI1ODQ2MTkwOQ==', 'Mzg3OTg2NTkxMw==', 'Mzg3ODU1OTE2MQ==', 'MzU0MjU5NjQ3NA==', 'MzkyMDE5NTM0NA==', 'Mzg3MTcyNzA1OQ==', 'Mzg4NTE0MDUwNg==', 'MzAwNzc0NzMwMw==', 'Mzg4ODEzNTExNw==', 'MzUyOTkwNTQwNQ==', 'MzA3OTE0MjQzMw==', 'MzIxNjMzMDE1NQ==', 'MzA5MjI1NjIyOA==', 'MzU5OTk0MTE3Mg==', 'MzU3ODg5ODQ3MA==', 'MzAwNDg0MDA4Mw==', 'MzIzNzc4ODkxOA==', 'Mzg4MTIzNzU4OQ==', 'MzA3NzE0MjcyMQ==', 'MzI2OTQ2NDg5Ng==', 'MzUxMzEyNTczNw==', 'MzA4NjEzNDYxMQ==', 'MzU2ODY1ODE1MQ==', 'MzA4NjAzMTIxNw==', 'MzA3OTMwMjc5Mg==', 'Mzg3NjcxNTMzNA==', 'MzkwMzI0MjEyNw==', 'MzA3MzQ5ODIyNA==', 'MzU4NjMyNzM3Nw==', 'MjM5MTg0MDE4NQ==', 'MzA3NzAwNjI5NA==', 'MzA5ODA4ODExMg==', 'Mzg4OTY4NDgxMA==', 'MzUzOTk3NzkxMg==', 'MzAxMzMwNTAxNQ==', 'Mzg4NjExNDUzMg==', 'MjM5NDc5MzgzNg==', 'MzI0NjA0MTUwNA==', 'MzA5MTk4NTgxNg==', 'MzAwNjA3NDQxMQ==', 'MjM5NjY2ODY0OQ==', 'MzA4ODg5NzU4NA==', 'MzA3OTQwMTAwOQ==', 'MzI4MjU0Njc1Ng==', 'MzA3MjMzNTQ1OQ==', 'MzI2ODA5NTg4Nw==', 'Mzg2Njc1NjM2OA==']
北京大学学生服务总队 MzU5NjYzNjg0Mw==
sleep 181
<Response [200]>
dic: {'app_msg_cnt': 565, 'app_msg_list': [{'aid': '2247493340_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2oHEkYsUWqZohDOuKX23fHjTJIX79OPsb9O4IxPiatbhbXgdmNsvCEUiag/0?wx_fmt=png', 'create_time': 1694503567, 'digest': '点击碎纸，看清信件“自把玉钗敲砌竹，清歌一曲月如霜。”清丽婉转的歌声，表达出歌唱者丰富饱满的心绪。“此曲只应', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=1&sn=5a7ee37b463a42e968ade96a7cb3b0a3&chksm=fe5d0318c92a8a0e97edb354f850e62c278fcdfe14a9a709dc1bf259091a55e39949ba307b7f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “燕园起航 艺路同行”系列课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2oVr7SzNE1XxuYngDcQyGsicsOHEibBJTWt9BmNluSoj9YxomtrHE1q0BA/0?wx_fmt=jpeg', 'create_time': 1694503567, 'digest': '前言： “远看山有色，近听水无声”赞美了中国画的生动传神！“垂露春光满，崩云骨气馀”展现了书法的丰筋多力!', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=2&sn=32f6f0dcb0ae5af82581090f73b924e7&chksm=fe5d0318c92a8a0e07d383d4fd61f7d416df9efff2d7e2e3b33757a1b30478e9dadd07562652#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “燕园起航 笔墨生辉” 书画类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2orR4icE9aRzvWevtS8xNwkUwBM94EBYEdEm1yzeJzuYs4ktOcOqbH18w/0?wx_fmt=png', 'create_time': 1694503567, 'digest': 'NEW TERM活动报名&nbsp;体育类兴趣课程报名启动前言：盼望着，盼望着体育类兴趣课程终于发车啦！快来', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=3&sn=2498c901ec65aa2ea689fb59e0cfb248&chksm=fe5d0318c92a8a0e3f87d4b4b3f456795f945c45cbffde362f354112450999d409a18d6e405e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “韵动燕园 青春起航”体育类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2ohQppeUV1UsXCLYqkGUd7x0jbwn0sRGD1rTXViayvqFxGibKIjib81nx4A/0?wx_fmt=png', 'create_time': 1694503567, 'digest': '前言：以乐会友，以舞传情舞步翩跹，弦音悠悠你是否希望拥有拓展兴趣，展示才华的舞台文艺兴趣小组的大门向你敞开！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=4&sn=04b593d715a80c025fd6b62c186fd245&chksm=fe5d0318c92a8a0e51d824c2a883bf15c037980bde1d5716bba2408b3205e4549fd60aa97f84#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “以乐会友 以舞传情”文艺类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493224_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQYEIOTz4M8yeJmbbxORG13iaDOSA7jw3rSFgGFLLzZfPYJZgn7P0HsXlxV0o2hycf0F9451gInn7Q/0?wx_fmt=jpeg', 'create_time': 1694427957, 'digest': '燕语殷时活动志愿者招募开始啦！快来收获跨越几百公里的友谊吧~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=1&sn=091295a163075b2d4ed9e2a33efcf515&chksm=fe5d03acc92a8aba1259ceb82846f63ed4b2228baa7963367151d975370555fd2cb495e9e741#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名｜燕语殷时活动志愿者招募开始啦', 'update_time': 1694428200}, {'aid': '2247493224_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwSovCNDmxao39yshtB0Ul9qJHdIiaD8C1roQCuwvtQI5o62LhF9oxg1pt9mPusSUd3EdXicBCA2cUhg/0?wx_fmt=png', 'create_time': 1694427957, 'digest': '一起将书籍流转起来吧！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=2&sn=0aa59e5f9568a925ba3b3c1ead0c5914&chksm=fe5d03acc92a8aba2b996fcf883f3da2fa086849145292f2bb26fccccfa2f61b0dc819c1a8c3#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '图书漂流 | 欢迎参加图书漂流——收书活动！', 'update_time': 1694428200}, {'aid': '2247493224_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQYEIOTz4M8yeJmbbxORG13HLDg6mgsZI5ISj5HfPRvXgtUOv0stWtNDVT8AUPRr26LbibicQiamjicXA/0?wx_fmt=jpeg', 'create_time': 1694427957, 'digest': '2023燕园起航第九组见面会成功举办！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=3&sn=907b5c8612583ecb42cc5197a46dfe5a&chksm=fe5d03acc92a8ababee3583b6013683460fa6239de0d4357889d83bab64d812fc28e50c5d8c7#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '起航快讯 | 满“新”欢喜，如约而至：23级燕园起航第9组成功举办破冰活动', 'update_time': 1694428200}, {'aid': '2247493193_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pwmnmfcibjt9vPggrjliaPmJSdHToYDT1by5IiaQh7AogibLYDf0icXB2fIQ/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '中央文明办三局、中国社会工作联合会共同开展2023年“圆梦工程”农村未成年人心理健康教育志愿服务项目大学生', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=1&sn=4d164e76ca0c91a6d146bbc627e7941a&chksm=fe5d038dc92a8a9be165469479dc58a0c52423ef92955808490f75fef7f11675563403c0ae35#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '2023年北京大学“弥渡心理”实践团赴大理自治州实践总结', 'update_time': 1694061000}, {'aid': '2247493193_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pd40UpbdIic0vBKhibibTGPtfg7lZG3FvJjLEWcfuwtZMPtGkMKDyDGZpw/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '2023年北京大学“弥渡心理”实践队赴大理自治州实践纪实①', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=2&sn=a1fe1edff08adb2bc0f4eff373ea70b3&chksm=fe5d038dc92a8a9b03dffb313e737d0eb2f3e00e454e1a965453860de43fe935f0a93c898f75#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '苍山宜洗马 名邦亦峥嵘——2023年圆梦计划“弥渡心理”18日简报', 'update_time': 1694061000}, {'aid': '2247493193_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pLyDWz9TEUYuQGa4ZRMRCWo5dBwIDFt9OibzkyiaR9TvGrrrKicPr1cxzw/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '2023年北京大学“弥渡心理”实践队赴大理自治州实践纪实②', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=3&sn=99cb159ae6d5943d8f4b93b2d03e30f1&chksm=fe5d038dc92a8a9b0fc2f543dc7975fa7bf32ab2d42e91c8d4582718f97aa3c8337f9127400e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '喜洲绽金花 古镇溯红色——2023年圆梦计划“弥渡心理”19日简报', 'update_time': 1694061000}, {'aid': '2247493193_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1px6ZxUxGjSMlmbmOZ0IX61XJLK5vaPKmxickCkibaicsxAYvs72ticiaKz3A/0?wx_fmt=jpeg', 'create_time': 1694060423, 'digest': '唤醒红色记忆，传承革命精神。2023年8月20日，北京大学“弥渡心理”志愿队踏上云南省大理市的土地，赶赴大理博物馆重走红色路线。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=4&sn=04b7931dd41936fb4b5c6b46cf5ef2dd&chksm=fe5d038dc92a8a9b8fc898b64a4e908a09eec97309d9f2b2d44b9daeb17898c232de2f048162#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '南诏存史韵 丹心报家国——2023年圆梦计划“弥渡心理”20日简报', 'update_time': 1694061000}, {'aid': '2247493146_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493146, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwSbbrTIky5xJDsjfLW2ibMTNj4l8LgPuPl01icRR17Ppz0ibz52RG4kh0KN64aQ1LLUrJVJpibgJT9ricA/0?wx_fmt=jpeg', 'create_time': 1693976163, 'digest': '2023研究生迎新活动顺利举行', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493146&idx=1&sn=0ce1429518aaa358af768ef93d59ba26&chksm=fe5d03dec92a8ac80ef681c639bb6ff7ebf1e65956d7388c4edbd874099ff0cc5c4fb4ce1630#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '志愿接力进行时：当我穿上蓝马甲……', 'update_time': 1693976162}, {'aid': '2247493073_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493073, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwSmxnbFeoxbdtAaibnXyART0B8sYIVvsXPZByffQxEXHd3JiaxdTPGvobtpwp2H54vO1jYiaAQlK572A/0?wx_fmt=jpeg', 'create_time': 1693824053, 'digest': '“燕语殷时”活动志愿者招募开始啦！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493073&idx=1&sn=dc78b1b5f3cecc30f6cb50eb2a897d3e&chksm=fe5d0015c92a8903d2bf450f38660c3cf0856985f4ed97b47ed3af6639700a2730224f953e21#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名｜“燕语殷时”活动志愿者招募开始啦', 'update_time': 1693824052}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
活动报名 | “燕园起航 艺路同行”系列课程报名启动！ http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=1&sn=5a7ee37b463a42e968ade96a7cb3b0a3&chksm=fe5d0318c92a8a0e97edb354f850e62c278fcdfe14a9a709dc1bf259091a55e39949ba307b7f#rd
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 445, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 440, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.10/http/client.py", line 1375, in getresponse
    response.begin()
  File "/usr/lib/python3.10/http/client.py", line 318, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.10/http/client.py", line 287, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
http.client.RemoteDisconnected: Remote end closed connection without response

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 755, in urlopen
    retries = retries.increment(
  File "/usr/lib/python3/dist-packages/urllib3/util/retry.py", line 532, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/usr/lib/python3/dist-packages/six.py", line 718, in reraise
    raise value.with_traceback(tb)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 445, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 440, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.10/http/client.py", line 1375, in getresponse
    response.begin()
  File "/usr/lib/python3.10/http/client.py", line 318, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.10/http/client.py", line 287, in _read_status
    raise RemoteDisconnected("Remote end closed connection without"
urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/info/PKUinfo/crawl/getURL.py", line 156, in <module>
    POSTER(link)
  File "/home/info/PKUinfo/crawl/getURL.py", line 140, in POSTER
    r = requests.post(url, data=json.dumps(data), headers=headers)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 119, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 544, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 657, in send
    r = adapter.send(request, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 498, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
['北京大学学生服务总队', '北京大学社会学系', '北京大学计算机学院', '北京大学历史学系', '北京大学经济学院', '北京大学数学科学学院', 'pku数学系', 'P大CoE教务', '北京大学中文系', '北大社会学', '北京大学智能学院', '北大国发院', '北京大学公共卫生学院生物统计系', '北京大学光华管理学院', '北京大学对外汉语教育学院', '北京大学物理学院人才培养', '北京大学教育学院', 'SMS_Stu_Union', '北大数院人', 'PKU言之有物', '北大物理人', '北京大学学生会', 'PKU医预之家', '大信科', '北京大学历史学系学生会', '北大数院青年志愿者协会', '数院研究生会', '物院学生会', '北大心理人', 'PKU信科职业发展中心', '光华CDC', '走进光华', '北大史学人', '北京大学教育学院团研', '北大脑科学', '北京大学人文社会科学研究院', '北京国际数学研究中心BICMR', '北京大学语言学实验室', '北京大学文学讲习所', '北京大学前沿计算研究中心', '大数据分析与应用国家工程实验室', '北京大学统计科学中心', '北京大学文化产业研究院', '北大古典语文学', '思想与社会', '北京大学严复班', '北京大学', '北大团委', '北大体育', '北京大学学生发展支持', '北大新青年', 'PKU体委', '北京大学教务部', '北大餐饮中心官方资讯', '燕园学子微助手', '平安燕园', '燕园微后勤', '北京大学招生办', '北京大学百周年纪念讲堂', '北大就业', '北大未名BBS', '北大政治法律与社会项目', 'Paideia_et_Cultura', '北京大学国发院经济双学位', '湘思PKU', '北大辩协', '北大红会', '爱心驿站', 'PKU思潜十周年', '未名超算队', '燕语配音社', 'PKUSAA', '北大猫协', '风雷街舞社FLCrew', '北大粤协', '北大耕读社', '元火动漫社', 'pku心协', 'PKU_CACA', 'PKU烹协', 'PKU创新学社', '北大汉推办', '北京通用人工智能研究院'] ['MzU5NjYzNjg0Mw==', 'MzU5MjczNjU0NQ==', 'MzU2MTEwNjk4Mg==', 'MzI0ODE4MjM5Mw==', 'MzIzMzM2NDA5Nw==', 'MzUzMzg4MzgxMQ==', 'MzkxNTM1MjU5Mw==', 'MzI4OTYxMzkyOA==', 'MzI0ODcwNjkwNw==', 'MzkxMzMxMzQ2NQ==', 'Mzk0NDE3ODg5Nw==', 'MjM5MDIwNDg0MA==', 'MzU5MDg1ODYyMA==', 'MjM5MDk3NDgwMQ==', 'MzA3ODU2MTk4NA==', 'MzUxODk4MDA4NA==', 'MzA4OTA5MjA4MA==', 'MzA5NDAxMDYzMQ==', 'MzU3NzA0OTA5Mg==', 'MzAwMDEwMzI0MQ==', 'MzA5NzUwODgxMw==', 'MzA3MDAxMTIxMQ==', 'MzAxOTAyMjk0MA==', 'MzA4MTAzMzQ5NA==', 'MzA3NDYwMzkxMg==', 'MjM5MDAwNzExMA==', 'MzAwNTA1MjA1OA==', 'MzIwNDEzMDI5OA==', 'MjM5NjQ4ODc1MA==', 'MzI3NTQ2MjM5NA==', 'MzA4MDM0NDcwMg==', 'MzkwMDIzNTgxMg==', 'MzkyODMwMzEwMw==', 'Mzg3MzE5MzQzNA==', 'MzAwNTEzNzcwNg==', 'MzIzNDQ0MDUwNg==', 'MzI1ODQ2MTkwOQ==', 'Mzg3OTg2NTkxMw==', 'Mzg3ODU1OTE2MQ==', 'MzU0MjU5NjQ3NA==', 'MzkyMDE5NTM0NA==', 'Mzg3MTcyNzA1OQ==', 'Mzg4NTE0MDUwNg==', 'MzAwNzc0NzMwMw==', 'Mzg4ODEzNTExNw==', 'MzUyOTkwNTQwNQ==', 'MzA3OTE0MjQzMw==', 'MzIxNjMzMDE1NQ==', 'MzA5MjI1NjIyOA==', 'MzU5OTk0MTE3Mg==', 'MzU3ODg5ODQ3MA==', 'MzAwNDg0MDA4Mw==', 'MzIzNzc4ODkxOA==', 'Mzg4MTIzNzU4OQ==', 'MzA3NzE0MjcyMQ==', 'MzI2OTQ2NDg5Ng==', 'MzUxMzEyNTczNw==', 'MzA4NjEzNDYxMQ==', 'MzU2ODY1ODE1MQ==', 'MzA4NjAzMTIxNw==', 'MzA3OTMwMjc5Mg==', 'Mzg3NjcxNTMzNA==', 'MzkwMzI0MjEyNw==', 'MzA3MzQ5ODIyNA==', 'MzU4NjMyNzM3Nw==', 'MjM5MTg0MDE4NQ==', 'MzA3NzAwNjI5NA==', 'MzA5ODA4ODExMg==', 'Mzg4OTY4NDgxMA==', 'MzUzOTk3NzkxMg==', 'MzAxMzMwNTAxNQ==', 'Mzg4NjExNDUzMg==', 'MjM5NDc5MzgzNg==', 'MzI0NjA0MTUwNA==', 'MzA5MTk4NTgxNg==', 'MzAwNjA3NDQxMQ==', 'MjM5NjY2ODY0OQ==', 'MzA4ODg5NzU4NA==', 'MzA3OTQwMTAwOQ==', 'MzI4MjU0Njc1Ng==', 'MzA3MjMzNTQ1OQ==', 'MzI2ODA5NTg4Nw==', 'Mzg2Njc1NjM2OA==']
北京大学学生服务总队 MzU5NjYzNjg0Mw==
sleep 129
<Response [200]>
dic: {'app_msg_cnt': 565, 'app_msg_list': [{'aid': '2247493340_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2oHEkYsUWqZohDOuKX23fHjTJIX79OPsb9O4IxPiatbhbXgdmNsvCEUiag/0?wx_fmt=png', 'create_time': 1694503567, 'digest': '点击碎纸，看清信件“自把玉钗敲砌竹，清歌一曲月如霜。”清丽婉转的歌声，表达出歌唱者丰富饱满的心绪。“此曲只应', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=1&sn=5a7ee37b463a42e968ade96a7cb3b0a3&chksm=fe5d0318c92a8a0e97edb354f850e62c278fcdfe14a9a709dc1bf259091a55e39949ba307b7f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “燕园起航 艺路同行”系列课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2oVr7SzNE1XxuYngDcQyGsicsOHEibBJTWt9BmNluSoj9YxomtrHE1q0BA/0?wx_fmt=jpeg', 'create_time': 1694503567, 'digest': '前言： “远看山有色，近听水无声”赞美了中国画的生动传神！“垂露春光满，崩云骨气馀”展现了书法的丰筋多力!', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=2&sn=32f6f0dcb0ae5af82581090f73b924e7&chksm=fe5d0318c92a8a0e07d383d4fd61f7d416df9efff2d7e2e3b33757a1b30478e9dadd07562652#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “燕园起航 笔墨生辉” 书画类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2orR4icE9aRzvWevtS8xNwkUwBM94EBYEdEm1yzeJzuYs4ktOcOqbH18w/0?wx_fmt=png', 'create_time': 1694503567, 'digest': 'NEW TERM活动报名&nbsp;体育类兴趣课程报名启动前言：盼望着，盼望着体育类兴趣课程终于发车啦！快来', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=3&sn=2498c901ec65aa2ea689fb59e0cfb248&chksm=fe5d0318c92a8a0e3f87d4b4b3f456795f945c45cbffde362f354112450999d409a18d6e405e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “韵动燕园 青春起航”体育类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2ohQppeUV1UsXCLYqkGUd7x0jbwn0sRGD1rTXViayvqFxGibKIjib81nx4A/0?wx_fmt=png', 'create_time': 1694503567, 'digest': '前言：以乐会友，以舞传情舞步翩跹，弦音悠悠你是否希望拥有拓展兴趣，展示才华的舞台文艺兴趣小组的大门向你敞开！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=4&sn=04b593d715a80c025fd6b62c186fd245&chksm=fe5d0318c92a8a0e51d824c2a883bf15c037980bde1d5716bba2408b3205e4549fd60aa97f84#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “以乐会友 以舞传情”文艺类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493224_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQYEIOTz4M8yeJmbbxORG13iaDOSA7jw3rSFgGFLLzZfPYJZgn7P0HsXlxV0o2hycf0F9451gInn7Q/0?wx_fmt=jpeg', 'create_time': 1694427957, 'digest': '燕语殷时活动志愿者招募开始啦！快来收获跨越几百公里的友谊吧~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=1&sn=091295a163075b2d4ed9e2a33efcf515&chksm=fe5d03acc92a8aba1259ceb82846f63ed4b2228baa7963367151d975370555fd2cb495e9e741#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名｜燕语殷时活动志愿者招募开始啦', 'update_time': 1694428200}, {'aid': '2247493224_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwSovCNDmxao39yshtB0Ul9qJHdIiaD8C1roQCuwvtQI5o62LhF9oxg1pt9mPusSUd3EdXicBCA2cUhg/0?wx_fmt=png', 'create_time': 1694427957, 'digest': '一起将书籍流转起来吧！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=2&sn=0aa59e5f9568a925ba3b3c1ead0c5914&chksm=fe5d03acc92a8aba2b996fcf883f3da2fa086849145292f2bb26fccccfa2f61b0dc819c1a8c3#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '图书漂流 | 欢迎参加图书漂流——收书活动！', 'update_time': 1694428200}, {'aid': '2247493224_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQYEIOTz4M8yeJmbbxORG13HLDg6mgsZI5ISj5HfPRvXgtUOv0stWtNDVT8AUPRr26LbibicQiamjicXA/0?wx_fmt=jpeg', 'create_time': 1694427957, 'digest': '2023燕园起航第九组见面会成功举办！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=3&sn=907b5c8612583ecb42cc5197a46dfe5a&chksm=fe5d03acc92a8ababee3583b6013683460fa6239de0d4357889d83bab64d812fc28e50c5d8c7#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '起航快讯 | 满“新”欢喜，如约而至：23级燕园起航第9组成功举办破冰活动', 'update_time': 1694428200}, {'aid': '2247493193_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pwmnmfcibjt9vPggrjliaPmJSdHToYDT1by5IiaQh7AogibLYDf0icXB2fIQ/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '中央文明办三局、中国社会工作联合会共同开展2023年“圆梦工程”农村未成年人心理健康教育志愿服务项目大学生', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=1&sn=4d164e76ca0c91a6d146bbc627e7941a&chksm=fe5d038dc92a8a9be165469479dc58a0c52423ef92955808490f75fef7f11675563403c0ae35#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '2023年北京大学“弥渡心理”实践团赴大理自治州实践总结', 'update_time': 1694061000}, {'aid': '2247493193_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pd40UpbdIic0vBKhibibTGPtfg7lZG3FvJjLEWcfuwtZMPtGkMKDyDGZpw/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '2023年北京大学“弥渡心理”实践队赴大理自治州实践纪实①', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=2&sn=a1fe1edff08adb2bc0f4eff373ea70b3&chksm=fe5d038dc92a8a9b03dffb313e737d0eb2f3e00e454e1a965453860de43fe935f0a93c898f75#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '苍山宜洗马 名邦亦峥嵘——2023年圆梦计划“弥渡心理”18日简报', 'update_time': 1694061000}, {'aid': '2247493193_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pLyDWz9TEUYuQGa4ZRMRCWo5dBwIDFt9OibzkyiaR9TvGrrrKicPr1cxzw/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '2023年北京大学“弥渡心理”实践队赴大理自治州实践纪实②', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=3&sn=99cb159ae6d5943d8f4b93b2d03e30f1&chksm=fe5d038dc92a8a9b0fc2f543dc7975fa7bf32ab2d42e91c8d4582718f97aa3c8337f9127400e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '喜洲绽金花 古镇溯红色——2023年圆梦计划“弥渡心理”19日简报', 'update_time': 1694061000}, {'aid': '2247493193_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1px6ZxUxGjSMlmbmOZ0IX61XJLK5vaPKmxickCkibaicsxAYvs72ticiaKz3A/0?wx_fmt=jpeg', 'create_time': 1694060423, 'digest': '唤醒红色记忆，传承革命精神。2023年8月20日，北京大学“弥渡心理”志愿队踏上云南省大理市的土地，赶赴大理博物馆重走红色路线。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=4&sn=04b7931dd41936fb4b5c6b46cf5ef2dd&chksm=fe5d038dc92a8a9b8fc898b64a4e908a09eec97309d9f2b2d44b9daeb17898c232de2f048162#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '南诏存史韵 丹心报家国——2023年圆梦计划“弥渡心理”20日简报', 'update_time': 1694061000}, {'aid': '2247493146_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493146, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwSbbrTIky5xJDsjfLW2ibMTNj4l8LgPuPl01icRR17Ppz0ibz52RG4kh0KN64aQ1LLUrJVJpibgJT9ricA/0?wx_fmt=jpeg', 'create_time': 1693976163, 'digest': '2023研究生迎新活动顺利举行', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493146&idx=1&sn=0ce1429518aaa358af768ef93d59ba26&chksm=fe5d03dec92a8ac80ef681c639bb6ff7ebf1e65956d7388c4edbd874099ff0cc5c4fb4ce1630#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '志愿接力进行时：当我穿上蓝马甲……', 'update_time': 1693976162}, {'aid': '2247493073_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493073, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwSmxnbFeoxbdtAaibnXyART0B8sYIVvsXPZByffQxEXHd3JiaxdTPGvobtpwp2H54vO1jYiaAQlK572A/0?wx_fmt=jpeg', 'create_time': 1693824053, 'digest': '“燕语殷时”活动志愿者招募开始啦！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493073&idx=1&sn=dc78b1b5f3cecc30f6cb50eb2a897d3e&chksm=fe5d0015c92a8903d2bf450f38660c3cf0856985f4ed97b47ed3af6639700a2730224f953e21#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名｜“燕语殷时”活动志愿者招募开始啦', 'update_time': 1693824052}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
活动报名 | “燕园起航 艺路同行”系列课程报名启动！ http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=1&sn=5a7ee37b463a42e968ade96a7cb3b0a3&chksm=fe5d0318c92a8a0e97edb354f850e62c278fcdfe14a9a709dc1bf259091a55e39949ba307b7f#rd
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 169, in _new_conn
    conn = connection.create_connection(
  File "/usr/lib/python3/dist-packages/urllib3/util/connection.py", line 96, in create_connection
    raise err
  File "/usr/lib/python3/dist-packages/urllib3/util/connection.py", line 86, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 394, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 234, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "/usr/lib/python3.10/http/client.py", line 1283, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/usr/lib/python3.10/http/client.py", line 1329, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/usr/lib/python3.10/http/client.py", line 1278, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/lib/python3.10/http/client.py", line 1038, in _send_output
    self.send(msg)
  File "/usr/lib/python3.10/http/client.py", line 976, in send
    self.connect()
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 200, in connect
    conn = self._new_conn()
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 181, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7f6e85442800>: Failed to establish a new connection: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 755, in urlopen
    retries = retries.increment(
  File "/usr/lib/python3/dist-packages/urllib3/util/retry.py", line 574, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=8080): Max retries exceeded with url: /api/user/submit/link (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f6e85442800>: Failed to establish a new connection: [Errno 111] Connection refused'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/info/PKUinfo/crawl/getURL.py", line 156, in <module>
    POSTER(link)
  File "/home/info/PKUinfo/crawl/getURL.py", line 140, in POSTER
    r = requests.post(url, data=json.dumps(data), headers=headers)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 119, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 544, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 657, in send
    r = adapter.send(request, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=8080): Max retries exceeded with url: /api/user/submit/link (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f6e85442800>: Failed to establish a new connection: [Errno 111] Connection refused'))
['北京大学学生服务总队', '北京大学社会学系', '北京大学计算机学院', '北京大学历史学系', '北京大学经济学院', '北京大学数学科学学院', 'pku数学系', 'P大CoE教务', '北京大学中文系', '北大社会学', '北京大学智能学院', '北大国发院', '北京大学公共卫生学院生物统计系', '北京大学光华管理学院', '北京大学对外汉语教育学院', '北京大学物理学院人才培养', '北京大学教育学院', 'SMS_Stu_Union', '北大数院人', 'PKU言之有物', '北大物理人', '北京大学学生会', 'PKU医预之家', '大信科', '北京大学历史学系学生会', '北大数院青年志愿者协会', '数院研究生会', '物院学生会', '北大心理人', 'PKU信科职业发展中心', '光华CDC', '走进光华', '北大史学人', '北京大学教育学院团研', '北大脑科学', '北京大学人文社会科学研究院', '北京国际数学研究中心BICMR', '北京大学语言学实验室', '北京大学文学讲习所', '北京大学前沿计算研究中心', '大数据分析与应用国家工程实验室', '北京大学统计科学中心', '北京大学文化产业研究院', '北大古典语文学', '思想与社会', '北京大学严复班', '北京大学', '北大团委', '北大体育', '北京大学学生发展支持', '北大新青年', 'PKU体委', '北京大学教务部', '北大餐饮中心官方资讯', '燕园学子微助手', '平安燕园', '燕园微后勤', '北京大学招生办', '北京大学百周年纪念讲堂', '北大就业', '北大未名BBS', '北大政治法律与社会项目', 'Paideia_et_Cultura', '北京大学国发院经济双学位', '湘思PKU', '北大辩协', '北大红会', '爱心驿站', 'PKU思潜十周年', '未名超算队', '燕语配音社', 'PKUSAA', '北大猫协', '风雷街舞社FLCrew', '北大粤协', '北大耕读社', '元火动漫社', 'pku心协', 'PKU_CACA', 'PKU烹协', 'PKU创新学社', '北大汉推办', '北京通用人工智能研究院'] ['MzU5NjYzNjg0Mw==', 'MzU5MjczNjU0NQ==', 'MzU2MTEwNjk4Mg==', 'MzI0ODE4MjM5Mw==', 'MzIzMzM2NDA5Nw==', 'MzUzMzg4MzgxMQ==', 'MzkxNTM1MjU5Mw==', 'MzI4OTYxMzkyOA==', 'MzI0ODcwNjkwNw==', 'MzkxMzMxMzQ2NQ==', 'Mzk0NDE3ODg5Nw==', 'MjM5MDIwNDg0MA==', 'MzU5MDg1ODYyMA==', 'MjM5MDk3NDgwMQ==', 'MzA3ODU2MTk4NA==', 'MzUxODk4MDA4NA==', 'MzA4OTA5MjA4MA==', 'MzA5NDAxMDYzMQ==', 'MzU3NzA0OTA5Mg==', 'MzAwMDEwMzI0MQ==', 'MzA5NzUwODgxMw==', 'MzA3MDAxMTIxMQ==', 'MzAxOTAyMjk0MA==', 'MzA4MTAzMzQ5NA==', 'MzA3NDYwMzkxMg==', 'MjM5MDAwNzExMA==', 'MzAwNTA1MjA1OA==', 'MzIwNDEzMDI5OA==', 'MjM5NjQ4ODc1MA==', 'MzI3NTQ2MjM5NA==', 'MzA4MDM0NDcwMg==', 'MzkwMDIzNTgxMg==', 'MzkyODMwMzEwMw==', 'Mzg3MzE5MzQzNA==', 'MzAwNTEzNzcwNg==', 'MzIzNDQ0MDUwNg==', 'MzI1ODQ2MTkwOQ==', 'Mzg3OTg2NTkxMw==', 'Mzg3ODU1OTE2MQ==', 'MzU0MjU5NjQ3NA==', 'MzkyMDE5NTM0NA==', 'Mzg3MTcyNzA1OQ==', 'Mzg4NTE0MDUwNg==', 'MzAwNzc0NzMwMw==', 'Mzg4ODEzNTExNw==', 'MzUyOTkwNTQwNQ==', 'MzA3OTE0MjQzMw==', 'MzIxNjMzMDE1NQ==', 'MzA5MjI1NjIyOA==', 'MzU5OTk0MTE3Mg==', 'MzU3ODg5ODQ3MA==', 'MzAwNDg0MDA4Mw==', 'MzIzNzc4ODkxOA==', 'Mzg4MTIzNzU4OQ==', 'MzA3NzE0MjcyMQ==', 'MzI2OTQ2NDg5Ng==', 'MzUxMzEyNTczNw==', 'MzA4NjEzNDYxMQ==', 'MzU2ODY1ODE1MQ==', 'MzA4NjAzMTIxNw==', 'MzA3OTMwMjc5Mg==', 'Mzg3NjcxNTMzNA==', 'MzkwMzI0MjEyNw==', 'MzA3MzQ5ODIyNA==', 'MzU4NjMyNzM3Nw==', 'MjM5MTg0MDE4NQ==', 'MzA3NzAwNjI5NA==', 'MzA5ODA4ODExMg==', 'Mzg4OTY4NDgxMA==', 'MzUzOTk3NzkxMg==', 'MzAxMzMwNTAxNQ==', 'Mzg4NjExNDUzMg==', 'MjM5NDc5MzgzNg==', 'MzI0NjA0MTUwNA==', 'MzA5MTk4NTgxNg==', 'MzAwNjA3NDQxMQ==', 'MjM5NjY2ODY0OQ==', 'MzA4ODg5NzU4NA==', 'MzA3OTQwMTAwOQ==', 'MzI4MjU0Njc1Ng==', 'MzA3MjMzNTQ1OQ==', 'MzI2ODA5NTg4Nw==', 'Mzg2Njc1NjM2OA==']
北京大学学生服务总队 MzU5NjYzNjg0Mw==
sleep 363
<Response [200]>
dic: {'app_msg_cnt': 565, 'app_msg_list': [{'aid': '2247493340_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2oHEkYsUWqZohDOuKX23fHjTJIX79OPsb9O4IxPiatbhbXgdmNsvCEUiag/0?wx_fmt=png', 'create_time': 1694503567, 'digest': '点击碎纸，看清信件“自把玉钗敲砌竹，清歌一曲月如霜。”清丽婉转的歌声，表达出歌唱者丰富饱满的心绪。“此曲只应', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=1&sn=5a7ee37b463a42e968ade96a7cb3b0a3&chksm=fe5d0318c92a8a0e97edb354f850e62c278fcdfe14a9a709dc1bf259091a55e39949ba307b7f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “燕园起航 艺路同行”系列课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2oVr7SzNE1XxuYngDcQyGsicsOHEibBJTWt9BmNluSoj9YxomtrHE1q0BA/0?wx_fmt=jpeg', 'create_time': 1694503567, 'digest': '前言： “远看山有色，近听水无声”赞美了中国画的生动传神！“垂露春光满，崩云骨气馀”展现了书法的丰筋多力!', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=2&sn=32f6f0dcb0ae5af82581090f73b924e7&chksm=fe5d0318c92a8a0e07d383d4fd61f7d416df9efff2d7e2e3b33757a1b30478e9dadd07562652#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “燕园起航 笔墨生辉” 书画类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2orR4icE9aRzvWevtS8xNwkUwBM94EBYEdEm1yzeJzuYs4ktOcOqbH18w/0?wx_fmt=png', 'create_time': 1694503567, 'digest': 'NEW TERM活动报名&nbsp;体育类兴趣课程报名启动前言：盼望着，盼望着体育类兴趣课程终于发车啦！快来', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=3&sn=2498c901ec65aa2ea689fb59e0cfb248&chksm=fe5d0318c92a8a0e3f87d4b4b3f456795f945c45cbffde362f354112450999d409a18d6e405e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “韵动燕园 青春起航”体育类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493340_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493340, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwR4jl1WdR6TSBOf68VAjb2ohQppeUV1UsXCLYqkGUd7x0jbwn0sRGD1rTXViayvqFxGibKIjib81nx4A/0?wx_fmt=png', 'create_time': 1694503567, 'digest': '前言：以乐会友，以舞传情舞步翩跹，弦音悠悠你是否希望拥有拓展兴趣，展示才华的舞台文艺兴趣小组的大门向你敞开！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=4&sn=04b593d715a80c025fd6b62c186fd245&chksm=fe5d0318c92a8a0e51d824c2a883bf15c037980bde1d5716bba2408b3205e4549fd60aa97f84#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名 | “以乐会友 以舞传情”文艺类兴趣课程报名启动！', 'update_time': 1694503800}, {'aid': '2247493224_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQYEIOTz4M8yeJmbbxORG13iaDOSA7jw3rSFgGFLLzZfPYJZgn7P0HsXlxV0o2hycf0F9451gInn7Q/0?wx_fmt=jpeg', 'create_time': 1694427957, 'digest': '燕语殷时活动志愿者招募开始啦！快来收获跨越几百公里的友谊吧~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=1&sn=091295a163075b2d4ed9e2a33efcf515&chksm=fe5d03acc92a8aba1259ceb82846f63ed4b2228baa7963367151d975370555fd2cb495e9e741#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名｜燕语殷时活动志愿者招募开始啦', 'update_time': 1694428200}, {'aid': '2247493224_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwSovCNDmxao39yshtB0Ul9qJHdIiaD8C1roQCuwvtQI5o62LhF9oxg1pt9mPusSUd3EdXicBCA2cUhg/0?wx_fmt=png', 'create_time': 1694427957, 'digest': '一起将书籍流转起来吧！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=2&sn=0aa59e5f9568a925ba3b3c1ead0c5914&chksm=fe5d03acc92a8aba2b996fcf883f3da2fa086849145292f2bb26fccccfa2f61b0dc819c1a8c3#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '图书漂流 | 欢迎参加图书漂流——收书活动！', 'update_time': 1694428200}, {'aid': '2247493224_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493224, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQYEIOTz4M8yeJmbbxORG13HLDg6mgsZI5ISj5HfPRvXgtUOv0stWtNDVT8AUPRr26LbibicQiamjicXA/0?wx_fmt=jpeg', 'create_time': 1694427957, 'digest': '2023燕园起航第九组见面会成功举办！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=3&sn=907b5c8612583ecb42cc5197a46dfe5a&chksm=fe5d03acc92a8ababee3583b6013683460fa6239de0d4357889d83bab64d812fc28e50c5d8c7#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '起航快讯 | 满“新”欢喜，如约而至：23级燕园起航第9组成功举办破冰活动', 'update_time': 1694428200}, {'aid': '2247493193_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pwmnmfcibjt9vPggrjliaPmJSdHToYDT1by5IiaQh7AogibLYDf0icXB2fIQ/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '中央文明办三局、中国社会工作联合会共同开展2023年“圆梦工程”农村未成年人心理健康教育志愿服务项目大学生', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=1&sn=4d164e76ca0c91a6d146bbc627e7941a&chksm=fe5d038dc92a8a9be165469479dc58a0c52423ef92955808490f75fef7f11675563403c0ae35#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '2023年北京大学“弥渡心理”实践团赴大理自治州实践总结', 'update_time': 1694061000}, {'aid': '2247493193_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pd40UpbdIic0vBKhibibTGPtfg7lZG3FvJjLEWcfuwtZMPtGkMKDyDGZpw/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '2023年北京大学“弥渡心理”实践队赴大理自治州实践纪实①', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=2&sn=a1fe1edff08adb2bc0f4eff373ea70b3&chksm=fe5d038dc92a8a9b03dffb313e737d0eb2f3e00e454e1a965453860de43fe935f0a93c898f75#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '苍山宜洗马 名邦亦峥嵘——2023年圆梦计划“弥渡心理”18日简报', 'update_time': 1694061000}, {'aid': '2247493193_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1pLyDWz9TEUYuQGa4ZRMRCWo5dBwIDFt9OibzkyiaR9TvGrrrKicPr1cxzw/0?wx_fmt=png', 'create_time': 1694060423, 'digest': '2023年北京大学“弥渡心理”实践队赴大理自治州实践纪实②', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=3&sn=99cb159ae6d5943d8f4b93b2d03e30f1&chksm=fe5d038dc92a8a9b0fc2f543dc7975fa7bf32ab2d42e91c8d4582718f97aa3c8337f9127400e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '喜洲绽金花 古镇溯红色——2023年圆梦计划“弥渡心理”19日简报', 'update_time': 1694061000}, {'aid': '2247493193_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493193, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwQINZth7gTia1o3u0VdHMib1px6ZxUxGjSMlmbmOZ0IX61XJLK5vaPKmxickCkibaicsxAYvs72ticiaKz3A/0?wx_fmt=jpeg', 'create_time': 1694060423, 'digest': '唤醒红色记忆，传承革命精神。2023年8月20日，北京大学“弥渡心理”志愿队踏上云南省大理市的土地，赶赴大理博物馆重走红色路线。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=4&sn=04b7931dd41936fb4b5c6b46cf5ef2dd&chksm=fe5d038dc92a8a9b8fc898b64a4e908a09eec97309d9f2b2d44b9daeb17898c232de2f048162#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '南诏存史韵 丹心报家国——2023年圆梦计划“弥渡心理”20日简报', 'update_time': 1694061000}, {'aid': '2247493146_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493146, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwSbbrTIky5xJDsjfLW2ibMTNj4l8LgPuPl01icRR17Ppz0ibz52RG4kh0KN64aQ1LLUrJVJpibgJT9ricA/0?wx_fmt=jpeg', 'create_time': 1693976163, 'digest': '2023研究生迎新活动顺利举行', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493146&idx=1&sn=0ce1429518aaa358af768ef93d59ba26&chksm=fe5d03dec92a8ac80ef681c639bb6ff7ebf1e65956d7388c4edbd874099ff0cc5c4fb4ce1630#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '志愿接力进行时：当我穿上蓝马甲……', 'update_time': 1693976162}, {'aid': '2247493073_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247493073, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/rxicxOJLlQwSmxnbFeoxbdtAaibnXyART0B8sYIVvsXPZByffQxEXHd3JiaxdTPGvobtpwp2H54vO1jYiaAQlK572A/0?wx_fmt=jpeg', 'create_time': 1693824053, 'digest': '“燕语殷时”活动志愿者招募开始啦！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493073&idx=1&sn=dc78b1b5f3cecc30f6cb50eb2a897d3e&chksm=fe5d0015c92a8903d2bf450f38660c3cf0856985f4ed97b47ed3af6639700a2730224f953e21#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动报名｜“燕语殷时”活动志愿者招募开始啦', 'update_time': 1693824052}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
活动报名 | “燕园起航 艺路同行”系列课程报名启动！ http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=1&sn=5a7ee37b463a42e968ade96a7cb3b0a3&chksm=fe5d0318c92a8a0e97edb354f850e62c278fcdfe14a9a709dc1bf259091a55e39949ba307b7f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动报名 | “燕园起航 笔墨生辉” 书画类兴趣课程报名启动！ http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=2&sn=32f6f0dcb0ae5af82581090f73b924e7&chksm=fe5d0318c92a8a0e07d383d4fd61f7d416df9efff2d7e2e3b33757a1b30478e9dadd07562652#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动报名 | “韵动燕园 青春起航”体育类兴趣课程报名启动！ http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=3&sn=2498c901ec65aa2ea689fb59e0cfb248&chksm=fe5d0318c92a8a0e3f87d4b4b3f456795f945c45cbffde362f354112450999d409a18d6e405e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动报名 | “以乐会友 以舞传情”文艺类兴趣课程报名启动！ http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493340&idx=4&sn=04b593d715a80c025fd6b62c186fd245&chksm=fe5d0318c92a8a0e51d824c2a883bf15c037980bde1d5716bba2408b3205e4549fd60aa97f84#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动报名｜燕语殷时活动志愿者招募开始啦 http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=1&sn=091295a163075b2d4ed9e2a33efcf515&chksm=fe5d03acc92a8aba1259ceb82846f63ed4b2228baa7963367151d975370555fd2cb495e9e741#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
图书漂流 | 欢迎参加图书漂流——收书活动！ http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=2&sn=0aa59e5f9568a925ba3b3c1ead0c5914&chksm=fe5d03acc92a8aba2b996fcf883f3da2fa086849145292f2bb26fccccfa2f61b0dc819c1a8c3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
起航快讯 | 满“新”欢喜，如约而至：23级燕园起航第9组成功举办破冰活动 http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493224&idx=3&sn=907b5c8612583ecb42cc5197a46dfe5a&chksm=fe5d03acc92a8ababee3583b6013683460fa6239de0d4357889d83bab64d812fc28e50c5d8c7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
2023年北京大学“弥渡心理”实践团赴大理自治州实践总结 http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=1&sn=4d164e76ca0c91a6d146bbc627e7941a&chksm=fe5d038dc92a8a9be165469479dc58a0c52423ef92955808490f75fef7f11675563403c0ae35#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
苍山宜洗马 名邦亦峥嵘——2023年圆梦计划“弥渡心理”18日简报 http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=2&sn=a1fe1edff08adb2bc0f4eff373ea70b3&chksm=fe5d038dc92a8a9b03dffb313e737d0eb2f3e00e454e1a965453860de43fe935f0a93c898f75#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
喜洲绽金花 古镇溯红色——2023年圆梦计划“弥渡心理”19日简报 http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=3&sn=99cb159ae6d5943d8f4b93b2d03e30f1&chksm=fe5d038dc92a8a9b0fc2f543dc7975fa7bf32ab2d42e91c8d4582718f97aa3c8337f9127400e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
南诏存史韵 丹心报家国——2023年圆梦计划“弥渡心理”20日简报 http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493193&idx=4&sn=04b7931dd41936fb4b5c6b46cf5ef2dd&chksm=fe5d038dc92a8a9b8fc898b64a4e908a09eec97309d9f2b2d44b9daeb17898c232de2f048162#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
志愿接力进行时：当我穿上蓝马甲…… http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493146&idx=1&sn=0ce1429518aaa358af768ef93d59ba26&chksm=fe5d03dec92a8ac80ef681c639bb6ff7ebf1e65956d7388c4edbd874099ff0cc5c4fb4ce1630#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动报名｜“燕语殷时”活动志愿者招募开始啦 http://mp.weixin.qq.com/s?__biz=MzU5NjYzNjg0Mw==&mid=2247493073&idx=1&sn=dc78b1b5f3cecc30f6cb50eb2a897d3e&chksm=fe5d0015c92a8903d2bf450f38660c3cf0856985f4ed97b47ed3af6639700a2730224f953e21#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学社会学系 MzU5MjczNjU0NQ==
sleep 456
<Response [200]>
dic: {'app_msg_cnt': 1792, 'app_msg_list': [{'aid': '2247513715_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247513715, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/HCPeiarecdjn2WA2KFDSoDP4IBdLSqLOxokzaLrEZ9RKzJC29Pe3QwTJjYTKW5ywmria1mTBXwN2M8htwahAS7aA/0?wx_fmt=jpeg', 'create_time': 1694523453, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513715&idx=1&sn=6d2f3734bb3428f4a10897b2292b4dc1&chksm=fe19ce3dc96e472b0e8879a9db260700372cbff38cb3162b50dc4e663773c84ebe2b6379f6c0#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '预告 | 人类学后田野报告会（第八期）', 'update_time': 1694523453}, {'aid': '2247513709_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247513709, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/HCPeiarecdjnfqtoN3hak5LUcUawiaE8ETdxLoXSF8ibce9f8SUphQMbQDYAqAJExyJGPZDge7bdRbNJ4xbHWlS9w/0?wx_fmt=jpeg', 'create_time': 1694428867, 'digest': '9月10日，2013级本科班再次踏入燕园这片热土、回到母系，与恩师和同学，举行了入学十周年纪念活动。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513709&idx=1&sn=678ede717f8e9af399c7eb45194647bb&chksm=fe19ce23c96e47357c5d5b6d125104a1765ced4b52a98efa9c2ec0b58a8a6b8ae865887a2d61#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '携你我之手，赴十年之约  ——2013级本科班入学十周年返校纪念活动', 'update_time': 1694432460}, {'aid': '2247513699_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247513699, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/HCPeiarecdjmn2Wfa2se5JAj0ZSiaZKTw2Orj30U5LTw8VWKN5TdILALw7PPbhHQVfXXHlZy0s1SpePETkoLia6Ug/0?wx_fmt=jpeg', 'create_time': 1694349116, 'digest': '饮其流者怀其源，学有得时念吾师。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513699&idx=1&sn=c648c6d823d05fad5835760f7650fc5e&chksm=fe19ce2dc96e473b50a995305a052a96e85c9e24e1cd392778c66688b0c48c924abe3d692ff7#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '教师节 | 感谢与祝福，请收下吧！', 'update_time': 1694349116}, {'aid': '2247513691_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247513691, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/HCPeiarecdjkInkPRUVpuMhP8ryowFR4ub8vm9jeGw1OxH9v8g6w2Rup6hjhxGVQpzrZxN08mOSTrPHXj5HmjnQ/0?wx_fmt=jpeg', 'create_time': 1694254314, 'digest': '邱泽奇 教书育人先锋获得者', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513691&idx=1&sn=a501e99fbf0cf8c4661c47a0c517cd34&chksm=fe19ce15c96e470316214ff9c5182c3d3a99b55d3425cf443ba94550d1e1569ecf72cd635b09#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '育人先锋 | 邱泽奇：身体力行教学、务实求真治学', 'update_time': 1694258160}, {'aid': '2247513691_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247513691, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/HCPeiarecdjleibuhnfXUZpS4NGvO2Nx8PoWpNPpt38G6afNoupzLX1R8PxmgPhFMEEIcLoWTX79Uiat8IFOgJsCA/0?wx_fmt=jpeg', 'create_time': 1694254314, 'digest': '2023年9月7日上午，由系团委体育中心筹办的“社会学系新生体育团建暨社会学系运动队招新”在北京大学第二体育场成功举办！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513691&idx=2&sn=6e35931a749e12f874ef34953d94756d&chksm=fe19ce15c96e4703ce3d5b0d8dab64f934db52dabe28f12692d18c23d2dc164b97a7b773a28d#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '回顾｜社会学系新生体育团建暨运动队招新圆满成功！', 'update_time': 1694258160}, {'aid': '2247513617_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247513617, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/HCPeiarecdjleibuhnfXUZpS4NGvO2Nx8PU0Ijrdiazj6dnvnPDdYJGx3opZUibeicoufIttToBbleUHFxPalHceWibA/0?wx_fmt=jpeg', 'create_time': 1694169891, 'digest': '9月5日上午，北京大学社会学系“党委书记讲党课”新生教育活动在二教301教室成功举办。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513617&idx=1&sn=12c337e62ec295a3bbdbebb7934abe5d&chksm=fe19ce5fc96e4749af19c3508d4caeb97e96f636478f58a6214b9c2a0da053c9c26836bcb509#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '社会学系“党委书记讲党课”新生教育活动顺利举行', 'update_time': 1694174400}, {'aid': '2247513617_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247513617, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/HCPeiarecdjleibuhnfXUZpS4NGvO2Nx8PgSSgwFX28LpgqJyRLvicFy5Yxan1Rx4LXnJKzhEU2Ur7k45E0uCkCAA/0?wx_fmt=jpeg', 'create_time': 1694169891, 'digest': '9月5日下午，北京大学社会学系新生教育系列活动之中国社会学史与中国社会专题讲座于二教301教室成功举行。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513617&idx=2&sn=2238468615a8ec146266e88858473a46&chksm=fe19ce5fc96e474966890a1d0fd42bad2dc4b63cdc9e7d52f044dc086b3720635200bcc02922#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '社会学系“中国社会学史与中国社会” 专题讲座顺利举行', 'update_time': 1694174400}, {'aid': '2247513617_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247513617, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/HCPeiarecdjkKGBod8QS3hcyibtnIdYUPp94I4DsCUWcMcXJ1qBqEseicnhNyYXrH1w6VBCYBM9qDBqX9CebdUpgw/0?wx_fmt=jpeg', 'create_time': 1694169891, 'digest': '一起为老师送上祝福吧！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513617&idx=3&sn=b02f0e8a85fb344cb01b893b2f47e257&chksm=fe19ce5fc96e474978a0629001f6c4515c569d4acd1e57a9bec133682826ca65f57c87d8a172#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动·教师节 | 预热：秋风送祝福', 'update_time': 1694174400}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
预告 | 人类学后田野报告会（第八期） http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513715&idx=1&sn=6d2f3734bb3428f4a10897b2292b4dc1&chksm=fe19ce3dc96e472b0e8879a9db260700372cbff38cb3162b50dc4e663773c84ebe2b6379f6c0#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
携你我之手，赴十年之约  ——2013级本科班入学十周年返校纪念活动 http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513709&idx=1&sn=678ede717f8e9af399c7eb45194647bb&chksm=fe19ce23c96e47357c5d5b6d125104a1765ced4b52a98efa9c2ec0b58a8a6b8ae865887a2d61#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教师节 | 感谢与祝福，请收下吧！ http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513699&idx=1&sn=c648c6d823d05fad5835760f7650fc5e&chksm=fe19ce2dc96e473b50a995305a052a96e85c9e24e1cd392778c66688b0c48c924abe3d692ff7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
育人先锋 | 邱泽奇：身体力行教学、务实求真治学 http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513691&idx=1&sn=a501e99fbf0cf8c4661c47a0c517cd34&chksm=fe19ce15c96e470316214ff9c5182c3d3a99b55d3425cf443ba94550d1e1569ecf72cd635b09#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回顾｜社会学系新生体育团建暨运动队招新圆满成功！ http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513691&idx=2&sn=6e35931a749e12f874ef34953d94756d&chksm=fe19ce15c96e4703ce3d5b0d8dab64f934db52dabe28f12692d18c23d2dc164b97a7b773a28d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
社会学系“党委书记讲党课”新生教育活动顺利举行 http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513617&idx=1&sn=12c337e62ec295a3bbdbebb7934abe5d&chksm=fe19ce5fc96e4749af19c3508d4caeb97e96f636478f58a6214b9c2a0da053c9c26836bcb509#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
社会学系“中国社会学史与中国社会” 专题讲座顺利举行 http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513617&idx=2&sn=2238468615a8ec146266e88858473a46&chksm=fe19ce5fc96e474966890a1d0fd42bad2dc4b63cdc9e7d52f044dc086b3720635200bcc02922#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动·教师节 | 预热：秋风送祝福 http://mp.weixin.qq.com/s?__biz=MzU5MjczNjU0NQ==&mid=2247513617&idx=3&sn=b02f0e8a85fb344cb01b893b2f47e257&chksm=fe19ce5fc96e474978a0629001f6c4515c569d4acd1e57a9bec133682826ca65f57c87d8a172#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学计算机学院 MzU2MTEwNjk4Mg==
sleep 547
<Response [200]>
dic: {'app_msg_cnt': 536, 'app_msg_list': [{'aid': '2247501265_1', 'album_id': '2118363018114678785', 'appmsg_album_infos': [{'album_id': 2118363018114678785, 'appmsg_album_infos': [], 'id': '2118363018114678785', 'tagSource': 4, 'title': '计算机学院'}, {'album_id': 2067504265857646593, 'appmsg_album_infos': [], 'id': '2067504265857646593', 'tagSource': 4, 'title': '新闻'}, {'album_id': 2570507764880359426, 'appmsg_album_infos': [], 'id': '2570507764880359426', 'tagSource': 3, 'title': '教师节'}], 'appmsgid': 2247501265, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/kmjNGgoMOczKvQzlT4Eolds221l7wN7C5ibblGIUEPxwXohNDCYQCq1svFPMnbjVicGXBI3VRPML9OniaICwA6PnQ/0?wx_fmt=jpeg', 'create_time': 1694679329, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501265&idx=1&sn=7d3ef5775b6962013f9793b5a40bb186&chksm=fc7f5c98cb08d58e18c0e15b897291dcb3e3abd36060475fcec8ffd58e4719f470191edee341#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '新闻丨教师节期间，校领导看望杨芙清老师', 'update_time': 1694692800}, {'aid': '2247501245_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247501245, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/kmjNGgoMOczJVINL7Hrp7tpdNr5bkRicjSzEbb1CUEicB6dhf1WSjXIqic0BGduVDmYnyMVD5N62kUEGHRibMImiayQ/0?wx_fmt=jpeg', 'create_time': 1694529395, 'digest': '请查收新生趣味运动会的精彩瞬间！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501245&idx=1&sn=72d49e0b0d6150d607fc5e48908b6005&chksm=fc7f5cf4cb08d5e27d6371c3d62a681954666c2f92737afa1f0629538df00c2cef66742cc9f4#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '计算充电站 | 欢迎新同学，一起来运动！——新生趣味运动会举办', 'update_time': 1694529394}, {'aid': '2247501201_1', 'album_id': '2705301818972553218', 'appmsg_album_infos': [{'album_id': 2705301818972553218, 'appmsg_album_infos': [], 'id': '2705301818972553218', 'tagSource': 0, 'title': '计算志愿'}], 'appmsgid': 2247501201, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/kmjNGgoMOcz3wDnThmPaNiaYC824AaBrXmT1JXic0lytBYzhwsA3Tib2jZZNV2nibpx9RkOvvj5Jl8gPnEnaqRFvxA/0?wx_fmt=jpeg', 'create_time': 1694272441, 'digest': '校园网使用有问题？我们来为你排忧解难！网络安全知识不扎实？冲刺答题赢奖品！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501201&idx=1&sn=a99b63cfd63c61e66ca707b66a437fa0&chksm=fc7f5cd8cb08d5cee579afc8970fd07232f2ca048a16f89301487dccff444b75642a9ee42648#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '志愿网维｜网络维护与安全，我为同学办实事', 'update_time': 1694272441}, {'aid': '2247501175_1', 'album_id': '2118363018114678785', 'appmsg_album_infos': [{'album_id': 2118363018114678785, 'appmsg_album_infos': [], 'id': '2118363018114678785', 'tagSource': 4, 'title': '计算机学院'}, {'album_id': 2067504265857646593, 'appmsg_album_infos': [], 'id': '2067504265857646593', 'tagSource': 4, 'title': '新闻'}], 'appmsgid': 2247501175, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/kmjNGgoMOcyAq2ZibiaOR7kMka2tlYWbfQqBicr4cufWxECUuc30HyBX8HiclWBPnyghNibV7neKFWw7Rn7CZCSYoVQ/0?wx_fmt=jpeg', 'create_time': 1694081572, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501175&idx=1&sn=d2b57d9a384b3a1ee3b27ae7637623a6&chksm=fc7f5c3ecb08d5283f15f58ecef410a0c935eb0b4738690de07f23445fac2d3963f900b62850#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': 'CS迎新季｜计算机学院举办2023年开学典礼暨新生第一课', 'update_time': 1694088000}, {'aid': '2247501175_2', 'album_id': '2118363018114678785', 'appmsg_album_infos': [{'album_id': 2118363018114678785, 'appmsg_album_infos': [], 'id': '2118363018114678785', 'tagSource': 4, 'title': '计算机学院'}, {'album_id': 2067504265857646593, 'appmsg_album_infos': [], 'id': '2067504265857646593', 'tagSource': 4, 'title': '新闻'}], 'appmsgid': 2247501175, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/kmjNGgoMOcyAq2ZibiaOR7kMka2tlYWbfQ8ibvtO6SExaLFToEUt0cbmtsM9KHYeIIPhGqE3Yk1CmgyIqTGJiaAuRw/0?wx_fmt=png', 'create_time': 1694081572, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501175&idx=2&sn=6bf93fd53b43e49bbec7e141c40fd642&chksm=fc7f5c3ecb08d52803994a62d33fc196a829f1e7da84b9c84438d99c07ba4d0ccdbe03dfb556#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '新闻｜北京大学计算机学院 7 篇论文入选数据库顶级会议VLDB 2023', 'update_time': 1694088000}, {'aid': '2247501146_1', 'album_id': '2118363018114678785', 'appmsg_album_infos': [{'album_id': 2118363018114678785, 'appmsg_album_infos': [], 'id': '2118363018114678785', 'tagSource': 3, 'title': '计算机学院'}], 'appmsgid': 2247501146, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/kmjNGgoMOcy0iabI6N0WwAaL97dE3Wx4wFykpLOyXSRWXJE4ibRyfXVLCNiaX8qKicI01vKhUAGK0xfycnicQH1mQNQ/0?wx_fmt=jpeg', 'create_time': 1693992478, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501146&idx=1&sn=f2dd06d7fcc599cc7d4a75b61af137af&chksm=fc7f5c13cb08d505c538485ba51142e72879fa19f4488b26de0753a1ab508d552d4f34672595#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': 'CS迎新季 | “走进学生心中”——计算机学院走访新校区2023级全体新生宿舍', 'update_time': 1694001600}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
新闻丨教师节期间，校领导看望杨芙清老师 http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501265&idx=1&sn=7d3ef5775b6962013f9793b5a40bb186&chksm=fc7f5c98cb08d58e18c0e15b897291dcb3e3abd36060475fcec8ffd58e4719f470191edee341#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
计算充电站 | 欢迎新同学，一起来运动！——新生趣味运动会举办 http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501245&idx=1&sn=72d49e0b0d6150d607fc5e48908b6005&chksm=fc7f5cf4cb08d5e27d6371c3d62a681954666c2f92737afa1f0629538df00c2cef66742cc9f4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
志愿网维｜网络维护与安全，我为同学办实事 http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501201&idx=1&sn=a99b63cfd63c61e66ca707b66a437fa0&chksm=fc7f5cd8cb08d5cee579afc8970fd07232f2ca048a16f89301487dccff444b75642a9ee42648#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
CS迎新季｜计算机学院举办2023年开学典礼暨新生第一课 http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501175&idx=1&sn=d2b57d9a384b3a1ee3b27ae7637623a6&chksm=fc7f5c3ecb08d5283f15f58ecef410a0c935eb0b4738690de07f23445fac2d3963f900b62850#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻｜北京大学计算机学院 7 篇论文入选数据库顶级会议VLDB 2023 http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501175&idx=2&sn=6bf93fd53b43e49bbec7e141c40fd642&chksm=fc7f5c3ecb08d52803994a62d33fc196a829f1e7da84b9c84438d99c07ba4d0ccdbe03dfb556#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
CS迎新季 | “走进学生心中”——计算机学院走访新校区2023级全体新生宿舍 http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501146&idx=1&sn=f2dd06d7fcc599cc7d4a75b61af137af&chksm=fc7f5c13cb08d505c538485ba51142e72879fa19f4488b26de0753a1ab508d552d4f34672595#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学历史学系 MzI0ODE4MjM5Mw==
sleep 364
<Response [200]>
书讯 | 荣新江、朱玉麒主编 《黄文弼所获西域文书》 http://mp.weixin.qq.com/s?__biz=MzI0ODE4MjM5Mw==&mid=2247493878&idx=1&sn=7446c709854a2e58f96476c842b6e6a3&chksm=e9a60be0ded182f67447dd5bd163d4285ff2dce1c8e2eaa599dd109caf952ad3d2d29d905eb9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座｜Paul Erdkamp：古代民众的粮食骚乱与“道德经济学” http://mp.weixin.qq.com/s?__biz=MzI0ODE4MjM5Mw==&mid=2247493875&idx=1&sn=9f83a4f185227334b6a15c7bc2b0cf64&chksm=e9a60be5ded182f3f71d3c91dfa4eea3f8cd05b7a5ed8089ad745fc163c83e3293014bc62bea#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学致辞｜徐天：历史学可以是一种博大的共情体验 http://mp.weixin.qq.com/s?__biz=MzI0ODE4MjM5Mw==&mid=2247493866&idx=1&sn=f1f0bbaf2b02982bd7fa59468c41d9f2&chksm=e9a60bfcded182ea9cb0bbfcd1c65a6adea273c39b9835b3d0ae1d2270b78aea86ce68af6860#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
书讯丨臧运祜、吴文浩主编《近百年中日关系论——中国青年学者的视角》 http://mp.weixin.qq.com/s?__biz=MzI0ODE4MjM5Mw==&mid=2247493861&idx=1&sn=d5d3b9b8438518073466f7a85c00b2a7&chksm=e9a60bf3ded182e50b442d944bddbf3a35b709392d8c5b01156783cce44ca123a9cf3e7bbb63#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座 | 朱青生教授总策划：世界艺术史卓越学者对话 http://mp.weixin.qq.com/s?__biz=MzI0ODE4MjM5Mw==&mid=2247493861&idx=2&sn=68c4fea8295bff79e58a9e3c85d8fca7&chksm=e9a60bf3ded182e5d2a5198c54bd0d326fce2c890f81fd0c933a6decfcc36a975ac45e6eda6a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教师节 | 苗润博：真正的传承离不开切实的批评 http://mp.weixin.qq.com/s?__biz=MzI0ODE4MjM5Mw==&mid=2247493856&idx=1&sn=ce32570b677fc0903a92a9b65e0f4e94&chksm=e9a60bf6ded182e08fe19ad38f113db9d91ed5d7b488875ebd658f43e5cb8aad16d3b37db59c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座｜Paul Erdkamp：战场之外：罗马共和国中期战争的地形与后勤 http://mp.weixin.qq.com/s?__biz=MzI0ODE4MjM5Mw==&mid=2247493856&idx=2&sn=0677bb486e10a168fa95f44e35e99cae&chksm=e9a60bf6ded182e0e1fefcd654eb45e91b2fd21e0a946da0b6c73b7089be53c3c592814d14ad#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学经济学院 MzIzMzM2NDA5Nw==
sleep 137
<Response [200]>
北大经院学者 | 刘新立：气候异常形势严峻 风险减量正当其时（上） http://mp.weixin.qq.com/s?__biz=MzIzMzM2NDA5Nw==&mid=2247551663&idx=1&sn=47298f2fd18531e06499ac8f1e795003&chksm=e8848541dff30c579f98bf3f5cc96d2c5cc899cec3bda1f9e49e12ba2596bfa8578fbb94b9c2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大经院学者 | 苏剑：恢复和扩大需求是经济回稳向好的关键 http://mp.weixin.qq.com/s?__biz=MzIzMzM2NDA5Nw==&mid=2247551655&idx=1&sn=d981d121dc259211310151009dd00112&chksm=e8848549dff30c5fd26980af7c16996b475e09529fa8d7a68b5025a0d9186493fdd3b75369c5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大经院科研 | 袁野助理教授合作论文在Journal of Development Economics发表 http://mp.weixin.qq.com/s?__biz=MzIzMzM2NDA5Nw==&mid=2247551646&idx=1&sn=d002291b1968f7cc8596fac616363137&chksm=e8848570dff30c66a26ce435818208518d5f1cdba2b3ebe1a1c4cf3d91bc696666074b8d78a7#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
广府新路珠江畔，岭南兴怀一旦来｜北大经院师生赴广州开展思政实践 http://mp.weixin.qq.com/s?__biz=MzIzMzM2NDA5Nw==&mid=2247551646&idx=2&sn=1db497a59d2473dd97fe3e7b2d0a67c5&chksm=e8848570dff30c661f25d124b798cb3827efd8ca13ce128df96eeefdf7cfbd18d9fbef6b7593#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大经院学者 | 锁凌燕：数字化提升保险理赔服务质效 http://mp.weixin.qq.com/s?__biz=MzIzMzM2NDA5Nw==&mid=2247551572&idx=1&sn=513f48c99be81069b548ec7ba78e302c&chksm=e88485badff30cac7df8565dc0831b7d8209f5e6cdc7bbe829dff49c5f8bd8120eb8892d8519#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大经院 | 讲座预告（9.13） http://mp.weixin.qq.com/s?__biz=MzIzMzM2NDA5Nw==&mid=2247551572&idx=2&sn=7b0b93f6bbbee5e65e3b33bee89ee60d&chksm=e88485badff30cac7a4a8d2281671572a3ca94f9372050c4c580797f28c205f486c2746d0e0d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大经院科研 | 郝煜长聘副教授获国家自然科学基金面上项目资助 http://mp.weixin.qq.com/s?__biz=MzIzMzM2NDA5Nw==&mid=2247551558&idx=1&sn=3c1aafbdb35514f37d912b247d2f5c32&chksm=e88485a8dff30cbecd4ff70e9dfbb0cce56aab1780753bc7f71ebea7c3c57000a0a4c7f17738#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学数学科学学院 MzUzMzg4MzgxMQ==
sleep 112
<Response [200]>
dic: {'app_msg_cnt': 647, 'app_msg_list': [{'aid': '2247496175_1', 'album_id': '2607773383514439686', 'appmsg_album_infos': [{'album_id': 2607773383514439686, 'appmsg_album_infos': [], 'id': '2607773383514439686', 'tagSource': 4, 'title': '北大数学110周年'}], 'appmsgid': 2247496175, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmBOUJFiakehPm9CVb0RzAQHp2vWadCnIPLiciaML9a2tHYcgOXIgNvWxZzR42CyljbFnVb2mQtIVkCvw/0?wx_fmt=jpeg', 'create_time': 1694586436, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496175&idx=1&sn=2ad3bb7920f66bcfd066cdbc7c1ef6a8&chksm=fa9f8f23cde80635f990a91c58a8b9713e943323e866d81582f241d450b3698dd14d0207e0f6#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '110周年庆 | 概率论与随机分析国际会议', 'update_time': 1694586436}, {'aid': '2247496160_1', 'album_id': '2607773383514439686', 'appmsg_album_infos': [{'album_id': 2607773383514439686, 'appmsg_album_infos': [], 'id': '2607773383514439686', 'tagSource': 4, 'title': '北大数学110周年'}], 'appmsgid': 2247496160, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmAwLYk7bRY1T8x52kZYrVJ0xQI982KjFicJ9dEibjl1Ng2up81xOKgiav1ybZ1UhgNfuRxs8BiaibDnzoA/0?wx_fmt=jpeg', 'create_time': 1694424153, 'digest': '智华楼四元厅首场报告 2023-09-15  15:00', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496160&idx=1&sn=4fa32438d247ba4f2b3550a823cbd2d2&chksm=fa9f8f2ccde8063a8b2bb40c6afaed84cd17459808f45b9f1e8eb12b2d7236a8a63c7d957e13#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '110周年庆·杰出学者报告 | 南开大学张伟平院士', 'update_time': 1694424153}, {'aid': '2247496160_2', 'album_id': '2903364320653524995', 'appmsg_album_infos': [{'album_id': 2903364320653524995, 'appmsg_album_infos': [], 'id': '2903364320653524995', 'tagSource': 4, 'title': '期刊建设'}], 'appmsgid': 2247496160, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDwO07ObyUISYCiaiaT1ZRKqgMA7bib6vaia42MqW61AnONKIGQbqQdQuRdq7Uiaia51vZt7tkgxY4EH4xA/0?wx_fmt=jpeg', 'create_time': 1694424153, 'digest': '欢迎阅读PMJ最新文章', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496160&idx=2&sn=b5a127d3bb6b664e78225c2cf71f484a&chksm=fa9f8f2ccde8063a56504f1554cddd33e08587613aad9c3b76500760d7733dc4f40bb444707e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '《北京数学杂志（英文）》2023年在线出版文章速递（五）', 'update_time': 1694424153}, {'aid': '2247496151_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247496151, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmAWktPaXHMt00kMTZlP2ic2zZUfHFTic4iafficGoGh532icIsXoUoV8aBLsIk3J0ZOQcx9jzNK5QKVUDg/0?wx_fmt=jpeg', 'create_time': 1694309807, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 8, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496151&idx=1&sn=64eec049d84a241d97faef1d6bfe5ba0&chksm=fa9f8f1bcde8060d14f683082066e65388877f8a7a997d058d5cfa07c83600a89a9254563ce5#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '北京大学数学科学学院祝老师们教师节快乐', 'update_time': 1694309807}, {'aid': '2247496151_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247496151, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmAWktPaXHMt00kMTZlP2ic2zGgBcXMePK1U94LfYpRIdWSONwNiadD8dG3FicP2hgCxxGhDbktetBuxw/0?wx_fmt=jpeg', 'create_time': 1694309807, 'digest': '北大数学讲座预告来啦，快看看有哪些你感兴趣的讲座吧！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496151&idx=2&sn=4c1fb084ca1c8851016a9eeb7815147e&chksm=fa9f8f1bcde8060dae49bc0f4f8a73ad110ac25b3dce28d7197f0c29f5049c71e58b19d49fe5#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告 | 北大数学一周学术报告一览（09.11-09.17）', 'update_time': 1694309807}, {'aid': '2247496108_1', 'album_id': '3095357131987664903', 'appmsg_album_infos': [{'album_id': 3095357131987664903, 'appmsg_album_infos': [], 'id': '3095357131987664903', 'tagSource': 4, 'title': '2023年开学典礼'}], 'appmsgid': 2247496108, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNq7zxTCc0Fial7QicI0B6EBOgeicG7JN3e5evUrU5VbuxEvFp2hrKVfmibg/0?wx_fmt=jpeg', 'create_time': 1694252037, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496108&idx=1&sn=62e9797fc63d588d86050624d815fe27&chksm=fa9f8f60cde806761583d06fceb28012ef8b805de71081c4675774bac586cd5f717c6cd0e7ef#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '本科生新生代表胡殊闻在北大数院2023年开学典礼上的发言', 'update_time': 1694252037}, {'aid': '2247496108_2', 'album_id': '3095357131987664903', 'appmsg_album_infos': [{'album_id': 3095357131987664903, 'appmsg_album_infos': [], 'id': '3095357131987664903', 'tagSource': 4, 'title': '2023年开学典礼'}], 'appmsgid': 2247496108, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNNZrP0bhV8E8A6Wq23IJKNM3YFIITI9Bgw1oWkglnqhlyOLYjiaHy9FQ/0?wx_fmt=jpeg', 'create_time': 1694252037, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496108&idx=2&sn=bcdc033ab99f8e9129d0430cb7c66bbc&chksm=fa9f8f60cde8067680aaecf972419beeee57974a140b1c6fa89a87ca5fcdb4f1561d73972484#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '硕士研究生新生代表王楚凡在北大数院2023年开学典礼上的发言', 'update_time': 1694252037}, {'aid': '2247496108_3', 'album_id': '3095357131987664903', 'appmsg_album_infos': [{'album_id': 3095357131987664903, 'appmsg_album_infos': [], 'id': '3095357131987664903', 'tagSource': 4, 'title': '2023年开学典礼'}], 'appmsgid': 2247496108, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSN7urC1DdfbIrgm3iaq48qwNYiciaNYfv3cdVxicJGBU5hjILxWuAEhlKgqQ/0?wx_fmt=jpeg', 'create_time': 1694252037, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496108&idx=3&sn=2eb5fc8b4b80c53003c5c718ff4924f4&chksm=fa9f8f60cde806767c444e576a1dc05de8bdd6861f8509d730bf402cf3439bd37015ebd404ca#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '博士研究生新生代表史庭潇在北大数院2023年开学典礼上的发言', 'update_time': 1694252037}, {'aid': '2247496108_4', 'album_id': '3095357131987664903', 'appmsg_album_infos': [{'album_id': 3095357131987664903, 'appmsg_album_infos': [], 'id': '3095357131987664903', 'tagSource': 4, 'title': '2023年开学典礼'}], 'appmsgid': 2247496108, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNLhia1YLjTjPRicS50BvUWYuiaWsTEwnucLjlk2IWW7nM3UyLicRxTENuqQ/0?wx_fmt=jpeg', 'create_time': 1694252037, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496108&idx=4&sn=c08cf22a6aebbd50e5c268c500eae571&chksm=fa9f8f60cde80676ec64e58301534508cae1274e792b19486f494c313ba8cda15bb6f1f76976#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '老生代表杨晨曦在北大数院2023年开学典礼上的发言', 'update_time': 1694252037}, {'aid': '2247496084_1', 'album_id': '3095357131987664903', 'appmsg_album_infos': [{'album_id': 3095357131987664903, 'appmsg_album_infos': [], 'id': '3095357131987664903', 'tagSource': 4, 'title': '2023年开学典礼'}], 'appmsgid': 2247496084, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNJWyJzM7a5ZibMYwll8Vyc3yVVGaL3ibtEwVf8V969Rf4icXwFpVhZVP4g/0?wx_fmt=jpeg', 'create_time': 1694155365, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496084&idx=1&sn=13936e2ee124b289d3e3ea71ee1af376&chksm=fa9f8f58cde8064e38b3047998086ea5fdef872f9e34c1b9c4c890c264be22841bffb21f0fe6#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '培养更多数学拔尖人才 | 院长陈大岳在北大数院2023年开学典礼上的致辞', 'update_time': 1694155365}, {'aid': '2247496084_2', 'album_id': '3095357131987664903', 'appmsg_album_infos': [{'album_id': 3095357131987664903, 'appmsg_album_infos': [], 'id': '3095357131987664903', 'tagSource': 4, 'title': '2023年开学典礼'}], 'appmsgid': 2247496084, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNVz44ia5vTJyyGwpHYtOYAGppiblWZwzXOUwGibdbA4SURtln1pzULcwCA/0?wx_fmt=jpeg', 'create_time': 1694155365, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496084&idx=2&sn=20e2f417923398e341f4361bf3237737&chksm=fa9f8f58cde8064ed3aa8c63c1af19235caa15b0eed854cc073e98a926a824740df49dd251be#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '教师代表卢朓在北大数院2023年开学典礼上的发言', 'update_time': 1694155365}, {'aid': '2247496084_3', 'album_id': '3095357131987664903', 'appmsg_album_infos': [{'album_id': 3095357131987664903, 'appmsg_album_infos': [], 'id': '3095357131987664903', 'tagSource': 4, 'title': '2023年开学典礼'}], 'appmsgid': 2247496084, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSN7Jianticz4xp7UrT1DwJaWSSib0QibXNbOL7R7RJiac2XnHjs2q8TIc87Wg/0?wx_fmt=jpeg', 'create_time': 1694155365, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496084&idx=3&sn=224410866f1e5280d3edd9ceb3f63242&chksm=fa9f8f58cde8064ecbbc3553b593dc2cfcf595943dd6a7109094f69573e8e99b1a15855f010b#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '院友代表于品在北大数院2023年开学典礼上的发言', 'update_time': 1694155365}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
110周年庆 | 概率论与随机分析国际会议 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496175&idx=1&sn=2ad3bb7920f66bcfd066cdbc7c1ef6a8&chksm=fa9f8f23cde80635f990a91c58a8b9713e943323e866d81582f241d450b3698dd14d0207e0f6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
110周年庆·杰出学者报告 | 南开大学张伟平院士 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496160&idx=1&sn=4fa32438d247ba4f2b3550a823cbd2d2&chksm=fa9f8f2ccde8063a8b2bb40c6afaed84cd17459808f45b9f1e8eb12b2d7236a8a63c7d957e13#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
《北京数学杂志（英文）》2023年在线出版文章速递（五） http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496160&idx=2&sn=b5a127d3bb6b664e78225c2cf71f484a&chksm=fa9f8f2ccde8063a56504f1554cddd33e08587613aad9c3b76500760d7733dc4f40bb444707e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学数学科学学院祝老师们教师节快乐 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496151&idx=1&sn=64eec049d84a241d97faef1d6bfe5ba0&chksm=fa9f8f1bcde8060d14f683082066e65388877f8a7a997d058d5cfa07c83600a89a9254563ce5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告 | 北大数学一周学术报告一览（09.11-09.17） http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496151&idx=2&sn=4c1fb084ca1c8851016a9eeb7815147e&chksm=fa9f8f1bcde8060dae49bc0f4f8a73ad110ac25b3dce28d7197f0c29f5049c71e58b19d49fe5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本科生新生代表胡殊闻在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496108&idx=1&sn=62e9797fc63d588d86050624d815fe27&chksm=fa9f8f60cde806761583d06fceb28012ef8b805de71081c4675774bac586cd5f717c6cd0e7ef#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
硕士研究生新生代表王楚凡在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496108&idx=2&sn=bcdc033ab99f8e9129d0430cb7c66bbc&chksm=fa9f8f60cde8067680aaecf972419beeee57974a140b1c6fa89a87ca5fcdb4f1561d73972484#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
博士研究生新生代表史庭潇在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496108&idx=3&sn=2eb5fc8b4b80c53003c5c718ff4924f4&chksm=fa9f8f60cde806767c444e576a1dc05de8bdd6861f8509d730bf402cf3439bd37015ebd404ca#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
老生代表杨晨曦在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496108&idx=4&sn=c08cf22a6aebbd50e5c268c500eae571&chksm=fa9f8f60cde80676ec64e58301534508cae1274e792b19486f494c313ba8cda15bb6f1f76976#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
培养更多数学拔尖人才 | 院长陈大岳在北大数院2023年开学典礼上的致辞 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496084&idx=1&sn=13936e2ee124b289d3e3ea71ee1af376&chksm=fa9f8f58cde8064e38b3047998086ea5fdef872f9e34c1b9c4c890c264be22841bffb21f0fe6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教师代表卢朓在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496084&idx=2&sn=20e2f417923398e341f4361bf3237737&chksm=fa9f8f58cde8064ed3aa8c63c1af19235caa15b0eed854cc073e98a926a824740df49dd251be#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
院友代表于品在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzUzMzg4MzgxMQ==&mid=2247496084&idx=3&sn=224410866f1e5280d3edd9ceb3f63242&chksm=fa9f8f58cde8064ecbbc3553b593dc2cfcf595943dd6a7109094f69573e8e99b1a15855f010b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
pku数学系 MzkxNTM1MjU5Mw==
sleep 280
<Response [200]>
dic: {'app_msg_cnt': 280, 'app_msg_list': [{'aid': '2247486640_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486640, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/VF4eJICZxquPCgsm0PLX4F1YA1c4IHYl7picygicwj7psYgZU4ehaS6kzE2GUsTw3aJTM55z8jES8rmCSZeRphqQ/0?wx_fmt=jpeg', 'create_time': 1694411598, 'digest': '数学科学学院数学系一周学术报告预告，等你来听！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486640&idx=1&sn=d670158e3dab1d5f28c40ef2543d774f&chksm=c16131cef616b8d875dca3ca4e981d981fa092dd5f543af8d1c7e071a927248696c52c5be509#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告 | 数学系一周学术报告汇总', 'update_time': 1694411880}, {'aid': '2247486634_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486634, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/VF4eJICZxqu79ibdD8s2E1gBJ0PZLs9lVibPJibBkddXKHT01emIRfffEsh9a5qmaqicIMhUV2FP2fjqic5XHu8Igag/0?wx_fmt=jpeg', 'create_time': 1693965453, 'digest': '数学科学学院数学系一周学术报告预告，等你来听！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486634&idx=1&sn=564d011b67c2eed35ad2ed8f32a6e660&chksm=c16131d4f616b8c2af9c12a3cad7d2fea9b5afb093212deab4b09e1ae0ab35e063c3ca62876d#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告 | 数学系一周学术报告汇总', 'update_time': 1693965720}, {'aid': '2247486628_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486628, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/VF4eJICZxqu5Bnd5FuBibaHGR2Rvic2jYDjWYOy2qMx8eBxuT89vlxShicUwEFia845LKQHmRggrJmrjYHnv1ibsFeA/0?wx_fmt=jpeg', 'create_time': 1688950679, 'digest': '数学科学学院数学系一周学术报告预告，等你来听！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486628&idx=1&sn=5975df539e06636551b8176b08d86b0f&chksm=c16131daf616b8ccc41975f48ab37588223c738ca3baf9c211c0d2d2a69046c346b47fb91f78#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告 | 数学系一周学术报告汇总', 'update_time': 1688950679}, {'aid': '2247486615_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486615, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/VF4eJICZxquNgjzUvAmsUevvBLqOMv48AB0ttNPtUfqGhUQiaHOIKrGV1jm9VXxHUiafKuhah73oS1xibxaxiaQDjg/0?wx_fmt=jpeg', 'create_time': 1688525841, 'digest': '本周又有新报告了，欢迎各位老师和同学参加~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486615&idx=1&sn=d8dfb7a09681f9df3c63cb4f68eb7dc5&chksm=c16131e9f616b8ff390399f989880f7709ed699541c10fde3f4c0ed52d3e656bfb2586153b78#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告 | 数学系本周新增学术报告', 'update_time': 1688526120}, {'aid': '2247486609_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486609, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/VF4eJICZxqvqqpqxXnU46q6185iaCso43y9oEllka9yiavKiafSIEhAGZcM7MRRaia4NFCqxwiaEt9tkibNs0eEo6faw/0?wx_fmt=jpeg', 'create_time': 1688271404, 'digest': '数学科学学院数学系一周学术报告预告，等你来听！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486609&idx=1&sn=0c2de7f170f5d1e70c7e4267965ebe48&chksm=c16131eff616b8f973219c0aac73f856b4ac86c585f10613f90b7609ca9f7a8f4b15dea66984#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告 | 数学系一周学术报告汇总', 'update_time': 1688271660}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
讲座预告 | 数学系一周学术报告汇总 http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486640&idx=1&sn=d670158e3dab1d5f28c40ef2543d774f&chksm=c16131cef616b8d875dca3ca4e981d981fa092dd5f543af8d1c7e071a927248696c52c5be509#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告 | 数学系一周学术报告汇总 http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486634&idx=1&sn=564d011b67c2eed35ad2ed8f32a6e660&chksm=c16131d4f616b8c2af9c12a3cad7d2fea9b5afb093212deab4b09e1ae0ab35e063c3ca62876d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告 | 数学系一周学术报告汇总 http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486628&idx=1&sn=5975df539e06636551b8176b08d86b0f&chksm=c16131daf616b8ccc41975f48ab37588223c738ca3baf9c211c0d2d2a69046c346b47fb91f78#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告 | 数学系本周新增学术报告 http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486615&idx=1&sn=d8dfb7a09681f9df3c63cb4f68eb7dc5&chksm=c16131e9f616b8ff390399f989880f7709ed699541c10fde3f4c0ed52d3e656bfb2586153b78#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告 | 数学系一周学术报告汇总 http://mp.weixin.qq.com/s?__biz=MzkxNTM1MjU5Mw==&mid=2247486609&idx=1&sn=0c2de7f170f5d1e70c7e4267965ebe48&chksm=c16131eff616b8f973219c0aac73f856b4ac86c585f10613f90b7609ca9f7a8f4b15dea66984#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
P大CoE教务 MzI4OTYxMzkyOA==
sleep 249
<Response [200]>
dic: {'app_msg_cnt': 390, 'app_msg_list': [{'aid': '2247489954_1', 'album_id': '1980042326395715585', 'appmsg_album_infos': [{'album_id': 1980042326395715585, 'appmsg_album_infos': [], 'id': '1980042326395715585', 'tagSource': 4, 'title': '本科生通知'}], 'appmsgid': 2247489954, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/R17pLE8xoENnrppdxyjGJc73Pz09GPiaTu3micMF4yr9KUSllwxyxnCoAUs9kW2EiaxrvP6IqRhfYQBUaFWjn9NWg/0?wx_fmt=jpeg', 'create_time': 1694591201, 'digest': '2022年立项本科生科研项目结题工作及优秀项目评选的通知', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489954&idx=1&sn=fb3bfc260d1aaa5ee488da076b35b4ae&chksm=ec2d28a5db5aa1b31d37047e093eeda63080cd9df93482a7997630f3b36bfbb54446fc869251#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '本科生科研 | 2022年立项项目目结题工作及优秀项目评选的通知', 'update_time': 1694591201}, {'aid': '2247489946_1', 'album_id': '2046688859479998465', 'appmsg_album_infos': [{'album_id': 2046688859479998465, 'appmsg_album_infos': [], 'id': '2046688859479998465', 'tagSource': 4, 'title': '现代工学通论'}], 'appmsgid': 2247489946, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/R17pLE8xoEMV3qtDf8dZ8kicvNOIRnC8IQgA9g3hzHtOTyTNIv4eXD1GXib1sUzSEOU5o1fPAHx0abg8NM7aOiccg/0?wx_fmt=jpeg', 'create_time': 1694418280, 'digest': '现代工学通论', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489946&idx=1&sn=8315f67668fc013a03d597a7693cef2e&chksm=ec2d289ddb5aa18bf97f8a9698051725e3bd93dd6167e32f0de9530e0481e6c9c3c0237d71ae#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '本科生 | 预告 · 现代工学通论（2023-1）', 'update_time': 1694418279}, {'aid': '2247489937_1', 'album_id': '1553828835706667013', 'appmsg_album_infos': [{'album_id': 1553828835706667013, 'appmsg_album_infos': [], 'id': '1553828835706667013', 'tagSource': 1, 'title': '培养方案'}], 'appmsgid': 2247489937, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/R17pLE8xoEMFR51ID6EQ9iaMooptI5DynAcyFmCGzpwPIshLibwAIWKGw2Xaskj5ibYGRBLgI9SklEGrO0DB6Udqg/0?wx_fmt=jpeg', 'create_time': 1694169665, 'digest': '读懂工院本科培养方案只需要搞明白四大类型', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489937&idx=1&sn=7b11433c11f9ca13ee5ce36ce63519be&chksm=ec2d2896db5aa1802b5d5d4e89e559321c67a2e51c7e29b47f82e8158e04638001b3812d86e3#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '本科生 | 读懂工院本科培养方案', 'update_time': 1694169665}, {'aid': '2247489937_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247489937, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/R17pLE8xoEMFR51ID6EQ9iaMooptI5DynTmh1eYtcAP5THtgIhUJx4KtDIJrl9LNu15BLI2BLbJxEZ9LrloicicEQ/0?wx_fmt=jpeg', 'create_time': 1694169665, 'digest': '2023级本科新生图像采集的通知', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489937&idx=2&sn=e2dfe25375e9c63eb74881716720eb3f&chksm=ec2d2896db5aa18029359e9c4f129bbb7276a4f348724d99274aa8e56ef2ecaef1c97218924f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '本科生 | 关于2023级本科新生图像采集的通知', 'update_time': 1694169665}, {'aid': '2247489905_1', 'album_id': '2131089677435666432', 'appmsg_album_infos': [{'album_id': 2131089677435666432, 'appmsg_album_infos': [], 'id': '2131089677435666432', 'tagSource': 4, 'title': '招生'}], 'appmsgid': 2247489905, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/R17pLE8xoENDia2XT0STmz60cyiay8q1u7LPsLFwfK9dG4SZdrux8actAgv3DXlPwrYMwDDwqraC1r4P0QZOqseg/0?wx_fmt=jpeg', 'create_time': 1693806251, 'digest': '推免系统开放时间9月4日-9月8日16:00', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489905&idx=1&sn=918dcd9b814349c4d6971dac5d8ca9ac&chksm=ec2d2876db5aa160a7d47378c58cc18d98e2fa8cf4884666ba9f4be733b190329ec1f0f47413#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '研招 | 北京大学工学院2024年接收推免生说明', 'update_time': 1693806251}, {'aid': '2247489905_2', 'album_id': '2131089677435666432', 'appmsg_album_infos': [{'album_id': 2131089677435666432, 'appmsg_album_infos': [], 'id': '2131089677435666432', 'tagSource': 4, 'title': '招生'}], 'appmsgid': 2247489905, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/R17pLE8xoENDia2XT0STmz60cyiay8q1u7n2ibJwd10NTRCAs8Dicicmyp4obofhdeibHzBXue6R4H8odSCFGeYjUj9A/0?wx_fmt=jpeg', 'create_time': 1693806251, 'digest': '机械专业全日制直博', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489905&idx=2&sn=54f54e5631ae5351b7d0adc1aff89b86&chksm=ec2d2876db5aa160a01df271cd54083a5e28886babc70ec271fe801490aef43abc9cf00272de#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '研招 | 北京大学2024年工程博士培养改革专项研究生招生说明', 'update_time': 1693806251}, {'aid': '2247489862_1', 'album_id': '1980042326395715585', 'appmsg_album_infos': [{'album_id': 1980042326395715585, 'appmsg_album_infos': [], 'id': '1980042326395715585', 'tagSource': 4, 'title': '本科生通知'}], 'appmsgid': 2247489862, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/R17pLE8xoEMFzaZIgfVdftmV6HDcqkOOg6TYK7Wv2oYN0Z68iciak2lT851GNubDGlzKNdbLX3Oa26zfx0ODRbxQ/0?wx_fmt=jpeg', 'create_time': 1693550550, 'digest': '2023-2024学年第一学期在校本科生注册通知', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489862&idx=1&sn=6918031bea57432bd6867f3fad3835d1&chksm=ec2d2841db5aa1571b6c154d751ade06b535227fffb90af3c6bad7323c4d29f31e91430b2800#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '本科生 | 2023-2024学年第一学期在校本科生注册通知', 'update_time': 1693550550}, {'aid': '2247489862_2', 'album_id': '1918188990822744072', 'appmsg_album_infos': [{'album_id': 1918188990822744072, 'appmsg_album_infos': [], 'id': '1918188990822744072', 'tagSource': 4, 'title': '研究生通知'}], 'appmsgid': 2247489862, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/R17pLE8xoEMFzaZIgfVdftmV6HDcqkOO71LUq7g7SX3Wh4n6ksQTg4BMpaib1jtrBwZxvbC4j1XoRuTVE6PvIvg/0?wx_fmt=jpeg', 'create_time': 1693550550, 'digest': '2023-2024学年第一学期学术型在校研究生注册工作的通知', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489862&idx=2&sn=23d2735b963f88ab8b4840ae7706eb8a&chksm=ec2d2841db5aa1571d60de54a55135af497c50ed87d89230364659d0ad95f2f82f4d41d66b5e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '研究生 | 2023-2024学年第一学期学术型在校研究生注册工作的通知', 'update_time': 1693550550}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
本科生科研 | 2022年立项项目目结题工作及优秀项目评选的通知 http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489954&idx=1&sn=fb3bfc260d1aaa5ee488da076b35b4ae&chksm=ec2d28a5db5aa1b31d37047e093eeda63080cd9df93482a7997630f3b36bfbb54446fc869251#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本科生 | 预告 · 现代工学通论（2023-1） http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489946&idx=1&sn=8315f67668fc013a03d597a7693cef2e&chksm=ec2d289ddb5aa18bf97f8a9698051725e3bd93dd6167e32f0de9530e0481e6c9c3c0237d71ae#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本科生 | 读懂工院本科培养方案 http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489937&idx=1&sn=7b11433c11f9ca13ee5ce36ce63519be&chksm=ec2d2896db5aa1802b5d5d4e89e559321c67a2e51c7e29b47f82e8158e04638001b3812d86e3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本科生 | 关于2023级本科新生图像采集的通知 http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489937&idx=2&sn=e2dfe25375e9c63eb74881716720eb3f&chksm=ec2d2896db5aa18029359e9c4f129bbb7276a4f348724d99274aa8e56ef2ecaef1c97218924f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
研招 | 北京大学工学院2024年接收推免生说明 http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489905&idx=1&sn=918dcd9b814349c4d6971dac5d8ca9ac&chksm=ec2d2876db5aa160a7d47378c58cc18d98e2fa8cf4884666ba9f4be733b190329ec1f0f47413#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
研招 | 北京大学2024年工程博士培养改革专项研究生招生说明 http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489905&idx=2&sn=54f54e5631ae5351b7d0adc1aff89b86&chksm=ec2d2876db5aa160a01df271cd54083a5e28886babc70ec271fe801490aef43abc9cf00272de#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本科生 | 2023-2024学年第一学期在校本科生注册通知 http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489862&idx=1&sn=6918031bea57432bd6867f3fad3835d1&chksm=ec2d2841db5aa1571b6c154d751ade06b535227fffb90af3c6bad7323c4d29f31e91430b2800#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
研究生 | 2023-2024学年第一学期学术型在校研究生注册工作的通知 http://mp.weixin.qq.com/s?__biz=MzI4OTYxMzkyOA==&mid=2247489862&idx=2&sn=23d2735b963f88ab8b4840ae7706eb8a&chksm=ec2d2841db5aa1571d60de54a55135af497c50ed87d89230364659d0ad95f2f82f4d41d66b5e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学中文系 MzI0ODcwNjkwNw==
sleep 193
<Response [200]>
dic: {'app_msg_cnt': 437, 'app_msg_list': [{'aid': '2247496122_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247496122, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/zgWANhYRuGqCOCEE4BwiaibibqRFgqXLibEzjTP10PXnUSib0AFT7SqRzia46S76NGCicWef9ibqVPRKFIgiadfAHMkxx9w/0?wx_fmt=jpeg', 'create_time': 1694651060, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496122&idx=1&sn=6d25d8aabb07d55fb40ff2a96dfb84e0&chksm=e99e138edee99a98b59b130e9a96fc162d5995d69eab25bb7a935a69f109dbf65d64f5651681#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 教师代表张辉：读书人的本色', 'update_time': 1694656800}, {'aid': '2247496122_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247496122, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/zgWANhYRuGricm7Qy4OzQX7QRPapC1es62yNOJCZZxfo6Ljicfbrp2ItvMU4ZZ5c0XrQrhDANIH8YaO3BjNvWLCQ/0?wx_fmt=jpeg', 'create_time': 1694651060, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496122&idx=2&sn=76cfd202d629df0c89815b1947a63d01&chksm=e99e138edee99a98cb94167c97e3366ddeb40a73802098b6750014b54bb121e1eb3cc00a7d4d#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 本科生新生代表黄臻：在中文系2023年开学典礼上的发言', 'update_time': 1694656800}, {'aid': '2247496122_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247496122, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/zgWANhYRuGricm7Qy4OzQX7QRPapC1es6Ua46ZmXVLtS82VwAiboSFXQUZWLR32c3XzB3UOzVPVnOnV5cdfjYKLg/0?wx_fmt=jpeg', 'create_time': 1694651060, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496122&idx=3&sn=9636568e678530c2c7d9894a1f3f9607&chksm=e99e138edee99a98fe5ead638b75ddeebfde2a590bbf99454940eaa5c4fe181f1b190082da79#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 研究生新生代表赵炳亮：行走在星空与大地之间', 'update_time': 1694656800}, {'aid': '2247496122_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247496122, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/zgWANhYRuGricm7Qy4OzQX7QRPapC1es6975ic02r39Ij6bSbxJzI3zBojdDcJqNxGHsDbs8aoayUBcUorcLKpicA/0?wx_fmt=jpeg', 'create_time': 1694651060, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496122&idx=4&sn=b45f58075beac52740885e95169983b9&chksm=e99e138edee99a9834bdf86f51722414f460d62fd51ca2ff24479ba3e5f644921c86ab2bee62#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 在校生代表蔡千千：在中文系2023年开学典礼上的发言', 'update_time': 1694656800}, {'aid': '2247496077_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247496077, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/zgWANhYRuGoJzvDwriaSh8W940rzIKcjJiaAOCDIka64ya7NFstVz7MQH8gH77bN9O9CksJ98PoGv5mR7uwwf9pw/0?wx_fmt=jpeg', 'create_time': 1694502328, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496077&idx=1&sn=56df9839678115ef05b41c710ea5477b&chksm=e99e13b9dee99aafb2699a40556ebeed64898fefed74fd5607dc2f12124c5ecf09b30149fed3#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '北京大学中国语言文学系举办2023年开学典礼', 'update_time': 1694502328}, {'aid': '2247496077_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247496077, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/zgWANhYRuGoJzvDwriaSh8W940rzIKcjJ3iaxyz29vnApIo9uLQkyicLyhwZ45EjJQzKScT8ST0edRwwOxbC5QIicg/0?wx_fmt=jpeg', 'create_time': 1694502328, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496077&idx=2&sn=ad842f0da5ddcea99bfe03f2bb47c876&chksm=e99e13b9dee99aaf0d2638c87b8e192297f96078a50f27c4b519a4a237054d96096bb0d816ef#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 系主任杜晓勤：问学·问难·问道', 'update_time': 1694502328}, {'aid': '2247495963_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247495963, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/zgWANhYRuGpq007xH1AKSQosia2AfzBtp2CuvkXNxjdWzWu38ibAxlMVKcW8TP7AnIhTwdqk4clakU68t3zICHpw/0?wx_fmt=jpeg', 'create_time': 1694308371, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247495963&idx=1&sn=ba64924cc0f377ba861b0be5dd6a1b14&chksm=e99e132fdee99a397994f1a14007a759b83814fdd0ac802971674c4dd0d3a0016eaceb175d79#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '教师节 | 热烈祝贺中文系教师获得系列教学奖', 'update_time': 1694311200}, {'aid': '2247495962_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247495962, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/zgWANhYRuGqzR0Tpniaib4icUyb0bZic7qKQrv6libAucicBdRQWY4XdeYMaI0ff2lzcaS6YYZvmO5gE2SmZasx7IpqA/0?wx_fmt=jpeg', 'create_time': 1694231902, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247495962&idx=1&sn=7c1337fff4e71bca56bc58e1f648c129&chksm=e99e132edee99a389cd790d87cea38e88b72ed4e87456ab43ca021e67a1da18d0e389614c78c#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告 | 宋刚：神力之争：晚明中西文化相遇中的神迹故事', 'update_time': 1694231902}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
开学典礼 | 教师代表张辉：读书人的本色 http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496122&idx=1&sn=6d25d8aabb07d55fb40ff2a96dfb84e0&chksm=e99e138edee99a98b59b130e9a96fc162d5995d69eab25bb7a935a69f109dbf65d64f5651681#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 本科生新生代表黄臻：在中文系2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496122&idx=2&sn=76cfd202d629df0c89815b1947a63d01&chksm=e99e138edee99a98cb94167c97e3366ddeb40a73802098b6750014b54bb121e1eb3cc00a7d4d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 研究生新生代表赵炳亮：行走在星空与大地之间 http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496122&idx=3&sn=9636568e678530c2c7d9894a1f3f9607&chksm=e99e138edee99a98fe5ead638b75ddeebfde2a590bbf99454940eaa5c4fe181f1b190082da79#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 在校生代表蔡千千：在中文系2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496122&idx=4&sn=b45f58075beac52740885e95169983b9&chksm=e99e138edee99a9834bdf86f51722414f460d62fd51ca2ff24479ba3e5f644921c86ab2bee62#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学中国语言文学系举办2023年开学典礼 http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496077&idx=1&sn=56df9839678115ef05b41c710ea5477b&chksm=e99e13b9dee99aafb2699a40556ebeed64898fefed74fd5607dc2f12124c5ecf09b30149fed3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 系主任杜晓勤：问学·问难·问道 http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247496077&idx=2&sn=ad842f0da5ddcea99bfe03f2bb47c876&chksm=e99e13b9dee99aaf0d2638c87b8e192297f96078a50f27c4b519a4a237054d96096bb0d816ef#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教师节 | 热烈祝贺中文系教师获得系列教学奖 http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247495963&idx=1&sn=ba64924cc0f377ba861b0be5dd6a1b14&chksm=e99e132fdee99a397994f1a14007a759b83814fdd0ac802971674c4dd0d3a0016eaceb175d79#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告 | 宋刚：神力之争：晚明中西文化相遇中的神迹故事 http://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247495962&idx=1&sn=7c1337fff4e71bca56bc58e1f648c129&chksm=e99e132edee99a389cd790d87cea38e88b72ed4e87456ab43ca021e67a1da18d0e389614c78c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大社会学 MzkxMzMxMzQ2NQ==
sleep 322
<Response [200]>
dic: {'app_msg_cnt': 161, 'app_msg_list': [{'aid': '2247488384_1', 'album_id': '2998055354922090497', 'appmsg_album_infos': [{'album_id': 2998055354922090497, 'appmsg_album_infos': [], 'id': '2998055354922090497', 'tagSource': 5, 'title': '北大社会学刊'}], 'appmsgid': 2247488384, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/2tPksG6xqozvic1nwTkzx7QuSJ4frtZGXucE17MbeOySzUSibgUe22Jrq5B1UGzGp8yVcCuiaXFXLMmDHN9sBPUhA/0?wx_fmt=jpeg', 'create_time': 1694338026, 'digest': '城市居住空间分布形态是城市社会学的一个核心议题。探究当代中国城市居住空间分布形态及其形成机制，对于我们理解当今中国社会的运行逻辑具有重要意义。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488384&idx=1&sn=1f62e9f9c972f88bee33b87522551a3b&chksm=c17ec856f6094140f914a35afed90cbfec3b981b324c24e483d1ab47906bf369c089a9c58819#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '北大社会学刊 | 孙秀林：当代中国城市居住模式的空间结构与动力机制', 'update_time': 1694343600}, {'aid': '2247488301_1', 'album_id': '3017196194890170371', 'appmsg_album_infos': [{'album_id': 3017196194890170371, 'appmsg_album_infos': [], 'id': '3017196194890170371', 'tagSource': 4, 'title': '先声'}], 'appmsgid': 2247488301, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/2tPksG6xqoxNatk9S6wUX9cfiaib83Ja1fHjAt26WTg46SuyP9kiaD1HmSpgUBuEV2p6iaJ8b06QlVfSxBTOyHwt1g/0?wx_fmt=jpeg', 'create_time': 1693727581, 'digest': '廖泰初提出，应超越纸笔问答式的问卷调查、搁置现实的档案研究以及缺乏深度的谈话式调查，而应以“居住调查法”为了解农村社会的调查方法，在同吃、同住、同劳动的过程中，以热烈之参与、冷静之观察，求得真切、整体而鲜活的社会事实。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488301&idx=1&sn=658bc56f84910fc416582f5eac8e92d3&chksm=c17ec8fbf60941edc8abb22a170984df9568d9c8c18091d3e4bd321659b806e620f3b596ab46#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '先声 | 廖泰初：从定县的经验说到农村社会调查的缺欠和补救的方法', 'update_time': 1693738800}, {'aid': '2247488287_1', 'album_id': '2998055354922090497', 'appmsg_album_infos': [{'album_id': 2998055354922090497, 'appmsg_album_infos': [], 'id': '2998055354922090497', 'tagSource': 4, 'title': '北大社会学刊'}], 'appmsgid': 2247488287, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/2tPksG6xqowQic4DUFkToDB9ch18YlV0PJiaxey5rwlSXicjClKYhOgdeeHbPvAxyGYfavlTWwJXgE6aa4kbInfHQ/0?wx_fmt=jpeg', 'create_time': 1693132173, 'digest': '本文从自我、对象、互动、制度四个方面探讨了影响团结形成的主要机制和因素，总结了现有文献的研究成果，也指出了现有文献所忽视的问题和存在的盲点。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488287&idx=1&sn=29371ea1cba7243e27fe1aa3c2d8a50e&chksm=c17ec8c9f60941df5757071f4d96f506aeb3c81469f4778dd78dacd3607bc50c53abf355502e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '北大社会学刊 | 陶林：社会团结的概念及其发生机制——国外研究文献评述', 'update_time': 1693134000}, {'aid': '2247488258_1', 'album_id': '3042844296271544321', 'appmsg_album_infos': [{'album_id': 3042844296271544321, 'appmsg_album_infos': [], 'id': '3042844296271544321', 'tagSource': 4, 'title': '砥行'}], 'appmsgid': 2247488258, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/2tPksG6xqoz0SwR7r4woArXaRTfGUFa33LkkR2zQiaricfhM77mCIsa8gsZicCAmbkm0RhVrmf7FBva0C0aSMZmVQ/0?wx_fmt=jpeg', 'create_time': 1692522525, 'digest': '本文立足2021年夏季对甘肃省兰州市圭行县的田野访谈，试图对当地的高原夏菜产业的源起、历史、现状进行概括与梳理，选取作为重要生产场域的菜库与作为农产品生产者的菜农为核心内容展开分析。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488258&idx=1&sn=dc056d9c95a710e9a33c7dfe00d97cf8&chksm=c17ec8d4f60941c2c54c6cbacf1e37eb3352a69c7e6fcae22213c272c418b029c265889de794#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '砥行 | 白雨琪：庞然的菜库与踟蹰的菜农——基于甘肃圭行的经验研究', 'update_time': 1692529200}, {'aid': '2247488238_1', 'album_id': '3017196194890170371', 'appmsg_album_infos': [{'album_id': 3017196194890170371, 'appmsg_album_infos': [], 'id': '3017196194890170371', 'tagSource': 4, 'title': '先声'}], 'appmsgid': 2247488238, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/2tPksG6xqozz4RfO6ib4tiawDuqoibvrVSkWSWXFu5gJ4PuQ4yIHCOEU8ldGxj46bib8u5TeicfP0j7haGuq47Y7IAA/0?wx_fmt=jpeg', 'create_time': 1691924486, 'digest': '吴文藻于本文中系统地整理了彼时社会调查、民族志以及社区研究三类实地研究的发展情况。在此基础上，吴文藻提出，“中国社会学者今后最重要的一部分工作，即在迅速的、有计划的进行现代社区的实地研究，对于各地方的事实材料，作系统而详尽的搜集”。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488238&idx=1&sn=a81a4ecb359545faa83c06cbf08e85c2&chksm=c17ec938f609402e4805ce9f4829185cc56c88a0ddf1da7869c6e404b00249e5cbbde9b6eba5#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '先声 | 吴文藻：中国社区研究的西洋影响与国内近状', 'update_time': 1691924486}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
北大社会学刊 | 孙秀林：当代中国城市居住模式的空间结构与动力机制 http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488384&idx=1&sn=1f62e9f9c972f88bee33b87522551a3b&chksm=c17ec856f6094140f914a35afed90cbfec3b981b324c24e483d1ab47906bf369c089a9c58819#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
先声 | 廖泰初：从定县的经验说到农村社会调查的缺欠和补救的方法 http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488301&idx=1&sn=658bc56f84910fc416582f5eac8e92d3&chksm=c17ec8fbf60941edc8abb22a170984df9568d9c8c18091d3e4bd321659b806e620f3b596ab46#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大社会学刊 | 陶林：社会团结的概念及其发生机制——国外研究文献评述 http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488287&idx=1&sn=29371ea1cba7243e27fe1aa3c2d8a50e&chksm=c17ec8c9f60941df5757071f4d96f506aeb3c81469f4778dd78dacd3607bc50c53abf355502e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
砥行 | 白雨琪：庞然的菜库与踟蹰的菜农——基于甘肃圭行的经验研究 http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488258&idx=1&sn=dc056d9c95a710e9a33c7dfe00d97cf8&chksm=c17ec8d4f60941c2c54c6cbacf1e37eb3352a69c7e6fcae22213c272c418b029c265889de794#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
先声 | 吴文藻：中国社区研究的西洋影响与国内近状 http://mp.weixin.qq.com/s?__biz=MzkxMzMxMzQ2NQ==&mid=2247488238&idx=1&sn=a81a4ecb359545faa83c06cbf08e85c2&chksm=c17ec938f609402e4805ce9f4829185cc56c88a0ddf1da7869c6e404b00249e5cbbde9b6eba5#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学智能学院 Mzk0NDE3ODg5Nw==
sleep 100
<Response [200]>
dic: {'app_msg_cnt': 334, 'app_msg_list': [{'aid': '2247488959_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247488959, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/tNVx3TaaVWGvu2Pguff6UCl1qGoYZbUu6M0ONyAN1hteGkBAdqgaVs3tCJqzP7CqxrYKNGMIa5Yiaibz8c2iaDcFQ/0?wx_fmt=jpeg', 'create_time': 1694739445, 'digest': '硕士班学生代表蒋济懋在北京大学智能学院2023年开学典礼发言。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488959&idx=1&sn=4b0eafbbac589bad5639ea325f0b3e07&chksm=c329c601f45e4f173de9f63617bc6fdba218b76a09110371fcfda3f558c4c96b347ee7f6b28a#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': 'SIST迎新 | 蒋济懋：北京大学智能学院2023年开学典礼学生代表发言', 'update_time': 1694739445}, {'aid': '2247488958_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247488958, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/tNVx3TaaVWGvu2Pguff6UCl1qGoYZbUunCR2XeQGicvw0NpHAE4FAwq1KEqawiaM4TP31icC7xCrrOgr2CIh4sHmw/0?wx_fmt=jpeg', 'create_time': 1694651558, 'digest': '北京大学智能学院2023级博士班学生代表钟伊凡在开学典礼的发言。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488958&idx=1&sn=ed06ca234f4637e13a278f8e3813613f&chksm=c329c600f45e4f16b2fcd1a3d0f00584b6981e19f6aaa74fd4cfcbdb3bb196904374605e04e6#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': 'SIST迎新 | 钟伊凡：北京大学智能学院2023年开学典礼学生代表发言', 'update_time': 1694651558}, {'aid': '2247488957_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247488957, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/tNVx3TaaVWGvu2Pguff6UCl1qGoYZbUu8lXp81JvHsToiaAZQ1rw0dMiafdSu4NWWufzfE6oWR3K0SLCmfgrmYPw/0?wx_fmt=jpeg', 'create_time': 1694565577, 'digest': '教师代表张牧涵在北京大学智能学院2023年开学典礼上的发言。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488957&idx=1&sn=8f1bf4cbaba62de7528a6cc73e3d1df6&chksm=c329c603f45e4f15cfd38487656c3e4429947284af12be393676a9fba8599bb9bc26fdcb07ed#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': 'SIST迎新 | 教师代表张牧涵在北京大学智能学院2023年开学典礼上的发言', 'update_time': 1694565577}, {'aid': '2247488956_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247488956, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/tNVx3TaaVWGvu2Pguff6UCl1qGoYZbUuwvmvemwicqYy3EWDvCZrHFNesrua5JU9uLY1ta8c19gxXofJ3M1X7Aw/0?wx_fmt=jpeg', 'create_time': 1694495951, 'digest': '吴玺宏书记在北京大学智能学院2023年开学典礼上的讲话。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488956&idx=1&sn=538515efa95f9ec51315722ddaac6440&chksm=c329c602f45e4f14833875254452e0c15ba66b28c6e23fb14c75ab83fca9e3c7646e0112526d#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': 'SIST迎新 | 吴玺宏书记在北京大学智能学院2023年开学典礼上的讲话', 'update_time': 1694495951}, {'aid': '2247488948_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247488948, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/tNVx3TaaVWGvu2Pguff6UCl1qGoYZbUuVFq4ibibHgjrpEHXv0NdpkoNibNcwFR880IO6uSKUCv3mibKaAcUcbQn4g/0?wx_fmt=jpeg', 'create_time': 1694442079, 'digest': '9月6日下午，北京大学智能学院2023年开学典礼暨开学第一课在北京大学昌平新校区教学楼115举行。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488948&idx=1&sn=b86794f16f791f11080b9e5b35e60755&chksm=c329c60af45e4f1c9632c2b731555ada58557b3209101e7a3c777afb1ca5ff3f9a7ecf918a8f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': 'SIST迎新 | 北京大学智能学院举行2023年开学典礼暨开学第一课', 'update_time': 1694442079}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
SIST迎新 | 蒋济懋：北京大学智能学院2023年开学典礼学生代表发言 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488959&idx=1&sn=4b0eafbbac589bad5639ea325f0b3e07&chksm=c329c601f45e4f173de9f63617bc6fdba218b76a09110371fcfda3f558c4c96b347ee7f6b28a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SIST迎新 | 钟伊凡：北京大学智能学院2023年开学典礼学生代表发言 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488958&idx=1&sn=ed06ca234f4637e13a278f8e3813613f&chksm=c329c600f45e4f16b2fcd1a3d0f00584b6981e19f6aaa74fd4cfcbdb3bb196904374605e04e6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SIST迎新 | 教师代表张牧涵在北京大学智能学院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488957&idx=1&sn=8f1bf4cbaba62de7528a6cc73e3d1df6&chksm=c329c603f45e4f15cfd38487656c3e4429947284af12be393676a9fba8599bb9bc26fdcb07ed#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SIST迎新 | 吴玺宏书记在北京大学智能学院2023年开学典礼上的讲话 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488956&idx=1&sn=538515efa95f9ec51315722ddaac6440&chksm=c329c602f45e4f14833875254452e0c15ba66b28c6e23fb14c75ab83fca9e3c7646e0112526d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SIST迎新 | 北京大学智能学院举行2023年开学典礼暨开学第一课 http://mp.weixin.qq.com/s?__biz=Mzk0NDE3ODg5Nw==&mid=2247488948&idx=1&sn=b86794f16f791f11080b9e5b35e60755&chksm=c329c60af45e4f1c9632c2b731555ada58557b3209101e7a3c777afb1ca5ff3f9a7ecf918a8f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大国发院 MjM5MDIwNDg0MA==
sleep 342
<Response [200]>
dic: {'app_msg_cnt': 2704, 'app_msg_list': [{'aid': '2649902769_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2649902769, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/mF7A0MYeUIH8CiaSreqtQuGHjiaEicDiaQKibq9CNXIDjIRHeyOHrFDvgI5iaHSdJTib27OSfXvvE1CEIKpaEZoiabdDmQ/0?wx_fmt=jpeg', 'create_time': 1694594333, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902769&idx=1&sn=628b661b949bdd21fe93c8f29bdca85b&chksm=be4eb87689393160654e4310640ce8981df6fdd0907ed46018da4f600b68c10d369852c9642b#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '视频全集 | 宫玉振+杨壮+侯宏：变局时代的战略定力与领导力', 'update_time': 1694604660}, {'aid': '2649902769_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2649902769, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/mF7A0MYeUIH8CiaSreqtQuGHjiaEicDiaQKibtNejqKSUsiaSbibmCSicicC58KUkicFv5TiauiaWMYdEgX0og6yaqcfVFYgmQ/0?wx_fmt=jpeg', 'create_time': 1694594333, 'digest': '15日19:30-21:30，欢迎收看直播', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902769&idx=2&sn=f648469be1415b2c1de0ae72698871d8&chksm=be4eb87689393160e7ec8d71628c8dff994a852a04f11a859274d26554cd1dcbe5e7ec664271#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '9.15论坛直播 | 剧变时代的品类创新与战略定位', 'update_time': 1694604660}, {'aid': '2649902750_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2649902750, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/mF7A0MYeUIH77S9UgM0hONO4CriaTNZeNWQMAc0EndW1hocfJFMBLznHicESno80qZ3VTrC4CAdDOw51EmRyktwg/0?wx_fmt=jpeg', 'create_time': 1694496702, 'digest': '欢迎报名', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902750&idx=1&sn=e4a06a4bbecd0d50ca0d33a48aadee1e&chksm=be4eb8598939314f5c7e4312af0d67f9295730d535d6ade0ff0bd3e09faf0ea425c91b0de8e4#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '9.15论坛报名 | 剧变时代的品类创新与战略定位', 'update_time': 1694518560}, {'aid': '2649902741_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2649902741, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/mF7A0MYeUIF8a5z3zCk72tUHZuOA4s2l6UXF6s0T5tYhAuWNSOyQrPUAiaeciakZs2nbYjibTy4AjMuVWX5oknJ4g/0?wx_fmt=jpeg', 'create_time': 1694422034, 'digest': '12日 19:00，欢迎收看', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902741&idx=1&sn=04ed7e176604fcecbaea9cfc04c04f85&chksm=be4eb852893931443f695a14791b764edf1bf3ba180110245e50d41229065ec0e26de0e7fc12#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '9.12讲座预告 | 林毅夫：百年未有大变局加速演进下党的二十大“两大任务”的实现路径', 'update_time': 1694432100}, {'aid': '2649902728_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2649902728, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/mF7A0MYeUIFz5xIz7Zf4zbkQwZebxZCknmMNv0WnF8NrMExvGgnK71cPgUllqnoPAxkC3cTIsicZd0luFnkymsA/0?wx_fmt=jpeg', 'create_time': 1694320426, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902728&idx=1&sn=0d0d78f023ee07431559061b7315178b&chksm=be4eb84f893931593f691638078fc8bb0ecadda1065995a34cf0120f11933427f02d480ed548#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '黄益平：清晰区别调控、监管与市场的功能', 'update_time': 1694320426}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
视频全集 | 宫玉振+杨壮+侯宏：变局时代的战略定力与领导力 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902769&idx=1&sn=628b661b949bdd21fe93c8f29bdca85b&chksm=be4eb87689393160654e4310640ce8981df6fdd0907ed46018da4f600b68c10d369852c9642b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
9.15论坛直播 | 剧变时代的品类创新与战略定位 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902769&idx=2&sn=f648469be1415b2c1de0ae72698871d8&chksm=be4eb87689393160e7ec8d71628c8dff994a852a04f11a859274d26554cd1dcbe5e7ec664271#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
9.15论坛报名 | 剧变时代的品类创新与战略定位 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902750&idx=1&sn=e4a06a4bbecd0d50ca0d33a48aadee1e&chksm=be4eb8598939314f5c7e4312af0d67f9295730d535d6ade0ff0bd3e09faf0ea425c91b0de8e4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
9.12讲座预告 | 林毅夫：百年未有大变局加速演进下党的二十大“两大任务”的实现路径 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902741&idx=1&sn=04ed7e176604fcecbaea9cfc04c04f85&chksm=be4eb852893931443f695a14791b764edf1bf3ba180110245e50d41229065ec0e26de0e7fc12#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
黄益平：清晰区别调控、监管与市场的功能 http://mp.weixin.qq.com/s?__biz=MjM5MDIwNDg0MA==&mid=2649902728&idx=1&sn=0d0d78f023ee07431559061b7315178b&chksm=be4eb84f893931593f691638078fc8bb0ecadda1065995a34cf0120f11933427f02d480ed548#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学公共卫生学院生物统计系 MzU5MDg1ODYyMA==
sleep 206
<Response [200]>
dic: {'app_msg_cnt': 246, 'app_msg_list': [{'aid': '2247491819_1', 'album_id': '2873352876331630593', 'appmsg_album_infos': [{'album_id': 2873352876331630593, 'appmsg_album_infos': [], 'id': '2873352876331630593', 'tagSource': 4, 'title': '太平洋'}], 'appmsgid': 2247491819, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/5D3oUEN9PS8aXsDJHzvia1y0tSWHyMgkJRJuGR9IqDZjibXr1UZZr5cXuEdFHnZrQp7roL9CalK2kYv5EowOwWmw/0?wx_fmt=jpeg', 'create_time': 1694764863, 'digest': '9月16-17中关新园科学报告厅+online，欢迎各位师生参加~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491819&idx=1&sn=f86769f66f75b3a6d4fef1d2a9bd6530&chksm=fe3570f8c942f9ee73cf93d29052853a19c8da4a54bdb1e5ded388f40f02c0c60db75aa0c460#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '线下+线上：2023PCIC泛太平洋因果推断大会倒计时1天', 'update_time': 1694764863}, {'aid': '2247491794_1', 'album_id': '1642251086319124483', 'appmsg_album_infos': [{'album_id': 1642251086319124483, 'appmsg_album_infos': [], 'id': '1642251086319124483', 'tagSource': 4, 'title': '系列学术讲座'}, {'album_id': 1801689339475591177, 'appmsg_album_infos': [], 'id': '1801689339475591177', 'tagSource': 4, 'title': '生物统计'}], 'appmsgid': 2247491794, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/5D3oUEN9PSibASjLRzgR16TqRiaUdtH93q3zwTdN72OY7iaKSKFsaaibibmI2c7IkrtBafd9DBraBEHQaS2CAGHPbeA/0?wx_fmt=jpeg', 'create_time': 1694657557, 'digest': '下周2下午2点北京大学镜春园78号院(怀新园)77201', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491794&idx=1&sn=6383976bee995fbd4ec435e720466dc6&chksm=fe3570c1c942f9d71ff3d66f0d5705fc7f9a9ffca4c13f37404e0083202420a92087801f8d95#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告|(9月19日) ——Theis Lange（University of Copenhagen）', 'update_time': 1694657557}, {'aid': '2247491786_1', 'album_id': '1642251086319124483', 'appmsg_album_infos': [{'album_id': 1642251086319124483, 'appmsg_album_infos': [], 'id': '1642251086319124483', 'tagSource': 4, 'title': '系列学术讲座'}, {'album_id': 1801689339475591177, 'appmsg_album_infos': [], 'id': '1801689339475591177', 'tagSource': 4, 'title': '生物统计'}], 'appmsgid': 2247491786, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/5D3oUEN9PS9MaicvjXDriaKqad8RKiaougqEGnWaOgGQ189kKcY7XRtcPuOsXUNOgR9OP0OvXWpoCvtK8vfxMEjqQ/0?wx_fmt=jpeg', 'create_time': 1694504337, 'digest': '下周1下午2点北京大学全斋9', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491786&idx=1&sn=632d0392c514767f85eccdf8d513b6e4&chksm=fe3570d9c942f9cf3196dc78f73280d99dafad1da886f4b9f17e2a82724e799d307db9a7c9b4#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告|(9月18日) ——Kun Zhang（Carnegie Mellon University & MBZUAI）', 'update_time': 1694504336}, {'aid': '2247491781_1', 'album_id': '1642251086319124483', 'appmsg_album_infos': [{'album_id': 1642251086319124483, 'appmsg_album_infos': [], 'id': '1642251086319124483', 'tagSource': 4, 'title': '系列学术讲座'}, {'album_id': 1801689339475591177, 'appmsg_album_infos': [], 'id': '1801689339475591177', 'tagSource': 4, 'title': '生物统计'}], 'appmsgid': 2247491781, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/5D3oUEN9PSicTw3naNIkHac0RrWyELxuol8ZVWsmXia2UMOo4iawl5m8ZDr4d0iaT8yVsYeUlqicCaFkqytgMWVOMxQ/0?wx_fmt=jpeg', 'create_time': 1694402382, 'digest': '本周5下午2点北京大学全斋9', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491781&idx=1&sn=379952060e9e1498dbd6a31d71e4db2b&chksm=fe3570d6c942f9c0c2f551370aec1ebb7822b2be22002bec958ac536bf529a4276442f162651#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告|(9月15日) ——Mingming Gong（The University of Melbourne）', 'update_time': 1694402381}, {'aid': '2247491775_1', 'album_id': '1642251086319124483', 'appmsg_album_infos': [{'album_id': 1642251086319124483, 'appmsg_album_infos': [], 'id': '1642251086319124483', 'tagSource': 4, 'title': '系列学术讲座'}, {'album_id': 1801689339475591177, 'appmsg_album_infos': [], 'id': '1801689339475591177', 'tagSource': 4, 'title': '生物统计'}], 'appmsgid': 2247491775, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/5D3oUEN9PSibibWsRlKCibnJ9UbRXuaLN0PXd2Pgc44PiaiaicYVuNLNjNLtch2130UdWicLU4icxdDRSw4icA5OnLjjEeQ/0?wx_fmt=jpeg', 'create_time': 1694075587, 'digest': '下周四下午2点北京大学全斋9', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491775&idx=1&sn=7f8ae66da288c72c667ecade4287735a&chksm=fe3570acc942f9ba6d15efb61f2a77089eecac872eedafe5ee68cae2045c4e3e6fb91f052083#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '讲座预告|(9月14日) ——申舒廷（杜克大学）', 'update_time': 1694075587}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
线下+线上：2023PCIC泛太平洋因果推断大会倒计时1天 http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491819&idx=1&sn=f86769f66f75b3a6d4fef1d2a9bd6530&chksm=fe3570f8c942f9ee73cf93d29052853a19c8da4a54bdb1e5ded388f40f02c0c60db75aa0c460#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告|(9月19日) ——Theis Lange（University of Copenhagen） http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491794&idx=1&sn=6383976bee995fbd4ec435e720466dc6&chksm=fe3570c1c942f9d71ff3d66f0d5705fc7f9a9ffca4c13f37404e0083202420a92087801f8d95#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告|(9月18日) ——Kun Zhang（Carnegie Mellon University & MBZUAI） http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491786&idx=1&sn=632d0392c514767f85eccdf8d513b6e4&chksm=fe3570d9c942f9cf3196dc78f73280d99dafad1da886f4b9f17e2a82724e799d307db9a7c9b4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告|(9月15日) ——Mingming Gong（The University of Melbourne） http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491781&idx=1&sn=379952060e9e1498dbd6a31d71e4db2b&chksm=fe3570d6c942f9c0c2f551370aec1ebb7822b2be22002bec958ac536bf529a4276442f162651#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
讲座预告|(9月14日) ——申舒廷（杜克大学） http://mp.weixin.qq.com/s?__biz=MzU5MDg1ODYyMA==&mid=2247491775&idx=1&sn=7f8ae66da288c72c667ecade4287735a&chksm=fe3570acc942f9ba6d15efb61f2a77089eecac872eedafe5ee68cae2045c4e3e6fb91f052083#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学光华管理学院 MjM5MDk3NDgwMQ==
sleep 442
<Response [200]>
dic: {'app_msg_cnt': 1866, 'app_msg_list': [{'aid': '2661400065_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400065, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSpbqoCiaUUrRN7NEcflZMebWObDnlTMy83hwaCibEXYyckSFIND57DLqlERpAAOMXfRzjYlOicxDJSvw/0?wx_fmt=jpeg', 'create_time': 1694769896, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400065&idx=1&sn=ab1b593230330045f838b3d8aef579f9&chksm=bde9883f8a9e0129637cbbdc8e364dd137b6ff6a1a6b09c94e7250a951833bcc7ca6e1d16e8e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '翁翕：成为思想的主人@北大光华2023开学典礼', 'update_time': 1694770200}, {'aid': '2661400065_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400065, 'audio_info': {'audio_infos': [{'audio_id': 'MjM5MDk3NDgwMV81MTM5MTYyODI=', 'masssend_audio_id': 'MjM5MDk3NDgwMV8yNjYxNDAwMDY0', 'play_length': 202, 'title': '燕园情', 'trans_state': 1, 'voice_verify_state': 3}]}, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqaBFsAvuL30Ym2VeoyDXhiaCo6ic94A2m74KdcnPhuNynia52pBcrjV3WuKlOIEJic41UJuL5bLOz6Ww/0?wx_fmt=jpeg', 'create_time': 1694769896, 'digest': '未来更多精彩故事\r\n期待大家共同书写', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400065&idx=2&sn=4a5c9cca027815411a3dfbca32b78532&chksm=bde9883f8a9e012909d1375fc397d8886bdb97a1c28407987a5c289b0c360aa00a44864d62fb#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '你好，光华EMBA新同学！', 'update_time': 1694770200}, {'aid': '2661400020_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400020, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDATLKib71dqNQJuayQNXuRROmhl4h8E2tUDofFOO4uBPgap2L6JUDQ0foA/0?wx_fmt=jpeg', 'create_time': 1694683921, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400020&idx=1&sn=f51e023d44155bb50e4f155b82221055&chksm=bde98bea8a9e02fc400a02103b00e473a6575a282d28891bfa065d532587df3a54a66d76c694#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '郭翔：携笔从戎男儿志，百战归来再读书@北大光华2023开学典礼', 'update_time': 1694683920}, {'aid': '2661400020_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400020, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDAT2EutuKnHZEwsAicBVq3NvgudaAaRP2A7icQaFl0Ex91N49UiaeGUlVvVg/0?wx_fmt=jpeg', 'create_time': 1694683921, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400020&idx=2&sn=f895e9789fc429a7cc651e7c8e7d9299&chksm=bde98bea8a9e02fcea0969971556ef67205b8234b13a1f2dd570fc923d78f735ec9b75293fec#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '张新朝：百战归来再读书，寻找发展的力量@北大光华2023开学典礼', 'update_time': 1694683920}, {'aid': '2661400020_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400020, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDATnp3TdzPCSqdyOYiaXo3sF0ah5U0SdoaMWBMTuwuqwALyMWcE6hRibLNQ/0?wx_fmt=jpeg', 'create_time': 1694683921, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400020&idx=3&sn=d0185f5dab98b2994c7e44b0e8a946e0&chksm=bde98bea8a9e02fc40adfb3f48402ccda9c595cbc35f848784f31a6628dfe4156c0acd9bbe27#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '刘春河：赤子笃行，扬帆向光华@北大光华2023开学典礼', 'update_time': 1694683920}, {'aid': '2661400015_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400015, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDATryGeQtJr6jcic7hgBNGBSmnKF1ic1ibkRVpqDJ71PG01VJVY9r9g9myOA/0?wx_fmt=jpeg', 'create_time': 1694597440, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400015&idx=1&sn=c58d3ad74b514eb46419ac33660d9e39&chksm=bde98bf18a9e02e74d6c27f4d7ec828f221dd2cf70d98e5dd3e54252f397a18cc7f9ff11d86a#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '杨毅：拥抱变化，破局成长@北大光华2023开学典礼', 'update_time': 1694597440}, {'aid': '2661400015_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400015, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDATQibx4GBkLPyRJoFpycDUhTLM9kMeOXmMLeKbqpSrNTILLdCObia5oNIg/0?wx_fmt=jpeg', 'create_time': 1694597440, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400015&idx=2&sn=24272a5b708ca35ac3cd1ce79642d454&chksm=bde98bf18a9e02e73e93eaad526b2928d61e3d7c0846891379038beb8bddecb6acfe35e6a64e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '钱婧涵：拥抱变化，破局成长@北大光华2023开学典礼', 'update_time': 1694597440}, {'aid': '2661400015_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400015, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDATQ2iboxzYNNK9xqYFv1EOopMia228yoCCTlnIiaiaTrpiakOmwShAJsd7WfQ/0?wx_fmt=jpeg', 'create_time': 1694597440, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400015&idx=3&sn=0aca5bf9fa221f1d2afc99ac342e5f4c&chksm=bde98bf18a9e02e7064d0b2bf1adf91e81799f74308cff3a6e51c110aeb7937b94924289abfd#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '佀骅羽：拥抱变化，破局成长@北大光华2023开学典礼', 'update_time': 1694597440}, {'aid': '2661400008_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400008, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDATfVQGQEE0uep9AUXVFRK6gDU58rsZZ6jhoG2o1SdwTzEE5lLDwLLZgQ/0?wx_fmt=jpeg', 'create_time': 1694525609, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=1&sn=075e63369d747a9f7965e94c45bcb2b3&chksm=bde98bf68a9e02e0866614b7563b7df22a918d897686cdfafb14b531628c94629e83bca9ae9b#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '韩靖熙：梦落生花，梦始光华@北大光华2023开学典礼', 'update_time': 1694525609}, {'aid': '2661400008_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400008, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDATHJfVBl9WWnXf2mBwsoXHC31jVS65H9tYBicY5Fg763CSypfWib3YprUg/0?wx_fmt=jpeg', 'create_time': 1694525609, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=2&sn=227999afb9874d4c8c5dc5950d5f3197&chksm=bde98bf68a9e02e01b03968748f6b0095f40dd55b04a31c66909d706250932575464cc7a05f4#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': 'CURE Matheo: Chase the light, follow the dream@北大光华2023开学典礼', 'update_time': 1694525609}, {'aid': '2661400008_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400008, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDATUH5A4ShKYJhibnGJdZA6cDWEpMvZIKnSLvFL7GL7RGlvt8ePuia19BKg/0?wx_fmt=jpeg', 'create_time': 1694525609, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=3&sn=11119ae3720d48ab6f5ec49995db5673&chksm=bde98bf68a9e02e0f6b9ce9c288c966adfb6daa17952e60e8a55e8be76962831709673e5ec8e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '杨子夏：履方致远，逐梦追光@北大光华2023开学典礼', 'update_time': 1694525609}, {'aid': '2661400008_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2661400008, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/52pdbE99OSqW9mEYvObeCz6Tax3NicDATL8WZEPFDqTzbsUQwyBVvrqSGEiaV6vxWfwDmhiatyDcoGajr0wiapQwxQ/0?wx_fmt=jpeg', 'create_time': 1694525609, 'digest': '你好，新同学！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=4&sn=36d986fba37694fefe3dfaefaf644438&chksm=bde98bf68a9e02e0ad98f5652c0d8f9a52dcf16f6a2d17780b355320b44ffa59e03eae5c82f4#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '欢迎你们！第四届“未来领导者”新生', 'update_time': 1694525609}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
翁翕：成为思想的主人@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400065&idx=1&sn=ab1b593230330045f838b3d8aef579f9&chksm=bde9883f8a9e0129637cbbdc8e364dd137b6ff6a1a6b09c94e7250a951833bcc7ca6e1d16e8e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
你好，光华EMBA新同学！ http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400065&idx=2&sn=4a5c9cca027815411a3dfbca32b78532&chksm=bde9883f8a9e012909d1375fc397d8886bdb97a1c28407987a5c289b0c360aa00a44864d62fb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
郭翔：携笔从戎男儿志，百战归来再读书@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400020&idx=1&sn=f51e023d44155bb50e4f155b82221055&chksm=bde98bea8a9e02fc400a02103b00e473a6575a282d28891bfa065d532587df3a54a66d76c694#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
张新朝：百战归来再读书，寻找发展的力量@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400020&idx=2&sn=f895e9789fc429a7cc651e7c8e7d9299&chksm=bde98bea8a9e02fcea0969971556ef67205b8234b13a1f2dd570fc923d78f735ec9b75293fec#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
刘春河：赤子笃行，扬帆向光华@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400020&idx=3&sn=d0185f5dab98b2994c7e44b0e8a946e0&chksm=bde98bea8a9e02fc40adfb3f48402ccda9c595cbc35f848784f31a6628dfe4156c0acd9bbe27#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
杨毅：拥抱变化，破局成长@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400015&idx=1&sn=c58d3ad74b514eb46419ac33660d9e39&chksm=bde98bf18a9e02e74d6c27f4d7ec828f221dd2cf70d98e5dd3e54252f397a18cc7f9ff11d86a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
钱婧涵：拥抱变化，破局成长@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400015&idx=2&sn=24272a5b708ca35ac3cd1ce79642d454&chksm=bde98bf18a9e02e73e93eaad526b2928d61e3d7c0846891379038beb8bddecb6acfe35e6a64e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
佀骅羽：拥抱变化，破局成长@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400015&idx=3&sn=0aca5bf9fa221f1d2afc99ac342e5f4c&chksm=bde98bf18a9e02e7064d0b2bf1adf91e81799f74308cff3a6e51c110aeb7937b94924289abfd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
韩靖熙：梦落生花，梦始光华@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=1&sn=075e63369d747a9f7965e94c45bcb2b3&chksm=bde98bf68a9e02e0866614b7563b7df22a918d897686cdfafb14b531628c94629e83bca9ae9b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
CURE Matheo: Chase the light, follow the dream@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=2&sn=227999afb9874d4c8c5dc5950d5f3197&chksm=bde98bf68a9e02e01b03968748f6b0095f40dd55b04a31c66909d706250932575464cc7a05f4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
杨子夏：履方致远，逐梦追光@北大光华2023开学典礼 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=3&sn=11119ae3720d48ab6f5ec49995db5673&chksm=bde98bf68a9e02e0f6b9ce9c288c966adfb6daa17952e60e8a55e8be76962831709673e5ec8e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
欢迎你们！第四届“未来领导者”新生 http://mp.weixin.qq.com/s?__biz=MjM5MDk3NDgwMQ==&mid=2661400008&idx=4&sn=36d986fba37694fefe3dfaefaf644438&chksm=bde98bf68a9e02e0ad98f5652c0d8f9a52dcf16f6a2d17780b355320b44ffa59e03eae5c82f4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学对外汉语教育学院 MzA3ODU2MTk4NA==
sleep 169
<Response [200]>
dic: {'app_msg_cnt': 503, 'app_msg_list': [{'aid': '2650728914_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650728914, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/jNl98sibbS57FQOFlDDLVu0l2GO3lWkw4oNERCCBTvEY0GNRQENe41cult9xITcGbdHHhNWBicfXlcUsQ5QLj6PQ/0?wx_fmt=jpeg', 'create_time': 1692936530, 'digest': '2023年8月22日', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728914&idx=1&sn=12a98c20446cc1b5f51dd138a8b8779e&chksm=874a9e7db03d176b8c90840439f02c3b72dba858ce99971095497153654a3e63edd03ea72591#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '舞梦敦煌，国风古韵：对外汉语教育学院举办敦煌舞体验活动', 'update_time': 1692936900}, {'aid': '2650728899_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650728899, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/jNl98sibbS57kIhkTOeR79dmjPnkZ1KX7U3CAQHwQmlm5oeuDA49ox77nHMV8u9EzEfpDYkb0gSBucxtAMDPrpA/0?wx_fmt=jpeg', 'create_time': 1692753368, 'digest': '2023年8月22日', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728899&idx=1&sn=e970230a65a3e3b2debf4f4cd7c04a17&chksm=874a9e6cb03d177accc8ec7b37013703d243d82ea57bde3a35a26202f8d7daf348ecf064bd2a#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【北京大学国际中文教育讲坛】代云海《经济学视角下的国际中文教育》讲座纪要', 'update_time': 1692753368}, {'aid': '2650728887_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650728887, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/jNl98sibbS55TxaKNQMwFIEiaY5QxVMicYWcwiaEicxxibSSsLu4QGFwcBGNncXWMIdicyqO74FZkS91qAnoRpGnHdIEw/0?wx_fmt=jpeg', 'create_time': 1692683005, 'digest': '2023年8月18日-19日', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728887&idx=1&sn=d582400f437c42c2769f44f5385e4a24&chksm=874a9e18b03d170ec2342c080e35fd43f32677b74dd503858fcf6c0be6747dda705b408dc070#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '对外汉语教育学院举办第七届汉语作为第二语言研究国际研讨会（CASLAR-7）', 'update_time': 1692683005}, {'aid': '2650728865_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650728865, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/jNl98sibbS57EnibGuNRpOx6pfmdZj9n7XfnBZibiaNTsrxKeRts19mL3nbZleTYia7SplUtiaQYPllE3IOOJyNx5QGA/0?wx_fmt=jpeg', 'create_time': 1692228593, 'digest': '2023年8月17日-19日', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 8, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728865&idx=1&sn=380089548e4ac82b85d5aacb2bff28bd&chksm=874a9e0eb03d1718fec700569eb4a19f665dbed0d36ce2cb12862680af7b9ba54a2ea14c98da#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '第七届汉语作为第二语言研究国际研讨会', 'update_time': 1692230400}, {'aid': '2650728852_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650728852, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/jNl98sibbS57M4nPDqAl6LedwvwRu3C9X3XO82CXic8soiaNsiaFbJ9IPss50E2icswFribCc3I6hdrKkfFY0GCYKbHw/0?wx_fmt=jpeg', 'create_time': 1692061336, 'digest': '时间:2023年8月22日(周二)下午14:00~15:30', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728852&idx=1&sn=11528e02ae602206ac6a6ac3090d063d&chksm=874a9e3bb03d172d9d478871670af1de72cb6330af519e3223ce99fffb143241731dea337cfd#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【北大国际中文教育讲坛预告】代云海：经济学视角下的国际中文教育', 'update_time': 1692061336}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
舞梦敦煌，国风古韵：对外汉语教育学院举办敦煌舞体验活动 http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728914&idx=1&sn=12a98c20446cc1b5f51dd138a8b8779e&chksm=874a9e7db03d176b8c90840439f02c3b72dba858ce99971095497153654a3e63edd03ea72591#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【北京大学国际中文教育讲坛】代云海《经济学视角下的国际中文教育》讲座纪要 http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728899&idx=1&sn=e970230a65a3e3b2debf4f4cd7c04a17&chksm=874a9e6cb03d177accc8ec7b37013703d243d82ea57bde3a35a26202f8d7daf348ecf064bd2a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
对外汉语教育学院举办第七届汉语作为第二语言研究国际研讨会（CASLAR-7） http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728887&idx=1&sn=d582400f437c42c2769f44f5385e4a24&chksm=874a9e18b03d170ec2342c080e35fd43f32677b74dd503858fcf6c0be6747dda705b408dc070#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
第七届汉语作为第二语言研究国际研讨会 http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728865&idx=1&sn=380089548e4ac82b85d5aacb2bff28bd&chksm=874a9e0eb03d1718fec700569eb4a19f665dbed0d36ce2cb12862680af7b9ba54a2ea14c98da#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【北大国际中文教育讲坛预告】代云海：经济学视角下的国际中文教育 http://mp.weixin.qq.com/s?__biz=MzA3ODU2MTk4NA==&mid=2650728852&idx=1&sn=11528e02ae602206ac6a6ac3090d063d&chksm=874a9e3bb03d172d9d478871670af1de72cb6330af519e3223ce99fffb143241731dea337cfd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学物理学院人才培养 MzUxODk4MDA4NA==
sleep 227
<Response [200]>
dic: {'app_msg_cnt': 176, 'app_msg_list': [{'aid': '2247486933_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486933, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/U0VlGg9Licu4mRZKsic9JNFgotNAaKOsicWYjuEs7Xqg7buZddtMricnLzlaNvLLPnQuDUB0uKAM0NrgDtcdBMVPibA/0?wx_fmt=jpeg', 'create_time': 1693963048, 'digest': '近日，北京市教委公布了2023年度北京市高等学校教学名师奖获奖结果。在本次评审中，物理学院刘川老师获评2023年度北京市高等学校教学名师奖。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486933&idx=1&sn=6f3dff5ba632a98fa2d42a8f7751f0b0&chksm=f981e54ecef66c5855d61722c94a9192eea2e8949cf591b51ebe5110fc7f2c00d9e1e900fcd9#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '新闻 | 物理学院刘川老师获2023年度北京市高等学校教学名师奖', 'update_time': 1693965600}, {'aid': '2247486776_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486776, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqPiayxxGe4EPVKuPibDNl4YiboLhdYkABbgpzDFcMiaBic4dAcARNiaQSczq9c263o1ojP1sxY2GicP86eWA/0?wx_fmt=jpeg', 'create_time': 1693814616, 'digest': '2023年7月23日—27日，第九届全国大学生物理实验竞赛（Chinese Undergraduate', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486776&idx=1&sn=58176c59738aa1c4e66dbc65db06f7f2&chksm=f981e5a3cef66cb505d992d21904195321d323d60eb6924a4307fc544d37d3ecde9427ddd785#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '新闻 | 北京大学代表队在第九届全国大学生物理实验竞赛（教学赛）中获一项一等奖和两项二等奖', 'update_time': 1693816200}, {'aid': '2247486771_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486771, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/U0VlGg9Licu6hS8MzchNlKmdlfV17myeZb8ZpA6XYWMUrnZlKrM42e26sImtia4Siaj75BjkUjPSF2iaRO76NXyiahg/0?wx_fmt=jpeg', 'create_time': 1693446096, 'digest': '\u200b2023秋季物理学院免修考试通知来了~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486771&idx=1&sn=6d5f5a5cdad4682444ab541e7e257664&chksm=f981e5a8cef66cbe813e4c759e1b1cf57deeead882fa2bca179a53b9d4d4d612861deff09c02#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '通知｜2023秋季物理学院免修考试', 'update_time': 1693447200}, {'aid': '2247486758_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486758, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/U0VlGg9Licu7nS5qiaD65ORZ2Mt5mjcT05rTeIiaibAr6EHJN4mI9rhuVGheiaXmMufuTzBvv0glQ41BkZMfb2ocJibg/0?wx_fmt=jpeg', 'create_time': 1691979828, 'digest': '北大团队是怎样进行实验和分析的？他们的发现说明了什么？中国对超导材料的研究又到了什么样的阶段？为获得这些问题的答案，北大物理学院特别采访了此论文的作者郭凯臻同学和贾爽教授。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486758&idx=1&sn=9c177973ae0721a952514a1f8b8218ab&chksm=f981e5bdcef66cab327a5e7080cdbedd8aaa77b3b92303d7ff77021dd3df1795d4bbad1c1de2#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '专访 | 北大物理学院量子材料科学中心研究团队发表论文回应“全球首个室温超导材料”', 'update_time': 1691982000}, {'aid': '2247486744_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247486744, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/U0VlGg9Licu6euHAJECGLlGyib8YCN5x4vRJb7sLK63lYGpicBf5TKSfLV4sXATvsKibYksXicYKr7m88NdGTYIWLGQ/0?wx_fmt=jpeg', 'create_time': 1691030980, 'digest': '2023年7月10-14日，北京大学物理学院大气与海洋科学系成功举办了“北京大学2023年全国物理学与大气科学优秀大学生暑期学校”。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486744&idx=1&sn=e5bdc0bb15f5a563b856963dd70f756b&chksm=f981e583cef66c954532d14d26b4844c9ed1d212e1ef6acb60a690467be24b9df35f7c6a5c31#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '回顾 ｜ 北京大学2023年全国物理学与大气科学优秀大学生暑期学校成功举办', 'update_time': 1691031600}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
新闻 | 物理学院刘川老师获2023年度北京市高等学校教学名师奖 http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486933&idx=1&sn=6f3dff5ba632a98fa2d42a8f7751f0b0&chksm=f981e54ecef66c5855d61722c94a9192eea2e8949cf591b51ebe5110fc7f2c00d9e1e900fcd9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻 | 北京大学代表队在第九届全国大学生物理实验竞赛（教学赛）中获一项一等奖和两项二等奖 http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486776&idx=1&sn=58176c59738aa1c4e66dbc65db06f7f2&chksm=f981e5a3cef66cb505d992d21904195321d323d60eb6924a4307fc544d37d3ecde9427ddd785#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知｜2023秋季物理学院免修考试 http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486771&idx=1&sn=6d5f5a5cdad4682444ab541e7e257664&chksm=f981e5a8cef66cbe813e4c759e1b1cf57deeead882fa2bca179a53b9d4d4d612861deff09c02#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
专访 | 北大物理学院量子材料科学中心研究团队发表论文回应“全球首个室温超导材料” http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486758&idx=1&sn=9c177973ae0721a952514a1f8b8218ab&chksm=f981e5bdcef66cab327a5e7080cdbedd8aaa77b3b92303d7ff77021dd3df1795d4bbad1c1de2#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回顾 ｜ 北京大学2023年全国物理学与大气科学优秀大学生暑期学校成功举办 http://mp.weixin.qq.com/s?__biz=MzUxODk4MDA4NA==&mid=2247486744&idx=1&sn=e5bdc0bb15f5a563b856963dd70f756b&chksm=f981e583cef66c954532d14d26b4844c9ed1d212e1ef6acb60a690467be24b9df35f7c6a5c31#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学教育学院 MzA4OTA5MjA4MA==
sleep 216
<Response [200]>
dic: {'app_msg_cnt': 768, 'app_msg_list': [{'aid': '2652738439_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2652738439, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/ticHC8ntVtuyEYYA6Rajp3XcKUxTwNWfSwiaSdiaiap7tnY4BeUu7su27nSdicBXEsenrgoQNibYWFBGJbGzttWTywsA/0?wx_fmt=jpeg', 'create_time': 1694769038, 'digest': '北京大学教育学院教育技术系贾积有教授荣获2023年度第三十届Emerald Outstanding Paper Award（杰出论文奖）。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738439&idx=1&sn=102f7db0cff3de0b21aef5d55b5bc7cb&chksm=8bc90918bcbe800e65be59e44a71f021fbf137e11dbd47f7dc78b5725ab58cc9508aa4ed157a#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '贾积有教授获Emerald杰出论文奖', 'update_time': 1694769038}, {'aid': '2652738434_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2652738434, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/ticHC8ntVtuxYKLQcFUeJ0FibUTZIIIxNpN5o0As2dqkELNfibNxdE0dpRr6aCqkCqpMNHQLVjLmeqOyicFIrzGD4w/0?wx_fmt=jpeg', 'create_time': 1694523246, 'digest': '我院Ed.D.于晶荣获2023年全国新时代“百姓学习之星”称号。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738434&idx=1&sn=1bcd35b09683bcb300d64a5d19d8eb04&chksm=8bc9091dbcbe800b0e958bc38468afeadc7f9c0aa5742be167520ffda166e32b459159dad3ef#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '我院Ed.D.于晶荣获2023年全国新时代“百姓学习之星”称号', 'update_time': 1694523245}, {'aid': '2652738416_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2652738416, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/ticHC8ntVtuzYIF5NZl7rWIh1XNvMrnWbBBTA1bcYMJuhOTM7RtJ6yf0Mn6wcmSFvSyNDjeoiaFHzvK9hpHHjibkA/0?wx_fmt=jpeg', 'create_time': 1693902750, 'digest': '北京大学教育学院招聘博士后研究人员-汪琼教授（北京大学国家智能社会治理教育特色实验基地主任）', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738416&idx=1&sn=2a2c23d6addbeeaf1256ab652c8c5154&chksm=8bc909efbcbe80f9b65cd5e5226f52d345a023ad9a1e332e3455ffed43d7b44c5569a3a550b4#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招聘 | 北京大学教育学院招聘博士后研究人员', 'update_time': 1693902749}, {'aid': '2652738416_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2652738416, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/ticHC8ntVtuybWnNM95uZH5VqsreahiclCiatXGTlLnAsTwzOk5mEVzEgsahqicT8rica2K70tpqScqBVHp4H3znaYA/0?wx_fmt=jpeg', 'create_time': 1693902750, 'digest': '北京大学教育学院 2024 年接收推荐免试研究生的说明', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738416&idx=2&sn=a04091a499e6bc82b2bd5505ec05bf33&chksm=8bc909efbcbe80f96c15443779566a7dd34a2ee05f716db4e2ea5511504898ed8ceec9391757#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '北京大学教育学院2024年接收推荐免试研究生的说明', 'update_time': 1693902749}, {'aid': '2652738408_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2652738408, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/ticHC8ntVtuybWnNM95uZH5VqsreahiclCiatXGTlLnAsTwzOk5mEVzEgsahqicT8rica2K70tpqScqBVHp4H3znaYA/0?wx_fmt=jpeg', 'create_time': 1693815862, 'digest': '北京大学教育学院 2024 年接收推荐免试研究生的说明', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738408&idx=1&sn=7a73a1cd80b8c76e8b5608025a4b3423&chksm=8bc909f7bcbe80e1a29bacff271d7b0a9ef5b02b6cdfdfdb13dff1135336bfb4bfca43338eba#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '北京大学教育学院2024年接收推荐免试研究生的说明', 'update_time': 1693815862}, {'aid': '2652738395_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2652738395, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/ticHC8ntVtuzMSbhsy69pMg4Fys8u9jTmWylNgepWLmbOuIQAD5nst4uaalWB3oFXS9EUVGvRLKhEUVYEcWDx3A/0?wx_fmt=jpeg', 'create_time': 1693292668, 'digest': '认知智能全国重点实验室联合人工智能领军企业科大讯飞股份有限公司于2023年8月15日至8月25日在安徽合肥讯飞总部举办了首届科大讯飞星火训练营Spark Camp，营员包括全国29所高校和科研机构选拔、推荐的115位优秀在校生。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738395&idx=1&sn=96ddc1c9922f2e382d75633bb7de22b1&chksm=8bc909c4bcbe80d28efcaf51e93687aed387b79c2b300e382c676315ae27447444a9d72e640e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '北京大学学生参加2023科大讯飞星火营并荣获佳绩', 'update_time': 1693299600}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
贾积有教授获Emerald杰出论文奖 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738439&idx=1&sn=102f7db0cff3de0b21aef5d55b5bc7cb&chksm=8bc90918bcbe800e65be59e44a71f021fbf137e11dbd47f7dc78b5725ab58cc9508aa4ed157a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
我院Ed.D.于晶荣获2023年全国新时代“百姓学习之星”称号 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738434&idx=1&sn=1bcd35b09683bcb300d64a5d19d8eb04&chksm=8bc9091dbcbe800b0e958bc38468afeadc7f9c0aa5742be167520ffda166e32b459159dad3ef#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招聘 | 北京大学教育学院招聘博士后研究人员 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738416&idx=1&sn=2a2c23d6addbeeaf1256ab652c8c5154&chksm=8bc909efbcbe80f9b65cd5e5226f52d345a023ad9a1e332e3455ffed43d7b44c5569a3a550b4#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学教育学院2024年接收推荐免试研究生的说明 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738416&idx=2&sn=a04091a499e6bc82b2bd5505ec05bf33&chksm=8bc909efbcbe80f96c15443779566a7dd34a2ee05f716db4e2ea5511504898ed8ceec9391757#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学教育学院2024年接收推荐免试研究生的说明 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738408&idx=1&sn=7a73a1cd80b8c76e8b5608025a4b3423&chksm=8bc909f7bcbe80e1a29bacff271d7b0a9ef5b02b6cdfdfdb13dff1135336bfb4bfca43338eba#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学学生参加2023科大讯飞星火营并荣获佳绩 http://mp.weixin.qq.com/s?__biz=MzA4OTA5MjA4MA==&mid=2652738395&idx=1&sn=96ddc1c9922f2e382d75633bb7de22b1&chksm=8bc909c4bcbe80d28efcaf51e93687aed387b79c2b300e382c676315ae27447444a9d72e640e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
SMS_Stu_Union MzA5NDAxMDYzMQ==
sleep 528
<Response [200]>
dic: {'app_msg_cnt': 1808, 'app_msg_list': [{'aid': '2650886177_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886177, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/KauYtq0hn2z86krwGIPM4ysvxHskqZu6YhRjMMFMB9tIsaiaMy8Xvdv6qzFQCWlDR3osxzFmVpoCIVDh1MEfSRg/0?wx_fmt=jpeg', 'create_time': 1694775115, 'digest': '四六级来啦！你准备好了吗？', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886177&idx=1&sn=e64a51a7b8e11576dfb65d6d0d8d92e9&chksm=8ba0dc49bcd7555f99c73b7df400c5e1386e30672d9785a92fa7ea8bad2c2ab2326b8e92be4f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【小贴士】2023年下半年全国大学英语四、六级考试报名通知', 'update_time': 1694775114}, {'aid': '2650886177_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886177, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/KauYtq0hn2z86krwGIPM4ysvxHskqZu67o2NiclpQ541F2ZsISutmbVOibrw23WIKqgDVWC33bBDlbcBT2ed1qeg/0?wx_fmt=jpeg', 'create_time': 1694775115, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886177&idx=2&sn=c5c0d9fd0f7657830dedd44f58e545a7&chksm=8ba0dc49bcd7555f7d88b307e6cae1ac4ab5e22ba1dd7fb2907c0152a202a7113c2e7408e964#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【推广】宽德投资2024全球校招现已启动！', 'update_time': 1694775114}, {'aid': '2650886159_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886159, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/KauYtq0hn2xxXQInDd9GllU36obzMsBsZtozSCuibNOlQXMCyq4ibcmjsgiamH9BQoAN3Wb5P6ibhQDecqmP9Hgw6w/0?wx_fmt=jpeg', 'create_time': 1694685712, 'digest': '阿赛颁奖盛典系列活动第三弹', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886159&idx=1&sn=78f09ae2cef978d956995994ce7f5c30&chksm=8ba0dc67bcd755713a04208b57c68cec14a18da3847e7dc047e453be4ca2a0be34b9f80a4c2f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【颁奖盛典】数学游园会预热', 'update_time': 1694685711}, {'aid': '2650886159_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886159, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/KauYtq0hn2x2LyD1JnUnoOkTj0QZHRicu8z9BCfO8ibAQexjtz5UobJxsU7WibS2M1ksyOib1CMKn7on5ChSuYLfRw/0?wx_fmt=png', 'create_time': 1694685712, 'digest': 'Optiver', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886159&idx=2&sn=a7b8632d10dfe082f1215bdc6f9f2892&chksm=8ba0dc67bcd75571bfa237bae27cf71e986513ed5c3c4cdf1872d188588709c8da9f341af380#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【推广】Optiver北京大学专场活动报名', 'update_time': 1694685711}, {'aid': '2650886141_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886141, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/KauYtq0hn2xxXQInDd9GllU36obzMsBse10kq9YTaCVhvRXLv14SefT4iab6KHjmpjG09BibXkzic2CPFbj6ibwWibA/0?wx_fmt=jpeg', 'create_time': 1694605489, 'digest': '探求生态文明建设，赓续西南联大精神', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886141&idx=1&sn=12884fb667af1e03c9c8825064b60f36&chksm=8ba0c395bcd74a83ff9e8d652c5f73bbe03bfa2090b3b34ec71dc5dab396ca2c77bcb99de662#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【暑期实践】探求生态文明建设，赓续西南联大精神——北京大学数学科学学院2023年云南实践团', 'update_time': 1694605489}, {'aid': '2650886141_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886141, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/KauYtq0hn2xuhBAdyEO7o8sCnOLGrzxQkJAJ7NlEFHibib6kFcz66q07pibEH8ElRUX4BYQcXDSVTFmboibeXJgGJQ/0?wx_fmt=jpeg', 'create_time': 1694605489, 'digest': '新生破冰活动圆满结束', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886141&idx=2&sn=95828b448839b751d647812f0d7de53b&chksm=8ba0c395bcd74a833a4e1c592ae17d967b787276e4028ec1f31234bd40d4423c635c9615023e#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【新生破冰】回顾·参与丰富活动，融化社交初冰', 'update_time': 1694605489}, {'aid': '2650886127_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886127, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/KauYtq0hn2xxXQInDd9GllU36obzMsBsZtozSCuibNOlQXMCyq4ibcmjsgiamH9BQoAN3Wb5P6ibhQDecqmP9Hgw6w/0?wx_fmt=jpeg', 'create_time': 1694512610, 'digest': '阿赛颁奖盛典系列活动第二弹', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886127&idx=1&sn=4aa1f016d13079383b2fb3474f40f06f&chksm=8ba0c387bcd74a9177218d914188deb309727ee8221e694f97ab48ec785576379cc4e3b39387#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【颁奖盛典】主题辩论：AI能否取代数学工作者', 'update_time': 1694512610}, {'aid': '2650886110_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886110, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/KauYtq0hn2xxXQInDd9GllU36obzMsBsZtozSCuibNOlQXMCyq4ibcmjsgiamH9BQoAN3Wb5P6ibhQDecqmP9Hgw6w/0?wx_fmt=jpeg', 'create_time': 1694426840, 'digest': '阿赛颁奖盛典系列活动第一弹', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886110&idx=1&sn=8329bfa136b3dafb0f766e5a854903a3&chksm=8ba0c3b6bcd74aa0691700f2abf050f5ef668d4fd728ac583ff62506bf468a33dca9337fcb9b#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【颁奖盛典】阿赛数学讲坛震撼来袭', 'update_time': 1694426839}, {'aid': '2650886110_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886110, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/KauYtq0hn2xYfUClicIm7jILawTfhaWXRb74DJo5CRdqmxB4QBaAo6j2HibDOibRHfjJ3nibFj2B8T4gutEmRuv33Q/0?wx_fmt=jpeg', 'create_time': 1694426840, 'digest': 'Nuts留学线上讲座', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886110&idx=2&sn=1140c2703818a86ebde38a1931825072&chksm=8ba0c3b6bcd74aa0508347a5f82513eb2491100a3f33ab373a1387de690fa73d4cf867c4281f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【推广】“不踩坑”“有效率”—【大三申请规划】优秀模板到！', 'update_time': 1694426839}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
【小贴士】2023年下半年全国大学英语四、六级考试报名通知 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886177&idx=1&sn=e64a51a7b8e11576dfb65d6d0d8d92e9&chksm=8ba0dc49bcd7555f99c73b7df400c5e1386e30672d9785a92fa7ea8bad2c2ab2326b8e92be4f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【推广】宽德投资2024全球校招现已启动！ http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886177&idx=2&sn=c5c0d9fd0f7657830dedd44f58e545a7&chksm=8ba0dc49bcd7555f7d88b307e6cae1ac4ab5e22ba1dd7fb2907c0152a202a7113c2e7408e964#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【颁奖盛典】数学游园会预热 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886159&idx=1&sn=78f09ae2cef978d956995994ce7f5c30&chksm=8ba0dc67bcd755713a04208b57c68cec14a18da3847e7dc047e453be4ca2a0be34b9f80a4c2f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【推广】Optiver北京大学专场活动报名 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886159&idx=2&sn=a7b8632d10dfe082f1215bdc6f9f2892&chksm=8ba0dc67bcd75571bfa237bae27cf71e986513ed5c3c4cdf1872d188588709c8da9f341af380#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【暑期实践】探求生态文明建设，赓续西南联大精神——北京大学数学科学学院2023年云南实践团 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886141&idx=1&sn=12884fb667af1e03c9c8825064b60f36&chksm=8ba0c395bcd74a83ff9e8d652c5f73bbe03bfa2090b3b34ec71dc5dab396ca2c77bcb99de662#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【新生破冰】回顾·参与丰富活动，融化社交初冰 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886141&idx=2&sn=95828b448839b751d647812f0d7de53b&chksm=8ba0c395bcd74a833a4e1c592ae17d967b787276e4028ec1f31234bd40d4423c635c9615023e#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【颁奖盛典】主题辩论：AI能否取代数学工作者 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886127&idx=1&sn=4aa1f016d13079383b2fb3474f40f06f&chksm=8ba0c387bcd74a9177218d914188deb309727ee8221e694f97ab48ec785576379cc4e3b39387#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【颁奖盛典】阿赛数学讲坛震撼来袭 http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886110&idx=1&sn=8329bfa136b3dafb0f766e5a854903a3&chksm=8ba0c3b6bcd74aa0691700f2abf050f5ef668d4fd728ac583ff62506bf468a33dca9337fcb9b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【推广】“不踩坑”“有效率”—【大三申请规划】优秀模板到！ http://mp.weixin.qq.com/s?__biz=MzA5NDAxMDYzMQ==&mid=2650886110&idx=2&sn=1140c2703818a86ebde38a1931825072&chksm=8ba0c3b6bcd74aa0508347a5f82513eb2491100a3f33ab373a1387de690fa73d4cf867c4281f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大数院人 MzU3NzA0OTA5Mg==
sleep 164
<Response [200]>
dic: {'app_msg_cnt': 1058, 'app_msg_list': [{'aid': '2247499185_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499185, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/QuZf3kWa7zVoKYI1HhTWezwBI2YmHnIb3BKxwfCSdlWibcUUibtCTRpw5BiaOetM6J74BHibQHkjXmC3ZqNrSQ2CmA/0?wx_fmt=jpeg', 'create_time': 1694695438, 'digest': '9月12日中午，数学科学学院在理科一号楼1114室召开带班辅导员新学期见面会。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499185&idx=1&sn=5e22f7df15f21ce4aedee9996180c993&chksm=fd083adaca7fb3cc70cb9df10b46e66e26766bbb9a745eff4adbd4062ba6759cb5b3592224df#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '数学科学学院召开带班辅导员新学期见面会', 'update_time': 1694695437}, {'aid': '2247499142_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499142, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/QuZf3kWa7zWAicspRgvHzev64KDOicSETKbicriaEvKuaVnofeTYWU45c96vsD2ycb6roNbvyucGbOGKTfEpahyRKw/0?wx_fmt=jpeg', 'create_time': 1694523895, 'digest': '9月7日晚8时40分，数学科学学院“薪火相传”旧书回收活动在理科一号楼交流425N教室如期举行。 旧书收集', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499142&idx=1&sn=872ec858010675a812aec3cf6060519f&chksm=fd083aedca7fb3fba40bad4a65c7c344c66cef1b436d4d7273d1c6d666629eb1c3c1347b9194#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动回顾 | “薪火相传”旧书回收活动顺利举办！', 'update_time': 1694527200}, {'aid': '2247499142_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499142, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/QuZf3kWa7zXLFaaII2xf1ksX0h5uAE44l5vpR0e5mYSweACkMIYA9vMU2HEAuvmEFpY1ic7Johdzvj7GZRTERQw/0?wx_fmt=jpeg', 'create_time': 1694523895, 'digest': '阿赛颁奖盛典系列活动第一弹', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499142&idx=2&sn=e0e220b65c024d9610b6820254c9c0c0&chksm=fd083aedca7fb3fbd20f7e243b39830b93a1de3e770580b47a081172fa23d56eb59cb9f0dab6#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '颁奖盛典 | 阿赛数学讲坛震撼来袭', 'update_time': 1694527200}, {'aid': '2247499142_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499142, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/QuZf3kWa7zXLFaaII2xf1ksX0h5uAE44l5vpR0e5mYSweACkMIYA9vMU2HEAuvmEFpY1ic7Johdzvj7GZRTERQw/0?wx_fmt=jpeg', 'create_time': 1694523895, 'digest': '阿赛颁奖盛典系列活动第二弹', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499142&idx=3&sn=104dcb7544130385902a294d4806a270&chksm=fd083aedca7fb3fb7f40a998a5591a4277c8d9328bc53fc9958438b923418e2687d9e66945ba#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '颁奖盛典 | 主题辩论：AI能否取代数学工作者', 'update_time': 1694527200}, {'aid': '2247499133_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499133, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNq7zxTCc0Fial7QicI0B6EBOgeicG7JN3e5evUrU5VbuxEvFp2hrKVfmibg/0?wx_fmt=jpeg', 'create_time': 1694270453, 'digest': '尊敬的各位领导、各位来宾，亲爱的老师、同学们：大家下午好！我是北京大学数学科学学院2023级本科生胡殊闻，非', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=1&sn=e887c8e8bdb0f6374809dc87860495cc&chksm=fd083a16ca7fb300d52737f7606093c1922e40408c87fc3b6a1a6daf03f0efbbac724ba97675#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '本科生新生代表胡殊闻在北大数院2023年开学典礼上的发言', 'update_time': 1694270453}, {'aid': '2247499133_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499133, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNNZrP0bhV8E8A6Wq23IJKNM3YFIITI9Bgw1oWkglnqhlyOLYjiaHy9FQ/0?wx_fmt=jpeg', 'create_time': 1694270453, 'digest': '尊敬的各位领导、老师，亲爱的同学们：大家下午好。我是北京大学数学科学学院2023级的大数据专业硕士王楚凡，很', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=2&sn=a5da0b7ebc8a59fec8ba0bc3bc55cdfe&chksm=fd083a16ca7fb300902172736b99b2a5d6138b1638a2f93771c18ee4c622af0898919e7bb456#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '硕士研究生新生代表王楚凡在北大数院2023年开学典礼上的发言', 'update_time': 1694270453}, {'aid': '2247499133_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499133, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSN7urC1DdfbIrgm3iaq48qwNYiciaNYfv3cdVxicJGBU5hjILxWuAEhlKgqQ/0?wx_fmt=jpeg', 'create_time': 1694270453, 'digest': '尊敬的各位领导、老师，亲爱的同学们：大家下午好！我是数学科学学院2023级直博生史庭潇，非常荣幸能够作为博士', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=3&sn=ab0c81747d066b108533187a400c7257&chksm=fd083a16ca7fb3007a5b03c4a047d619e9df2f6e5ac9906aa08b9835f5c77b6d28e784359b7c#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '博士研究生新生代表史庭潇在北大数院2023年开学典礼上的发言', 'update_time': 1694270453}, {'aid': '2247499133_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499133, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNLhia1YLjTjPRicS50BvUWYuiaWsTEwnucLjlk2IWW7nM3UyLicRxTENuqQ/0?wx_fmt=jpeg', 'create_time': 1694270453, 'digest': '尊敬的各位领导老师、亲爱的同学们：大家下午好！我是来自数学科学学院应用数学专业的2020级博士研究生杨晨曦，', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=4&sn=ff251ad0d7416956475235abfc52ee2e&chksm=fd083a16ca7fb300280a6b8f14c2040d4a6fe41186b241d5192671c5a0c35193c32a019bd391#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '老生代表杨晨曦在北大数院2023年开学典礼上的发言', 'update_time': 1694270453}, {'aid': '2247499126_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499126, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNJWyJzM7a5ZibMYwll8Vyc3yVVGaL3ibtEwVf8V969Rf4icXwFpVhZVP4g/0?wx_fmt=jpeg', 'create_time': 1694185775, 'digest': '同学们，老师们，朋友们：大家下午好！首先我代表数学科学学院向今年入学的191名本科新同学和163名研究生新同', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499126&idx=1&sn=3eeaeb009d5b36ae12cc844ca7ce5c7e&chksm=fd083a1dca7fb30b2e8ebacaf57d50a158da4baf9e061b778b3f7007f692752e7b6994ab8bf8#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '培养更多数学拔尖人才 | 院长陈大岳在北大数院2023年开学典礼上的致辞', 'update_time': 1694185774}, {'aid': '2247499126_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499126, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSNVz44ia5vTJyyGwpHYtOYAGppiblWZwzXOUwGibdbA4SURtln1pzULcwCA/0?wx_fmt=jpeg', 'create_time': 1694185775, 'digest': '各位老师，各位同学，下午好！我是卢朓，我非常荣幸也非常高兴站在这儿，作为教师代表发言。首先，向你们的到来表示', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499126&idx=2&sn=8fd2a4843952ecae12775d0dfa21e1b2&chksm=fd083a1dca7fb30b12878e36482e53a1226dadc4cf227e2f439c2367aadbb04b13cb900912f3#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '教师代表卢朓在北大数院2023年开学典礼上的发言', 'update_time': 1694185774}, {'aid': '2247499126_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499126, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/BT5MuUU7jmDJtpaYS2docswB11UccPSN7Jianticz4xp7UrT1DwJaWSSib0QibXNbOL7R7RJiac2XnHjs2q8TIc87Wg/0?wx_fmt=jpeg', 'create_time': 1694185775, 'digest': '各位师弟师妹，各位老师，你们好。今天天气闷热，很像我来北大报到的那天，学校有大巴从北京站把新同学接到学校，一', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499126&idx=3&sn=d283a8a67ba3289b8676573d2262fc18&chksm=fd083a1dca7fb30b7d2166470532335fa7e61c3dae685ee52925c7d7c3e044c858042d8f5c91#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '院友代表于品在北大数院2023年开学典礼上的发言', 'update_time': 1694185774}, {'aid': '2247499121_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499121, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/QuZf3kWa7zUbOsKV2yL736PRBae7MGht6hK5VkKx2jlialCOP2qTChYlHvY0XYoxyqh2zAIOndcMvJQuvdKrTdg/0?wx_fmt=jpeg', 'create_time': 1694097805, 'digest': '9月7日下午北京大学数学科学学院2023年开学典礼在智华楼文远堂隆重举行这是智华楼维修改造后首场大型活动典礼', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499121&idx=1&sn=384b04a60f55fbbc1373ab745229c780&chksm=fd083a1aca7fb30c0e92f190af50555108c6b2bb858d2bb5c80db21ca2abdc562d0112bafb4b#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '北京大学数学科学学院2023年开学典礼在智华楼隆重举行', 'update_time': 1694098200}, {'aid': '2247499121_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2247499121, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/QuZf3kWa7zUbOsKV2yL736PRBae7MGhtcCwt9HlU7yW6icj1h7x4oZAxWWibkRg6g4SNl0ahfPibMXrbFgLfespmg/0?wx_fmt=jpeg', 'create_time': 1694097805, 'digest': '110周年庆系列文章春秋代序，百十峥嵘。2023年，北京大学数学学科迎来成立110周年，百十年经风雨而续薪火', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499121&idx=2&sn=24aca25a403976b9700227d0b1c6c710&chksm=fd083a1aca7fb30cb93a5aa7ea7eeac47fe9dd2fcd669f5c7e71a2fae653cbc3f7a77ddd2164#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '110周年庆·数学学人 | 王诗宬：从书房出发，到全世界去', 'update_time': 1694098200}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
数学科学学院召开带班辅导员新学期见面会 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499185&idx=1&sn=5e22f7df15f21ce4aedee9996180c993&chksm=fd083adaca7fb3cc70cb9df10b46e66e26766bbb9a745eff4adbd4062ba6759cb5b3592224df#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动回顾 | “薪火相传”旧书回收活动顺利举办！ http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499142&idx=1&sn=872ec858010675a812aec3cf6060519f&chksm=fd083aedca7fb3fba40bad4a65c7c344c66cef1b436d4d7273d1c6d666629eb1c3c1347b9194#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
颁奖盛典 | 阿赛数学讲坛震撼来袭 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499142&idx=2&sn=e0e220b65c024d9610b6820254c9c0c0&chksm=fd083aedca7fb3fbd20f7e243b39830b93a1de3e770580b47a081172fa23d56eb59cb9f0dab6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
颁奖盛典 | 主题辩论：AI能否取代数学工作者 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499142&idx=3&sn=104dcb7544130385902a294d4806a270&chksm=fd083aedca7fb3fb7f40a998a5591a4277c8d9328bc53fc9958438b923418e2687d9e66945ba#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
本科生新生代表胡殊闻在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=1&sn=e887c8e8bdb0f6374809dc87860495cc&chksm=fd083a16ca7fb300d52737f7606093c1922e40408c87fc3b6a1a6daf03f0efbbac724ba97675#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
硕士研究生新生代表王楚凡在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=2&sn=a5da0b7ebc8a59fec8ba0bc3bc55cdfe&chksm=fd083a16ca7fb300902172736b99b2a5d6138b1638a2f93771c18ee4c622af0898919e7bb456#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
博士研究生新生代表史庭潇在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=3&sn=ab0c81747d066b108533187a400c7257&chksm=fd083a16ca7fb3007a5b03c4a047d619e9df2f6e5ac9906aa08b9835f5c77b6d28e784359b7c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
老生代表杨晨曦在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499133&idx=4&sn=ff251ad0d7416956475235abfc52ee2e&chksm=fd083a16ca7fb300280a6b8f14c2040d4a6fe41186b241d5192671c5a0c35193c32a019bd391#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
培养更多数学拔尖人才 | 院长陈大岳在北大数院2023年开学典礼上的致辞 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499126&idx=1&sn=3eeaeb009d5b36ae12cc844ca7ce5c7e&chksm=fd083a1dca7fb30b2e8ebacaf57d50a158da4baf9e061b778b3f7007f692752e7b6994ab8bf8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
教师代表卢朓在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499126&idx=2&sn=8fd2a4843952ecae12775d0dfa21e1b2&chksm=fd083a1dca7fb30b12878e36482e53a1226dadc4cf227e2f439c2367aadbb04b13cb900912f3#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
院友代表于品在北大数院2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499126&idx=3&sn=d283a8a67ba3289b8676573d2262fc18&chksm=fd083a1dca7fb30b7d2166470532335fa7e61c3dae685ee52925c7d7c3e044c858042d8f5c91#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学数学科学学院2023年开学典礼在智华楼隆重举行 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499121&idx=1&sn=384b04a60f55fbbc1373ab745229c780&chksm=fd083a1aca7fb30c0e92f190af50555108c6b2bb858d2bb5c80db21ca2abdc562d0112bafb4b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
110周年庆·数学学人 | 王诗宬：从书房出发，到全世界去 http://mp.weixin.qq.com/s?__biz=MzU3NzA0OTA5Mg==&mid=2247499121&idx=2&sn=24aca25a403976b9700227d0b1c6c710&chksm=fd083a1aca7fb30cb93a5aa7ea7eeac47fe9dd2fcd669f5c7e71a2fae653cbc3f7a77ddd2164#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU言之有物 MzAwMDEwMzI0MQ==
sleep 334
<Response [200]>
dic: {'app_msg_cnt': 1712, 'app_msg_list': [{'aid': '2697832576_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2697832576, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/QAEJXB03eMCT4KiaAFkH53lFdFTUmsVnZjkUPLUEQJOxkkFExGtUeMib9ry6icRibmnicbwB3UiaDU8diaWIZf5MTPMOw/0?wx_fmt=jpeg', 'create_time': 1694776400, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832576&idx=1&sn=a34c5181777d08ae232e2d1dd19cc30f&chksm=bfd70ea688a087b0a374c6966501f40bb89ee0d063227ad78970f24f0de8058faf2f1034efe9#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '《奥本海默》中没有她，但物理界不能没有她', 'update_time': 1694776400}, {'aid': '2697832575_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2697832575, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/6pPuFiaOzcpJR6V80FvXN8fapzl4o4eYaDxLYp757JH0ib0oWZ4MYS7V8FoOFflXhIzcZjh3OouDNoru6bZYCguQ/0?wx_fmt=jpeg', 'create_time': 1694692077, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832575&idx=1&sn=412a44fba3cc574dc641ca90722fc79d&chksm=bfd70e5988a0874fa2eef895c5275393c54d149c98ab0b7e8809a8769e4b314051cbed57b387#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '物理·班团丨青春不息，奔赴不止——物理学院2023级本科10班开展班级建设暨团建总结交流会', 'update_time': 1694692076}, {'aid': '2697832554_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2697832554, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/6pPuFiaOzcpKMicn7961c3DAtfrYgezDicVj5n2vk67NInq2v1WNibPD8TC8pSWF477Ros0V0icRS4n2cTGMKGBse7A/0?wx_fmt=jpeg', 'create_time': 1694612245, 'digest': '物院团委组织部招新啦！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832554&idx=1&sn=515bd2295976d746e157a0d2a8cf57fa&chksm=bfd70e4c88a0875ad2e1c0e2181d3ad8d1a77ebe38c2315e59dfdd8eab9b9a87d0a5449c6317#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新丨“团”学聚星火，“组”织汇英才——物院团组等你加入', 'update_time': 1694612244}, {'aid': '2697832554_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2697832554, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/6pPuFiaOzcpKMicn7961c3DAtfrYgezDicVhseuMVWa0abMg58fJxib5043b15mhumXDiajUe56hIC3MfCW60R9Ejqg/0?wx_fmt=jpeg', 'create_time': 1694612245, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832554&idx=2&sn=46a8989ad559e031ec29c67585d251ec&chksm=bfd70e4c88a0875a67bac82f8767796a48692361ffeda4fc4470d5ea5472cb51ba44cdad2fbe#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '物院·就业丨联影医疗宣讲会成功举办', 'update_time': 1694612244}, {'aid': '2697832502_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2697832502, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/6pPuFiaOzcpLJ8viaPWMcTevHovq87c4qicDeHsIiaXF4ibbPZ8J3Jic8MIiaB1nfHb4UicKn9yGTgF1Sic3pE2KdOvibvIw/0?wx_fmt=jpeg', 'create_time': 1694519183, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=1&sn=3697089919596e58ce19e3b9bfe0e97c&chksm=bfd70e1088a08706c1266ffbc9768e3c6a229d3c1981c2da086ed17230caaa1af53fcd540b2a#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '迎新丨探理博雅梦，格物迎新篇——2023级北京大学物理学院研究生迎新与入学教育综合报道', 'update_time': 1694519183}, {'aid': '2697832502_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2697832502, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/6pPuFiaOzcpLibqU6piancC1IZvpn3M3icyAINO0Jb7FOPgRbSydn8cjv9yKrnFy486dp3auIjQbUmeQeZcByvyYNQ/0?wx_fmt=png', 'create_time': 1694519183, 'digest': '9月15日下午15:00，等你参与！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=2&sn=990d9ace5cc7077edb4409531ab9b26f&chksm=bfd70e1088a08706a4523c33df4345ace8d3ba3262484ca5cf7ca125c1c5bdf28b4014697feb#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '物理人如何拥抱新能源时代？第二期“物理+”校友沙龙等你参与！', 'update_time': 1694519183}, {'aid': '2697832502_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2697832502, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/6pPuFiaOzcpLibqU6piancC1IZvpn3M3icyA3j1apshVmvAia0ty994qsKr0tO0GFibSJwibnXJdWTDYae5eiaibb9zQHPQ/0?wx_fmt=png', 'create_time': 1694519183, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=3&sn=94123a90b986798165ac173c6ee70c74&chksm=bfd70e1088a08706ecce58d0afe72aaea0e0b5aa3603204aea3d16dec30c057895b403b46a65#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '物院·就业 | 2024届毕业生就业指导会报名通知', 'update_time': 1694519183}, {'aid': '2697832502_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2697832502, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/6pPuFiaOzcpLibqU6piancC1IZvpn3M3icyAbic52r8iaf9xOlIuquOCKOZYn5kwXYoxk4B9662uojZMNIkRegfuTiaoA/0?wx_fmt=png', 'create_time': 1694519183, 'digest': '9月17日(周日)19:00~21:00，物理学院西113，欢迎热爱电影的你到来~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=4&sn=e1afb39dfde5557dbbe5b9a28f565115&chksm=bfd70e1088a08706c71f4ddcb9f8099801838b084d05b34913c7d87fd2263e3d9959009b7e15#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '研会·放映丨《教父3》', 'update_time': 1694519183}, {'aid': '2697832482_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2697832482, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/6pPuFiaOzcpLJ8viaPWMcTevHovq87c4qic1rq4iaClfULk9fjNz1Fz54N735XAaEAFzVcdfsnF2XsdeyOUWPjUAzQ/0?wx_fmt=jpeg', 'create_time': 1694439231, 'digest': '第一时间掌握学校学院就业相关信息！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832482&idx=1&sn=8f9548f78678ef19c4a0942517dcb031&chksm=bfd70e0488a08712e9e1820196b514f3610d2620c2ebfd5dcd7a2ba9114acd9d4c0cfbc1943a#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '物院·就业丨燕园快讯直通车 (第一期)', 'update_time': 1694439231}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
《奥本海默》中没有她，但物理界不能没有她 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832576&idx=1&sn=a34c5181777d08ae232e2d1dd19cc30f&chksm=bfd70ea688a087b0a374c6966501f40bb89ee0d063227ad78970f24f0de8058faf2f1034efe9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物理·班团丨青春不息，奔赴不止——物理学院2023级本科10班开展班级建设暨团建总结交流会 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832575&idx=1&sn=412a44fba3cc574dc641ca90722fc79d&chksm=bfd70e5988a0874fa2eef895c5275393c54d149c98ab0b7e8809a8769e4b314051cbed57b387#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新丨“团”学聚星火，“组”织汇英才——物院团组等你加入 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832554&idx=1&sn=515bd2295976d746e157a0d2a8cf57fa&chksm=bfd70e4c88a0875ad2e1c0e2181d3ad8d1a77ebe38c2315e59dfdd8eab9b9a87d0a5449c6317#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物院·就业丨联影医疗宣讲会成功举办 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832554&idx=2&sn=46a8989ad559e031ec29c67585d251ec&chksm=bfd70e4c88a0875a67bac82f8767796a48692361ffeda4fc4470d5ea5472cb51ba44cdad2fbe#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
迎新丨探理博雅梦，格物迎新篇——2023级北京大学物理学院研究生迎新与入学教育综合报道 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=1&sn=3697089919596e58ce19e3b9bfe0e97c&chksm=bfd70e1088a08706c1266ffbc9768e3c6a229d3c1981c2da086ed17230caaa1af53fcd540b2a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物理人如何拥抱新能源时代？第二期“物理+”校友沙龙等你参与！ http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=2&sn=990d9ace5cc7077edb4409531ab9b26f&chksm=bfd70e1088a08706a4523c33df4345ace8d3ba3262484ca5cf7ca125c1c5bdf28b4014697feb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物院·就业 | 2024届毕业生就业指导会报名通知 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=3&sn=94123a90b986798165ac173c6ee70c74&chksm=bfd70e1088a08706ecce58d0afe72aaea0e0b5aa3603204aea3d16dec30c057895b403b46a65#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
研会·放映丨《教父3》 http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832502&idx=4&sn=e1afb39dfde5557dbbe5b9a28f565115&chksm=bfd70e1088a08706c71f4ddcb9f8099801838b084d05b34913c7d87fd2263e3d9959009b7e15#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
物院·就业丨燕园快讯直通车 (第一期) http://mp.weixin.qq.com/s?__biz=MzAwMDEwMzI0MQ==&mid=2697832482&idx=1&sn=8f9548f78678ef19c4a0942517dcb031&chksm=bfd70e0488a08712e9e1820196b514f3610d2620c2ebfd5dcd7a2ba9114acd9d4c0cfbc1943a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大物理人 MzA5NzUwODgxMw==
sleep 454
<Response [200]>
dic: {'app_msg_cnt': 1155, 'app_msg_list': [{'aid': '2656058326_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058326, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_png/XJ36S7nyjqMwDiaBOPBwDHSHPwMfDdxyXV0vyxKKODgYUAaFdCTJDChcQTiaZYH6IcfrD3ZrcEy5qnSBhibv5R7aA/0?wx_fmt=png', 'create_time': 1694765382, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058326&idx=1&sn=d4f4878c45e83b0c3e69f415cb2b7ff9&chksm=8b3b5774bc4cde625592bff77a19b684b5f9611711b432ff21eb6a460b01eac3d6e59543615f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '学术 | 讲座预告', 'update_time': 1694765382}, {'aid': '2656058326_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058326, 'checking': 0, 'copyright_type': 2, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/nc2VgE7pk8sukd0fmcKaeHdyN8uUK5Vc33HC1HfFFSu3FfTFk8t2Jfrs2hzJ1xH2najH7jSTT5mkWXFLGzPwJA/0?wx_fmt=jpeg', 'create_time': 1694765382, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 11, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058326&idx=2&sn=9a77b61497994680ad5951063aca1135&chksm=8b3b5774bc4cde62ae9352c25a294c6d244da8865f6faa194fd6d03f9e4bbb6a4c5735632364#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '转载 | 彭莹莹课题组与合作者发现铜氧超导体过掺杂存在普遍电荷序', 'update_time': 1694765382}, {'aid': '2656058320_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058320, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqMJ9R6FpvgluREIiaPQDsc1RnJrspicWv5v23icwEa6cYfQbibLCVPayicHQnu1QWYr4p8yLdENiawRrSbQ/0?wx_fmt=jpeg', 'create_time': 1694675411, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058320&idx=1&sn=6325a5e6f5faac81b1c5f81892b33956&chksm=8b3b5772bc4cde64e7ee7656da63cd75293ef96dc4ef09efe89d5f169a3e12056d7ebf74cb77#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '成果 | 极端光学创新研究团队刘运全、龚旗煌等在二维过渡金属硫化物各向异性间接层间激子态的超快电子动力学研究中取得重要进展', 'update_time': 1694675411}, {'aid': '2656058312_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058312, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqOvoB6lMRaQic8ibIU6UTtOhI7qjE3XrWcqibP4MWZbjEVEDebuwjEG85j7hoL54tiarWoPLKMdI7y7iaw/0?wx_fmt=jpeg', 'create_time': 1694504011, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058312&idx=1&sn=9b48235343a49045e6c2f18aa0bfaa42&chksm=8b3b576abc4cde7c74dc5c2ddd5f289dc27529388f72e2c27e753e404ba1e577609a88b33b92#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '预告 | 北京大学物理学院学术论坛（第二十六讲）', 'update_time': 1694504011}, {'aid': '2656058312_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058312, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqOvoB6lMRaQic8ibIU6UTtOhIezdWq1SNlQuSBg02YvPN6Q4wTia165aaxTicK4N7tJaXCr5meLfEGH3A/0?wx_fmt=jpeg', 'create_time': 1694504011, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058312&idx=2&sn=7e069fb3e525f4e481f1342a9f5aa095&chksm=8b3b576abc4cde7ca4ceed5a1c66fc275c901f83c73c2c92fde16e3357c650cbce3828bd8ecb#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '预告 | 格致论坛（第十七讲）：超冷原子气体中的精密测量、精密调控及其若干应用', 'update_time': 1694504011}, {'aid': '2656058295_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058295, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqM96CvMA43knN0LF1w7fkIGJW3Rz4FF4VBkcV5ml4WicVITMXfeicGDKcflzickV2mB1Xnwe7lxqIKiaQ/0?wx_fmt=jpeg', 'create_time': 1694400658, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058295&idx=1&sn=a722546cef89c21cb28efc8ae77043f5&chksm=8b3b5715bc4cde03f0caa0423b73d83bd98cc02f9b289044f53d6e07f9c76c8781f352d99496#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '预告 | 北京大学物理学科卓越人才培养计划讲堂：名师面对面（一）', 'update_time': 1694400657}, {'aid': '2656058295_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058295, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqM96CvMA43knN0LF1w7fkIGlzVTZSAVur8zqVVvk6zHShmf53icicQpj1xSRqCeYu0YI1wKoOdChyZg/0?wx_fmt=jpeg', 'create_time': 1694400658, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058295&idx=2&sn=720a8b57e6216002b7cb9845109d80ca&chksm=8b3b5715bc4cde0331f1eda8cf82845bc7b1b7ec72473917237ae4407a44e7f1e3136dbc3a32#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '预告 | 北京大学物理学科卓越人才培养计划讲堂：名师面对面（第十三期）', 'update_time': 1694400657}, {'aid': '2656058287_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058287, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqPjr3YglNv2leYbZu6h383x9tdWlu7E6U8wcyk789iabTn2fmfFCU2f9JPxdfibVT5WcIkaf32judAg/0?wx_fmt=jpeg', 'create_time': 1694305258, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=1&sn=1e59d085db07b4e4448cece35b7a05f7&chksm=8b3b570dbc4cde1b4facff5a6b766ee17fb3fb55970be506fe6012a85e8f722792bcf27e402f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '节日 | 恭祝物理学院全体教师节日快乐！', 'update_time': 1694305257}, {'aid': '2656058287_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058287, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqPjr3YglNv2leYbZu6h383xZnlWHYl4GdQWLQ8vVvZWT8jWicgm1RUMsXSeA1prdepU2n6e6Uu7icWg/0?wx_fmt=jpeg', 'create_time': 1694305258, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=2&sn=68313d8894c367ff73b8a6d8697d3858&chksm=8b3b570dbc4cde1ba3daba229807f1395bffbc8f3abe427be2a7e4463916b62b13fd8189ab89#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 院长高原宁致辞', 'update_time': 1694305257}, {'aid': '2656058287_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058287, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqPjr3YglNv2leYbZu6h383xK4EfmO9WKF7py0JnE7QFPMIsCJnzZzaibUx7m9uicdPEDl7WQAXFy0LQ/0?wx_fmt=jpeg', 'create_time': 1694305258, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=3&sn=062f556e65117a2b80ffae3d1b965bfa&chksm=8b3b570dbc4cde1bbd7f12fea6ae3aff1f1500e3440f3cf9b20b7f71788b9cb5eef431d716ef#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 校友代表贾金锋发言', 'update_time': 1694305257}, {'aid': '2656058287_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058287, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqPjr3YglNv2leYbZu6h383x5SFL2yvy5YI4eAicWwmyTrwVYr32vmpicYibbEEyW5HLKHib5E7cpN46jA/0?wx_fmt=jpeg', 'create_time': 1694305258, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=4&sn=f44cbc67ab648b08c1f14778bc28bae3&chksm=8b3b570dbc4cde1b54faee5b16bef833ca321b7e35ed17c2fa30c031e7529663d8efa3ae49ec#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 教师代表俞妍发言', 'update_time': 1694305257}, {'aid': '2656058287_5', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058287, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqPjr3YglNv2leYbZu6h383xkCEmx5Ck7ptzwquLlA9jGjU9uP8NWiagdKlWFqlibCWtvuFsniaj5Gguw/0?wx_fmt=jpeg', 'create_time': 1694305258, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 5, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=5&sn=17fcb687696f5409cc89f5095dad62a9&chksm=8b3b570dbc4cde1ba2be4c174556e935d2736de48d0efd5739fcf0793c3fdb9b2ff65d319413#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 本科生在校生代表柳天昊发言', 'update_time': 1694305257}, {'aid': '2656058287_6', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058287, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqPjr3YglNv2leYbZu6h383xCict1tpt2ibu56Ox3ia9ibC7H1JLCicNIZRclbX38WrxsPT0oicXOm1Cz4zA/0?wx_fmt=jpeg', 'create_time': 1694305258, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 6, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=6&sn=9f4887c642a99ff0309290571aaba9f1&chksm=8b3b570dbc4cde1bbf8f67b7239f2d79a179d7bed6201320e0aa82b11c007d431d847b24b149#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 研究生在校生代表戴天祥发言', 'update_time': 1694305257}, {'aid': '2656058287_7', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058287, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqPjr3YglNv2leYbZu6h383xjhRSjOhz9ic0KNNVuDBHU0VEDJ9anibajCvhkSOzxZNQAbpInpYHanlQ/0?wx_fmt=jpeg', 'create_time': 1694305258, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 7, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=7&sn=85ab6b51fc80b93a78ddc14a9d5f9bec&chksm=8b3b570dbc4cde1be54a2bdf5f4691db076934334cd1598dcb2101e225d20bffc44425ec384d#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 本科生新生代表李开阳发言', 'update_time': 1694305257}, {'aid': '2656058287_8', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656058287, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/mmbiz_jpg/XJ36S7nyjqPjr3YglNv2leYbZu6h383xR9AWCQkOGW9ib3TossU0TAqibFnjnGdePZVqgr41InvmZPFic752Tr0uw/0?wx_fmt=jpeg', 'create_time': 1694305258, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 8, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=8&sn=94a3958866adc4551d0c7c469a03978f&chksm=8b3b570dbc4cde1bb31ff390c4f2c437cd77afeddbf98ae6809c06c8215635fc76ffcbe266ad#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '开学典礼 | 研究生新生代表顾昱晨发言', 'update_time': 1694305257}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
学术 | 讲座预告 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058326&idx=1&sn=d4f4878c45e83b0c3e69f415cb2b7ff9&chksm=8b3b5774bc4cde625592bff77a19b684b5f9611711b432ff21eb6a460b01eac3d6e59543615f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
转载 | 彭莹莹课题组与合作者发现铜氧超导体过掺杂存在普遍电荷序 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058326&idx=2&sn=9a77b61497994680ad5951063aca1135&chksm=8b3b5774bc4cde62ae9352c25a294c6d244da8865f6faa194fd6d03f9e4bbb6a4c5735632364#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
成果 | 极端光学创新研究团队刘运全、龚旗煌等在二维过渡金属硫化物各向异性间接层间激子态的超快电子动力学研究中取得重要进展 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058320&idx=1&sn=6325a5e6f5faac81b1c5f81892b33956&chksm=8b3b5772bc4cde64e7ee7656da63cd75293ef96dc4ef09efe89d5f169a3e12056d7ebf74cb77#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告 | 北京大学物理学院学术论坛（第二十六讲） http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058312&idx=1&sn=9b48235343a49045e6c2f18aa0bfaa42&chksm=8b3b576abc4cde7c74dc5c2ddd5f289dc27529388f72e2c27e753e404ba1e577609a88b33b92#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告 | 格致论坛（第十七讲）：超冷原子气体中的精密测量、精密调控及其若干应用 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058312&idx=2&sn=7e069fb3e525f4e481f1342a9f5aa095&chksm=8b3b576abc4cde7ca4ceed5a1c66fc275c901f83c73c2c92fde16e3357c650cbce3828bd8ecb#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告 | 北京大学物理学科卓越人才培养计划讲堂：名师面对面（一） http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058295&idx=1&sn=a722546cef89c21cb28efc8ae77043f5&chksm=8b3b5715bc4cde03f0caa0423b73d83bd98cc02f9b289044f53d6e07f9c76c8781f352d99496#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
预告 | 北京大学物理学科卓越人才培养计划讲堂：名师面对面（第十三期） http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058295&idx=2&sn=720a8b57e6216002b7cb9845109d80ca&chksm=8b3b5715bc4cde0331f1eda8cf82845bc7b1b7ec72473917237ae4407a44e7f1e3136dbc3a32#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
节日 | 恭祝物理学院全体教师节日快乐！ http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=1&sn=1e59d085db07b4e4448cece35b7a05f7&chksm=8b3b570dbc4cde1b4facff5a6b766ee17fb3fb55970be506fe6012a85e8f722792bcf27e402f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 院长高原宁致辞 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=2&sn=68313d8894c367ff73b8a6d8697d3858&chksm=8b3b570dbc4cde1ba3daba229807f1395bffbc8f3abe427be2a7e4463916b62b13fd8189ab89#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 校友代表贾金锋发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=3&sn=062f556e65117a2b80ffae3d1b965bfa&chksm=8b3b570dbc4cde1bbd7f12fea6ae3aff1f1500e3440f3cf9b20b7f71788b9cb5eef431d716ef#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 教师代表俞妍发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=4&sn=f44cbc67ab648b08c1f14778bc28bae3&chksm=8b3b570dbc4cde1b54faee5b16bef833ca321b7e35ed17c2fa30c031e7529663d8efa3ae49ec#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 本科生在校生代表柳天昊发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=5&sn=17fcb687696f5409cc89f5095dad62a9&chksm=8b3b570dbc4cde1ba2be4c174556e935d2736de48d0efd5739fcf0793c3fdb9b2ff65d319413#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 研究生在校生代表戴天祥发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=6&sn=9f4887c642a99ff0309290571aaba9f1&chksm=8b3b570dbc4cde1bbf8f67b7239f2d79a179d7bed6201320e0aa82b11c007d431d847b24b149#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 本科生新生代表李开阳发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=7&sn=85ab6b51fc80b93a78ddc14a9d5f9bec&chksm=8b3b570dbc4cde1be54a2bdf5f4691db076934334cd1598dcb2101e225d20bffc44425ec384d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
开学典礼 | 研究生新生代表顾昱晨发言 http://mp.weixin.qq.com/s?__biz=MzA5NzUwODgxMw==&mid=2656058287&idx=8&sn=94a3958866adc4551d0c7c469a03978f&chksm=8b3b570dbc4cde1bb31ff390c4f2c437cd77afeddbf98ae6809c06c8215635fc76ffcbe266ad#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学学生会 MzA3MDAxMTIxMQ==
sleep 301
<Response [200]>
dic: {'app_msg_cnt': 1918, 'app_msg_list': [{'aid': '2651120168_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120168, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/sTHGDZ2o0PQMRBpD0qXvtqBgFOLjEChHibv5ibS8XlxMd2tLdEEq3ajz2AmCLJeZgnhBbicCUdibljxUWOo0SdNybw/0?wx_fmt=jpeg', 'create_time': 1694602566, 'digest': '百载回眸风云在，青春如歌响红楼', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120168&idx=1&sn=4c88ab79aa6904669b5bc22bbdfaeb39&chksm=8533120cb2449b1ab92a1e3242d60f93ccaa830d92ba87dc04cac468f1e0fc57396b011804db#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '星野·回顾 | “星野”社会实践团赴北大红楼开展实践活动', 'update_time': 1694602566}, {'aid': '2651120116_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120116, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/sTHGDZ2o0PQcMa0Zg8gknDgib1g6Mj5ibL1f6vDHoNpeThrD5QWGIF38ZeftwREMicd3aF3sqoGmfXUmmlAju6tQw/0?wx_fmt=png', 'create_time': 1694347027, 'digest': '你好，新同学！\r\n这里是综合办公室！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120116&idx=1&sn=2de9fe587417622adaad7d04f6c928bd&chksm=853311d0b24498c6b069ef8b70640ce482b7e429609ab8d3ab7c49c41b077929523a112f453b#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新｜综办在等你', 'update_time': 1694347027}, {'aid': '2651120116_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120116, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/sTHGDZ2o0PQcMa0Zg8gknDgib1g6Mj5ibLoB8dnvBSGClBOFQhh8icJPjxdFhica3H0O03z9BSCuqezww5icLdXAkvw/0?wx_fmt=png', 'create_time': 1694347027, 'digest': '快来加入监察部吧~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120116&idx=2&sn=60fbe5d1932226b0948a012b12c43ea5&chksm=853311d0b24498c67aa0a120e383584ea52be89d0e3bbd242838911b412e388a0f7f635f77e8#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 快来加入监察部吧~', 'update_time': 1694347027}, {'aid': '2651120116_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120116, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/sTHGDZ2o0PQcMa0Zg8gknDgib1g6Mj5ibLlEiaMicCibPBpfoyOd9lrjMahAafibFhWKRGvYic9ZXVj7uj4XKWrlIQZtQ/0?wx_fmt=jpeg', 'create_time': 1694347027, 'digest': '全心权益，期待有你！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120116&idx=3&sn=5d2d0236ce7b2ac65c32f4e00676817f&chksm=853311d0b24498c64d96401f07d9adca18e30fe30e34d388ba7a7abe7b83259b6bc8294d3301#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 常代会权益提案部期待你的加入！', 'update_time': 1694347027}, {'aid': '2651120115_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120115, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/sTHGDZ2o0PRJiafmhTR4kPNZSzo5fHR1TYiajLM6tpVy1vibgmZO1H3t4o33UM6vnnp4mT5c3NoSrPcTsjanibbxvw/0?wx_fmt=jpeg', 'create_time': 1694246580, 'digest': '决赛待发，冠军争锋！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120115&idx=1&sn=b40087af58627bea3c0cac471fd8f8b2&chksm=853311d7b24498c12cb5544c2c84efbb54bbb04886261c0a995cc6618960f0b8fecb733bf673#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '北大之锋 | 决赛预告', 'update_time': 1694246580}, {'aid': '2651120091_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120091, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/sTHGDZ2o0PSiazzvfR2ibwg3NL5KUGwzibF8FbwPaHX4o8QFGhCqF7q2YlrxAs5IlZSXqUP9qRheu23EOzSwK3eww/0?wx_fmt=png', 'create_time': 1694174854, 'digest': '北京大学学生会期待你的加入！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=1&sn=213830056e89c1abe5c474db95a1ba52&chksm=853311ffb24498e91dd996fc264100b723a9249dbdc2d9bd2ceedc7ff73edfc3741c7b6c2dfc#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 北大学生会，期待每一朵星火', 'update_time': 1694174854}, {'aid': '2651120091_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120091, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/sTHGDZ2o0PRJiafmhTR4kPNZSzo5fHR1THh4fNh0A7kmCoo0hoJric7Mllz0LhicrEsJVFyGsbwiaR7iaeDBmV3ibI5Q/0?wx_fmt=jpeg', 'create_time': 1694174854, 'digest': '综合管理部，期待你的加入！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=2&sn=f9b72ac5fbf0c6fdaabe388b22ea57c8&chksm=853311ffb24498e94104cc798a2b68ac6278949de780dbbe3a4144d3933fd5d40f281d257f3d#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 综合管理部：综以有序，扎实建树', 'update_time': 1694174854}, {'aid': '2651120091_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120091, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/sTHGDZ2o0PSiazzvfR2ibwg3NL5KUGwzibFa7T2oBm8LmtFJPFhWIib5TK9ZUosGd8zquycwxAYibz1YKIcOibicjlGvg/0?wx_fmt=jpeg', 'create_time': 1694174854, 'digest': '宣传交流部拍了拍你，邀请你一起前行~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=3&sn=c62346986a935b0f19e70315a6b05f6d&chksm=853311ffb24498e9080001e32f95cc62eb9e257213714d54bd4655ea46d564dbeed194db245f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 宣传交流部拍了拍你，邀请你一起前行', 'update_time': 1694174854}, {'aid': '2651120091_4', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120091, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/sTHGDZ2o0PSiazzvfR2ibwg3NL5KUGwzibFnYcE7TIIictasYq3NiaIKoIeiaHsk5Fiaj3L4vafmX5KwY5ib92V3LwtOeA/0?wx_fmt=jpeg', 'create_time': 1694174854, 'digest': '风采实践部，欢迎你的到来！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 4, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=4&sn=9ba8f10175426d3f90204cd5ee6d2d31&chksm=853311ffb24498e9dc8befe37cca349f44aa9d3f5de51a97896d789e777bfbff2f65612e8c1b#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 风采实践部：承风采神韵，开实践新风', 'update_time': 1694174854}, {'aid': '2651120091_5', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120091, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/sTHGDZ2o0PRJiafmhTR4kPNZSzo5fHR1TpuCsR91kSXJlON5sTXfN4OVicx1Yib8iaX6PeKUYzmE9RahfJvsAmj3yg/0?wx_fmt=png', 'create_time': 1694174854, 'digest': '同知共行，知行合一\r\n志愿与共，笃实求新', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 5, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=5&sn=5e22367eb1193ff2ddbb6d1c160976ed&chksm=853311ffb24498e96c961f043963c85f777522a8a659ff950dee54a7fe3c5a337e02bd5cbbcd#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 学术科创部：亦知亦行，求实创新', 'update_time': 1694174854}, {'aid': '2651120091_6', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120091, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/sTHGDZ2o0PSiazzvfR2ibwg3NL5KUGwzibFgr260jytiafqjxE1M7YeoFxXVs9h7gHJ1KoSo07GbyAcvKZe0lajejQ/0?wx_fmt=png', 'create_time': 1694174854, 'digest': '和我们一起，用热情点亮同学们的校园生活！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 6, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=6&sn=8c04413274bc30e099fd483791160891&chksm=853311ffb24498e9b7b0ed00c408db3d3b6e30ca3607502bb94d63e852e767c1c08e80518dcf#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 赋生活以精彩，许服务以未来——我们在生活服务部等你哦~', 'update_time': 1694174854}, {'aid': '2651120091_7', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651120091, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/sTHGDZ2o0PSiazzvfR2ibwg3NL5KUGwzibF2bDALmOsMAyCUSmEo77epFYGEyDosLPHMTl0aUicpXPCXOYLfhFlj8g/0?wx_fmt=png', 'create_time': 1694174854, 'digest': '有趣+舞台+活力+温暖+热情+高效+创造=文体部+你！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 7, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=7&sn=56a08fc35e1d5ddb2bd62e6bcab610dd&chksm=853311ffb24498e9aa4f53c9f5d04c09d81735504eed5fe2dd38c322ea1fc28057a619a39c2c#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 文化体育部：发光的少年，请留步！你五行缺文体！', 'update_time': 1694174854}, {'aid': '2651119983_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2651119983, 'checking': 0, 'copyright_type': 1, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/sTHGDZ2o0PQq6ApLZ8IKdUIIIcYltu1Mbz19icOLHJAhNqEjN06WG5ec4SvrP9XjqIhIprDjx0t094t2XPmibicaA/0?wx_fmt=png', 'create_time': 1693909855, 'digest': '叮咚！你有一份招新宣讲邀请函，请签收！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651119983&idx=1&sn=503464da24f9fd7914f6d9d604a2e3cf&chksm=8533114bb244985da7e765db5c2aec42b71109049f9f5543040b3e0a34d3df363d329c048745#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '招新 | 心心念念，从新出发', 'update_time': 1693909855}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
星野·回顾 | “星野”社会实践团赴北大红楼开展实践活动 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120168&idx=1&sn=4c88ab79aa6904669b5bc22bbdfaeb39&chksm=8533120cb2449b1ab92a1e3242d60f93ccaa830d92ba87dc04cac468f1e0fc57396b011804db#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新｜综办在等你 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120116&idx=1&sn=2de9fe587417622adaad7d04f6c928bd&chksm=853311d0b24498c6b069ef8b70640ce482b7e429609ab8d3ab7c49c41b077929523a112f453b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 快来加入监察部吧~ http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120116&idx=2&sn=60fbe5d1932226b0948a012b12c43ea5&chksm=853311d0b24498c67aa0a120e383584ea52be89d0e3bbd242838911b412e388a0f7f635f77e8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 常代会权益提案部期待你的加入！ http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120116&idx=3&sn=5d2d0236ce7b2ac65c32f4e00676817f&chksm=853311d0b24498c64d96401f07d9adca18e30fe30e34d388ba7a7abe7b83259b6bc8294d3301#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北大之锋 | 决赛预告 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120115&idx=1&sn=b40087af58627bea3c0cac471fd8f8b2&chksm=853311d7b24498c12cb5544c2c84efbb54bbb04886261c0a995cc6618960f0b8fecb733bf673#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 北大学生会，期待每一朵星火 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=1&sn=213830056e89c1abe5c474db95a1ba52&chksm=853311ffb24498e91dd996fc264100b723a9249dbdc2d9bd2ceedc7ff73edfc3741c7b6c2dfc#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 综合管理部：综以有序，扎实建树 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=2&sn=f9b72ac5fbf0c6fdaabe388b22ea57c8&chksm=853311ffb24498e94104cc798a2b68ac6278949de780dbbe3a4144d3933fd5d40f281d257f3d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 宣传交流部拍了拍你，邀请你一起前行 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=3&sn=c62346986a935b0f19e70315a6b05f6d&chksm=853311ffb24498e9080001e32f95cc62eb9e257213714d54bd4655ea46d564dbeed194db245f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 风采实践部：承风采神韵，开实践新风 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=4&sn=9ba8f10175426d3f90204cd5ee6d2d31&chksm=853311ffb24498e9dc8befe37cca349f44aa9d3f5de51a97896d789e777bfbff2f65612e8c1b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 学术科创部：亦知亦行，求实创新 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=5&sn=5e22367eb1193ff2ddbb6d1c160976ed&chksm=853311ffb24498e96c961f043963c85f777522a8a659ff950dee54a7fe3c5a337e02bd5cbbcd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 赋生活以精彩，许服务以未来——我们在生活服务部等你哦~ http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=6&sn=8c04413274bc30e099fd483791160891&chksm=853311ffb24498e9b7b0ed00c408db3d3b6e30ca3607502bb94d63e852e767c1c08e80518dcf#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 文化体育部：发光的少年，请留步！你五行缺文体！ http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651120091&idx=7&sn=56a08fc35e1d5ddb2bd62e6bcab610dd&chksm=853311ffb24498e9aa4f53c9f5d04c09d81735504eed5fe2dd38c322ea1fc28057a619a39c2c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
招新 | 心心念念，从新出发 http://mp.weixin.qq.com/s?__biz=MzA3MDAxMTIxMQ==&mid=2651119983&idx=1&sn=503464da24f9fd7914f6d9d604a2e3cf&chksm=8533114bb244985da7e765db5c2aec42b71109049f9f5543040b3e0a34d3df363d329c048745#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
PKU医预之家 MzAxOTAyMjk0MA==
sleep 465
<Response [200]>
dic: {'app_msg_cnt': 1480, 'app_msg_list': [{'aid': '2656048752_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656048752, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/RTDeyXeNGKxM3e4M35sjc9OcYDO9lxKAfsGica1QMCFv2Yt8TlQrw8Vzxyjf9VMhZcibxfVZ5ibWnTWJCk3HaibE3w/0?wx_fmt=png', 'create_time': 1694701069, 'digest': '朋辈π系列活动来袭，PS和Canva专场首报到！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048752&idx=1&sn=438a09d75812618db8ff59677585181b&chksm=8069e343b71e6a5504ece02a4d5b4483d05c81deaf554eafc73c60815c28a8696c9aa773901b#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【志实部.055&&助理团.021】朋辈π：PS和Canva保姆级教学来喽~', 'update_time': 1694701068}, {'aid': '2656048739_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656048739, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/RTDeyXeNGKyiahZLc3fwEsLYxcxVbnHoCAZT9Nic6BzNiaD3qksB3jDAFosPCkhTBCr5CTaIeZ7hCQNbym4NuID3w/0?wx_fmt=jpeg', 'create_time': 1694587286, 'digest': '2023级医学预科主席团&部长团复试通知与志愿者招募', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048739&idx=1&sn=1c323b416254599ad33be7dddf2c7ef1&chksm=8069e350b71e6a46a0fa3d8d401434c898c43eaf894051b5e62483b3e321e136f30e3e09b6af#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '医路奋进，踏浪高歌｜医预主席团&部长团复试通知与志愿者招募', 'update_time': 1694587286}, {'aid': '2656048726_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656048726, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/RTDeyXeNGKydaTx5r7J4GGQrLPw7gI9t2nGT1pkdnzZMqSwiaiaXU8sjoaLqowcByS3nZsaKk22enyiaa0Q9ntwHg/0?wx_fmt=png', 'create_time': 1694419518, 'digest': '军训三营八连积极响应号召，充分利用自选动作时间，创新活动形式，丰富军训内涵。具有医学特色的军训橄榄绿在这个盛夏绽放出绚烂的色彩。', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048726&idx=1&sn=8cc50a1a4a73d0c92e9930c1e29edb8f&chksm=8069e365b71e6a739aabc2cfbe92ae0dac24d72c0353d12b3a591d4b46a2bc18280df90986da#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '医学特色橄榄绿在盛夏绽放 ——三营八连军训连队活动简报', 'update_time': 1694419518}, {'aid': '2656048695_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656048695, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/RTDeyXeNGKztRRgjbNsOOjibbOFbM1KqhILPZrhMJNxUZP6EWZpicSHFJOGjB6EQZl9kia2EqusJVd3adngoajkpg/0?wx_fmt=jpeg', 'create_time': 1694088167, 'digest': '医学预科学业辅导与生涯发展规划工作室开张啦！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048695&idx=1&sn=71137534a6d895c3302922e13dbd7174&chksm=8069e304b71e6a12a154a848037707f87d5231bb9369c0f46aeab3610dc492291eccd78576a9#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '医路扬帆新梦想，奋进征程同启航——医学预科学业辅导与生涯发展规划工作室开张啦！', 'update_time': 1694088167}, {'aid': '2656048688_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2656048688, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/RTDeyXeNGKwaLWUJOScwicrCbrmXv362LPbxlJd7p0uHq9WJNHTRATibpCdWVplibCWwt43CD4NAWh7zgyhYwQpdQ/0?wx_fmt=jpeg', 'create_time': 1694002489, 'digest': '医歌不辍，薪火相传｜快来捧走学长学姐“沉甸甸”的爱～', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048688&idx=1&sn=8d52aa5a2676139b6b8b5191b7be9810&chksm=8069e303b71e6a153bfe24599eed6235bd0bbf9342ad9fa8a7deb6f111743fff1ba81bcd8b27#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '【学习部.040】医歌不辍，薪火相传｜快来捧走学长学姐“沉甸甸”的爱～', 'update_time': 1694002489}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
【志实部.055&&助理团.021】朋辈π：PS和Canva保姆级教学来喽~ http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048752&idx=1&sn=438a09d75812618db8ff59677585181b&chksm=8069e343b71e6a5504ece02a4d5b4483d05c81deaf554eafc73c60815c28a8696c9aa773901b#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
医路奋进，踏浪高歌｜医预主席团&部长团复试通知与志愿者招募 http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048739&idx=1&sn=1c323b416254599ad33be7dddf2c7ef1&chksm=8069e350b71e6a46a0fa3d8d401434c898c43eaf894051b5e62483b3e321e136f30e3e09b6af#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
医学特色橄榄绿在盛夏绽放 ——三营八连军训连队活动简报 http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048726&idx=1&sn=8cc50a1a4a73d0c92e9930c1e29edb8f&chksm=8069e365b71e6a739aabc2cfbe92ae0dac24d72c0353d12b3a591d4b46a2bc18280df90986da#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
医路扬帆新梦想，奋进征程同启航——医学预科学业辅导与生涯发展规划工作室开张啦！ http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048695&idx=1&sn=71137534a6d895c3302922e13dbd7174&chksm=8069e304b71e6a12a154a848037707f87d5231bb9369c0f46aeab3610dc492291eccd78576a9#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
【学习部.040】医歌不辍，薪火相传｜快来捧走学长学姐“沉甸甸”的爱～ http://mp.weixin.qq.com/s?__biz=MzAxOTAyMjk0MA==&mid=2656048688&idx=1&sn=8d52aa5a2676139b6b8b5191b7be9810&chksm=8069e303b71e6a153bfe24599eed6235bd0bbf9342ad9fa8a7deb6f111743fff1ba81bcd8b27#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
大信科 MzA4MTAzMzQ5NA==
sleep 80
<Response [200]>
dic: {'app_msg_cnt': 1932, 'app_msg_list': [{'aid': '2650886182_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886182, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/u1KmGicxXMEPoLx8Lph4f26Q9Eic9pOrYkYo2T9CHgUH1l0PxkXsFukmegRtaAdBofRjCjFG2urP232lcMiaV9tJQ/0?wx_fmt=jpeg', 'create_time': 1694695030, 'digest': '北京大学显示技术系列讲座第3期', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886182&idx=1&sn=6673c569b3e4ca9211f3fdca2a87774e&chksm=846ed05fb31959499957318767d493e0549befabd9bc116e43f802fff3bf3dab270e87cad73f#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '预告 | 北京大学显示技术系列讲座第3期——OLED材料的发展和趋势分析', 'update_time': 1694696400}, {'aid': '2650886182_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886182, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/u1KmGicxXMEMZfHS4spABwvDgicPhrIsRc9NHcfSDTYFnMorU7FicEWvTuY5VHTMsIqQmfYbbxvwR79fu4FpqVG5w/0?wx_fmt=jpeg', 'create_time': 1694695030, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886182&idx=2&sn=8a0952186ec984d98adc52ead5f71225&chksm=846ed05fb31959491602352865c849ab41a6ea596c115c70b6015935a4b059bb625fff465a9c#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '回顾 | 信息科学技术学院2023年“新生杯”  乒乓球赛', 'update_time': 1694696400}, {'aid': '2650886182_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886182, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/u1KmGicxXMEPoLx8Lph4f26Q9Eic9pOrYkQchB1X25EYxI7xtKvyHVp32yCkIicwHoiasOoDtIOJ5gKicviaIztInbmw/0?wx_fmt=jpeg', 'create_time': 1694695030, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886182&idx=3&sn=1bf410ff6c03b687438cdb328b95ed7c&chksm=846ed05fb3195949c25976836eb5628e58890d44e98ebda1ddc0998e9f9badde72f371efe9da#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '信息科学技术学院2023级本科生陈浩伟在北京大学2023年开学典礼上的发言', 'update_time': 1694696400}, {'aid': '2650886172_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886172, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/u1KmGicxXMENv2GeThk9y6z9VJjGdqjC31vibzbE983pFz4VGvic8j5Zv6moibia8NAPAnibTd6q4HrVZVHALWVbQekg/0?wx_fmt=png', 'create_time': 1694609621, 'digest': '信科萌新们，快来参加定向越野吧！', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886172&idx=1&sn=0a45715bcedb7719e416a1edffa01c16&chksm=846ed065b319597340be07578807fc19b5a4d17c515f740cc822b99fe47a6f79c170d59b82e6#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '活动 | 新生定向越野报名启动', 'update_time': 1694610000}, {'aid': '2650886172_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886172, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/u1KmGicxXMEMZfHS4spABwvDgicPhrIsRcyBzCDIlibtBfTdxBoNmCnbqp9WdL1ckricUCggaDqGjGkxDIDhqLw4BA/0?wx_fmt=jpeg', 'create_time': 1694609621, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886172&idx=2&sn=44b242859f175871cb964b2bad4c2285&chksm=846ed065b3195973c89f99d30c8e90a0b3f9fd45fccef206ad6e67c23939d26b6762903136cd#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '信有所行 | 披荆斩棘鸿蒙启，中华有为天下先——2023信息科学技术学院赴华为北京研究所思政实践纪实（上）', 'update_time': 1694610000}, {'aid': '2650886172_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886172, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/u1KmGicxXMEMZfHS4spABwvDgicPhrIsRcFC0LZqzbVN7Nv2gYDia2Q92Ft7nhQcibANc8nbkAicAOvFztSLOvJGKIQ/0?wx_fmt=jpeg', 'create_time': 1694609621, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886172&idx=3&sn=1d39ea9113a5d5144ac1cbada91d64a2&chksm=846ed065b31959737054419fd5aa758a84327f58a6ee3e20c3885bc62353201c530ea91fa8e8#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '信有所行 | 厚积薄发创芯业，以行践言开新篇——2023信息科学技术学院赴华为北京研究所思政实践纪实（下）', 'update_time': 1694610000}, {'aid': '2650886132_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886132, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/u1KmGicxXMENS0icoaMwMMuruRSa3IID7ib59eQLibRJI5bibiaJMeictrN8Rq4Cj1vZM0NcPEbxzvXXLZT2E0V6LEQ0A/0?wx_fmt=jpeg', 'create_time': 1694514993, 'digest': '虚拟机配置教程~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886132&idx=1&sn=0c59c88a2697d9ac98a5805f95bb1383&chksm=846ecf8db319469bed08bed545b1b0ad166dc83724c82296f6d854d920598e25ce585429237d#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '学术丨虚拟机配置教程', 'update_time': 1694523600}, {'aid': '2650886132_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886132, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/u1KmGicxXMENS0icoaMwMMuruRSa3IID7ibibbeL9icDEKuONPZjV8JOIku2CIoQlTZcuefNfjyqzATAxUcafqpa6icQ/0?wx_fmt=jpeg', 'create_time': 1694514993, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886132&idx=2&sn=8601151f24005d7d324d297630cf3916&chksm=846ecf8db319469b775895dcea79f355c6e5affe1d6096dde222c88fe61441792cd674b77f73#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '信有所行 | 高举旗帜跟党走，躬耕实践促新知——2023信息科学技术学院赴重庆璧山思政实践纪实（上）', 'update_time': 1694523600}, {'aid': '2650886132_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886132, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/u1KmGicxXMENS0icoaMwMMuruRSa3IID7ibk62H1qlSSjgCE3QIIhBFIC9R8e8cCqCDOhC7cPKCf0HGHognSNgZ3g/0?wx_fmt=jpeg', 'create_time': 1694514993, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886132&idx=3&sn=eae39a63db580f5225a31716c303d5e2&chksm=846ecf8db319469b151a63fdb8f018ddbc46c29f8a1633dc20303b2cf419fc5787a8eed99b5a#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '信有所行 | 红岩精神传薪火，勇立潮头谱新篇——2023信息科学技术学院赴重庆璧山思政实践纪实（下）', 'update_time': 1694523600}, {'aid': '2650886121_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886121, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/u1KmGicxXMEPTgCTdz6D2iaOyibiaymDIicAHI08MIeuGks127tKePHWKp7Np374zwg1GJiblXDPyecF38F98icVhGu5g/0?wx_fmt=png', 'create_time': 1694427974, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886121&idx=1&sn=43aacf62444db4243c6a1e0cb4a549d1&chksm=846ecf90b3194686e88f6a2370489e88522985f18632f3550fe2bbba22198a2079ec0be89e07#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '通知 | 北京大学信息科学技术学院2023-2024年度团委部长团招募通知', 'update_time': 1694437200}, {'aid': '2650886121_2', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886121, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_jpg/u1KmGicxXMEPg1xWVc6cNVBIXnBUMP3G6A8huQ3mndHO6lF2VCXGHpSZdjBbGtTFRvKVBO3eQRN0RkKHuNORIqA/0?wx_fmt=jpeg', 'create_time': 1694427974, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 2, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886121&idx=2&sn=f921c41f1a54c35012cb1aba860d0caf&chksm=846ecf90b3194686ebfa74f45638eb41de5f39abacb1cb7403a2543003cb72554f932b736a94#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '新闻 | 2023-2024学年信息科学技术学院团学各部门交流会顺利召开', 'update_time': 1694437200}, {'aid': '2650886121_3', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886121, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/u1KmGicxXMENS0icoaMwMMuruRSa3IID7ib5XiaFh0ATB3N76EibdtcjX2z9sEZvibqvic5kSibX5b4EUicatBtoEzzUMZw/0?wx_fmt=png', 'create_time': 1694427974, 'digest': 'vscode配置教程~', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 3, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886121&idx=3&sn=a7832f79c4fec88e1b35cc5ff0c90800&chksm=846ecf90b3194686697fd30493243f5b61af6801ea711e269b2ae10e4e9b608ce31f0f1ef1a6#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '学术丨vscode配置', 'update_time': 1694437200}, {'aid': '2650886064_1', 'album_id': '0', 'appmsg_album_infos': [], 'appmsgid': 2650886064, 'checking': 0, 'copyright_type': 0, 'cover': 'https://mmbiz.qlogo.cn/sz_mmbiz_png/u1KmGicxXMEPg1xWVc6cNVBIXnBUMP3G6caaR2dwga5YKJhxyCqzD19WSkl05hjicdNwRUelT5KxaRiaEgOKgniaiaQ/0?wx_fmt=png', 'create_time': 1694258081, 'digest': '', 'has_red_packet_cover': 0, 'is_pay_subscribe': 0, 'item_show_type': 0, 'itemidx': 1, 'link': 'http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886064&idx=1&sn=ca4099aa4e684dee7025e39b79bc9597&chksm=846ecfc9b31946df6b8e2556be17644cb39568d8452b428da790656a78e1ca016590a55fd7da#rd', 'media_duration': '0:00', 'mediaapi_publish_status': 0, 'pay_album_info': {'appmsg_album_infos': []}, 'tagid': [], 'title': '“信”理论，“心”思想 ——北京大学信息科学技术学院本科生第五党支部与北京师范大学心理学部本科生第二党支部主题教育党课', 'update_time': 1694264400}], 'base_resp': {'err_msg': 'ok', 'ret': 0}}
预告 | 北京大学显示技术系列讲座第3期——OLED材料的发展和趋势分析 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886182&idx=1&sn=6673c569b3e4ca9211f3fdca2a87774e&chksm=846ed05fb31959499957318767d493e0549befabd9bc116e43f802fff3bf3dab270e87cad73f#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
回顾 | 信息科学技术学院2023年“新生杯”  乒乓球赛 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886182&idx=2&sn=8a0952186ec984d98adc52ead5f71225&chksm=846ed05fb31959491602352865c849ab41a6ea596c115c70b6015935a4b059bb625fff465a9c#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信息科学技术学院2023级本科生陈浩伟在北京大学2023年开学典礼上的发言 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886182&idx=3&sn=1bf410ff6c03b687438cdb328b95ed7c&chksm=846ed05fb3195949c25976836eb5628e58890d44e98ebda1ddc0998e9f9badde72f371efe9da#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
活动 | 新生定向越野报名启动 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886172&idx=1&sn=0a45715bcedb7719e416a1edffa01c16&chksm=846ed065b319597340be07578807fc19b5a4d17c515f740cc822b99fe47a6f79c170d59b82e6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信有所行 | 披荆斩棘鸿蒙启，中华有为天下先——2023信息科学技术学院赴华为北京研究所思政实践纪实（上） http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886172&idx=2&sn=44b242859f175871cb964b2bad4c2285&chksm=846ed065b3195973c89f99d30c8e90a0b3f9fd45fccef206ad6e67c23939d26b6762903136cd#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信有所行 | 厚积薄发创芯业，以行践言开新篇——2023信息科学技术学院赴华为北京研究所思政实践纪实（下） http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886172&idx=3&sn=1d39ea9113a5d5144ac1cbada91d64a2&chksm=846ed065b31959737054419fd5aa758a84327f58a6ee3e20c3885bc62353201c530ea91fa8e8#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
学术丨虚拟机配置教程 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886132&idx=1&sn=0c59c88a2697d9ac98a5805f95bb1383&chksm=846ecf8db319469bed08bed545b1b0ad166dc83724c82296f6d854d920598e25ce585429237d#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信有所行 | 高举旗帜跟党走，躬耕实践促新知——2023信息科学技术学院赴重庆璧山思政实践纪实（上） http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886132&idx=2&sn=8601151f24005d7d324d297630cf3916&chksm=846ecf8db319469b775895dcea79f355c6e5affe1d6096dde222c88fe61441792cd674b77f73#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
信有所行 | 红岩精神传薪火，勇立潮头谱新篇——2023信息科学技术学院赴重庆璧山思政实践纪实（下） http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886132&idx=3&sn=eae39a63db580f5225a31716c303d5e2&chksm=846ecf8db319469b151a63fdb8f018ddbc46c29f8a1633dc20303b2cf419fc5787a8eed99b5a#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
通知 | 北京大学信息科学技术学院2023-2024年度团委部长团招募通知 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886121&idx=1&sn=43aacf62444db4243c6a1e0cb4a549d1&chksm=846ecf90b3194686e88f6a2370489e88522985f18632f3550fe2bbba22198a2079ec0be89e07#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
新闻 | 2023-2024学年信息科学技术学院团学各部门交流会顺利召开 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886121&idx=2&sn=f921c41f1a54c35012cb1aba860d0caf&chksm=846ecf90b3194686ebfa74f45638eb41de5f39abacb1cb7403a2543003cb72554f932b736a94#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
学术丨vscode配置 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886121&idx=3&sn=a7832f79c4fec88e1b35cc5ff0c90800&chksm=846ecf90b3194686697fd30493243f5b61af6801ea711e269b2ae10e4e9b608ce31f0f1ef1a6#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
“信”理论，“心”思想 ——北京大学信息科学技术学院本科生第五党支部与北京师范大学心理学部本科生第二党支部主题教育党课 http://mp.weixin.qq.com/s?__biz=MzA4MTAzMzQ5NA==&mid=2650886064&idx=1&sn=ca4099aa4e684dee7025e39b79bc9597&chksm=846ecfc9b31946df6b8e2556be17644cb39568d8452b428da790656a78e1ca016590a55fd7da#rd
<Response [200]>
{"code":0,"data":null,"msg":"链接错误"}
sleep 15
北京大学历史学系学生会 MzA3NDYwMzkxMg==
sleep 114
<Response [200]>
'''
#get all Link(link=*) from the text to a list
import re
import requests
def POSTER(link):
    import json
    headers = {'Content-Type': 'application/json'}
    url = 'http://localhost:8081/api/user/submit/link'
    data = {'link': link}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r)
    print(r.text)
    
def getLinkList(text):
    linkList = []
    linkPattern = re.compile(r'http://..*')
    linkList = linkPattern.findall(text)
    #delete Link(link=)
    # for i in range(len(linkList)):
        # linkList[i] = linkList[i][10:-1]
    return linkList

res = getLinkList(text)
#reverse
res = res[::-1]
res = res[200:]
import time
for link in res:
    if(len(link) < 5 * len('http://mp.weixin.qq.com/s?__biz=MzU2MTEwNjk4Mg==&mid=2247501265&idx=1&sn=7d3ef5775b6962013f9793b5a40bb186&chksm=fc7f5c98cb08d58e18c0e15b897291dcb3e3abd36060475fcec8ffd58e4719f470191edee341#rd')):
        print(link)
        POSTER(link)
        time.sleep(1)