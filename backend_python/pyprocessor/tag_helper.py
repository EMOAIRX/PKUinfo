from keys import zhipuai_APIKEY
from zhipuai import ZhipuAI
import numpy as np
import zhipuai
def read_tags(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        tags = [line.strip() for line in lines]
        return tags
def ask_chatgpt(message): 
       # print(message)
     #   print({"role": "user", "content": message})
        
        client = ZhipuAI(api_key=zhipuai_APIKEY) # 请填写您自己的APIKey
        response = client.chat.completions.create(
            model="glm-3-turbo",
            messages=[
                {"role": "user", "content": message},
            ],
            
        ) 
        result = response.choices[0].message.content
      #  print(result)
        while (len(result) > 0 and result[0] == ' '):
            result = result[1:]
        print('ANS=',result)
        return result
def test_tag(content, tag):
    prompt = "这里有一个活动的相关内容，请你判断是否是" + tag + "的内容。内容如下：" + content + "\n请你看完严格回答一个字'是'或'否'来表示你的判断，不要格外任何信息。"
    ask_chatgpt(prompt)

def get_embedding(content):
    
    client = ZhipuAI(api_key = zhipuai_APIKEY) 
    response = client.embeddings.create(
        model="embedding-2", #填写需要调用的模型名称
        input=content,
    )
    return response.data[0].embedding

def only_test_gpt(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    content = ""
    for line in lines:
        content += line + ' '
    with open("tag_list.txt","r") as f:
        tags = f.readlines()
        tags = [tag.strip() for tag in tags]
    for tag in tags:
        test_tag(content,tag)
def only_test_embedding(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if len(line.strip()) > 0]
    content = ""
    for line in lines:
        content += line + ' '
    content_embedding = get_embedding(content)
    content_embedding = np.array(content_embedding)
    with open("tag_list.txt","r") as f:
        tags = f.readlines()
        tags = [tag.strip() for tag in tags]
    v_list = []
    for tag in tags:
        tag_embedding = get_embedding(tag)    
        tag_embedding = np.array(tag_embedding)
        cos_sim = content_embedding.dot(tag_embedding) / (np.linalg.norm(content_embedding) * np.linalg.norm(tag_embedding))
        v_list.append((cos_sim,tag))
    v_list.sort(reverse=True)
    v_all = np.sum([v[0] for v in v_list])
    v_list = [(v[0]/v_all,v[1]) for v in v_list]
    tag1 = 0
    tag2 = 0
    for i in range(len(v_list)):
        x = v_list[i]
        if x[1].startswith("招聘"):
            tag1 = i
        elif x[1].startswith("招新"):
            tag2 = i
    if v_list[tag1][0] > v_list[tag2][0]:
        v_list[tag2] = (0,"")
    else:
        v_list[tag1] = (0,"")
    print(v_list)
    threshold = 1 / len(tags)
    v_list = [v for v in v_list if v[0] > threshold]
    print(v_list)
    print([v[1][:2] for v in v_list[:3]])

def get_tags_from_content(content):
    content_embedding = get_embedding(content)
    content_embedding = np.array(content_embedding)
    with open("tag_list.txt","r") as f:
        tags = f.readlines()
        tags = [tag.strip() for tag in tags]
    v_list = []
    for tag in tags:
        tag_embedding = get_embedding(tag)    
        tag_embedding = np.array(tag_embedding)
        cos_sim = content_embedding.dot(tag_embedding) / (np.linalg.norm(content_embedding) * np.linalg.norm(tag_embedding))
        v_list.append((cos_sim,tag))
    v_list.sort(reverse=True)
    v_all = np.sum([v[0] for v in v_list])
    v_list = [(v[0]/v_all,v[1]) for v in v_list]
    tag1 = 0
    tag2 = 0
    for i in range(len(v_list)):
        x = v_list[i]
        if x[1].startswith("招聘"):
            tag1 = i
        elif x[1].startswith("招新"):
            tag2 = i
    if v_list[tag1][0] > v_list[tag2][0]:
        v_list[tag2] = (0,"")
    else:
        v_list[tag1] = (0,"")
    threshold = 1 / len(tags)
    v_list = [v for v in v_list if v[0] > threshold]
    return [v[1][:2] for v in v_list[:3]]


if __name__ == "__main__":
    #only_test_gpt("activity_example.txt")
    only_test_embedding("activity_example.txt")