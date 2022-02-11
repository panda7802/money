import tinify

tinify.key = "0xZRHrhyBz6FBGhp9gqkrz9RQlqJykcB"

pic_name = "1"
pic_dir = r"C:\Users\81425\Desktop\新建文件夹\\"
pic_path = "%s\\%s.png" % (pic_dir, pic_name)
obj_path = "%s\\%s_compress.png" % (pic_dir, pic_name)
with open(pic_path, 'rb') as source:
    source_data = source.read()
    result_data = tinify.from_buffer(source_data).to_file(obj_path)
